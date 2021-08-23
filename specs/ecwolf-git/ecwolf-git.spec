%define revision ac4a229	

Name:		ecwolf-git
Version:	1.3.3
Release:	%{revision}%{?dist}
Summary:	Original Wolfenstein 3D and Doom source releases plus Wolf4SDL
License:	GPLv2 or EULA
URL: 		https://bitbucket.org/ecwolf/ecwolf/
BuildRequires:	gcc-c++ make cmake SDL2-devel SDL2_mixer-devel SDL2_net-devel git	
BuildRequires:	zlib-devel bzip2-devel libjpeg-turbo-devel gtk2-devel SDL-devel SDL_mixer-devel 

%define NVdir	%{name}-%{version}

%description
ECWolf is an advanced source port for Wolfenstein 3D, Spear of Destiny, and Super 3D Noah's Ark based off of the Wolf4SDL code base.

%prep
rm -rf %{NVdir}
git clone %{url}.git %{NVdir}
cd %{NVdir}
git checkout %{revision}

%build
cd %{NVdir}
cmake . -DCMAKE_BUILD_TYPE=Debug -DGPL=ON
make %{?_smp_mflags}
cat > ecwolf.sh <<EOF
#!/bin/bash
%{_prefix}/local/games/ecwolf \$@
EOF

%install
rm -rf $RPM_BUILD_ROOT
cd %{NVdir}
%make_install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 ecwolf.sh %{buildroot}/usr/local/bin/ecwolf

%files
%license %{_prefix}/local/share/doc/ecwolf/copyright
%{_prefix}/local/games/ecwolf
%{_prefix}/local/bin/ecwolf
%{_prefix}/local/share/applications/ecwolf.desktop
%{_prefix}/local/share/doc/ecwolf/changelog.gz
%{_prefix}/local/share/ecwolf/ecwolf.pk3
%{_prefix}/local/share/icons/hicolor/scalable/apps/ecwolf.svg
%{_prefix}/local/share/man/man6/ecwolf.6.gz

%changelog
* Mon Aug 23 2021 Patrick Pace <pqp@fedoraproject.org> - 1.3.3-ac4a229	
 - Initial revision
