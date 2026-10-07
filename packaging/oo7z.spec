Name:           oo7z
Version:        0.1.0
Release:        1%{?dist}
Summary:        7-Zip multi-format container unpacker and lister with AES-256 encryption.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oo7z
Source0:        oo7z-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oo7z is a sovereign, capability-bounded 7Z HANDLER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oo7z
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oo7z-uninstall

%files
/usr/bin/oo7z
/usr/bin/oo7z-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
