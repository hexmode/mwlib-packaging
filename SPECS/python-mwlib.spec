%global module_name mwlib

%{?filter_setup:
%filter_provides_in %{python_sitearch}.*\.so$
%filter_setup
}

Name:           python-%{module_name}
Version:        0.15.14
Release:        1%{?dist}
Summary:        MediaWiki parser and utility library

License:        BSD
URL:            http://pediapress.com/code/
Source0:        http://pypi.python.org/packages/source/m/mwlib/%{module_name}-%{version}.zip
Source1:        README.fedora

# Removes the following "requires" from setup.py for these reasons:
#   roman: part of python-docutils
#   timelib: replaced with dateutil
Patch0:         mwlib-clean-up-dependencies.patch

# Replaces timelib with dateutil
Patch1:         mwlib-replace-timelib-with-dateutil.patch

# Ensure all console scripts are prefixed with 'mw-'
Patch2:         mwlib-prefix-console-scripts.patch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-odfpy >= 0.9
BuildRequires:  pyPdf >= 1.12
BuildRequires:  pyparsing >= 1.4.11
BuildRequires:  python-apipkg >= 1.2
BuildRequires:  python-bottle >= 0.10
BuildRequires:  python-dateutil
BuildRequires:  python-docutils
BuildRequires:  python-gevent
BuildRequires:  python-lxml
BuildRequires:  python-pillow
BuildRequires:  python-py >= 1.4
BuildRequires:  python-qserve >= 0.2.7
BuildRequires:  python-simplejson >= 2.3
BuildRequires:  python-sqlite3dbm
BuildRequires:  pytest
Requires:       python-odfpy >= 0.9
Requires:       pyPdf >= 1.12
Requires:       pyparsing >= 1.4.11
Requires:       python-apipkg >= 1.2
Requires:       python-bottle >= 0.10
Requires:       python-dateutil
Requires:       python-docutils
Requires:       python-gevent
Requires:       python-lxml
Requires:       python-pillow
Requires:       python-py >= 1.4
Requires:       python-qserve >= 0.2.7
Requires:       python-setuptools
Requires:       python-simplejson >= 2.3
Requires:       python-sqlite3dbm

%description
mwlib provides a library for parsing MediaWiki articles and converting them to
different output formats. mwlib is used by Wikipedia's "Print/export" feature
in order to generate PDF documents from Wikipedia articles.


%prep
%setup -qn %{module_name}-%{version}

# Clean up dependencies
%patch0 -p1

# Replace timelib with dateutil
%patch1 -p1

# Ensure all console scripts are prefixed with 'mw-'
%patch2 -p1

sed -i '/^#!/d' mwlib/*.py mwlib/*/*.py mwlib/snippets.txt
chmod a-x mwlib/*.py mwlib/*/*.py mwlib/snippets.txt


%build
CFLAGS="%{optflags}" %{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{module_name}
rm %{buildroot}%{python_sitearch}/%{module_name}/templ/*.c

cp %{SOURCE1} ./

%check
# imports from mwlib don't work without this for some reason
touch %{buildroot}%{python_sitearch}/mwlib/__init__.py

# enforce importing from the installation directory
sed -i 's/sys\.path\.append.*//' conftest.py
PATH=%{buildroot}%{_bindir}:$PATH \
   PYTHONPATH=%{buildroot}%{python_sitearch} \
   py.test-%{python_version} -v tests/ \
       --ignore tests/test_nserve.py \
       --ignore tests/test_redirect.py \
       --ignore tests/test_zipwiki.py \
       --ignore tests/test_nuwiki.py \
       -k 'not test_codes and not test_time_minus_days'
# 1. wsgi_intercept is missing
# 2. rl renderer is missing
# 3. no network
# 4. https://github.com/pediapress/mwlib/issues/51

rm %{buildroot}%{python_sitearch}/mwlib/__init__.py

%files
%doc changelog.rst README.rst README.fedora docs
%{python_sitearch}/*
%{_bindir}/mw-*
%{_datadir}/%{module_name}


%changelog
* Fri Jan 30 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.15.14-1
- Update to 0.15.14 and enable tests (#1031279)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 18 2013 Ian Weller <iweller@redhat.com> - 0.15.11-2
- Prefix all console scripts with mw- (RHBZ 998164)

* Tue Aug 13 2013 Ian Weller <iweller@redhat.com> - 0.15.11-1
- Update to 0.15.11

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.14.3-2
- Perl 5.18 rebuild

* Tue Jan 29 2013 Ian Weller <iweller@redhat.com> - 0.14.3-1
- Update to upstream 0.14.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Ian Weller <iweller@redhat.com> - 0.13.8-1
- Update to 0.13.8

* Tue Mar 13 2012 Ian Weller <iweller@redhat.com> - 0.13.6-1
- enhancement: implement protocol relative urls in named links
- enhancement: make mw-zip -gg post test.pediapress.com

* Mon Mar 05 2012 Ian Weller <iweller@redhat.com> - 0.13.5-1
- Update to 0.13.5 upstream

* Wed Feb 15 2012 Ian Weller <iweller@redhat.com> - 0.13.4-1
- Update to 0.13.4 upstream
- Update Requires: python-qserve >= 0.2.7
- Add Requires: python-simplejson
- Rebase Patch0 (Clean up dependencies)
- Rebase Patch1 (Unbundle apipkg)
- Rename patches to not be version-specific
- rm rm -rf buildroot

* Mon Feb 13 2012 Ian Weller <iweller@redhat.com> - 0.13.3-4
- Requires: python-setuptools

* Mon Feb 13 2012 Ian Weller <iweller@redhat.com> - 0.13.3-3
- BuildRequires: python-setuptools

* Sat Feb 11 2012 Ian Weller <iweller@redhat.com> - 0.13.3-2
- Move off of py.apipkg into the separate module
- Do a better job of unbundling apipkg completely
- Fix provides filtering

* Fri Jan 13 2012 Ian Weller <iweller@redhat.com> - 0.13.3-1
- Initial package build (again)
