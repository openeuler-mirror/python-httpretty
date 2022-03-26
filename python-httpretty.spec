Name:           python-httpretty
Version:        0.9.5
Release:        8
Summary:        HTTP Client mocking tool for Python
License:        MIT
URL:            https://pypi.org/project/httpretty/
Source0:        https://files.pythonhosted.org/packages/source/h/httpretty/httpretty-%{version}.tar.gz

Patch0001:      python-httpretty-fakesock_getpeercert_noconnect.patch
Patch0002:      0001-Handle-bugs-in-older-urllib3-versions-in-one-of-the-.patch
Patch0003:      0001-Call-reset-from-setUp-and-tearDown-in-addition-to-en.patch
%if "%{_arch}" == "riscv64"
#due to network issue, skip some test for riscv
Patch0004:      skip_test_due_to_build_platform.patch
Patch0005:      fix-riscv-time-diff.patch
%endif riscv

BuildArch:      noarch

%description
HTTP Client mocking tool for Python.Provides a full fake TCP socket module.

%package   -n   python3-httpretty
Summary:        HTTP Client mocking tool for Python3
BuildRequires:  python3-devel python3-setuptools python3-httplib2 python3-mock
BuildRequires:  python3-nose python3-requests python3-sure python3-urllib3 python3-tornado
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
LANG=en_US.UTF-8 %{__python3} -m nose -v

%files -n python3-httpretty
%doc README.rst
%license COPYING
%{python3_sitelib}/httpretty
%{python3_sitelib}/httpretty-%{version}-py3.?.egg-info

%changelog
* Sun Mar 27 2022 YukariChiba <i@0x7f.cc> - 0.9.5-8
- Remove time item in diff check to pass test for RISC-V
- Add ifarch macro

* Wed Feb 22 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 0.9.5-7
- bug fix, %ifarch has no effect when BuildArch is noarch
  skip test for riscv

* Tue Feb 15 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 0.9.5-6
- skip some test for riscv

* Wed Aug 5 2020 zhangtao <zhangtao221@huawei.com> - 0.9.5-5
- Remove python2

* Sat Nov 23 2019 zhouyihang <zhouyihang1@huawei.com> - 0.9.5-4
- Package init
