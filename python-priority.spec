#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A HTTP/2 Priority Implementation
Summary(pl.UTF-8):	Implementacja priorytetów HTTP/2
Name:		python-priority
Version:	1.3.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/priority/
Source0:	https://files.pythonhosted.org/packages/source/p/priority/priority-%{version}.tar.gz
# Source0-md5:	4f1ff52f7fa448e9d9cb46337ae86d1e
URL:		https://pypi.org/project/priority/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-hypothesis
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-hypothesis
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Priority is a pure-Python implementation of the priority logic for
HTTP/2, set out in RFC 7540 Section 5.3 (Stream Priority). This logic
allows for clients to express a preference for how the server
allocates its (limited) resources to the many outstanding HTTP
requests that may be running over a single HTTP/2 connection.

%description -l pl.UTF-8
Priority to czysto pythonowa implementacja logiki priorytetów dla
HTTP/2, zgodnej z sekcją 5.3 (Stream Priority) RFC 7540. Logika ta
pozwala klientom wyrażać preferencje, jak serwer ma przydzielać swoje
(ograniczone) zasoby na wiele oczekujących żądań HTTP, które mogą być
uruchomione na pojedynczym połączeniu HTTP/2.

%package -n python3-priority
Summary:	A HTTP/2 Priority Implementation
Summary(pl.UTF-8):	Implementacja priorytetów HTTP/2
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-priority
Priority is a pure-Python implementation of the priority logic for
HTTP/2, set out in RFC 7540 Section 5.3 (Stream Priority). This logic
allows for clients to express a preference for how the server
allocates its (limited) resources to the many outstanding HTTP
requests that may be running over a single HTTP/2 connection.

%description -n python3-priority -l pl.UTF-8
Priority to czysto pythonowa implementacja logiki priorytetów dla
HTTP/2, zgodnej z sekcją 5.3 (Stream Priority) RFC 7540. Logika ta
pozwala klientom wyrażać preferencje, jak serwer ma przydzielać swoje
(ograniczone) zasoby na wiele oczekujących żądań HTTP, które mogą być
uruchomione na pojedynczym połączeniu HTTP/2.

%prep
%setup -q -n priority-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
# test_period_of_repetition seems unreliable (too sensitive to system load)
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest test -k 'not test_period_of_repetition'
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest test -k 'not test_period_of_repetition'
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS.rst HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/priority
%{py_sitescriptdir}/priority-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-priority
%defattr(644,root,root,755)
%doc CONTRIBUTORS.rst HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/priority
%{py3_sitescriptdir}/priority-%{version}-py*.egg-info
%endif
