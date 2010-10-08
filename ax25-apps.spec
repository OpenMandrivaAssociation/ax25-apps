%define name	ax25-apps
%define version	0.0.8
%define prerel	rc2
%define release	1

Name:		%{name}
Version:	%{version}
Release:	%mkrel -c %{prerel} %{release}
Summary:	Applications for kernel AX.25 support
Group:		Communications
License:	GPLv2+
Url:		http://www.linux-ax25.org/wiki/LinuxAX25
Source:		http://www.linux-ax25.org/pub/ax25-apps/%{name}-%{version}-%{prerel}.tar.gz
Buildrequires:	ax25-devel
Buildrequires:	libncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Applications for kernel AX.25 support.

This package is split off from the previous ax25-utils and contains the
following applications : ax25ipd, ax25mond, ax25rtctl, ax25rtd, call, listen.

%prep
%setup -q -n %{name}-%{version}-%{prerel}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std installconf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}/*
%doc README NEWS AUTHORS ChangeLog
%dir %{_sysconfdir}/ax25
%config(noreplace) %{_sysconfdir}/ax25/ax25ipd.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25mond.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25rtd.conf
%{_bindir}/call
%{_bindir}/listen
%{_sbindir}/ax25*
%{_mandir}/*/*
