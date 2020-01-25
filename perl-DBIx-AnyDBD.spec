#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	DBIx
%define		pnam	AnyDBD
Summary:	DBIx::AnyDBD - DBD independent class
Summary(pl.UTF-8):	DBIx::AnyDBD - klasa niezależności od DBD
Name:		perl-DBIx-AnyDBD
Version:	2.01
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b8dcb0ec10bcc7e8d83e1a031b73ab6b
URL:		http://search.cpan.org/dist/DBIx-AnyDBD/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides application developers with an abstraction class a
level away from DBI, that allows them to write an application that
works on multiple database platforms. The idea isn't to take away the
responsibility for coding different SQL on different platforms, but to
simply provide a platform that uses the right class at the right time
for whatever DB is currently in use.

%description -l pl.UTF-8
Ta klasa udostępnia programistom aplikacji klasę abstrakcji na
poziomie ponad DBI, pozwalającą pisać aplikacje działające na wielu
platformach bazodanowych. Ideą nie jest wyeliminowanie konieczności
używania różnego SQL dla różnych platform, ale dostarczenie platformy
używającej właściwej klasy we właściwym czasie, w zależności od
aktualnie używanej bazy danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/%{pdir}/*.pm
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
