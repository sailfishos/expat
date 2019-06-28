%global unversion 2_2_7

Summary: An XML parser library
Name: expat
Version: 2.2.7
Release: 1
Source0: %{name}-%{version}.tar.gz
URL: https://libexpat.github.io/
License: MIT
BuildRequires: autoconf, libtool

%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package doc
Summary:    Documentation for the expat package
Group:      Development/Documentation
Requires:   %{name} = %{version}-%{release}
Requires:   expat = %{version}-%{release}

%description doc
Documentation for the expat package.

%package devel
Summary: Libraries and header files to develop applications using expat
Requires: expat%{?_isa} = %{version}-%{release}

%description devel
The expat-devel package contains the libraries, include files and documentation
to develop XML applications with expat.

%prep
%setup -q -n expat-%{version}/upstream/expat
sed -i 's/install-data-hook/do-nothing-please/' lib/Makefile.am
./buildconf.sh

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure --without-docbook --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%{_bindir}/*
%{_libdir}/lib*.so.*

%files doc
%defattr(-,root,root,-)
%doc doc/reference.html doc/*.png doc/*.css examples/*.c
%doc %{_datadir}/doc/expat/AUTHORS
%doc %{_datadir}/doc/expat/Changes

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h