%global tl_name avremu
%global tl_revision 71991

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	An 8-Bit Microcontroller Simulator written in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/avremu
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/avremu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/avremu.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/avremu.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A fully working package to simulate a Microprocessor in pure LaTeX. The
simulator is able to calculate complex pictures, like Mandelbrot sets.

