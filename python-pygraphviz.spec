Name:           python-pygraphviz
Version:        1.3
Release:        3.rc2%{?dist}
Summary:        Create and Manipulate Graphs and Networks
License:        BSD
# https://github.com/pygraphviz/pygraphviz/issues/39
URL:            http://networkx.lanl.gov/pygraphviz/
Source0:        http://pypi.python.org/packages/source/p/pygraphviz/pygraphviz-1.3rc2.tar.gz

BuildRequires:  python2-devel python3-devel
BuildRequires:  python-sphinx
BuildRequires:  graphviz-devel

%global _description                                                  \
PyGraphviz is a Python interface to the Graphviz graph layout and     \
visualization package. With PyGraphviz you can create, edit, read,    \
write, and draw graphs using Python to access the Graphviz graph data \
structure and layout algorithms. PyGraphviz is independent from       \
NetworkX but provides a similar programming interface.

%description %_description

%package -n python2-pygraphviz
Summary:        %{summary}
Requires:	python-nose
%{?python_provide:%python_provide python2-pygraphviz}
Obsoletes:      python-pygraphviz < 1.3-3.rc2

%description -n python2-pygraphviz %_description

This package contains the version for Python 2.

%package -n python3-pygraphviz
Summary:        %{summary}
Requires:	python3-nose
%{?python_provide:%python_provide python3-pygraphviz}

%description -n python3-pygraphviz %_description

This package contains the version for Python 3.

%package doc
Summary:        Documentation for pygraphviz
Provides:       bundled(jquery)
BuildArch:      noarch

%description doc
Documentation for PyGraphViz.

%prep
%setup -q -n pygraphviz-1.3rc2
# remove she-bang line
sed -i '1d' pygraphviz/tests/test.py
rm doc/source/static/empty.txt

%build
%py2_build
%py3_build


# docs
%{__python2} setup.py build_ext -i
%make_build -C doc html PYTHONPATH=..

%install
%py2_install
%py3_install
mv %{buildroot}%{_docdir}/pygraphviz-* %{buildroot}%{_pkgdocdir}
rm %{buildroot}%{_pkgdocdir}/INSTALL.txt
rm doc/build/html/.buildinfo
cp -av doc/build/html %{buildroot}%{_pkgdocdir}/
chmod g-w %{buildroot}%{python_sitearch}/pygraphviz/_graphviz.so \
          %{buildroot}%{python3_sitearch}/pygraphviz/_graphviz.*.so

%global _docdir_fmt %{name}

%files -n python2-pygraphviz
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
* Tue Apr  5 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-3.rc2
- Rename python2 subpackage to python2-pygraphviz
- Fix Requires (#1324237)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2.rc2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 30 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-2rc2
- Reformat version string to follow guidelines for pre-release versions

* Sat Nov 29 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3rc2-2
- Fixed after review: use more macros, include directories in %files,
  add provides for bundled jquery, remove empty file.

* Mon Nov 24 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3rc2-1
- Update to latest version, build sphinx docs, add python3 subpackage.

* Wed Oct 26 2011 Vedran Miletić <rivanvx@gmail.com> - 1.1-1
- Initial package.
