Summary:	A SUID sandbox program
Name:		firejail
Version:	0.9.36
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	https://github.com/netblue30/firejail/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	98a5b96118822aae423528cfe22b4a3c
URL:		https://github.com/netblue30/firejail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firejail is a SUID security sandbox program that reduces the risk of
security breaches by restricting the running environment of untrusted
applications using Linux namespaces and seccomp-bpf. It allows a
process and all its descendants to have their own private view of the
globally shared kernel resources, such as the network stack, process
table, and mount table.

%prep
%setup -qn %{name}-%{version}

# Fix libdir.
sed -i -e 's#/usr/lib#%{_libdir}#g' etc/disable-devel.inc

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod +x $RPM_BUILD_ROOT%{_libdir}/firejail/*.so

# Install documentation ourselves.
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%files
%defattr(644,root,root,755)
%doc README README.md RELNOTES
%doc COPYING

%attr(4755,root,root) %{_bindir}/firejail
%attr(755,root,root) %{_bindir}/firemon
%dir %{_datadir}/bash-completion
%dir %{bash_compdir}
%{bash_compdir}/firejail
%{bash_compdir}/firemon
%{_mandir}/man1/firejail.1*
%{_mandir}/man1/firemon.1*
%{_mandir}/man5/firejail-login.5*
%{_mandir}/man5/firejail-profile.5*

%dir %{_libdir}/firejail
%{_libdir}/firejail/fshaper.sh
%{_libdir}/firejail/ftee
%{_libdir}/firejail/libtrace.so
%{_libdir}/firejail/libtracelog.so

%dir %{_sysconfdir}/firejail
%config(noreplace) %{_sysconfdir}/firejail/audacious.profile
%config(noreplace) %{_sysconfdir}/firejail/bitlbee.profile
%config(noreplace) %{_sysconfdir}/firejail/chromium-browser.profile
%config(noreplace) %{_sysconfdir}/firejail/chromium.profile
%config(noreplace) %{_sysconfdir}/firejail/clementine.profile
%config(noreplace) %{_sysconfdir}/firejail/conkeror.profile
%config(noreplace) %{_sysconfdir}/firejail/deadbeef.profile
%config(noreplace) %{_sysconfdir}/firejail/deluge.profile
%config(noreplace) %{_sysconfdir}/firejail/disable-common.inc
%config(noreplace) %{_sysconfdir}/firejail/disable-devel.inc
%config(noreplace) %{_sysconfdir}/firejail/disable-mgmt.inc
%config(noreplace) %{_sysconfdir}/firejail/disable-secret.inc
%config(noreplace) %{_sysconfdir}/firejail/dnscrypt-proxy.profile
%config(noreplace) %{_sysconfdir}/firejail/dropbox.profile
%config(noreplace) %{_sysconfdir}/firejail/empathy.profile
%config(noreplace) %{_sysconfdir}/firejail/evince.profile
%config(noreplace) %{_sysconfdir}/firejail/fbreader.profile
%config(noreplace) %{_sysconfdir}/firejail/filezilla.profile
%config(noreplace) %{_sysconfdir}/firejail/firefox.profile
%config(noreplace) %{_sysconfdir}/firejail/generic.profile
%config(noreplace) %{_sysconfdir}/firejail/gnome-mplayer.profile
%config(noreplace) %{_sysconfdir}/firejail/google-chrome-beta.profile
%config(noreplace) %{_sysconfdir}/firejail/google-chrome-stable.profile
%config(noreplace) %{_sysconfdir}/firejail/google-chrome-unstable.profile
%config(noreplace) %{_sysconfdir}/firejail/google-chrome.profile
%config(noreplace) %{_sysconfdir}/firejail/hexchat.profile
%config(noreplace) %{_sysconfdir}/firejail/icecat.profile
%config(noreplace) %{_sysconfdir}/firejail/icedove.profile
%config(noreplace) %{_sysconfdir}/firejail/iceweasel.profile
%config(noreplace) %{_sysconfdir}/firejail/login.users
%config(noreplace) %{_sysconfdir}/firejail/midori.profile
%config(noreplace) %{_sysconfdir}/firejail/nolocal.net
%config(noreplace) %{_sysconfdir}/firejail/opera-beta.profile
%config(noreplace) %{_sysconfdir}/firejail/opera.profile
%config(noreplace) %{_sysconfdir}/firejail/parole.profile
%config(noreplace) %{_sysconfdir}/firejail/pidgin.profile
%config(noreplace) %{_sysconfdir}/firejail/qbittorrent.profile
%config(noreplace) %{_sysconfdir}/firejail/quassel.profile
%config(noreplace) %{_sysconfdir}/firejail/rhythmbox.profile
%config(noreplace) %{_sysconfdir}/firejail/rtorrent.profile
%config(noreplace) %{_sysconfdir}/firejail/server.profile
%config(noreplace) %{_sysconfdir}/firejail/skype.profile
%config(noreplace) %{_sysconfdir}/firejail/spotify.profile
%config(noreplace) %{_sysconfdir}/firejail/steam.profile
%config(noreplace) %{_sysconfdir}/firejail/thunderbird.profile
%config(noreplace) %{_sysconfdir}/firejail/totem.profile
%config(noreplace) %{_sysconfdir}/firejail/transmission-gtk.profile
%config(noreplace) %{_sysconfdir}/firejail/transmission-qt.profile
%config(noreplace) %{_sysconfdir}/firejail/unbound.profile
%config(noreplace) %{_sysconfdir}/firejail/vlc.profile
%config(noreplace) %{_sysconfdir}/firejail/webserver.net
%config(noreplace) %{_sysconfdir}/firejail/weechat-curses.profile
%config(noreplace) %{_sysconfdir}/firejail/weechat.profile
%config(noreplace) %{_sysconfdir}/firejail/whitelist-common.inc
%config(noreplace) %{_sysconfdir}/firejail/wine.profile
%config(noreplace) %{_sysconfdir}/firejail/xchat.profile

%clean
rm -rf $RPM_BUILD_ROOT
