Name:		texlive-avremu
Version:	71991
Release:	1
Summary:	An 8-Bit Microcontroller Simulator written in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/avremu
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/avremu.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/avremu.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/avremu.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A fully working package to simulate a Microprocessor in pure
LaTeX. The simulator is able to calculate complex pictures,
like Mandelbrot sets.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/avremu
%{_texmfdistdir}/tex/latex/avremu
%doc %{_texmfdistdir}/doc/latex/avremu

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
