%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname simplejson
%global sum Simple, fast, extensible JSON encoder/decoder for Python
%global desc simplejson is a simple, fast, complete, correct and extensible JSON encoder and decoder for Python 2.5+ and Python 3.3+. It is pure Python code with no dependencies, but includes an optional C extension for a serious speed boost.
%global ver 3.8.0
%global url https://github.com/simplejson/simplejson
%global lic MIT License

Name: python-%{srcname}
Version: %{ver}
Release: 1
Summary: %{sum}
AutoReqProv: no

Source0: https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
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

