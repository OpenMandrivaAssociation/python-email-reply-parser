Name:		python-email-reply-parser
Version:	0.5.12
Release:	2
Summary:	Email reply parser
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/email-reply-parser/
Source0:	email_reply_parser-0.5.12.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
Email reply parser.

%files
%{py_sitedir}/*
