%define name swfdec
%define version 0.8.4
%define api 0.8
%define major 0
%define libname %mklibname %name %{api} %{major}
%define develname %mklibname -d %name
%define rel 1

Name:		%name
Version:	%version
Release:	%mkrel %rel 
Summary:	Flash animations rendering library
Group:		System/Libraries
License:	LGPLv2+
URL:		http://swfdec.freedesktop.org/
Source0:	http://swfdec.freedesktop.org/download/%name/%api/%{name}-%{version}.tar.gz
BuildRequires:  libxt-devel
BuildRequires:  libmad-devel
BuildRequires:  libalsa-devel
BuildRequires:	liboil-devel >= 0.3
BuildRequires:	autoconf2.5 >= 2.58
BuildRequires:	ffmpeg-devel
BuildRequires:  pkgconfig(gstreamer-pbutils-0.10)
BuildRequires:	libgstreamer-devel
BuildRequires:	gtk2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libsoup-2.4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
Libswfdec is a library for rendering Flash animations. Currently it
handles mostFlash 3 animations and some Flash 4. No interactivity is
supported yet.

%package -n %libname
Summary: Shared library for decoding Flash animations
Group: System/Libraries
Obsoletes: %mklibname swfdec 0.6

%description -n %libname
Libswfdec is a library for rendering Flash animations. Currently it
handles mostFlash 3 animations and some Flash 4. No interactivity is
supported yet.

This package contains the shared library needed to run libswfdec
applications.

%package -n %develname
Summary:	Swfdec development files and static libraries
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	libswfdec-devel = %version-%release
Provides:	swfdec-devel = %version-%release
Obsoletes:	%mklibname -d %name 0.5

%description -n %develname
This contains the files needed to build packages that depend on
swfdec.

%prep
%setup -q 

%build
%configure2_5x --disable-static 
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libswfdec-%{api}.so.%{major}*
%{_libdir}/libswfdec-gtk-%{api}.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/libswfdec-%api.so
%{_libdir}/libswfdec-gtk-%api.so
%{_libdir}/libswfdec-%api.la
%{_libdir}/libswfdec-gtk-%api.la
%{_libdir}/pkgconfig/swfdec-%api.pc
%{_libdir}/pkgconfig/swfdec-gtk-%api.pc
%dir %{_includedir}/swfdec-%api/
%{_includedir}/swfdec-%api/*
%_datadir/gtk-doc/html/%name/
