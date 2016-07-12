Summary:	A SUID sandbox program
Name:		firejail
Version:	0.9.36
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://github.com/netblue30/firejail/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	98a5b96118822aae423528cfe22b4a3c
URL:		https://firejail.wordpress.com/
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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/login.users
%attr(4755,root,root) %{_bindir}/firejail
%attr(755,root,root) %{_bindir}/firemon
%{_mandir}/man1/firejail.1*
%{_mandir}/man1/firemon.1*
%{_mandir}/man5/firejail-login.5*
%{_mandir}/man5/firejail-profile.5*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/fshaper.sh
%attr(755,root,root) %{_libdir}/%{name}/ftee
%attr(755,root,root) %{_libdir}/%{name}/libtrace.so
%attr(755,root,root) %{_libdir}/%{name}/libtracelog.so

# bash-completions
%{bash_compdir}/firejail
%{bash_compdir}/firemon
