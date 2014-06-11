Summary:        A globally-deduplicating backup tool
Name:           zbackup
Version:        1.2.4
Release:        1
License:        GPL v2+
Group:          Applications/Archiving
URL:            http://zbackup.org/
Source0:        https://github.com/jalli/zbackup/archive/%{version}.tar.gz
BuildRequires:  cmake >= 2.8.2
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
BuildRequires:  zlib-devel
BuildRequires:  xz-devel
BuildRoot:      %{_tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:       openssl
Requires:       protobuf
Requires:       zlib
Requires:       xz

%description
zbackup is a globally-deduplicating backup tool, based on the ideas
found in rsync. Feed a large .tar into it, and it will store duplicate
regions of it only once, then compress and optionally encrypt the
result. Feed another .tar file, and it will also re-use any data found
in any previous backups. This way only new changes are stored, and as
long as the files are not very different, the amount of storage
required is very low.

%prep
%setup -q

%build
cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -m 755 scripts/r%{name} ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/rzbackup
%config(noreplace) %{_sysconfdir}/rzbackup.conf
%config(noreplace) %{_sysconfdir}/zbackup.pwd

%post 
%{_bindir}/rzbackup install || :

%changelog
* Wed Jun 11 2014 Jarl Stefansson <jarl.stefansson@gmail.com> 1.2.4-1
-  Test

* Wed Jun 11 2014 Jarl Stefansson <jarl.stefansson@gmail.com> 1.2.2-1
- new package built with tito
* Wed Jun 11 2014 Jarl Stefansson <jarl.stefansson@gmail.com>
- adopted for rzbackup
* Mon Apr 28 2014 Dmitriy Slupytskyi <dslupytskyi@gmail.com>
- added dependencies for install

