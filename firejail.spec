Summary:	A SUID sandbox program
Name:		firejail
Version:	0.9.62
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://github.com/netblue30/firejail/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	784efb67eb4c33d8c456e44876371792
URL:		https://firejail.wordpress.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firejail is a SUID security sandbox program that reduces the risk of
security breaches by restricting the running environment of untrusted
applications using Linux namespaces and seccomp-bpf. It allows a
process and all its descendants to have their own private view of the
globally shared kernel resources, such as the network stack, process
table, and mount table.

%package -n bash-completion-%{name}
Summary:	bash-completion for firejail
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla firejail
Group:		Applications/Shells
Requires:	%{name}
Requires:	bash-completion >= 2.0
BuildArch:	noarch

%description -n bash-completion-%{name}
bash-completion for firejail.

%description -n bash-completion-%{name} -l pl.UTF-8
bashowe uzupełnianie nazw dla firejail.

%prep
%setup -qn %{name}-%{version}

%{__sed} -i -e '1s|#!/usr/bin/env python3$|#!%{__python3}|'  contrib/*.py

# Fix libdir.
sed -i -e 's#/usr/lib#%{_libdir}#g' etc/disable-devel.inc

%build
%configure
CFLAGS="%{rpmcflags}" \
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod +x $RPM_BUILD_ROOT%{_libdir}/%{name}/*.so

# Install documentation ourselves.
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.md RELNOTES
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.inc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.net
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.profile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/login.users
%attr(4755,root,root) %{_bindir}/firejail
%attr(755,root,root) %{_bindir}/firecfg
%attr(755,root,root) %{_bindir}/firemon
%{_mandir}/man1/firecfg.1*
%{_mandir}/man1/firejail.1*
%{_mandir}/man1/firemon.1*
%{_mandir}/man5/firejail-login.5*
%{_mandir}/man5/firejail-profile.5*
%{_mandir}/man5/firejail-users.5*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/faudit
%attr(755,root,root) %{_libdir}/%{name}/fbuilder
%attr(755,root,root) %{_libdir}/%{name}/fcopy
%attr(755,root,root) %{_libdir}/%{name}/fix_private-bin.py
%attr(755,root,root) %{_libdir}/%{name}/fjclip.py
%attr(755,root,root) %{_libdir}/%{name}/fjdisplay.py
%attr(755,root,root) %{_libdir}/%{name}/fjresize.py
%attr(755,root,root) %{_libdir}/%{name}/fldd
%attr(755,root,root) %{_libdir}/%{name}/fnet
%attr(755,root,root) %{_libdir}/%{name}/fnetfilter
%attr(755,root,root) %{_libdir}/%{name}/fsec-optimize
%attr(755,root,root) %{_libdir}/%{name}/fsec-print
%attr(755,root,root) %{_libdir}/%{name}/fseccomp
%attr(755,root,root) %{_libdir}/%{name}/fshaper.sh
%attr(755,root,root) %{_libdir}/%{name}/ftee
%attr(755,root,root) %{_libdir}/%{name}/libpostexecseccomp.so
%attr(755,root,root) %{_libdir}/%{name}/libtrace.so
%attr(755,root,root) %{_libdir}/%{name}/libtracelog.so
%attr(755,root,root) %{_libdir}/%{name}/sort.py
%attr(755,root,root) %{_libdir}/%{name}/syscalls.sh
%{_libdir}/%{name}/firecfg.config
%{_libdir}/%{name}/seccomp
%{_libdir}/%{name}/seccomp.32
%{_libdir}/%{name}/seccomp.block_secondary
%{_libdir}/%{name}/seccomp.debug
%{_libdir}/%{name}/seccomp.mdwx

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/firejail
%{bash_compdir}/firemon
%{bash_compdir}/firecfg
