%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Huffman
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - lossless compression algorithm
Summary(pl):	%{_pearname} - bezstratny algorytm kompresji
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6a9030e04735db05f7cacf6b14d0254b
URL:		http://pear.php.net/package/Text_Huffman/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear >= 3:5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Huffman compression is a lossless compression algorithm that is ideal
for compressing textual data.

In PEAR status of this package is: %{_status}.

%description -l pl
Kompresja Huffmana to bezstartny algorytm kompresji idealny do
kompresji danych tekstowych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/test
%{php_pear_dir}/%{_class}/*.php
