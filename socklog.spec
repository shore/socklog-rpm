#
# spec file for package socklog (Version 2.1.0)
#
# Copyright (c) 2010 Ian Meyer <ianmmeyer@gmail.com>
# Copyright (c) 2015 Brian Shore <brian@networkredux.com>

## This package understands the following switches:
## --with dietlibc ...  statically links against dietlibc

Name:           socklog
Version:        2.1.0
Release:        1%{?_with_dietlibc:diet}%{?dist}.seastar

Group:          System/Base
License:        BSD

# Override _sbindir being /usr/sbin
# %define _sbindir /sbin

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Url:            http://smarden.org/socklog/
Source0:        http://smarden.org/socklog/socklog-2.1.0.tar.gz

Obsoletes: socklog <= %{version}-%{release}
Provides: socklog = %{version}-%{release}

BuildRequires: make gcc
%if 0%{?rhel} >= 6
BuildRequires:  glibc-static
%endif

%{?_with_dietlibc:BuildRequires:        dietlibc}

Summary:        system and kernel logging services

%description
socklog, in cooperation with the runit package, is a small and secure
replacement for syslogd.

Authors:
---------
    Gerrit Pape <pape@smarden.org>

%prep
%setup -q -n admin/%{name}-%{version}
pushd src
echo "%{?_with_dietlibc:diet -Os }%__cc $RPM_OPT_FLAGS" >conf-cc
echo "%{?_with_dietlibc:diet -Os }%__cc -s -Os -pipe"   >conf-ld
popd

%build
sh package/compile

%install
%{__rm} -rf %{buildroot}

for i in $(< package/commands) ; do
    %{__install} -D -m 0755 command/$i %{buildroot}/bin/$i
done

for i in man/* ; do
    sect=${i##*.}
    %{__install} -D -m 0644 $i %{buildroot}%{_mandir}/man${sect}/${i##man/}
done

for i in doc/* ; do
    %{__install} -D -m 0644 $i %{buildroot}%{_docdir}/${i##doc/}
done

for i in package/CHANGES package/COPYING package/README src/TODO ; do
    %{__install} -D -m 0644 $i %{buildroot}%{_docdir}/${i##*/}
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
/bin/*
%doc %{_docdir}/*
%doc %{_mandir}/man1/*
%doc %{_mandir}/man8/*
