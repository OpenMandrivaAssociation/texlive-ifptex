Name:		texlive-ifptex
Version:	62982
Release:	2
Summary:	Check if the engine is pTeX or one of its derivatives
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifptex
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifptex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifptex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The ifptex package is a counterpart of ifxetex, ifluatex, etc.
for the ptex engine. The ifuptex package is an alias to ifptex
provided for backward compatibility.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/ifptex
%doc %{_texmfdistdir}/doc/generic/ifptex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
