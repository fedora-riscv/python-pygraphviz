Name:           python-pygraphviz
Version:        1.3rc2
Release:        2%{?dist}
Summary:        Create and Manipulate Graphs and Networks
License:        BSD
# https://github.com/pygraphviz/pygraphviz/issues/39
URL:            http://networkx.lanl.gov/pygraphviz/
Source0:        http://pypi.python.org/packages/source/p/pygraphviz/pygraphviz-%{version}.tar.gz

BuildRequires:  python2-devel python3-devel
BuildRequires:  python-sphinx
BuildRequires:  graphviz-devel
Requires:       graphviz-python

%description
PyGraphviz is a Python interface to the Graphviz graph layout and
visualization package. With PyGraphviz you can create, edit, read,
write, and draw graphs using Python to access the Graphviz graph data
structure and layout algorithms. PyGraphviz is independent from
NetworkX but provides a similar programming interface.

This package contains the version for Python 2.

%package -n python3-pygraphviz
Summary:        Create and Manipulate Graphs and Networks
Requires:       graphviz-python

%description -n python3-pygraphviz
PyGraphviz is a Python interface to the Graphviz graph layout and
visualization package. With PyGraphviz you can create, edit, read,
write, and draw graphs using Python to access the Graphviz graph data
structure and layout algorithms. PyGraphviz is independent from
NetworkX but provides a similar programming interface.

This package contains the version for Python 3.

%package doc
Summary:        Documentation for pygraphviz
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
Provides:       bundled(jquery)
BuildArch:      noarch

%description doc
Documentation for pygraphviz

%prep
%setup -q -n pygraphviz-%{version}
# remove she-bang line
sed -i '1d' pygraphviz/tests/test.py
rm doc/source/static/empty.txt

%build
%{__python2} setup.py build
%{__python3} setup.py build

# docs
%{__python2} setup.py build_ext -i
make %{?_smp_mflags} -C doc html PYTHONPATH=..

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
mv %{buildroot}%{_docdir}/pygraphviz-%{version} %{buildroot}%{_pkgdocdir}
rm %{buildroot}%{_pkgdocdir}/INSTALL.txt
rm -r doc/build/html/.buildinfo
cp -av doc/build/html %{buildroot}%{_pkgdocdir}/
chmod g-w %{buildroot}%{python_sitearch}/pygraphviz/_graphviz.so \
          %{buildroot}%{python3_sitearch}/pygraphviz/_graphviz.*.so

%files
%{python_sitearch}/*
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.txt

%files -n python3-pygraphviz
%{python3_sitearch}/*
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.txt

%files doc
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/examples

%changelog
* Sat Nov 29 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3rc2-2
- Fixed after review: use more macros, include directories in %files,
  add provides for bundled jquery, remove empty file.

* Mon Nov 24 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3rc2-1
- Update to latest version, build sphinx docs, add python3 subpackage.

* Wed Oct 26 2011 Vedran Miletić <rivanvx@gmail.com> - 1.1-1
- Initial package.
