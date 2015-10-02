%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname sqlite3dbm
%global sum sqlite-backed dictionary

Name: python-%{srcname}
Version: 0.1.4
Release: 1
Summary: %{sum}
AutoReqProv: no
BuildRoot: /var/tmp/%{name}-buildroot

Prefix: /

Group: default
License: Apache
Vendor: none
URL: http://github.com/Yelp/sqlite3dbm/
Source0: https://pypi.python.org/packages/source/s/sqlite3dbm/sqlite3dbm-%{version}.tar.gz
Packager: Mark A. Hershberger <mah@nichework.com>

%description
%{desc}

%prep
%setup -n sqlite3dbm-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files -n python-%{srcname}
%defattr(-,root,root,-)
%{python2_sitelib}/*

%changelog

