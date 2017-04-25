#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4DE8FF2A63C7CC90 (smcv@debian.org)
#
Name     : dbus
Version  : 1.10.18
Release  : 39
URL      : https://dbus.freedesktop.org/releases/dbus/dbus-1.10.18.tar.gz
Source0  : https://dbus.freedesktop.org/releases/dbus/dbus-1.10.18.tar.gz
Source99 : https://dbus.freedesktop.org/releases/dbus/dbus-1.10.18.tar.gz.asc
Summary  : Free desktop message bus (uninstalled copy)
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+
Requires: dbus-bin
Requires: dbus-config
Requires: dbus-autostart
Requires: dbus-lib
Requires: dbus-data
Requires: dbus-doc
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32libsystemd)
BuildRequires : pkgconfig(32sm)
BuildRequires : pkgconfig(32systemd)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(x11)
BuildRequires : xmlto
Patch1: 0001-Add-support-for-ignore_missing-attribute-in-included.patch
Patch2: malloc_trim.patch
Patch3: memory.patch

%description
Sections in this file describe:
- introduction and overview
- low-level vs. high-level API
- version numbers
- options to the configure script
- ABI stability policy

%package autostart
Summary: autostart components for the dbus package.
Group: Default

%description autostart
autostart components for the dbus package.


%package bin
Summary: bin components for the dbus package.
Group: Binaries
Requires: dbus-data
Requires: dbus-config

%description bin
bin components for the dbus package.


%package config
Summary: config components for the dbus package.
Group: Default

%description config
config components for the dbus package.


%package data
Summary: data components for the dbus package.
Group: Data

%description data
data components for the dbus package.


%package dev
Summary: dev components for the dbus package.
Group: Development
Requires: dbus-lib
Requires: dbus-bin
Requires: dbus-data
Provides: dbus-devel

%description dev
dev components for the dbus package.


%package dev32
Summary: dev32 components for the dbus package.
Group: Default
Requires: dbus-lib32
Requires: dbus-bin
Requires: dbus-data
Requires: dbus-dev

%description dev32
dev32 components for the dbus package.


%package doc
Summary: doc components for the dbus package.
Group: Documentation

%description doc
doc components for the dbus package.


%package extras
Summary: extras components for the dbus package.
Group: Default

%description extras
extras components for the dbus package.


%package lib
Summary: lib components for the dbus package.
Group: Libraries
Requires: dbus-data
Requires: dbus-config

%description lib
lib components for the dbus package.


%package lib32
Summary: lib32 components for the dbus package.
Group: Default
Requires: dbus-data
Requires: dbus-config

%description lib32
lib32 components for the dbus package.


%prep
%setup -q -n dbus-1.10.18
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a dbus-1.10.18 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493111370
%configure --disable-static --with-systemdunitdir=/usr/lib/systemd/system \
--disable-xml-docs \
--enable-systemd \
--enable-user-session \
--enable-epoll \
--with-system-socket=/run/dbus/system_bus_socket \
--with-system-pid-file=/run/dbus/pid \
--with-console-auth-dir=/run/console/
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --with-systemdunitdir=/usr/lib/systemd/system \
--disable-xml-docs \
--enable-systemd \
--enable-user-session \
--enable-epoll \
--with-system-socket=/run/dbus/system_bus_socket \
--with-system-pid-file=/run/dbus/pid \
--with-console-auth-dir=/run/console/ --without-dbus-glib \
--disable-tests  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493111370
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/dbus.target.wants/dbus.socket
/usr/lib/systemd/system/multi-user.target.wants/dbus.service
/usr/lib/systemd/system/sockets.target.wants/dbus.socket

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/dbus-launch
%exclude /usr/libexec/dbus-daemon-launch-helper
/usr/bin/dbus-cleanup-sockets
/usr/bin/dbus-daemon
/usr/bin/dbus-monitor
/usr/bin/dbus-run-session
/usr/bin/dbus-send
/usr/bin/dbus-test-tool
/usr/bin/dbus-update-activation-environment
/usr/bin/dbus-uuidgen

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/dbus.target.wants/dbus.socket
%exclude /usr/lib/systemd/system/multi-user.target.wants/dbus.service
%exclude /usr/lib/systemd/system/sockets.target.wants/dbus.socket
/usr/lib/systemd/system/dbus.service
/usr/lib/systemd/system/dbus.socket
/usr/lib/systemd/user/dbus.service
/usr/lib/systemd/user/dbus.socket
/usr/lib/systemd/user/sockets.target.wants/dbus.socket

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/session.conf
/usr/share/dbus-1/system.conf

%files dev
%defattr(-,root,root,-)
/usr/include/dbus-1.0/dbus/dbus-address.h
/usr/include/dbus-1.0/dbus/dbus-bus.h
/usr/include/dbus-1.0/dbus/dbus-connection.h
/usr/include/dbus-1.0/dbus/dbus-errors.h
/usr/include/dbus-1.0/dbus/dbus-macros.h
/usr/include/dbus-1.0/dbus/dbus-memory.h
/usr/include/dbus-1.0/dbus/dbus-message.h
/usr/include/dbus-1.0/dbus/dbus-misc.h
/usr/include/dbus-1.0/dbus/dbus-pending-call.h
/usr/include/dbus-1.0/dbus/dbus-protocol.h
/usr/include/dbus-1.0/dbus/dbus-server.h
/usr/include/dbus-1.0/dbus/dbus-shared.h
/usr/include/dbus-1.0/dbus/dbus-signature.h
/usr/include/dbus-1.0/dbus/dbus-syntax.h
/usr/include/dbus-1.0/dbus/dbus-threads.h
/usr/include/dbus-1.0/dbus/dbus-types.h
/usr/include/dbus-1.0/dbus/dbus.h
/usr/lib32/dbus-1.0/include/dbus/dbus-arch-deps.h
/usr/lib64/dbus-1.0/include/dbus/dbus-arch-deps.h
/usr/lib64/libdbus-1.so
/usr/lib64/pkgconfig/dbus-1.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libdbus-1.so
/usr/lib32/pkgconfig/32dbus-1.pc
/usr/lib32/pkgconfig/dbus-1.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/dbus/*

%files extras
%defattr(-,root,root,-)
/usr/bin/dbus-launch

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdbus-1.so.3
/usr/lib64/libdbus-1.so.3.14.11

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libdbus-1.so.3
/usr/lib32/libdbus-1.so.3.14.11
