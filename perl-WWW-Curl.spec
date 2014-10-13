%include	/usr/lib/rpm/macros.perl

%define		pdir	WWW
%define		pnam	Curl

Summary:	erl extension interface for libcurl
Name:		perl-WWW-Curl
Version:	4.17
Release:	1
License:	MPL or MIT/X
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SZ/SZBALINT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	997ac81cd6b03b30b36f7cd930474845
URL:		http://curl.haxx.se/libcurl/perl/
BuildRequires:	curl-devel
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Curl::easy provides an interface to the libcurl C library.

%prep
%setup -qn %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	OPTIMIZE="%{rpmcflags}" \
	OTHERLDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/auto/WWW/Curl
%attr(755,root,root) %{perl_vendorarch}/auto/WWW/Curl/Curl.so
%{perl_vendorarch}/WWW/Curl
%{perl_vendorarch}/WWW/Curl.pm
%{_mandir}/man3/WWW::Curl.3pm*

