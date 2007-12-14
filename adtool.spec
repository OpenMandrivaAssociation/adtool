Summary:	Active Directory administration utility for Unix
Name:		adtool
Version:	1.3
Release:	%mkrel 6
License:	GPL
Group:		File tools
URL:		http://dexy.mine.nu/adtool/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	gdbm-devel
BuildRequires:	openldap-devel
BuildRequires:	libsasl-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
adtool is a unix command line utility for Active Directory
administration. Features include user and group creation,
deletion, modification, password setting and directory query and
search capabilities. 

%prep

%setup -q

%build

%configure2_5x \
    --with-ldap=%{_prefix}

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

mv %{buildroot}%{_sysconfdir}/adtool.cfg.dist %{buildroot}%{_sysconfdir}/adtool.cfg

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO tests/test.sh
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/adtool.cfg
%{_bindir}/adtool
%{_mandir}/man1/adtool.1*
