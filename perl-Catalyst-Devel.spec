%define	realname	Catalyst-Devel
%define	modprefix	Catalyst
%define	name		perl-%{realname}

%define	realversion	1.02
%define	version		1.02

%define	release		%mkrel 1

Summary:	Catalyst Development Tools
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{realname}-%{realversion}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Catalyst) >= 5.7000
BuildRequires:	perl(Catalyst::Action::RenderView) >= 0.04
BuildRequires:	perl(Catalyst::Plugin::ConfigLoader)
BuildRequires:	perl(Catalyst::Plugin::Static::Simple) >= 0.14
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl(Module::Install) >= 0.64
BuildRequires:	perl(Path::Class) >= 0.09
BuildRequires:	perl(Template) >= 2.14
BuildRequires:	perl(YAML) >= 0.55
Requires:	perl >= 5.8.1
Requires:	perl-Catalyst >= 5.7000
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
Catalyst is an elegant web application framework, extremely flexible yet
extremely simple. It's similar to Ruby on Rails, Spring (Java) and Maypole,
upon which it was originally based.

This package provides Catalyst development tools.


%prep
%setup -q -n %{realname}-%{realversion}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/%{modprefix}*
%{perl_vendorlib}/Module
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


