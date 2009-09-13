Summary:	Querying sensor data /temperatures, voltages, fan speeds, .../ via libsensors
Summary(hu.UTF-8):	Szenzor adatok (hőmérséklet, feszültség, ventilátor-sebesség, ...) lekérdezése libsensor-on keresztül
Name:		lua-sensors
Version:	0.1.0
Release:	1
License:	BSD-like
Group:		Development/Languages
Patch0:		%{name}-makefile.patch
Source0:	http://luaforge.net/frs/download.php/4243/%{name}-%{version}.tar.gz
# Source0-md5:	f5bc6d17938df925cbdb8388fb53be6d
URL:		http://luaforge.net/projects/lua-sensors/
BuildRequires:	lua51-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Querying sensor data /temperatures, voltages, fan speeds, .../ via
libsensors.

%description -l hu.UTF-8
Szenzor adatok (hőmérséklet, feszültség, ventilátor-sebesség, ...)
lekérdezése libsensor-on keresztül.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_libdir}}/lua/5.1
install print_r.lua sensors.lua $RPM_BUILD_ROOT%{_datadir}/lua/5.1
install libsensors.so $RPM_BUILD_ROOT%{_libdir}/lua/5.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc API.txt Changes README test1.lua test2.lua
%{_libdir}/lua/5.1/libsensors.so
%attr(755,root,root) %{_datadir}/lua/5.1/*
