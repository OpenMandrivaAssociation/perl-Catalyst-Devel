%define	upstream_name	 Catalyst-Devel
%define upstream_version 1.33

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Catalyst Development Tools
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::Action::RenderView)     >= 0.04
BuildRequires:	perl(Catalyst::Plugin::ConfigLoader)
BuildRequires:	perl(Catalyst::Plugin::Static::Simple) >= 0.14
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Config::General)
BuildRequires:	perl(File::ChangeNotify)
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(Module::Install)  >= 0.64
BuildRequires:	perl(Path::Class)      >= 0.09
BuildRequires:	perl(Template)         >= 2.14
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)       >= 0.940.0
BuildRequires:	perl(Test::Fatal)	>= 0.003
BuildRequires:	perl(YAML)             >= 0.55

BuildArch:	noarch

%description
Catalyst is an elegant web application framework, extremely flexible yet
extremely simple. It's similar to Ruby on Rails, Spring (Java) and Maypole,
upon which it was originally based.

This package provides Catalyst development tools.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
# jq - should be removed when 5.10.1 is out
export CATALYST_DEVEL_NO_510_CHECK=1
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/auto
%{perl_vendorlib}/Catalyst*
%{perl_vendorlib}/Module
%{_mandir}/*/*

%changelog
* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 1.330.0-1mdv2011.0
+ Revision: 672702
- br test::fatal
- br test

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.33

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.310.0-1
+ Revision: 634208
- update to new version 1.31

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.280.0-1mdv2011.0
+ Revision: 553574
- update to 1.28

* Wed Feb 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.270.0-1mdv2010.1
+ Revision: 510519
- update to 1.27

* Tue Jan 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.260.0-1mdv2010.1
+ Revision: 490127
- update to 1.26

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 1.250.0-1mdv2010.1
+ Revision: 485802
- update to 1.25

* Fri Dec 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.1
+ Revision: 476491
- adding missing buildrequires:
- adding missing buildrequires:
- update to 1.24

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-1mdv2010.1
+ Revision: 460927
- adding missing buildrequires:
- update to 1.21

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.0
+ Revision: 418416
- update to 1.20

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1.190.0-1mdv2010.0
+ Revision: 393646
- updating to 1.19 for real this time
- using %%perl_convert_version

* Tue Jun 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdv2010.0
+ Revision: 390833
- update to new version 1.19

* Sat Jun 13 2009 Jérôme Quelin <jquelin@mandriva.org> 1.18-2mdv2010.0
+ Revision: 385644
- bump mkrel
- removing a requires:

* Thu Jun 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2010.0
+ Revision: 385209
- update to new version 1.18

* Tue May 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2010.0
+ Revision: 379873
- update to new version 1.17

* Sun May 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2010.0
+ Revision: 379211
- update to new version 1.16

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2010.0
+ Revision: 377988
- update to new version 1.15

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2010.0
+ Revision: 370010
- update to new version 1.12

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2009.1
+ Revision: 338708
- update to new version 1.10

* Thu Feb 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2009.1
+ Revision: 337826
- update to new version 1.09

* Tue Jul 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2009.0
+ Revision: 235783
- update to new version 1.08

* Wed Jun 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2009.0
+ Revision: 215032
- update to new version 1.07

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2009.0
+ Revision: 193750
- update to new version 1.06

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.03-1mdv2008.1
+ Revision: 136668
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2008.0
+ Revision: 63920
- update to new version 1.03


* Tue Jan 30 2007 Scott Karns <scottk@mandriva.org> 1.02-1mdv2007.0
+ Revision: 115427
- Updated to CPAN version 1.02

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Catalyst-Devel

* Thu Sep 21 2006 Scott Karns <scottk@mandriva.org> 1.01-1mdv2007.0
- 1.01 CPAN release

* Sun Jul 09 2006 Scott Karns <scottk@mandriva.org> 1.00-1mdv2007.0
- 1.00 CPAN release

* Thu Jun 29 2006 Scott Karns <scottk@mandriva.org> 0.99.01-1mdv2007.0
- First Mandriva release: 0.99_01 CPAN developer release

