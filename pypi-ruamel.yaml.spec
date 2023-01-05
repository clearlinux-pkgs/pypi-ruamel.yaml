#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ruamel.yaml
Version  : 0.17.21
Release  : 69
URL      : https://files.pythonhosted.org/packages/46/a9/6ed24832095b692a8cecc323230ce2ec3480015fbfa4b79941bd41b23a3c/ruamel.yaml-0.17.21.tar.gz
Source0  : https://files.pythonhosted.org/packages/46/a9/6ed24832095b692a8cecc323230ce2ec3480015fbfa4b79941bd41b23a3c/ruamel.yaml-0.17.21.tar.gz
Summary  : ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order
Group    : Development/Tools
License  : MIT
Requires: pypi-ruamel.yaml-license = %{version}-%{release}
Requires: pypi-ruamel.yaml-python = %{version}-%{release}
Requires: pypi-ruamel.yaml-python3 = %{version}-%{release}
Requires: pypi(ruamel.yaml.clib)
BuildRequires : buildreq-distutils3

%description
ruamel.yaml
===========
``ruamel.yaml`` is a YAML 1.2 loader/dumper package for Python.

%package license
Summary: license components for the pypi-ruamel.yaml package.
Group: Default

%description license
license components for the pypi-ruamel.yaml package.


%package python
Summary: python components for the pypi-ruamel.yaml package.
Group: Default
Requires: pypi-ruamel.yaml-python3 = %{version}-%{release}

%description python
python components for the pypi-ruamel.yaml package.


%package python3
Summary: python3 components for the pypi-ruamel.yaml package.
Group: Default
Requires: python3-core
Provides: pypi(ruamel.yaml)
Requires: pypi(ruamel.yaml.clib)

%description python3
python3 components for the pypi-ruamel.yaml package.


%prep
%setup -q -n ruamel.yaml-0.17.21
cd %{_builddir}/ruamel.yaml-0.17.21
pushd ..
cp -a ruamel.yaml-0.17.21 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656405687
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ruamel.yaml
cp %{_builddir}/ruamel.yaml-0.17.21/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ruamel.yaml/8f07e3e11c4ec142283aff04e7de8ce15f14c32c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ruamel.yaml/8f07e3e11c4ec142283aff04e7de8ce15f14c32c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
