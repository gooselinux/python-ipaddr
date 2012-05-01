%define oname ipaddr

Name:           python-ipaddr
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        Library for easy IPv4 and IPv6 handling
Version:        2.1.9
Release:        3%{?dist}
URL:            http://code.google.com/p/ipaddr-py/
Source:         http://ipaddr-py.googlecode.com/files/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel

%description
Python Library for easy IPv4 and IPv6 handling.

%prep
%setup -q -n %{oname}-%{version}
# remove unneeded shebang
sed -i 1d ipaddr.py 

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%check
python ipaddr_test.py -v

%files
%defattr(-,root,root,-)
%{python_sitelib}
%doc COPYING README

#%files doc

%changelog
* Tue Aug 16 2011 Andy Grover <agrover@redhat.com> - 2.1.9-3
- Fix license string
- add %check
- Remove unneeded shebang

* Tue Aug 2 2011 Andy Grover <agrover@redhat.com> - 2.1.9-2
- Fix download URL

* Tue Jul 26 2011 Andy Grover <agrover@redhat.com> - 2.1.9-1
- Initial packaging
