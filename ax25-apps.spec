%define prerel	rc2
%define release	4

Name:		ax25-apps
Version:	0.0.8
Release:	%mkrel -c %{prerel} %{release}
Summary:	Applications for kernel AX.25 support
Group:		Communications
#ax25ipd is BSD licensed, rest is GPLv2+
License:	GPLv2+ and BSD
Url:		http://www.linux-ax25.org/wiki/LinuxAX25
Source:		http://www.linux-ax25.org/pub/ax25-apps/%{name}-%{version}-%{prerel}.tar.gz
Patch0:		ax25-apps-0.0.8-nongenericnames.patch
BuildRequires:	ax25-devel
BuildRequires:	pkgconfig(ncurses)

%description
Applications for kernel AX.25 support.

This package is split off from the previous ax25-utils and contains the
following applications : ax25ipd, ax25mond, ax25rtctl, ax25rtd, axcall,
axlisten.

%prep
%setup -q -n %{name}-%{version}-%{prerel}
%patch0 -p1 -b .nongenericnames

%build
sed -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/g' configure.ac
autoreconf -vfi
%configure2_5x
%make

%install
%makeinstall_std installconf

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog
%dir %{_sysconfdir}/ax25
%config(noreplace) %{_sysconfdir}/ax25/ax25ipd.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25mond.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25rtd.conf
%{_bindir}/ax*
%{_sbindir}/ax25*
%{_mandir}/*/*


%changelog
* Fri Oct 08 2010 Jani Välimaa <wally@mandriva.org> 0.0.8-0.rc2.2mdv2011.0
+ Revision: 584222
- fix license

* Fri Oct 08 2010 Jani Välimaa <wally@mandriva.org> 0.0.8-0.rc2.1mdv2011.0
+ Revision: 584221
- add patch (thanks goes to debian maintainers)
- fix file list
- fix description
- new version 0.0.8 rc2
- clean spec
- fix license

* Wed Oct 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.6-11mdv2010.0
+ Revision: 455737
- no need for explicit dependencies, especially when they prevent x86_64 installation

  + Thierry Vignaud <tv@mandriva.org>
    - use %%configure2_5x
    - rebuild
    - rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.0.6-8mdv2009.0
+ Revision: 243099
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.0.6-6mdv2008.1
+ Revision: 135826
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import ax25-apps


* Mon Jul 31 2006 Lenny Cartier <lenny@mandrakesoft.com> 0.0.6-6mdv2007.0
- rebuild

* Thu Aug 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.0.6-5mdk
- rebuild

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.0.6-4mdk
- rebuild

* Sat Apr 26 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.6-3mdk
- adjust buildrequires

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.6-2mdk
- rebuild

* Thu May 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.0.6-1mdk
- refresh requires & builrequires
- fix group
- submitted by Laurent Grawet <laurent.grawet@ibelgique.com>
