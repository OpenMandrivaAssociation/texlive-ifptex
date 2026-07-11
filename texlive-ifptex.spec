%global tl_name ifptex
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2c
Release:	%{tl_revision}.1
Summary:	Check if the engine is pTeX or one of its derivatives
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/ifptex
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifptex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifptex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The ifptex package is a counterpart of ifxetex, ifluatex, etc. for the
ptex engine. The ifuptex package is an alias to ifptex provided for
backward compatibility.

