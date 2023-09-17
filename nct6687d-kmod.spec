%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

%define buildforkernels akmod

Name:           nct6687d-kmod
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Kernel module (kmod) for nct6687d
License:        GPL-2.0
URL:            https://github.com/ublue-os/nct6687d
Source0:        %{url}/archive/refs/heads/main.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  elfutils-libelf-devel
BuildRequires:  kmodtool
Conflicts: 	    nct6687d-kmod-common

%{expand:%(kmodtool --target %{_target_cpu} --kmodname nct6687d %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
nct6687d kernel module

%prep
kmodtool --target %{_target_cpu} --kmodname nct6687d %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -n nct6687d-main

for kernel_version in %{?kernel_versions} ; do
    mkdir -p _kmod_build_${kernel_version%%___*}
    cp -a *.c _kmod_build_${kernel_version%%___*}/
    cp -a Makefile _kmod_build_${kernel_version%%___*}/
done

%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} VERSION=v%{version} modules
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/*.ko
done
%{?akmod_install}

%changelog
{{{ git_dir_changelog }}}
