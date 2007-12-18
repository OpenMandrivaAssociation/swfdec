%define name swfdec
%define version 0.5.5
%define major 0.5
%define libname %mklibname %name %{major}
%define develname %mklibname -d %name
%define rel 1

Name:		%name
Version:	%version
Release:	%mkrel %rel 
Summary:	Flash animations rendering library
Group:		System/Libraries
License:	LGPL
URL:		http://swfdec.freedesktop.org/
Source0:	http://swfdec.freedesktop.org/download/%name/%major/%{name}-%{version}.tar.gz
Source1:	http://swfdec.freedesktop.org/download/%name/%major/%{name}-%{version}.md5sum
BuildRequires:  libxt-devel
BuildRequires:  libmad-devel
BuildRequires:  gimp2-devel libalsa-devel
BuildRequires:	liboil-devel >= 0.3
BuildRequires:	autoconf2.5 >= 2.58
BuildRequires:	ffmpeg-devel
BuildRequires:	libgstreamer-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libsoup-2.2-devel
%description
Libswfdec is a library for rendering Flash animations. Currently it
handles mostFlash 3 animations and some Flash 4. No interactivity is
supported yet.

%package -n %libname
Summary: Shared library for decoding Flash animations
Group: System/Libraries
Requires: %name = %version

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
export CFLAGS="%optflags -DMOZ_X11"
%configure2_5x --enable-shared 
#gw parallel build does not work
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall 
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f %buildroot/%{_iconsdir}/hicolor/icon-theme.cache
#

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%files
%defattr(-,root,root)
%{_iconsdir}/hicolor/*/*/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libswfdec-%major.so.*
%{_libdir}/libswfdec-gtk-%major.so.*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/libswfdec-%major.a
%{_libdir}/libswfdec-gtk-%major.a
%{_libdir}/libswfdec-%major.so
%{_libdir}/libswfdec-gtk-%major.so
%{_libdir}/pkgconfig/swfdec-%major.pc
%{_libdir}/pkgconfig/swfdec-gtk-%major.pc
%dir %{_includedir}/swfdec-%major/
%{_includedir}/swfdec-%major/*
%_datadir/gtk-doc/html/%name/
