%define name ax25-apps
%define version 0.0.6
%define release %mkrel 11

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Applications for kernel AX.25 support (kernel >= 2.2)
Group: Communications
License: GPL
Url: http://ax25.sourceforge.net/
Source: %{name}-%{version}.tar.bz2
Buildrequires: ax25-devel
Buildrequires: libncurses-devel
Buildrequires: glibc-static-devel
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Applications for kernel AX.25 support (kernel >= 2.2).
This package is split off from the previous ax25-utils. 
It contains the following applications : ax25ipd, 
ax25mond, ax25rtctl, ax25rtd, call, listen.

%prep

%setup -q

%build

%configure2_5x --localstatedir=/var

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

