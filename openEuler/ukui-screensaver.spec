Name:           ukui-screensaver
Version:        3.0.1
Release:        4
Summary:        parallels toolbox for UKUI
License:        GPL-3+ GPL-2+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: glib2-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qttools-devel
BuildRequires: gsettings-qt-devel
BuildRequires: dconf-devel
BuildRequires: libXtst-devel
BuildRequires: cmake
BuildRequires: qt5-qtx11extras-devel
BuildRequires: pam-devel

Requires: glib2-devel
Requires: qt5-qtbase-devel
Requires: qt5-qtsvg-devel
Requires: qt5-qtmultimedia-devel
Requires: qt5-qttools-devel
Requires: gsettings-qt-devel
Requires: dconf-devel

%description
 The ukui-sidebar is mainly used in the desktop operating system.
 It pops up from the right side of the desktop in the form of a tray,
 displaying some application notification messages and some cutting
 storage information.

%prep
%setup -q

%build
cmake .
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc debian/copyright debian/changelog
%{_bindir}/ukui-screensaver-dialog
%{_bindir}/ukui-screensaver-backend
%{_bindir}/ukui-screensaver-command
%{_datadir}/ukui-screensaver/*
%{_datadir}/glib-2.0/schemas/org.ukui.screensaver.gschema.xml
%{_sysconfdir}/xdg/autostart/ukui-screensaver.desktop
%{_datadir}/desktop-directories/ukui-screensaver.directory
%{_sysconfdir}/xdg/menus/ukui-screensavers.menu
%{_sysconfdir}/pam.d/ukui-screensaver-qt
%{_prefix}/lib/ukui-screensaver/ukui-screensaver-default

%changelog
* Fri Jan 29 2021 lvhan <lvhan@kylinos.cn> - 3.0.1-4
- update to upstream version 3.0.0-1

* Wed Jan 13 2021 lvhan <lvhan@kylinos.cn> - 3.0.1-3
- 0002-fix-ukui-screensaver-dialog-lock.patch

* Wed Dec 9 2020 lvhan <lvhan@kylinos.cn> - 3.0.1-2
- 0001-fix-icon-misplaced.patch

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.1-1
- update to upstream version 3.0.0-1+1026

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.1.1-1
- Init package for openEuler
