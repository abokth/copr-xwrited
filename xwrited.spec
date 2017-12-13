Name:           xwrited
Version:        2
Release:        0%{?dist}
Summary:        Display write(1) and wall(1) messages as desktop notifications

License:        MIT
URL:            https://code.guido-berhoerster.org/projects/xwrited/
Source0:        https://code.guido-berhoerster.org/projects/xwrited/downloads/xwrited-2.tar.gz

BuildRequires:  dbus-glib-devel glib-devel libutempter-devel libnotify-devel libxslt intltool
#Requires:       

%description
The xwrited utility displays write(1) and wall(1) messages as desktop
notifications. A notification daemon compliant to the freedesktop.org
Desktop Notification Specification draft needs to be running in order
to display the notifications.

%prep
%autosetup


%build
tail -n 23 README >LICENSE
# can't get the makefile to work
touch data/xwrited.1
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make prefix="$RPM_BUILD_ROOT%{_prefix}" sysconfdir="$RPM_BUILD_ROOT%{_sysconfdir}" install
rm -f "$RPM_BUILD_ROOT%{_prefix}/share/man/man1/xwrited.1"

%files
%{_sysconfdir}/xdg/autostart/xwrited.desktop
%{_prefix}/bin/xwrited
%{_prefix}/share/locale/*/LC_MESSAGES/xwrited.mo
%license LICENSE
%doc README NEWS



%changelog
* Tue Dec 12 2017 Alexander Boström <abo@kth.se>
- 
