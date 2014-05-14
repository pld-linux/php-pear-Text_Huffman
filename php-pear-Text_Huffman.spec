%define		_status		beta
%define		_pearname	Text_Huffman
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - lossless compression algorithm
Summary(pl.UTF-8):	%{_pearname} - bezstratny algorytm kompresji
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	7
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6a9030e04735db05f7cacf6b14d0254b
URL:		http://pear.php.net/package/Text_Huffman/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.0.0-0.RC1
Requires:	php-pear >= 3:5.0.0
Obsoletes:	php-pear-Text_Huffman-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Huffman compression is a lossless compression algorithm that is ideal
for compressing textual data.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Kompresja Huffmana to bezstratny algorytm kompresji idealny do
kompresji danych tekstowych.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/Text/*.php
