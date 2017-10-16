Name:           python-rosdistro
Version:        0.6.2	
Release:        0%{?dist}
License:        BSD, MIT
Summary:        A tool to work with rosdistro files
Url:            http://wiki.ros.org/rosdistro
Group:          descriptionevelopment/Languages/Python
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  python-devel
BuildRequires:  python-argparse
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-mock
BuildRequires:  python-PyYAML
Requires:       python-argparse
Requires:       python-PyYAML
	
%description
A tool to work with rosdistro files

%prep
%setup -q
cp %{SOURCE1001} .	

%build
%{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_bindir}/rosdistro_build_cache
%{_bindir}/rosdistro_migrate_to_rep_141
%{_bindir}/rosdistro_migrate_to_rep_143
%{_bindir}/rosdistro_reformat
%{_bindir}/rosdistro_freeze_source
%{python_sitelib}/*

%changelog
