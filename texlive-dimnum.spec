Name:		texlive-dimnum
Version:	58774
Release:	2
Summary:	Commands for dimensionless numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dimnum
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dimnum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dimnum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dimnum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package simplifies the calling of Dimensionless Numbers in
math or text mode.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/dimnum
%{_texmfdistdir}/tex/latex/dimnum
%doc %{_texmfdistdir}/doc/latex/dimnum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
