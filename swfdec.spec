%define api 0.8
%define major 0
%define libname %mklibname %name %{api} %{major}
%define develname %mklibname -d %name

Name:		swfdec
Version:	0.8.4
Release:	4
Summary:	Flash animations rendering library
Group:		System/Libraries
License:	LGPLv2+
URL:		http://swfdec.freedesktop.org/
Source0:	http://swfdec.freedesktop.org/download/%name/%api/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(alsa)
BuildRequires:	pkgconfig(liboil-0.3)
BuildRequires:	autoconf2.5 >= 2.58
BuildRequires:	ffmpeg-devel
BuildRequires:  pkgconfig(gstreamer-pbutils-0.10)
BuildRequires:	libgstreamer-devel
BuildRequires:	gtk2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	pkgconfig(libsoup-2.4)
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
Provides:	libswfdec-devel = %{EVRD}
Provides:	swfdec-devel = %{EVRD}
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


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-3mdv2011.0
+ Revision: 615054
- the mass rebuild of 2010.1 packages

* Wed Mar 10 2010 Michael Scherer <misc@mandriva.org> 0.8.4-2mdv2010.1
+ Revision: 517352
- revert back to 0.8.4, as 0.9.2 is a developement version where youtube playback do not work

* Mon Jan 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-0mdv2010.1
+ Revision: 495697
- 0.9.2

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.8.4-2mdv2010.0
+ Revision: 445292
- rebuild

* Mon Dec 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.4-1mdv2009.1
+ Revision: 317476
- update to new version 0.8.4

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-2mdv2009.1
+ Revision: 301590
- rebuilt against new libxcb

* Sat Oct 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 297164
- new version
- update source URL
- update build deps

* Mon Sep 08 2008 Michael Scherer <misc@mandriva.org> 0.8.0-1mdv2009.0
+ Revision: 282546
- new version of swfdec

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 0.7.4-2mdv2009.0
+ Revision: 258051
- fix requires
- use %%makeinstall_std

* Thu Jul 31 2008 Frederic Crozat <fcrozat@mandriva.com> 0.7.4-1mdv2009.0
+ Revision: 257904
- Release 0.7.4
- Disable static libraries
- remove old options not needed anymore

  + Anssi Hannula <anssi@mandriva.org>
    - relax versioned dependency on data package so that libifying actually
      works

* Thu Jun 26 2008 Michael Scherer <misc@mandriva.org> 0.7.2-1mdv2009.0
+ Revision: 229331
- new version 0.7.2

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon May 12 2008 Funda Wang <fwang@mandriva.org> 0.6.6-2mdv2009.0
+ Revision: 206119
- fix libname (confused about libapi and major)

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 0.6.6-1mdv2009.0
+ Revision: 200726
- New version 0.6.6

* Mon Mar 31 2008 Frederic Crozat <fcrozat@mandriva.com> 0.6.2-1mdv2008.1
+ Revision: 191201
- Release 0.6.2 (fixes some crash bugs)

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 177094
- add missing deps
- new version

* Tue Feb 12 2008 Michael Scherer <misc@mandriva.org> 0.5.90-3mdv2008.1
+ Revision: 166306
- add BuildRoot, catched by rpmlint
- rebuild for new libsoup

* Fri Feb 01 2008 Frederic Crozat <fcrozat@mandriva.com> 0.5.90-2mdv2008.1
+ Revision: 161142
- Disable Pulseaudio backend for now, it isn't working as well as expected

* Fri Feb 01 2008 Frederic Crozat <fcrozat@mandriva.com> 0.5.90-1mdv2008.1
+ Revision: 161063
- Release 0.5.90
- Use PulseAudio backend by default

* Mon Jan 21 2008 Funda Wang <fwang@mandriva.org> 0.5.5-2mdv2008.1
+ Revision: 155485
- rebuild

* Tue Dec 18 2007 Frederic Crozat <fcrozat@mandriva.com> 0.5.5-1mdv2008.1
+ Revision: 132138
- Release 0.5.5

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Funda Wang <fwang@mandriva.org> 0.5.4-1mdv2008.1
+ Revision: 110163
- New version 0.5.4

* Sat Oct 13 2007 Funda Wang <fwang@mandriva.org> 0.5.3-1mdv2008.1
+ Revision: 97881
- New version 0.5.3

* Fri Aug 24 2007 Michael Scherer <misc@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 70996
- new version

* Sat Aug 04 2007 Michael Scherer <misc@mandriva.org> 0.5.1-2mdv2008.0
+ Revision: 58763
- bump version of the lib, asked by dev on irc

* Sat Aug 04 2007 Michael Scherer <misc@mandriva.org> 0.5.1-1mdv2008.0
+ Revision: 58757
- version 0.5.1

* Sat Jul 14 2007 Michael Scherer <misc@mandriva.org> 0.5.0-1mdv2008.0
+ Revision: 51907
- 0.5.0

* Sat Jun 09 2007 Michael Scherer <misc@mandriva.org> 0.4.5-1mdv2008.0
+ Revision: 37600
- update to 0.4.5

* Mon Apr 30 2007 Michael Scherer <misc@mandriva.org> 0.4.4-1mdv2008.0
+ Revision: 19489
- upgrade to version 0.4.4 ( with youtube support \o/ )


* Sat Feb 10 2007 Michael Scherer <misc@mandriva.org> 0.4.2-1mdv2007.0
+ Revision: 118671
- fix BuildRequires
- update to 0.4.2

* Mon Jan 15 2007 Michael Scherer <misc@mandriva.org> 0.4.1-1mdv2007.1
+ Revision: 109109
- update to 0.4.1 ( with initial video support )

* Mon Jan 08 2007 Michael Scherer <misc@mandriva.org> 0.4.0-1mdv2007.1
+ Revision: 106087
- remove various macro and no longer needed requires, that caused problem with buildsys
- new url
- new version 0.4.0
- no more gimp and gdk loader, they were not working
- clean the spec
- use %%rel for mkrel
- mozilla-plugin was splitted from main tarball, now in its own SRPM

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - fix gtk macros
    - unpack patch
    - Import swfdec

* Sun Jun 04 2006 Götz Waschk <waschk@mandriva.org> 0.3.6-5mdv2007.0
- fix gtk dep
- fix buildrequires

* Wed May 03 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.6-4mdk
- Rebuild

* Fri Apr 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.6-3mdk
- rebuild to fix mozilla dep

* Thu Jan 19 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.3.6-2mdk
- add missing requires to the mozilla plugin

* Thu Jan 12 2006 Götz Waschk <waschk@mandriva.org> 0.3.6-1mdk
- replace prereq
- drop patch 1
- update patch 0
- New release 0.3.6

* Mon Aug 22 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.3.4-3mdk
- allow build without plugin deps (mozilla, gstreamer-plugins)

* Tue Apr 19 2005 Götz Waschk <waschk@mandriva.org> 0.3.4-2mdk
- fix buildrequires

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 0.3.4-1mdk
- update the patch
- requires new oil
- new version

* Mon Mar 14 2005 Götz Waschk <waschk@linux-mandrake.com> 0.3.2-3mdk
- build with firefox

* Mon Feb 14 2005 Götz Waschk <waschk@linux-mandrake.com> 0.3.2-2mdk
- rebuild for new gimp

* Tue Nov 23 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.2-1mdk
- fix file list
- source URL
- add gimp plugin package
- major 0.3
- needs liboil and gimp
- drop all patches
- new source location
- new version

* Fri Oct 01 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.2.2-8mdk
- libtool fixes

* Thu Aug 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.2-7mdk
- biarch support

* Sun Jun 13 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2.2-6mdk
- fix deps of the mozilla plugin

* Tue May 25 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2.2-5mdk
- mozilla plugin doesn't require mozilla

* Fri May 14 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2.2-4mdk
- fix gtk directory
- 64-bit fixes

