Name:		xmh
Version:	1.0.5
Release:	1
Summary:	Send and read mail with an X interface to MH
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xt) >= 1.0.0
BuildRequires:	pkgconfig(xaw7) >= 1.0.1
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xbitmaps)

%description
The xmh program provides a graphical user interface to the MH Message
Handling System.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xmh
%{_datadir}/X11/app-defaults/Xmh
%doc %{_mandir}/man1/xmh.1*
