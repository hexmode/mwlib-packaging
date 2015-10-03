%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname mwlib.ext
%global sum provide dependencies for mwlib
%global desc mwlib.ext provides external dependencies needed by the mwlib library. It contains a copy of reportlab, which is a BSD licensed pdf generation library.
%global ver 0.13.2
%global url http://code.pediapress.com/
%global lic BSD

Name: python-%{srcname}
Version: %{ver}
Release: 1
Summary: %{sum}
AutoReqProv: no

Source0: https://pypi.python.org/packages/source/m/%{srcname}/%{srcname}-%{version}.zip
Prefix: /

Group: default
License: %{lic}
Vendor: none
URL: %{url}
Packager: Mark A. Hershberger <mah@nichework.com>

%description
%{desc}

%prep
%setup -n %{srcname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}


%check

%files -n python-%{srcname}
%{python2_sitearch}/*


%changelog

