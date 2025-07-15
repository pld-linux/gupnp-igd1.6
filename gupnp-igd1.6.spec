#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	Library to handle UPnP IGD port mapping
Summary(pl.UTF-8):	Biblioteka do obsługi odwzorowywania portów IGD dla UPnP
Name:		gupnp-igd1.6
Version:	1.6.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/gupnp-igd/1.6/gupnp-igd-%{version}.tar.xz
# Source0-md5:	87e2a870fe2f53b2a3f6a51ae5d17596
URL:		https://wiki.gnome.org/Projects/GUPnP
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.70
BuildRequires:	gobject-introspection-devel >= 0.10
BuildRequires:	gssdp1.6-devel >= 1.6.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.10}
BuildRequires:	gupnp1.6-devel >= 1.6.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.70
Requires:	gssdp1.6 >= 1.6.0
Requires:	gupnp1.6 >= 1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to handle UPnP Internet Gateway Device port mappings.

%description -l pl.UTF-8
Biblioteka do obsługi odwzorowywania portów IGD (Internet Gateway
Device - bramek internetowych) dla UPnP.

%package devel
Summary:	Header files for gupnp-igd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gupnp-igd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.70
Requires:	gssdp1.6-devel >= 1.6.0
Requires:	gupnp1.6-devel >= 1.6.0

%description devel
Header files for gupnp-igd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gupnp-igd.

%package static
Summary:	Static gupnp-igd library
Summary(pl.UTF-8):	Statyczna biblioteka gupnp-igd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gupnp-igd library.

%description static -l pl.UTF-8
Statyczna biblioteka gupnp-igd.

%package apidocs
Summary:	gupnp-igd library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gupnp-igd
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
gupnp-igd library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gupnp-igd.

%prep
%setup -q -n gupnp-igd-%{version}

%build
%meson \
	%{?with_apidocs:-Dgtk_doc=true}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%if %{with apidocs}
# make it parallel-installable with gupnp-igd 1.0/1.2
%{__mv} $RPM_BUILD_ROOT%{_gtkdocdir}/{gupnp-igd,gupnp-igd-1.6}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libgupnp-igd-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-igd-1.6.so.0
%{_libdir}/girepository-1.0/GUPnPIgd-1.6.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-igd-1.6.so
%{_includedir}/gupnp-igd-1.6
%{_pkgconfigdir}/gupnp-igd-1.6.pc
%{_datadir}/gir-1.0/GUPnPIgd-1.6.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-igd-1.6.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-igd-1.6
%endif
