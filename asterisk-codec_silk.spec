# TODO
# - to build, you need libSKP_SILK_SDK.a in link search path
%define		asterisk_ver	10
Summary:	Unofficial SILK translator for Asterisk
Name:		asterisk-codec_silk
Version:	0.1
Release:	0.1
License:	?
Group:		Applications/System
Source0:	http://developer.skype.com/silk/SILK_SDK_SRC_v1.0.8.zip
# NoSource0-md5:	e89be0474d8f1eb82ce743a1968005cd
NoSource:	0
Source1:	https://raw.github.com/mordak/codec_silk/master/codecs/ex_silk.h
# Source1-md5:	35818c24b55982312ce96b44ed721228
Source2:	https://raw.github.com/mordak/codec_silk/master/codecs/codec_silk.c
# Source2-md5:	d0a880489516272245e26db1d7d0804a
URL:		https://github.com/mordak/codec_silk
BuildRequires:	asterisk-devel
Requires:	asterisk >= %{asterisk_ver}
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		moduledir	%{_libdir}/asterisk/modules

%description
Unofficial SILK translator for Asterisk.

NOTE: This is not a SILK encoder/decoder. The coder is provided by the
SILK library, which you have to get separately, compile, and link
against.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{moduledir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
