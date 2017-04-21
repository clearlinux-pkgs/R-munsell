#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-munsell
Version  : 0.4.3
Release  : 33
URL      : http://cran.r-project.org/src/contrib/munsell_0.4.3.tar.gz
Source0  : http://cran.r-project.org/src/contrib/munsell_0.4.3.tar.gz
Summary  : Utilities for Using Munsell Colours
Group    : Development/Tools
License  : MIT
Requires: R-colorspace
BuildRequires : R-colorspace
BuildRequires : clr-R-helpers

%description
![Downloads](http://cranlogs.r-pkg.org/badges/last-week/munsell)
munsell
=======

%prep
%setup -q -c -n munsell

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492802284

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492802284
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library munsell
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library munsell


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
/usr/lib64/R/library/munsell/help/munsell.rdb
/usr/lib64/R/library/munsell/help/munsell.rdx
/usr/lib64/R/library/munsell/help/paths.rds
/usr/lib64/R/library/munsell/html/00Index.html
/usr/lib64/R/library/munsell/html/R.css
/usr/lib64/R/library/munsell/raw/getmunsellmap.R
/usr/lib64/R/library/munsell/raw/greys.dat
/usr/lib64/R/library/munsell/raw/real.dat
