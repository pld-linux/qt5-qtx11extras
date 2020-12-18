#
# Conditional build:
%bcond_without	doc	# Documentation

%define		orgname		qtx11extras
%define		qtbase_ver	%{version}
%define		qttools_ver	%{version}
Summary:	The Qt5 X11 Extras library
Summary(pl.UTF-8):	Biblioteka Qt5 X11 Extras
Name:		qt5-%{orgname}
Version:	5.15.2
Release:	2
License:	LGPL v3 or GPL v2 or GPL v3 or commercial
Group:		X11/Libraries
Source0:	http://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-src-%{version}.tar.xz
# Source0-md5:	92cf72015788bb4dcab14494f2835b32
URL:		https://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 X11 Extras library.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera bibliotekę Qt5 X11 Extras.

%package -n Qt5X11Extras
Summary:	The Qt5 X11 Extras library
Summary(pl.UTF-8):	Biblioteka Qt5 X11 Extras
Group:		Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Obsoletes:	qt5-qtx11extas

%description -n Qt5X11Extras
Qt5 X11 Extras library provides classes for developing for the X11
platform.

%description -n Qt5X11Extras -l pl.UTF-8
Biblioteka Qt5 X11 Extras dostarcza klasy do tworzenia oprogramowania
dla platformy X11.

%package -n Qt5X11Extras-devel
Summary:	Qt5 X11 Extras - development files
Summary(pl.UTF-8):	Biblioteka Qt5 X11 Extras - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5X11Extras = %{version}-%{release}
Obsoletes:	qt5-qtx11extas-devel

%description -n Qt5X11Extras-devel
Qt5 X11 Extras - development files.

%description -n Qt5X11Extras-devel -l pl.UTF-8
Biblioteka Qt5 X11 Extras - pliki programistyczne.

%package doc
Summary:	Qt5 X11 Extras documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 X11 Extras w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%{?noarchpackage}

%description doc
Qt5 X11 Extras documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do biblioteki Qt5 X11 Extras w formacie HTML.

%package doc-qch
Summary:	Qt5 X11 Extras documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 X11 Extras w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%{?noarchpackage}

%description doc-qch
Qt5 X11 Extras documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do biblioteki Qt5 X11 Extras w formacie QCH.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}

%build
qmake-qt5
%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5X11Extras -p /sbin/ldconfig
%postun	-n Qt5X11Extras -p /sbin/ldconfig

%files -n Qt5X11Extras
%defattr(644,root,root,755)
%doc LICENSE.GPL3-EXCEPT dist/changes-*
%attr(755,root,root) %{_libdir}/libQt5X11Extras.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5X11Extras.so.5

%files -n Qt5X11Extras-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5X11Extras.so
%{_libdir}/libQt5X11Extras.prl
%{_includedir}/qt5/QtX11Extras
%{_pkgconfigdir}/Qt5X11Extras.pc
%{_libdir}/cmake/Qt5X11Extras
%{qt5dir}/mkspecs/modules/qt_lib_x11extras.pri
%{qt5dir}/mkspecs/modules/qt_lib_x11extras_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtx11extras

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtx11extras.qch
%endif
