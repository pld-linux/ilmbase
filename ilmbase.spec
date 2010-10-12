Summary:	IlmBase - base math and exception libraries from OpenEXR project
Summary(pl.UTF-8):	IlmBase - podstawowe biblioteki matematyczne i wyjątków z projektu OpenEXR
Name:		ilmbase
Version:	1.0.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.savannah.nongnu.org/releases/openexr/%{name}-%{version}.tar.gz
# Source0-md5:	26c133ee8ca48e1196fbfb3ffe292ab4
Patch0:		%{name}-link.patch
Patch1:		%{name}-sh.patch
Patch2:		%{name}-gcc4.patch
URL:		http://www.openexr.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6.3
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IlmBase consists of the following libraries:

Half is a class that encapsulates our 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.  It currently supports pthreads and
Windows threads.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%description -l pl.UTF-8
IlmBase składa się z następujących bibliotek:

Half to klasa obudowująca 16-bitowy format zmiennoprzecinkowy.

IlmThread to biblioteka abstrakcji wątków przeznaczona dla OpenEXR i
innych pakietów oprogramowania. Aktualnie obsługuje standard pthreads
oraz wątki Windows.

Imath implementuje wektory 2D i 3D, macierze 3x3 i 4x4, kwaterniony i
inne przydatne funkcje matematyczne 2D i 3D.

Iex to biblioteka obsługi wyjątków.

%package devel
Summary:	Header files for IlmBase libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek IlmBase
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Conflicts:	OpenEXR-devel < 1.5.0

%description devel
Header files for IlmBase libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek IlmBase.

%package static
Summary:	Static IlmBase libraries
Summary(pl.UTF-8):	Statyczne biblioteki IlmBase
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	OpenEXR-static < 1.5.0

%description static
Static IlmBase libraries.

%description static -l pl.UTF-8
Statyczne biblioteki IlmBase.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
# no autoheader - missing templates
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libHalf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libHalf.so.6
%attr(755,root,root) %{_libdir}/libIex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIex.so.6
%attr(755,root,root) %{_libdir}/libIlmThread.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmThread.so.6
%attr(755,root,root) %{_libdir}/libImath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libImath.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libHalf.so
%attr(755,root,root) %{_libdir}/libIex.so
%attr(755,root,root) %{_libdir}/libIlmThread.so
%attr(755,root,root) %{_libdir}/libImath.so
%{_libdir}/libHalf.la
%{_libdir}/libIex.la
%{_libdir}/libIlmThread.la
%{_libdir}/libImath.la
%dir %{_includedir}/OpenEXR
%{_includedir}/OpenEXR/Iex*.h
%{_includedir}/OpenEXR/IlmBaseConfig.h
%{_includedir}/OpenEXR/IlmThread*.h
%{_includedir}/OpenEXR/Imath*.h
%{_includedir}/OpenEXR/half*.h
%{_pkgconfigdir}/IlmBase.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libHalf.a
%{_libdir}/libIex.a
%{_libdir}/libIlmThread.a
%{_libdir}/libImath.a
