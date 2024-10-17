Name: meego-panel-people
Summary: People panel for MeeGo
Group: Graphical desktop/Other 
Version: 0.2.4
License: LGPL 2.1
URL: https://www.meego.com
Release: %mkrel 1
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: anerley-devel
BuildRequires: gtk2-devel
BuildRequires: nbtk-devel
BuildRequires: meego-panel-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: libbonobo2_x-devel
Obsoletes: moblin-panel-people <= 0.0.10

%description
MeeGo people panel

%prep
%setup -q

%build
%configure2_5x \
  --disable-static \
  --with-online=connman

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS ChangeLog
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service
%{_datadir}/mutter-meego/panels/meego-panel-people.desktop
%{_datadir}/telepathy/clients/*
