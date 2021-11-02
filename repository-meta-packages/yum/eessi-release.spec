Name:           eessi-release
Version:        1
Release:        0
Summary:        Configuration package for the EESSI repository

Group:          System Environment/Base
License:        GPLv2

URL:            http://repo.eessi-infra.org/eessi/
Source0:        eessi.repo

BuildArch:     noarch
Requires:      cvmfs
Requires:      cvmfs-fuse3

%description
This package contains the required configuration for the EESSI repository to become available via yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key, when we get there.
#install -Dpm 644 %{SOURCE1} \
#    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EESSI

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Thu Nov 02 2021 Terje Kvernes <terje@kvernes.no> - 1.0
- Initial release
