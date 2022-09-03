#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mirt
Version  : 1.37.1
Release  : 36
URL      : https://cran.r-project.org/src/contrib/mirt_1.37.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mirt_1.37.1.tar.gz
Summary  : Multidimensional Item Response Theory
Group    : Development/Tools
License  : GPL-3.0
Requires: R-mirt-lib = %{version}-%{release}
Requires: R-Deriv
Requires: R-GPArotation
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-dcurver
Requires: R-gridExtra
Requires: R-pbapply
Requires: R-vegan
BuildRequires : R-Deriv
BuildRequires : R-GPArotation
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-dcurver
BuildRequires : R-gridExtra
BuildRequires : R-pbapply
BuildRequires : R-vegan
BuildRequires : buildreq-R

%description
unidimensional and multidimensional latent trait models under the Item

%package lib
Summary: lib components for the R-mirt package.
Group: Libraries

%description lib
lib components for the R-mirt package.


%prep
%setup -q -n mirt
cd %{_builddir}/mirt

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660168856

%install
export SOURCE_DATE_EPOCH=1660168856
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mirt/CITATION
/usr/lib64/R/library/mirt/DESCRIPTION
/usr/lib64/R/library/mirt/INDEX
/usr/lib64/R/library/mirt/Meta/Rd.rds
/usr/lib64/R/library/mirt/Meta/data.rds
/usr/lib64/R/library/mirt/Meta/features.rds
/usr/lib64/R/library/mirt/Meta/hsearch.rds
/usr/lib64/R/library/mirt/Meta/links.rds
/usr/lib64/R/library/mirt/Meta/nsInfo.rds
/usr/lib64/R/library/mirt/Meta/package.rds
/usr/lib64/R/library/mirt/Meta/vignette.rds
/usr/lib64/R/library/mirt/NAMESPACE
/usr/lib64/R/library/mirt/NEWS.md
/usr/lib64/R/library/mirt/R/mirt
/usr/lib64/R/library/mirt/R/mirt.rdb
/usr/lib64/R/library/mirt/R/mirt.rdx
/usr/lib64/R/library/mirt/data/Rdata.rdb
/usr/lib64/R/library/mirt/data/Rdata.rds
/usr/lib64/R/library/mirt/data/Rdata.rdx
/usr/lib64/R/library/mirt/doc/index.html
/usr/lib64/R/library/mirt/doc/mirt-vignettes.Rmd
/usr/lib64/R/library/mirt/doc/mirt-vignettes.html
/usr/lib64/R/library/mirt/help/AnIndex
/usr/lib64/R/library/mirt/help/aliases.rds
/usr/lib64/R/library/mirt/help/mirt.rdb
/usr/lib64/R/library/mirt/help/mirt.rdx
/usr/lib64/R/library/mirt/help/paths.rds
/usr/lib64/R/library/mirt/html/00Index.html
/usr/lib64/R/library/mirt/html/R.css
/usr/lib64/R/library/mirt/tests/tests/test-00-basics.R
/usr/lib64/R/library/mirt/tests/tests/test-01-mirtOne.R
/usr/lib64/R/library/mirt/tests/tests/test-02-mirtTwo.R
/usr/lib64/R/library/mirt/tests/tests/test-03-bfactor.R
/usr/lib64/R/library/mirt/tests/tests/test-04-multipleGroup.R
/usr/lib64/R/library/mirt/tests/tests/test-05-confmirtOne.R
/usr/lib64/R/library/mirt/tests/tests/test-06-confmirtTwo.R
/usr/lib64/R/library/mirt/tests/tests/test-07-mixedmirt.R
/usr/lib64/R/library/mirt/tests/tests/test-08-createItem.R
/usr/lib64/R/library/mirt/tests/tests/test-09-mirt.model.R
/usr/lib64/R/library/mirt/tests/tests/test-10-extras.R
/usr/lib64/R/library/mirt/tests/tests/test-11-discrete.R
/usr/lib64/R/library/mirt/tests/tests/test-12-gpcm_mats.R
/usr/lib64/R/library/mirt/tests/tests/test-13-grsmIRT.R
/usr/lib64/R/library/mirt/tests/tests/test-14-GGUM.R
/usr/lib64/R/library/mirt/tests/tests/test-15-IRTpars.R
/usr/lib64/R/library/mirt/tests/tests/test-16-DCIRT.R
/usr/lib64/R/library/mirt/tests/tests/test-17-DIF_DRF.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mirt/libs/mirt.so
/usr/lib64/R/library/mirt/libs/mirt.so.avx2
/usr/lib64/R/library/mirt/libs/mirt.so.avx512
