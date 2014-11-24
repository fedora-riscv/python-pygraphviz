Name:           python-pygraphviz
Version:        1.2
Release:        1%{?dist}
Summary:        Creates and Manipulates Graphs and Networks
License:        BSD
URL:            http://networkx.lanl.gov/pygraphviz/
Source0:        http://pypi.python.org/packages/source/p/pygraphviz/pygraphviz-%{version}.tar.gz
#BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  graphviz-devel
Requires:       graphviz-python
Requires:       python


%description
PyGraphviz is a Python interface to the Graphviz graph layout and visualization package. With PyGraphviz you can create, edit, read, write, and draw graphs using Python to access the Graphviz graph data structure and layout algorithms. PyGraphviz is independent from NetworkX but provides a similar programming interface.


%package doc
Summary:        Documentation for pygraphviz
Group:          Documentation
#BuildRequires:  python-sphinx
Requires:       %{name} = %{version}-%{release}


%description doc
Documentation for pygraphviz


%prep
%setup -q -n pygraphviz-%{version}

# Fix permissions
#find examples -type f -perm /0111 | xargs chmod a-x

# Fix line endings
#sed -e 's/\r//' examples/algorithms/hartford_drug.edgelist > hartford
#touch -r examples/algorithms/hartford_drug.edgelist hartford
#mv -f hartford examples/algorithms/hartford_drug.edgelist


%build
python setup.py build
#PYTHONPATH=`pwd`/build/lib make -C doc html

# Setup for python3
#mv build build2
#mv networkx/*.pyc build2

# Build for python3
#python3 setup.py build


%install
# Install the python3 version
#python3 setup.py install -O1 --skip-build --root %{buildroot}

# Setup for python2
#mv build build3
#mv build2 build
#mv -f build/*.pyc pygrapvhiz

# Install the python2 version
python setup.py install -O1 --skip-build --root %{buildroot}
rm -f %{buildroot}%{_docdir}/pygraphviz-%{version}/INSTALL.txt

# Fix permissions
#grep -FRl /usr/bin/env %{buildroot}%{python_sitelib} | xargs chmod a+x
#grep -FRl /usr/bin/env %{buildroot}%{python3_sitelib} | xargs chmod a+x

# Except unfix the one where the shebang was muffed
#chmod a-x %{buildroot}%{python_sitelib}/networkx/algorithms/link_analysis/hits_alg.py
#chmod a-x %{buildroot}%{python3_sitelib}/networkx/algorithms/link_analysis/hits_alg.py

 
#%check
#mkdir site-packages
#mv pygraphviz site-packages
#PYTHONPATH=`pwd`/site-packages python -c "import pygraphviz; pygraphviz.test()"


%files
%doc %{_docdir}/pygraphviz-%{version}/*
%doc %{_docdir}/pygraphviz-%{version}/examples/*
%{python_sitearch}/*


#files -n python3-networkx
#doc installed-docs/*
#{python3_sitelib}/*


#%files doc
#%doc doc/build/html/*


%changelog
* Wed Oct 23 2011 Vedran Miletić <rivanvx@gmail.com> - 1.1-1
- Initial package.
