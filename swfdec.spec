%define api 0.8
%define major 0
%define libname %mklibname %name %{api} %{major}
%define develname %mklibname -d %name

Name:		swfdec
Version:	0.8.4
Release:	5
Summary:	Flash animations rendering library
Group:		System/Libraries
License:	LGPLv2+
URL:		http://swfdec.freedesktop.org/
Source0:	http://swfdec.freedesktop.org/download/%name/%api/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(liboil-0.3)
BuildRequires:	autoconf2.5 >= 2.58
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(gstreamer-pbutils-0.10)
BuildRequires:	libgstreamer-devel
BuildRequires:	gtk2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	pkgconfig(libsoup-2.4)
%description
Libswfdec is a library for rendering Flash animations. Currently it
handles mostFlash 3 animations and some Flash 4. No interactivity is
supported yet.

%package -n %libname
Summary:	Shared library for decoding Flash animations
Group:		System/Libraries
Obsoletes:	%mklibname swfdec 0.6

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
Provides:	libswfdec-devel = %{EVRD}
Provides:	swfdec-devel = %{EVRD}
Obsoletes:	%mklibname -d %name 0.5

%description -n %develname
This contains the files needed to build packages that depend on
swfdec.

%prep
%setup -q 

%build
%configure --disable-static 
%make

%install
%makeinstall_std

%files -n %libname
%{_libdir}/libswfdec-%{api}.so.%{major}*
%{_libdir}/libswfdec-gtk-%{api}.so.%{major}*

%files -n %develname
%{_libdir}/libswfdec-%api.so
%{_libdir}/libswfdec-gtk-%api.so
%{_libdir}/pkgconfig/swfdec-%api.pc
%{_libdir}/pkgconfig/swfdec-gtk-%api.pc
%dir %{_includedir}/swfdec-%api/
%{_includedir}/swfdec-%api/*
%_datadir/gtk-doc/html/%name/

