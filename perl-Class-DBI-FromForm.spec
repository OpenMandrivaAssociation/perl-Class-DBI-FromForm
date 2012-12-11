%define upstream_name    Class-DBI-FromForm
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Update Class::DBI data using Data::FormValidator or HTML Widget
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Create and update Class::DBI objects from Data::FormValidator or HTML::Widget

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Class/*
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 680790
- mass rebuild

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 398797
- rebuild
- using %%perl_convert_version
- fixed source field

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.04-5mdv2009.0
+ Revision: 241178
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-3mdv2008.0
+ Revision: 86088
- rebuild


* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 21:12:03 (56081)
- rebuild

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 21:10:46 (56080)
Import perl-Class-DBI-FromForm

* Sat Apr 08 2006 Arnaud de Lorbeau <devel@mandriva.com> 0.04-1mdk
- Initial MDV RPM

