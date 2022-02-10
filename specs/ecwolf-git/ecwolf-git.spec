%global revision ac4a229

Name:     ecwolf-git
Version:  1.3.3
Release:  2%{revision}%{?dist}
Summary:  Original Wolfenstein 3D and Doom source releases plus Wolf4SDL
License:  GPLv2 or EULA
URL:      https://bitbucket.org/ecwolf/ecwolf/
Patch0:   ecwolf-git-change-exec-name.patch
BuildRequires:  gcc-c++ make cmake SDL2-devel SDL2_mixer-devel SDL2_net-devel git
BuildRequires:  zlib-devel bzip2-devel libjpeg-turbo-devel gtk2-devel SDL-devel SDL_mixer-devel 

%global NVdir %{name}-%{version}

%description
ECWolf is an advanced source port for games built on the Wolfenstein 3D engine.

%prep
rm -rf %{NVdir}
git clone %{url}.git %{NVdir}
cd %{NVdir}
git checkout %{revision}
%patch0

%build
cd %{NVdir}
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:path=/usr -DGPL=ON .
make %{?_smp_mflags}
cat > %{name}.sh <<EOF
#!/bin/bash
%{_prefix}/games/%{name} \$@
EOF

%install
rm -rf ${buildroot}
cd %{NVdir}
%make_install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{name}.sh %{buildroot}/usr/bin/%{name}

%files
%license %{_docdir}/%{name}/copyright
%{_prefix}/games/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/ecwolf.pk3
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_docdir}/%{name}/changelog.gz
%{_mandir}/man6/ecwolf.6.gz

%changelog
* Tue Aug 24 2021 Patrick Pace <pqp@fedoraproject.org> - 1.3.3-2-ac4a229
- Added patch that changes executable name to ecwolf-git

* Mon Aug 23 2021 Patrick Pace <pqp@fedoraproject.org> - 1.3.3-ac4a229
- Initial revision
