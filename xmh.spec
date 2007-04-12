Name: xmh
Version: 1.0.1
Release: %mkrel 4
Summary: Send and read mail with an X interface to MH
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The xmh program provides a graphical user interface to the MH Message
Handling System.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%pre 
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files
%defattr(-,root,root)
%{_bindir}/xmh
%{_datadir}/X11/app-defaults/Xmh
%{_includedir}/X11/bitmaps/box6
%{_includedir}/X11/bitmaps/black6
%{_mandir}/man1/xmh.1x.bz2


