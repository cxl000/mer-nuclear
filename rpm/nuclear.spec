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

%package devel
Summary:   Devel files for Nuclear a shell for Wayland's Weston
Group:     Development/Liraries
Requires:  %{name} = %{version}-%{release}

%description devel
Development files for a Weston shell plugin

%prep
%setup -q
cd nuclear
#%patch0 -p1
#%patch1 -p1

%build
cd nuclear
%ifnarch %{ix86} x86_64
# HACK!!! Please remove when possible.
# cmake is accelerated but version is too old
mkdir /tmp/bin
cp -a /usr/bin/cmake /usr/share/cmake/Modules /usr/share/cmake/Templates /tmp/bin/
PATH=/tmp/bin:$PATH
/tmp/bin/cmake -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib -DINCLUDE_INSTALL_DIR:PATH=/usr/include -DLIB_INSTALL_DIR:PATH=/usr/lib -DSYSCONF_INSTALL_DIR:PATH=/etc -DSHARE_INSTALL_PREFIX:PATH=/usr/share -DCMAKE_SKIP_RPATH:BOOL=ON -DBUILD_SHARED_LIBS:BOOL=ON . -DCMAKE_BUILD_TYPE=RelWithDebInfo
%else
%cmake
%endif
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
%{_libdir}/nuclear-shell/libnuclear-shell-common.so
%{_libdir}/nuclear-shell/nuclear-desktop-shell.so
#%{_libdir}/nuclear/services/libloginservice.so
#%{_libdir}/nuclear/services/libmixerservice.so
#%{_libdir}/nuclear/services/libprocesslauncher.so

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/nuclear.pc
%{_datadir}/nuclear-shell/nuclear-desktop-shell.xml
%{_datadir}/nuclear-shell/nuclear-settings.xml
%{_datadir}/nuclear-shell/nuclear-dropdown.xml

