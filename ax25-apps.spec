%define name ax25-apps
%define version 0.0.6
%define release %mkrel 10

Name: %{name}
Summary: Applications for kernel AX.25 support (kernel >= 2.2)
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Group: Communications
Url: http://ax25.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
Requires: libax25_0 >= 0.0.9  
Buildrequires: ax25-devel libncurses-devel glibc-static-devel

%description
Applications for kernel AX.25 support (kernel >= 2.2).
This package is split off from the previous ax25-utils. 
It contains the following applications : ax25ipd, 
ax25mond, ax25rtctl, ax25rtd, call, listen.

%prep

%setup -q

%build

%configure --localstatedir=/var

%make

%install

%makeinstall installconf

mkdir -p $RPM_BUILD_ROOT/var/ax25/ax25rtd

rm -rf $RPM_BUILD_ROOT/%_docdir/ax25-apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%dir %{_sysconfdir}/ax25
%dir /var/ax25/ax25rtd
%config(noreplace) %{_sysconfdir}/ax25/ax25ipd.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25mond.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25rtd.conf
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/*/*

