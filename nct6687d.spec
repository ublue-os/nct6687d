Name:           nct6687d
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Kernel module (kmod) for nct6687d
License:        GPL-2.0
URL:            https://github.com/ublue-os/nct6687d
Source0:        https://raw.githubusercontent.com/ublue-os/nct6687d/main/nct6687.conf

BuildRequires:  systemd-rpm-macros

# For kmod package
Provides:       %{name}-kmod-common = %{version}-%{release}
Requires:       %{name}-kmod >= %{version}

BuildArch:      noarch

%description
nct6687d kernel module

%prep

%build
# Nothing to build

%install

install -D -m 0644 %{SOURCE0} %{buildroot}%{_modulesloaddir}/nct6687.conf

%files
%{_modulesloaddir}/nct6687.conf

%changelog
{{{ git_dir_changelog }}}
