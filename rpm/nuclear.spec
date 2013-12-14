Summary: Nuclear is a shell for Wayland's Weston
Name: nuclear
Version: 0.0.0
Release: 1
License: LGPL21
Group: Development/Liraries
URL: https://github.com/giucam/nuclear.git
Source0: %{name}-%{version}.tar.bz2
Patch0:  0001-Remove-c-11-override-keyword.patch
Patch1:  0002-Add-class-to-friend-keyword.patch
BuildRequires: cmake >= 2.8
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(weston)
BuildRequires: pkgconfig(xkbcommon)


%description
It is composed of a Weston shell plugin and a shell client, made in Qt5,
with the interface in QtQuick 2.
Its goal is to produce a light and self-contained shell running on Wayland,
without many dependencies aside Weston and Qt.

%prep
%setup -q
cd nuclear
#%patch0 -p1
#%patch1 -p1

%build
cd nuclear
%cmake
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
cd nuclear
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%{_bindir}/nuclear
%{_libdir}/nuclear-shell/nuclear-shell.so
#%{_libdir}/nuclear/services/libloginservice.so
#%{_libdir}/nuclear/services/libmixerservice.so
#%{_libdir}/nuclear/services/libprocesslauncher.so
%{_datadir}/nuclear-shell/nuclear-desktop-shell.xml

