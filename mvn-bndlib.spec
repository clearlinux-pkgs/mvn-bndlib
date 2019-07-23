#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-bndlib
Version  : 2.1.0
Release  : 3
URL      : https://repo1.maven.org/maven2/biz/aQute/bnd/bndlib/2.1.0/bndlib-2.1.0.jar
Source0  : https://repo1.maven.org/maven2/biz/aQute/bnd/bndlib/2.1.0/bndlib-2.1.0.jar
Source1  : https://repo1.maven.org/maven2/biz/aQute/bnd/bndlib/2.1.0/bndlib-2.1.0.pom
Source2  : https://repo1.maven.org/maven2/biz/aQute/bnd/bndlib/2.3.0/bndlib-2.3.0.jar
Source3  : https://repo1.maven.org/maven2/biz/aQute/bnd/bndlib/2.3.0/bndlib-2.3.0.pom
Source4  : https://repo1.maven.org/maven2/biz/aQute/bnd/parent/2.1.0/parent-2.1.0.pom
Source5  : https://repo1.maven.org/maven2/biz/aQute/bnd/parent/2.3.0/parent-2.3.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-bndlib-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-bndlib package.
Group: Data

%description data
data components for the mvn-bndlib package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.1.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.1.0/bndlib-2.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.1.0/bndlib-2.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.3.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.3.0/bndlib-2.3.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.3.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.3.0/bndlib-2.3.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/parent/2.1.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/parent/2.1.0/parent-2.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/parent/2.3.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/parent/2.3.0/parent-2.3.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.1.0/bndlib-2.1.0.jar
/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.1.0/bndlib-2.1.0.pom
/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.3.0/bndlib-2.3.0.jar
/usr/share/java/.m2/repository/biz/aQute/bnd/bndlib/2.3.0/bndlib-2.3.0.pom
/usr/share/java/.m2/repository/biz/aQute/bnd/parent/2.1.0/parent-2.1.0.pom
/usr/share/java/.m2/repository/biz/aQute/bnd/parent/2.3.0/parent-2.3.0.pom
