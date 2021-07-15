Summary:	Universal command-line interface for SQL databases
Name:		usql
Version:	0.9.2
Release:	1
License:	MIT
Group:		Applications/Databases
#Source0Download: https://github.com/xo/usql/releases
Source0:	https://github.com/xo/usql/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	18b761050322f95a41f529b8d0d64e1d
# cd usql-%{version}
# go mod vendor
# cd ..
# tar cJf usql-vendor-%{version}.tar.xz usql-%{version}/vendor
Source1:	%{name}-vendor-%{version}.tar.xz
# Source1-md5:	951038d149c0f9856a8bf7f9e0cbe343
URL:		https://github.com/xo/usql
BuildRequires:	golang >= 1.14
BuildRequires:	libicu-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Suggests:	oracle-instantclient-basic
ExclusiveArch:	%{ix86} %{x8664} %{arm} aarch64 mips64 mips64le ppc64 ppc64le s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		tags	most godror oracle sqlite_app_armor sqlite_fts5 sqlite_introspect sqlite_json1 sqlite_stat4 sqlite_userauth sqlite_vtable sqlite_icu no_adodb no_h2

%description
A universal command-line interface for PostgreSQL, MySQL, Oracle
Database, SQLite3, Microsoft SQL Server, and many other databases
including NoSQL and non-relational databases!

%prep
%setup -q -b1

%{__mkdir_p} .go-cache

%build
GOCACHE="$(pwd)/.go-cache" go build -v -mod=vendor -tags="%{tags}" -ldflags="-X github.com/xo/usql/text.CommandName=%{name} -X github.com/xo/usql/text.CommandVersion=%{version}" -o bin/%{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

cp -p bin/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
