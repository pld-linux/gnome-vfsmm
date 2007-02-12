Summary:	C++ wrappers for gnome-vfs
Summary(pl.UTF-8):   Interfejsy C++ dla gnome-vfs
Name:		gnome-vfsmm
Version:	2.16.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-vfsmm/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	246ddae8dd588d250be2c3a8b13503b4
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel >= 2.12.3
BuildRequires:	gnome-vfs2-devel >= 2.16.3
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	pkgconfig
Requires:	glibmm >= 2.12.3
Requires:	gnome-vfs2-libs >= 2.16.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for gnome-vfs.

%description -l pl.UTF-8
Interfejsy C++ dla gnome-vfs.

%package devel
Summary:	Devel files for gnome-vfsmm
Summary(pl.UTF-8):   Pliki nagłówkowe dla gnome-vfsmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.12.3
Requires:	gnome-vfs2-devel >= 2.16.3

%description devel
Devel files for gnome-vfsmm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gnome-vfsmm.

%package static
Summary:	gnome-vfsmm static library
Summary(pl.UTF-8):   Biblioteka statyczna gnome-vfsmm
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
	--enable-static=yes

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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgnomevfsmm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomevfsmm*.so
%{_libdir}/libgnomevfsmm*.la
%{_includedir}/%{name}-2.*
%{_libdir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomevfsmm*.a
