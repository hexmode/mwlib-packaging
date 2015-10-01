%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname pillow
%global sum Python Imaging Library (Fork)

Name: python-%{srcname}
Version: 2.9.0
Release: 1
Summary: Python Imaging Library (Fork)
AutoReqProv: no
BuildRoot: /var/tmp/%{name}-buildroot
BuildRequires: python2-devel
BuildRequires: tk-devel
BuildRequires: tkinter
BuildRequires: libjpeg-devel
BuildRequires: libwebp-devel
BuildRequires: libwebp-tools
BuildRequires: lcms2-devel
BuildRequires: zlib-devel
BuildRequires: libtiff-devel
BuildRequires: freetype-devel
Requires: expat
Requires: fontconfig
Requires: freetype
Requires: lcms2
Requires: libjpeg-turbo
Requires: libtiff
Requires: libwebp
Requires: python-libs
Requires: tcl
Requires: tk
Requires: zlib

Source0: https://pypi.python.org/packages/source/P/Pillow/Pillow-%{version}.zip

Prefix: /

Group: default
License: Standard PIL License
Vendor: none
URL: http://python-pillow.github.io/
Packager: Mark A. Hershberger <mah@nichework.com>

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description
Pillow is the “friendly PIL fork” by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

%description -n python2-%{srcname}
Pillow is the “friendly PIL fork” by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

%prep
%setup -n Pillow-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}
for i in pildriver pilconvert pilfont pilprint pilfile; do
    mv %{buildroot}/usr/bin/$i.py %{buildroot}/usr/bin/$i
    chmod +x %{buildroot}/usr/bin/$i
done


%check

%files -n python-%{srcname}
%{python2_sitearch}/*
/usr/bin/*

%changelog
