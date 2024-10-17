Summary:	Active Directory administration utility for Unix
Name:		adtool
Version:	1.3.3
Release:	3
License:	GPLv2
Group:		File tools
URL:		https://www.gp2x.org/adtool/
Source0:	http://www.gp2x.org/adtool/%{name}-%{version}.tar.gz
BuildRequires:	gdbm-devel
BuildRequires:	openldap-devel
BuildRequires:	sasl-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
adtool is a unix command line utility for Active Directory
administration. Features include user and group creation,
deletion, modification, password setting and directory query and
search capabilities. 

%prep

%setup -q

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


%changelog
* Mon Nov 09 2009 Jérôme Brenier <incubusss@mandriva.org> 1.3.3-1mdv2010.1
+ Revision: 463837
- update to new version 1.3.3
- drop P0 (merged upstream)

* Fri Jun 12 2009 Jérôme Brenier <incubusss@mandriva.org> 1.3.2-1mdv2010.0
+ Revision: 385543
- update to new version 1.3.2
- fix URL / Source
- fix license tag

* Sat Sep 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3-10mdv2009.0
+ Revision: 286151
- fix linkage

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild

* Wed Dec 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3-7mdv2008.1
+ Revision: 137969
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 14 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.3-6mdv2008.1
+ Revision: 119818
- rebuild b/c of missing package on ia32

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3-5mdv2008.0
+ Revision: 83845
- rebuild


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-4mdv2007.0
+ Revision: 101601
- Import adtool

* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 1.3-4mdv2007.0
- rebuild

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-3mdk
- rebuilt against openssl-0.9.8a

* Wed Aug 31 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.3-2mdk
- Rebuild for libldap2.3

* Sun May 15 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdk
- 1.3

* Mon Feb 07 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.2-5mdk
- rebuild for ldap2.2_7

* Fri Feb 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2-4mdk
- rebuilt against new openldap libs

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2-3mdk
- fix deps

