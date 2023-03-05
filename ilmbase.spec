Summary:	IlmBase - base math and exception libraries from OpenEXR project
Summary(pl.UTF-8):	IlmBase - podstawowe biblioteki matematyczne i wyjątków z projektu OpenEXR
Name:		ilmbase
Version:	2.3.0
Release:	2
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/AcademySoftwareFoundation/openexr/releases
Source0:	https://github.com/AcademySoftwareFoundation/openexr/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	354bf86de3b930ab87ac63619d60c860
Patch0:		%{name}-link.patch
Patch1:		%{name}-sh.patch
URL:		https://openexr.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6.3
# C++ 03, 11, 14, 17 possible, but configure defaults to 14
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IlmBase consists of the following libraries:

Half is a class that encapsulates our 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.  It currently supports pthreads and
Windows threads.

Iex is an exception-handling library.

%description -l pl.UTF-8
IlmBase składa się z następujących bibliotek:

Half to klasa obudowująca 16-bitowy format zmiennoprzecinkowy.

IlmThread to biblioteka abstrakcji wątków przeznaczona dla OpenEXR i
innych pakietów oprogramowania. Aktualnie obsługuje standard pthreads
oraz wątki Windows.

Iex to biblioteka obsługi wyjątków.

%package devel
Summary:	Header files for IlmBase libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek IlmBase
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:5
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

# see Imath package
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libImath* $RPM_BUILD_ROOT%{_includedir}/OpenEXR/Imath*.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.md
%attr(755,root,root) %{_libdir}/libHalf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libHalf.so.24
%attr(755,root,root) %{_libdir}/libIex-2_3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIex-2_3.so.24
%attr(755,root,root) %{_libdir}/libIexMath-2_3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIexMath-2_3.so.24
%attr(755,root,root) %{_libdir}/libIlmThread-2_3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmThread-2_3.so.24

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libHalf.so
%attr(755,root,root) %{_libdir}/libIex.so
%attr(755,root,root) %{_libdir}/libIexMath.so
%attr(755,root,root) %{_libdir}/libIlmThread.so
%{_libdir}/libHalf.la
%{_libdir}/libIex.la
%{_libdir}/libIexMath.la
%{_libdir}/libIlmThread.la
%dir %{_includedir}/OpenEXR
%{_includedir}/OpenEXR/Iex*.h
%{_includedir}/OpenEXR/IlmBaseConfig.h
%{_includedir}/OpenEXR/IlmThread*.h
%{_includedir}/OpenEXR/half*.h
%{_pkgconfigdir}/IlmBase.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libHalf.a
%{_libdir}/libIex.a
%{_libdir}/libIexMath.a
%{_libdir}/libIlmThread.a
