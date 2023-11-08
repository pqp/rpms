Name:     ironwail
Version:  0.7.0
Release:  1%{?dist}
Summary:  GLQuake descendant with a focus on high performance
License:  GPLv2
URL:      https://github.com/andrei-drexler/ironwail
BuildRequires:  gcc-c++ make cmake SDL2-devel libvorbis-devel libmad-devel git
BuildRequires:  zlib-devel bzip2-devel libcurl-devel

%global NVdir %{name}-%{version}

%description
Ironwail is a fork of the popular GLQuake descendant QuakeSpasm with a focus on high performance instead of maximum compatibility.

%prep
rm -rf %{NVdir}
git clone %{url}.git %{NVdir}
cd %{NVdir}
git checkout v%{version}

%build
cd %{NVdir}/Quake
make %{?_smp_mflags}
cat > %{name}.sh <<EOF
#!/bin/bash
%{_prefix}/local/games/quake/%{name} \$@
EOF

%install
rm -rf ${buildroot}
cd %{NVdir}/Quake
mkdir -p %{buildroot}/usr/local/games/quake
cp ironwail %{buildroot}/usr/local/games/quake
cp ironwail.pak %{buildroot}/usr/local/games/quake
mkdir -p %{buildroot}/usr/bin
install -m 755 %{name}.sh %{buildroot}/usr/bin/%{name}

%files
%{_prefix}/local/games/quake/%{name}
%{_prefix}/local/games/quake/%{name}.pak
%{_bindir}/%{name}

%changelog
* Tue Nov 7 2023 Patrick Pace <pqp@fedoraproject.org> - 0.7.0
- Initial version
