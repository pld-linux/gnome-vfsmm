Summary:	C++ wrappers for gnome-vfs
Summary(pl):	Interfejsy C++ dla gnome-vfs
Name:		gnome-vfsmm
Version:	2.5.0
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	bdedd119b50a5e1b1ef0957a5c7bb995
URL:		http://www.gnome.org/
BuildRequires:	glibmm-devel >= 2.3.4
BuildRequires:	gnome-vfs2-devel >= 2.5.6
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
Requires:	glibmm-devel >= 2.3.4
Requires:	gnome-vfs2-devel >= 2.5.6

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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgnomevfsmm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomevfsmm*.so
%{_libdir}/libgnomevfsmm*.la
%{_includedir}/%{name}-2.*
%{_libdir}/%{name}-2.0
%{_libdir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomevfsmm*.a
