%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname apipkg
%global sum namespace control and lazy-import mechanism
%global desc With apipkg you can control the exported namespace of a python package and greatly reduce the number of imports for your users. It is a small pure python module that works on virtually all Python versions, including CPython2.3 to Python3.1, Jython and PyPy. It co-operates well with Python’s help() system, custom importers (PEP302) and common command line completion tools.


Name: python-%{srcname}
Version: 1.4
Release: 1
Summary: %{sum}
AutoReqProv: no

Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
Prefix: /

Group: default
License: MIT License
Vendor: none
URL: http://bitbucket.org/hpk42/apipkg
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
%{python2_sitelib}/*


%changelog

