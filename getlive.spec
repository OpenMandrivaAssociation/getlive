%define name	getlive
%define version	0.8
%define release %mkrel 1
%define oname GetLive
%define oversion %(echo %version |sed -e 's|\\.|_|')

Name: 	 	%{name}
Summary: 	Fetches mail from a Hotmail or Hotmail Live account
Version: 	%{version}
Release: 	%{release}
Epoch:		1
Source:		http://jaist.dl.sourceforge.net/sourceforge/getlive/%{oname}_%{oversion}.tgz
URL:		http://sourceforge.net/projects/getlive/
License:	GPL
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
%setup -q -c

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
