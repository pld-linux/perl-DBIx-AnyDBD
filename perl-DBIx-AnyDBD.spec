#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	AnyDBD
Summary:	DBIx::AnyDBD - DBD independent class
Summary(pl):	DBIx::AnyDBD - klasa niezale¿no¶ci od DBD
Name:		perl-DBIx-AnyDBD
Version:	2.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b8dcb0ec10bcc7e8d83e1a031b73ab6b
BuildRequires:	perl-devel >= 5.6
%if %{with tests}
BuildRequires:	perl-DBI
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides application developers with an abstraction class
a level away from DBI, that allows them to write an application that
works on multiple database platforms. The idea isn't to take away the
responsibility for coding different SQL on different platforms, but to
simply provide a platform that uses the right class at the right time
for whatever DB is currently in use.

%description -l pl
Ta klasa udostêpnia programistom aplikacji klasê abstrakcy na poziomie
ponad DBI, pozwalaj±c± pisaæ aplikacje dzia³aj±ce na wielu platformach
bazodanowych. Ide± nie jest wyeliminowanie konieczno¶ci u¿ywania
ró¿nego SQL dla ró¿nych platform, ale dostaczenie platformy u¿ywaj±cej
w³a¶ciwej klasy we w³a¶ciwym czasie, w zale¿no¶ci od aktualnie
u¿ywanej bazy danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -ar example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/%{pdir}/*.pm
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
