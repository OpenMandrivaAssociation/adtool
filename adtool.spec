Summary:	Active Directory administration utility for Unix
Name:		adtool
Version:	1.3
Release:	%mkrel 10
License:	GPL
Group:		File tools
URL:		http://dexy.mine.nu/adtool/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		adtool-linkage_fix.diff
BuildRequires:	gdbm-devel
BuildRequires:	openldap-devel
BuildRequires:	libsasl-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
adtool is a unix command line utility for Active Directory
administration. Features include user and group creation,
deletion, modification, password setting and directory query and
search capabilities. 

%prep

%setup -q
%patch0 -p0

# lib64 fix
perl -pi -e "s|/lib |/%{_lib} |g" configure*

%build
autoreconf -fis

%configure2_5x \
    --with-ldap=%{_prefix}

%make

%install
rm -rf %{buildroot}

%makeinstall

mv %{buildroot}%{_sysconfdir}/adtool.cfg.dist %{buildroot}%{_sysconfdir}/adtool.cfg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO tests/test.sh
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/adtool.cfg
%{_bindir}/adtool
%{_mandir}/man1/adtool.1*
