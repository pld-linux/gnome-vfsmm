Summary:	C++ wrappers for gnome-vfs
Summary(pl):	Interfejsy C++ dla gnome-vfs
Name:		gnome-vfsmm
Version:	1.3.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	0722ecf5b7fd05205405d8fc38cd16f4
URL:		http://www.gnome.org/
BuildRequires:	gnome-vfs2-devel >= 2.3.7
BuildRequires:	gtkmm-devel >= 2.2.7
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for gnome-vfs.

%description -l pl
Interfejsy C++ dla gnome-vfs.

%package devel
Summary:	Devel files for gnome-vfsmm
Summary(pl):	Pliki nag³ówkowe dla gnome-vfsmm
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Devel files for gnome-vfsmm.

%description devel -l pl
Pliki nag³ówkowe dla gnome-vfsmm.

%package static
Summary:	gnome-vfsmm static library
Summary(pl):	Biblioteka statyczna gnome-vfsmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
gnome-vfsmm static library.

%description static -l pl
Biblioteka statyczna gnome-vfsmm.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_libdir}/libgnomevfsmm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-2.0
%{_libdir}/libgnomevfsmm*.la
%{_libdir}/libgnomevfsmm*.so
%{_libdir}/%{name}-2.0
%{_pkgconfigdir}/%{name}-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomevfsmm*.a
