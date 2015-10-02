%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname odfpy
%global sum Python API and tools to manipulate OpenDocument files
%global desc odfpy is a library to manipulate OpenDocument 1.2 files.


Name: python-%{srcname}
Version: 1.3.1
Release: 1
Summary: %{sum}
AutoReqProv: no

Source0: https://pypi.python.org/packages/source/o/odfpy/odfpy-%{version}.tar.gz
Prefix: /

Group: default
License: GPLv2 or Apache v2
Vendor: none
URL: https://github.com/eea/odfpy
Packager: Mark A. Hershberger <mah@nichework.com>

%description
%{desc}

%prep
%setup -n odfpy-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}


%check

%files -n python-%{srcname}
%{python2_sitelib}/*
/usr/bin/csv2ods
/usr/bin/mailodf
/usr/bin/odf2mht
/usr/bin/odf2xhtml
/usr/bin/odf2xml
/usr/bin/odfimgimport
/usr/bin/odflint
/usr/bin/odfmeta
/usr/bin/odfoutline
/usr/bin/odfuserfield
/usr/bin/xml2odf
/usr/share/man/man1/csv2ods.1.gz
/usr/share/man/man1/mailodf.1.gz
/usr/share/man/man1/odf2mht.1.gz
/usr/share/man/man1/odf2xhtml.1.gz
/usr/share/man/man1/odf2xml.1.gz
/usr/share/man/man1/odfimgimport.1.gz
/usr/share/man/man1/odflint.1.gz
/usr/share/man/man1/odfmeta.1.gz
/usr/share/man/man1/odfoutline.1.gz
/usr/share/man/man1/odfuserfield.1.gz
/usr/share/man/man1/xml2odf.1.gz


%changelog

