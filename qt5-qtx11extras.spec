# TODO:
# - cleanup

%define		orgname		qtx11extras
Summary:	The Qt5 X11 Extras
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	1a11c4bb67503e2a5ef10b96bbe11b61
URL:		http://qt-project.org/
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	qt5-qttools-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%define		specflags	-fno-strict-aliasing
%define		_qtdir		%{_libdir}/qt5

%description
Qt5 X11 Extras libraries.

%package devel
Summary:	The Qt5 X11Extras - development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Qt5 X11 Extras - development files.

%package doc
Summary:	The Qt5 X11 Extras - docs
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 X11 Extras - documentation.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5X11Extras.so.?
%attr(755,root,root) %{_libdir}/libQt5X11Extras.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5X11Extras.so
%{_libdir}/libQt5X11Extras.la
%{_libdir}/libQt5X11Extras.prl
%{_libdir}/cmake/Qt5X11Extras
%{_includedir}/qt5/QtX11Extras
%{_pkgconfigdir}/*.pc
%{_qtdir}/mkspecs

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc
