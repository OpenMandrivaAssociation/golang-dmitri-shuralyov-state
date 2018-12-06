 # Run tests in check section
%bcond_without check

%global goipath         dmitri.shuralyov.com/state
%global commit          28bcc343414c6adcd7b6911f9d0ef1ad6fbf30ae

%global common_description %{expand:
States for domain types.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        States for domain types
License:        BSD
URL:            %{gourl}
# git clone dmitri.shuralyov.com/state
# cd github
# git archive --format tar.gz --prefix state-%%{commit}/ %%{commit} > state-%%{commit}.tar.gz
Source0:        state-%{commit}.tar.gz
Source1:        https://dmitri.shuralyov.com/LICENSE

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%autosetup -n state-%{commit}
cp %{S:1} .


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git28bcc34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420git28bcc34
- First package for Fedora

