Name: 	 	getlive
Summary: 	Fetches mail from a Hotmail or Hotmail Live account
Version: 	0.59
Release: 	3
Epoch:		1
Source:		http://jaist.dl.sourceforge.net/sourceforge/getlive/%{name}-%{version}.tgz
URL:		http://sourceforge.net/projects/getlive/
License:	GPLv2
Group:		Networking/Mail
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	curl
BuildArch:	noarch
Obsoletes:	gotmail
Provides:	gotmail

%description
GetLive is a perl script that fetches mail from your Hotmail or Hotmail
Live account. The mail is then presented to any filter (typically
procmail) for further processing or dropping in a local mailbox.

The scripts keeps track of all downloaded message-ids to avoid double
fetching.

Messages can be marked read or moved to a folder after being downloaded.

%prep
%setup -q 

%build
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%_bindir
install -m 755 GetLive.pl %{buildroot}/%_bindir/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog License Manual
%{_bindir}/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.59-2mdv2011.0
+ Revision: 610843
- rebuild

* Fri Apr 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 1:0.59-1mdv2010.1
+ Revision: 530787
- update to 0.59

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1:0.8-4mdv2010.0
+ Revision: 429193
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1:0.8-3mdv2009.0
+ Revision: 245943
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1:0.8-1mdv2008.1
+ Revision: 140735
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 19 2007 Funda Wang <fwang@mandriva.org> 1:0.8-1mdv2008.0
+ Revision: 53579
- New version
- getlive replaced gotmail

  + Jérôme Soyer <saispo@mandriva.org>
    - Import gotmail



* Sat Apr 29 2006 Austin Acton <austin@mandriva.org> 0.8.9-1mdk
- New release 0.8.9

* Mon Mar  6 2006 Austin Acton <austin@mandriva.org> 0.8.8-1mdk
- initial package
