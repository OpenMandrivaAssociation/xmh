Name:		xmh
Version:	1.0.3
Release:	2
Summary:	Send and read mail with an X interface to MH
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:		xmh-1.0.1-fix-str-fmt.patch
License:	MIT

BuildRequires:	pkgconfig(xt) >= 1.0.0
BuildRequires:	pkgconfig(xaw7) >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	x11-data-bitmaps

%description
The xmh program provides a graphical user interface to the MH Message
Handling System.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%configure
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/xmh
%{_datadir}/X11/app-defaults/Xmh
%{_mandir}/man1/xmh.1*
