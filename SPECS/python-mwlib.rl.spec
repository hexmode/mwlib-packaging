%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname mwlib.rl
%global sum generate pdfs from mediawiki markup
%global desc mwlib.rl provides a library for writing pdf documents from mediawiki articles which were parsed by the mwlib library.
%global ver 0.14.5
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
# enforce importing from the installation directory
PATH=%{buildroot}%{_bindir}:$PATH \
   PYTHONPATH=%{buildroot}%{python_sitelib} \
   py.test-%{python_version} -v tests/ \
       --ignore tests/test_translation.py \
       --ignore tests/test_advanced.py \
       --ignore tests/test_basicnodes.py \
       --ignore tests/test_snippets.py \
       --ignore tests/test_misc.py

%files -n python-%{srcname}
%{python2_sitelib}/*


%changelog

