Name:		python-relatorio
Summary:	A templating library able to output odt and pdf files

Version:	0.9.0
Release:	1
License:	GPLv3+
Group:		Development/Python
URL:		https://relatorio.openhex.org/
Source0:	https://files.pythonhosted.org/packages/99/42/66f2722399ea31799de75d51561da1a38c6c0247c057e977507b53bbd44d/relatorio-0.9.0.tar.gz
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



