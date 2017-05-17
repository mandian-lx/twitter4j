%{?_javapackages_macros:%_javapackages_macros}

%define oname Twitter4J
%define name %(echo %oname | tr [:upper:] [:lower:])

Summary:	An unofficial pure Java library for the Twitter API
Name:		%{name}
Version:	4.0.4
Release:	1
License:	ASL 2.0
Group:		Development/Java
URL:		http://twitter4j.org/
Source0:	https://github.com/yusuke/twitter4j/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	maven-local
#BuildRequires:	mvn(com.googlecode:kryo)
BuildRequires:	mvn(commons-logging:commons-logging-api)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(log4j:log4j)
BuildRequires:	mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:	mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:	mvn(org.slf4j:slf4j-api)
#BuildRequires:	mvn(org.springframework:spring)

%description
Twitter4J is a Twitter API binding library for the Java language.

%files -f .mfiles
%doc readme.txt
%doc readme-libs.txt
%doc LICENSE.txt

#----------------------------------------------------------------------------

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

#----------------------------------------------------------------------------

%prep
%setup -q
# Delete all prebuild JARs and classes
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Disable unbules due to unmeet dependencies
%pom_disable_module twitter4j-appengine #  com.google.appengine:appengine-api
%pom_disable_module twitter4j-http2-support #  com.squareup.okhttp:okhttp

%build
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

