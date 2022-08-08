Summary: Diagnose unhealthy DNS domains
Name: doc
Version: 2.2.3
Release: 19%{?dist}
License: Distributable
URL: http://www.shub-internet.org/brad/dns/
Group: Applications/Internet
Source0: ftp://ftp.shub-internet.org/pub/shub/brad/dns/%{name}-%{version}.tar.bz2
Patch1: doc-2.2.3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: bind-utils

%description
Doc is an automated tool for verifying (to an extent) that a domain
is configured and functioning correctly.  It makes no attempt to
validate the data inside a domain, only the structure.  The only
required parameter is the valid domain name of an existing domain.


%prep
%setup -q
%patch1 -p1

sed -i "s|#set auxd=/users/brad/bin/doc-2.2.3/|set auxd=%{_libexecdir}/|g" doc
sed -i 's|set logdir="."|set logdir="~/.doclogs/"\nmkdir -p $logdir|' doc
mv doc-1.awk doc-1.awk.noshebang
mv doc-3.awk doc-3.awk.noshebang
mv doc-4.awk doc-4.awk.noshebang
echo "#!/bin/awk" >doc-1.awk
echo "#!/bin/awk" >doc-3.awk
echo "#!/bin/awk" >doc-4.awk
cat doc-1.awk.noshebang >>doc-1.awk
cat doc-3.awk.noshebang >>doc-3.awk
cat doc-4.awk.noshebang >>doc-4.awk


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_libexecdir}
install -m 0755 doc %{buildroot}%{_bindir}
install -m 0755 doc-1.awk %{buildroot}%{_libexecdir}
install -m 0755 doc-3.awk %{buildroot}%{_libexecdir}
install -m 0755 doc-4.awk %{buildroot}%{_libexecdir}
install -m 0644 doc.8 %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc doc.txt README INFO RFC.XXXX
%doc %{_mandir}/man8/*
%{_bindir}/*
%{_libexecdir}/*

%changelog
* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.3-11
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 2.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.2.3-6
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.2.3-4
- rebuild for new F11 features

* Fri Jun 29 2007 Marc Bradshaw <packages@marcbradshaw.co.uk> 2.2.3-3%{?dist}
- tidyup patch and setup sections of specfile

* Thu Jun 28 2007 Marc Bradshaw <packages@marcbradshaw.co.uk> 2.2.3-2%{?dist}
- drop unnecessary gawk requirement
- move .awk files to libexec dir
- move default logfiles into ~/.doclogs/
- fix documentation files install location

* Wed Jun 20 2007 Marc Bradshaw <packages@marcbradshaw.co.uk> 2.2.3-1%{?dist}
- Initial release
