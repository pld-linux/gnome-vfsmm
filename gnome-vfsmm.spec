#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	C++ wrappers for gnome-vfs
Summary(pl.UTF-8):	Interfejsy C++ dla gnome-vfs
Name:		gnome-vfsmm
Version:	2.26.0
Release:	3
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-vfsmm/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	d27d34b6a8722c557366729071c1baab
URL:		https://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	glibmm-devel >= 2.14.0
BuildRequires:	gnome-vfs2-devel >= 2.24.0
BuildRequires:	graphviz
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	pkgconfig
Requires:	glibmm >= 2.14.0
Requires:	gnome-vfs2-libs >= 2.24.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for gnome-vfs.

%description -l pl.UTF-8
Interfejsy C++ dla gnome-vfs.

%package devel
Summary:	Devel files for gnome-vfsmm
Summary(pl.UTF-8):	Pliki nagłówkowe dla gnome-vfsmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.14.0
Requires:	gnome-vfs2-devel >= 2.24.0

%description devel
Devel files for gnome-vfsmm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gnome-vfsmm.

%package static
Summary:	gnome-vfsmm static library
Summary(pl.UTF-8):	Biblioteka statyczna gnome-vfsmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gnome-vfsmm static library.

%description static -l pl.UTF-8
Biblioteka statyczna gnome-vfsmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgnomevfsmm-2.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomevfsmm-2.6.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomevfsmm-2.6.so
%{_includedir}/gnome-vfsmm-2.6
%{_libdir}/gnome-vfsmm-2.6
%{_pkgconfigdir}/gnome-vfsmm-2.6.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomevfsmm-2.6.a
%endif
