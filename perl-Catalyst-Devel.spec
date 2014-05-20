%define	upstream_name	 Catalyst-Devel
%define upstream_version 1.39

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Catalyst Development Tools

License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Number::Compare)
BuildRequires: perl(Text::Glob)
BuildRequires: perl(Test::Tester)
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


