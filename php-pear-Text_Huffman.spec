%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Huffman
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - lossless compression algorithm
Summary(pl):	%{_pearname} - bezstratny algorytm kompresji
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6a9030e04735db05f7cacf6b14d0254b
URL:		http://pear.php.net/package/Text_Huffman/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:5.0.0RC1
Requires:	php-pear >= 3:5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Huffman compression is a lossless compression algorithm that is ideal
for compressing textual data.

In PEAR status of this package is: %{_status}.

%description -l pl
Kompresja Huffmana to bezstratny algorytm kompresji idealny do
kompresji danych tekstowych.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
