Name:           python-httpretty
Version:        0.9.5
Release:        6
Summary:        HTTP Client mocking tool for Python
License:        MIT
URL:            https://pypi.org/project/httpretty/
Source0:        https://files.pythonhosted.org/packages/source/h/httpretty/httpretty-%{version}.tar.gz

Patch0001:      python-httpretty-fakesock_getpeercert_noconnect.patch
Patch0002:      0001-Handle-bugs-in-older-urllib3-versions-in-one-of-the-.patch
Patch0003:      0001-Call-reset-from-setUp-and-tearDown-in-addition-to-en.patch
Patch0004:		0001-modify-python3.9-supportive-syntax.patch

BuildArch:      noarch

%description
HTTP Client mocking tool for Python.Provides a full fake TCP socket module.

%package   -n   python3-httpretty
Summary:        HTTP Client mocking tool for Python3
BuildRequires:  python3-devel python3-setuptools python3-httplib2 python3-mock 
BuildRequires:  python3-requests python3-sure python3-urllib3 python3-tornado 
BuildRequires:	python3-pip python3-nose2 python3-unittest2 python3-pytest python3-httplib2
Requires:       python3-six
%{?python_provide:%python_provide python3-httpretty}

%description -n python3-httpretty
HTTP Client mocking tool for Python3.Provides a full fake TCP socket module.

%prep
%autosetup -n httpretty-%{version} -p1
sed -i 's/^with-randomly = 1$//' setup.cfg
sed -i 's/^rednose = 1$//' setup.cfg

%build
LANG=en_US.UTF-8 %py3_build

%install
LANG=en_US.UTF-8 %py3_install

%check
export EVENTLET_NO_GREENDNS=yes
sed -Ei 's/(test_https?_passthrough)/_\1/' tests/functional/test_passthrough.py
sed -Ei 's/(test_streaming_responses)/_\1/'  tests/functional/test_requests.py
sed -Ei 's/(test_fakesock_socket_sendall_with_body_data_with_chunked_entry)/_\1/' tests/unit/test_core.py
LANG=en_US.UTF-8 %{__python3} -m nose2 -v

%files -n python3-httpretty
%doc README.rst
%license COPYING
%{python3_sitelib}/httpretty
%{python3_sitelib}/httpretty-%{version}-py3.?.egg-info

%changelog
* Mon Jan 10 2022 baizhonggui <baizhonggui@huawei.com> - 0.9.5-6
- Replace nose from nose2 dependence.

* Wed Aug 5 2020 zhangtao <zhangtao221@huawei.com> - 0.9.5-5
- Remove python2

* Sat Nov 23 2019 zhouyihang <zhouyihang1@huawei.com> - 0.9.5-4
- Package init
