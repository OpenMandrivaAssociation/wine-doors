Name:		wine-doors
Version:	0.1.2
Release:	5

Summary:	Graphical wine frontend
License:	GPL
Group:		Emulators
URL:		http://www.wine-doors.org
Source0:	wine-doors-%{version}.tar.gz

Requires:	libxml2-python python pygtk2.0 pygtk2.0-libglade
Requires:	python-cairo python-mate-rsvg python-mate-rsvg
Requires:	gnome-python-desktop
Requires:	cabextract
Requires:	wine
BuildRequires:	python pygtk2.0 pygtk2.0-libglade
BuildRequires:	gnome-python-desktop
BuildRequires:	wine
BuildRequires:	cabextract
BuildRequires:	desktop-file-utils
BuildArch:	noarch

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
python setup.py install --sysinstall --root=%{buildroot}

# fix menu
desktop-file-install \
  --remove-category="Applications" \
  --remove-category="Wine" \
  --add-category="GNOME" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%files
%doc LICENSE README
%{_bindir}/wine-doors
%{_datadir}/wine-doors/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%config(noreplace) %{_sysconfdir}/wine-doors/preferences.xml
