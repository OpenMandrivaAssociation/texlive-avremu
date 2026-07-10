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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A fully working package to simulate a Microprocessor in pure LaTeX. The
simulator is able to calculate complex pictures, like Mandelbrot sets.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/avremu
%dir %{_datadir}/texmf-dist/source/latex/avremu
%dir %{_datadir}/texmf-dist/tex/latex/avremu
%dir %{_datadir}/texmf-dist/source/latex/avremu/imgs
%dir %{_datadir}/texmf-dist/source/latex/avremu/test-suite
%doc %{_datadir}/texmf-dist/doc/latex/avremu/README
%doc %{_datadir}/texmf-dist/doc/latex/avremu/avremu.pdf
%doc %{_datadir}/texmf-dist/source/latex/avremu/avremu.tex
%doc %{_datadir}/texmf-dist/source/latex/avremu/imgs/mandelbrot-128x128.png
%doc %{_datadir}/texmf-dist/source/latex/avremu/imgs/mandelbrot-20x20.png
%doc %{_datadir}/texmf-dist/source/latex/avremu/imgs/mandelbrot-250x250.png
%doc %{_datadir}/texmf-dist/source/latex/avremu/simple-testsuite.tex
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/FOOTER
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/HEADER
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/complex-memory.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/empty-main.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/fibonacci-rec.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/float.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/func-ptr.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/mandelbrot.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/mul.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/printf.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/shift.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/string.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/sum-rec.c
%doc %{_datadir}/texmf-dist/source/latex/avremu/test-suite/test-suite
%{_datadir}/texmf-dist/tex/latex/avremu/avr.binary.tex
%{_datadir}/texmf-dist/tex/latex/avremu/avr.bitops.tex
%{_datadir}/texmf-dist/tex/latex/avremu/avr.draw.tex
%{_datadir}/texmf-dist/tex/latex/avremu/avr.instr.tex
%{_datadir}/texmf-dist/tex/latex/avremu/avr.io.tex
%{_datadir}/texmf-dist/tex/latex/avremu/avr.memory.tex
%{_datadir}/texmf-dist/tex/latex/avremu/avr.numbers.tex
%{_datadir}/texmf-dist/tex/latex/avremu/avr.testsuite.tex
%{_datadir}/texmf-dist/tex/latex/avremu/avremu.sty
