#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-munsell
Version  : 0.5.0
Release  : 88
URL      : https://cran.r-project.org/src/contrib/munsell_0.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/munsell_0.5.0.tar.gz
Summary  : Utilities for Using Munsell Colours
Group    : Development/Tools
License  : MIT
Requires: R-colorspace
BuildRequires : R-colorspace
BuildRequires : buildreq-R

%description
Provides easy access to, and manipulation of, the Munsell colours. Provides a
mapping between Munsell's original notation (e.g. "5R 5/10") and hexadecimal
strings suitable for use directly in R graphics. Also provides utilities to
explore slices through the Munsell colour tree, to transform Munsell colours
and display colour palettes.

%prep
%setup -q -c -n munsell
cd %{_builddir}/munsell

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641064693

%install
export SOURCE_DATE_EPOCH=1641064693
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library munsell
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library munsell
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library munsell
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc munsell || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/munsell/DESCRIPTION
/usr/lib64/R/library/munsell/INDEX
/usr/lib64/R/library/munsell/LICENSE
/usr/lib64/R/library/munsell/Meta/Rd.rds
/usr/lib64/R/library/munsell/Meta/features.rds
/usr/lib64/R/library/munsell/Meta/hsearch.rds
/usr/lib64/R/library/munsell/Meta/links.rds
/usr/lib64/R/library/munsell/Meta/nsInfo.rds
/usr/lib64/R/library/munsell/Meta/package.rds
/usr/lib64/R/library/munsell/NAMESPACE
/usr/lib64/R/library/munsell/NEWS.md
/usr/lib64/R/library/munsell/R/munsell
/usr/lib64/R/library/munsell/R/munsell.rdb
/usr/lib64/R/library/munsell/R/munsell.rdx
/usr/lib64/R/library/munsell/R/sysdata.rdb
/usr/lib64/R/library/munsell/R/sysdata.rdx
/usr/lib64/R/library/munsell/help/AnIndex
/usr/lib64/R/library/munsell/help/aliases.rds
/usr/lib64/R/library/munsell/help/figures/README-complement-slice-1.png
/usr/lib64/R/library/munsell/help/figures/README-manipulate-blue-1.png
/usr/lib64/R/library/munsell/help/figures/README-palette-1.png
/usr/lib64/R/library/munsell/help/munsell.rdb
/usr/lib64/R/library/munsell/help/munsell.rdx
/usr/lib64/R/library/munsell/help/paths.rds
/usr/lib64/R/library/munsell/html/00Index.html
/usr/lib64/R/library/munsell/html/R.css
/usr/lib64/R/library/munsell/raw/getmunsellmap.R
/usr/lib64/R/library/munsell/raw/greys.dat
/usr/lib64/R/library/munsell/raw/real.dat
/usr/lib64/R/library/munsell/tests/testthat.R
/usr/lib64/R/library/munsell/tests/testthat/test-alter.R
/usr/lib64/R/library/munsell/tests/testthat/test-convert.R
