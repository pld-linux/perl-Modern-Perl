#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Modern
%define		pnam	Perl
%include	/usr/lib/rpm/macros.perl
Summary:	Modern::Perl - enable all of the features of Modern Perl with one command
#Summary(pl.UTF-8):
Name:		perl-Modern-Perl
Version:	1.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CH/CHROMATIC/Modern-Perl-%{version}.tar.gz
# Source0-md5:	1338c29f86b109280f8c723ece49299e
URL:		http://search.cpan.org/dist/Modern-Perl/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Modern
%{perl_vendorlib}/Modern/*.pm
%{_mandir}/man3/*
