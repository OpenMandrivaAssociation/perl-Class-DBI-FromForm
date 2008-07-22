%define realname Class-DBI-FromForm
%define name perl-%{realname}
%define version 0.04
%define release %mkrel 5

Summary:	Update Class::DBI data using Data::FormValidator or HTML Widget
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		%{realname}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
Create and update Class::DBI objects from Data::FormValidator or HTML::Widget

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Class/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

