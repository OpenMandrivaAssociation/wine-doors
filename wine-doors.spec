Name:    wine-doors
Version: 0.1.2
Release: %mkrel 4

Summary: Graphical wine frontend
License: GPL
Group:   Emulators
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:     https://www.wine-doors.org
Source:  wine-doors-%{version}.tar.gz

Requires: libxml2-python, python, pygtk2.0, pygtk2.0-libglade
Requires: gnome-python-desktop
Requires: cabextract
Requires: python-cairo
Requires: wine
BuildRequires: python, pygtk2.0, pygtk2.0-libglade
BuildRequires: gnome-python-desktop
BuildRequires: wine
BuildRequires: cabextract
BuildRequires: desktop-file-utils
# BuildArch: noarch
ExclusiveArch:  %{ix86}

%description
Wine doors is an application designed to assist users in obtaining, installing,
uninstalling and working around the caveats associated with wine applications.
Using a web service to connect users to applications means wine-doors can be
community managed thus splitting application installation and configuration
from the user interface used to install the applications. 

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT
python setup.py install --sysinstall --root=$RPM_BUILD_ROOT

# fix menu
desktop-file-install \
  --remove-category="Applications" \
  --remove-category="Wine" \
  --add-category="GNOME" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE README
%{_bindir}/wine-doors
%{_datadir}/wine-doors/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%config(noreplace) %{_sysconfdir}/wine-doors/preferences.xml


%changelog
* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.2-4mdv2009.0
+ Revision: 261987
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.2-3mdv2009.0
+ Revision: 256025
- rebuild
- fix no-buildroot-tag

* Fri Jan 25 2008 Austin Acton <austin@mandriva.org> 0.1.2-1mdv2008.1
+ Revision: 158034
- exclusivearch ix86
- import wine-doors


