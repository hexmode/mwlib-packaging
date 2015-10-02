%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname qserve
%global sum job queue server
%global desc qserve is used in mwlib. It’s a job queue server written in python and it’s missing documentation.


Name: python-%{srcname}
Version: 0.2.8
Release: 1
Summary: %{sum}
AutoReqProv: no

Source0: https://pypi.python.org/packages/source/q/%{srcname}/%{srcname}-%{version}.zip
Prefix: /

Group: default
License: BSD
Vendor: none
URL: https://github.com/pediapress/qserve
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

