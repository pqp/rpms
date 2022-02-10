%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}
%global revision c48c4f2

Name:       quakespasm-spiked
Version:    2021.11.14
Release:    1%{?dist}
Summary:    A modern Quake 1 engine
Group:      Games
License:    GPLv2+
#URL:       https://triptohell.info/moodles/qss/
URL:        https://github.com/Shpoike/Quakespasm
Patch0:     quakespasm-spiked-change-exec-name.patch
Source1:    %{name}.desktop
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  gcc git
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  zlib-devel opusfile-devel

%global NVdir %{name}-%{version}

%description
An even more modern Quake 1 engine based on QuakeSpasm.

%prep
rm -rf %{NVdir}
git clone %{URL}.git %{NVdir}
cd %{NVdir}
git checkout %{revision}
%patch0

%build
cd %{NVdir}/quakespasm/Quake
%make_build DO_USERDIRS=1 USE_SDL2=1

%install
#Install the icon
%{__install} -D -p -m 644 %{name}-%{version}/quakespasm/Misc/QuakeSpasm_512.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

cd %{name}-%{version}/quakespasm/Quake
mkdir -p %{buildroot}%{_bindir}
cp %{name} %{buildroot}%{_bindir}

#Install the desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license %{name}-%{version}/quakespasm/LICENSE.txt
%{_bindir}/%{name}
%{_datarootdir}/icons/hicolor/512x512/apps/%{name}.png
%{_datarootdir}/applications/%{name}.desktop

%changelog
* Thu Feb 10 2022 Patrick Pace <pqp@coapt.net> 2021.11.14
- Initial specfile (based off Brandon Nielsen's quakespasm.spec)