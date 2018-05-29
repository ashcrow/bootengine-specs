%define dracutlibdir %{_prefix}/lib/dracut

Name:     dracut-bootengine
Version:  0.0.1
Release:  0.1%{?dist}
Summary:  Bootengine dracut modules for Container Linux
Group:    System Environment/Base
License:  BSD
URL:      https://github.com/coreos/bootengine
Source0:  dracut-bootengine-%{version}.tar.gz
Provides: dracut-bootengine = %{version}-%{release}
BuildArch: noarch

Requires: ignition
Requires: dracut
Requires: bash >= 4
Requires: coreutils
Requires: filesystem >= 2.1.0
Requires: findutils
Requires: grep
Requires: sed

%description
bootengine dracut modules for Container Linux.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build

%install
mkdir -p $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/
cp -rf dracut/30ignition $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/

%files
%defattr(-,root,root,0755)
%doc README.md NOTICE DCO
%license LICENSE
%{dracutlibdir}/modules.d/30ignition/coreos-digitalocean-network.service
%{dracutlibdir}/modules.d/30ignition/coreos-static-network.service
%{dracutlibdir}/modules.d/30ignition/ignition-disks.service
%{dracutlibdir}/modules.d/30ignition/ignition-files.service
%{dracutlibdir}/modules.d/30ignition/ignition-generator
%{dracutlibdir}/modules.d/30ignition/ignition-quench.service
%{dracutlibdir}/modules.d/30ignition/ignition-setup.sh
%{dracutlibdir}/modules.d/30ignition/module-setup.sh
%{dracutlibdir}/modules.d/30ignition/retry-umount.sh
%{dracutlibdir}/modules.d/30ignition/sysroot-boot.service

%changelog
* Tue May 29 2018 Steve Milner <smilner@redhat.com> - 0.0.1-0.1
- Initial spec
