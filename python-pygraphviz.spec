Name:           python-pygraphviz
Version:        1.3
Release:        2.rc2%{?dist}.1
Summary:        Create and Manipulate Graphs and Networks
License:        BSD
# https://github.com/pygraphviz/pygraphviz/issues/39
URL:            http://networkx.lanl.gov/pygraphviz/
Source0:        http://pypi.python.org/packages/source/p/pygraphviz/pygraphviz-1.3rc2.tar.gz

%global with_python3_other %{defined python3_other_pkgversion}

BuildRequires:  gcc
BuildRequires:  python2-devel
BuildRequires:  python%{python3_pkgversion}-devel
%if %with_python3_other
BuildRequires:  python%{python3_other_pkgversion}-devel
%endif
BuildRequires:  python%{python3_pkgversion}-sphinx
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
Requires:	python2-nose
%{?python_provide:%python_provide python2-pygraphviz}
Obsoletes:      python-pygraphviz < 1.3-3.rc2

%description -n python2-pygraphviz %_description

This package contains the version for Python 2.

%package -n python%{python3_pkgversion}-pygraphviz
Summary:        %{summary}
Requires:	python%{python3_pkgversion}-nose
%{?python_provide:%python_provide python%{python3_pkgversion}-pygraphviz}

%description -n python%{python3_pkgversion}-pygraphviz %_description

This package contains the version for Python %{python3_version}.

%if %with_python3_other
%package -n python%{python3_other_pkgversion}-pygraphviz
Summary:        %{summary}
Requires:	python%{python3_other_pkgversion}-nose
%{?python_provide:%python_provide python%{python3_other_pkgversion}-pygraphviz}

%description -n python%{python3_other_pkgversion}-pygraphviz %_description

This package contains the version for Python %{python3_other_version}.
%endif

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
%if %with_python3_other
%py3_other_build
%endif

# docs
%make_build -C doc SPHINXBUILD=sphinx-build-3 html PYTHONPATH=$(pwd)/build/lib.%{python3_platform}-%{python3_version}

%install
%py2_install
%py3_install
%if %with_python3_other
%py3_other_install
%endif
mv %{buildroot}%{_docdir}/pygraphviz-* %{buildroot}%{_pkgdocdir}
rm %{buildroot}%{_pkgdocdir}/INSTALL.txt
rm doc/build/html/.buildinfo
cp -av doc/build/html %{buildroot}%{_pkgdocdir}/
chmod g-w %{buildroot}%{python2_sitearch}/pygraphviz/_graphviz.so \
          %{buildroot}%{python3_sitearch}/pygraphviz/_graphviz.*.so \
%if %with_python3_other
          %{buildroot}%{python3_other_sitearch}/pygraphviz/_graphviz.*.so
%endif

%global _docdir_fmt %{name}

%files -n python2-pygraphviz
%{python2_sitearch}/*
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.txt

%files -n python%{python3_pkgversion}-pygraphviz
%{python3_sitearch}/*
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.txt

%if %with_python3_other
%files -n python%{python3_other_pkgversion}-pygraphviz
%{python3_other_sitearch}/*
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.txt
%endif

%files doc
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/examples

%changelog
* Wed Jan 23 2019 Scott K Logan <logans@cottsay.net> - 1.3-2rc2.1
- Update spec format and add Python 3.4 and 3.6 to EPEL7

* Sun Nov 30 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-2rc2
- Reformat version string to follow guidelines for pre-release versions

* Sat Nov 29 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3rc2-2
- Fixed after review: use more macros, include directories in %%files,
  add provides for bundled jquery, remove empty file.

* Mon Nov 24 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3rc2-1
- Update to latest version, build sphinx docs, add python3 subpackage.

* Wed Oct 26 2011 Vedran Miletić <rivanvx@gmail.com> - 1.1-1
- Initial package.
