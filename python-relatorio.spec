Name:		python-relatorio
Summary:	A templating library able to output odt and pdf files

Version:	0.6.0
Release:	2
License:	GPLv3+
Group:		Development/Python
URL:		http://relatorio.openhex.org/
Source0:	http://pypi.python.org/packages/source/r/relatorio/relatorio-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:	python-genshi
BuildRequires:	python-lxml
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
A templating library which provides a way to easily output all kind
of different files (odt, ods, png, svg, ...). Adding support for more filetype
is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python objects
and report together, find reports by mimetypes/name/python objects.

%prep
%setup -q -n relatorio-%{version}

%build


%install
PYTHONDONTWRITEBYTECODE=  python setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/relatorio*
%doc AUTHORS CHANGES README



