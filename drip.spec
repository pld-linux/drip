Summary:	DVD to DivX-Encoder
Summary(pl.UTF-8):	Koder formatu DVD do DivX
Name:		drip
Version:	0.9.0
%define		_rc	rc3
Release:	0.rc3.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://drip.sourceforge.net/files/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	0248e8e3cf788d2e3f6883fdc989381e
URL:		http://drip.sourceforge.net/
BuildRequires:	ImageMagick-devel
BuildRequires:	ORBit-devel
BuildRequires:	SDL-devel
BuildRequires:	a52dec-libs-devel >= 0.7.4
BuildRequires:	avifile-devel >= 3:0.7.22
BuildRequires:	esound-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libdvdcss-devel >= 1.2.2
BuildRequires:	libdvdread-devel >= 0.9.3
BuildRequires:	libxml2-devel
BuildRequires:	libstdc++-devel >= 5:3.0.0
BuildRequires:	mpeg2dec-devel >= 0.3.1
Requires:	avifile >= 3:0.7.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You'll need DeCSS for handling of the DVD MPEG-2 streams, and avifile
for DivX ;-) encoding. Don't forget to install the Windows DLL files
for avifile. A patched version of mpeg2divx is hooked into drip for
wrapping libmpeg3 and avifile. Also have DVD support in your OS, like
Linux 2.4. Good luck backing up your stuff.

Drip is not yet finished, it has bugs and not all of the features are
implemented. Basic DVD to DivX ripping seems to work.

%description -l pl.UTF-8
Drip używa DeCSS do obsługi strumieni DVD MPEG-2 oraz avifile do
kodowania DivX ;-). Potrzebuje plików DLL z Windows dla avifile.
Do obsługi płyt DVD trzeba mieć wsparcie w systemie (np. Linuksie
2.4).

Uwaga: Drip jeszcze nie jest skończony, ma błędy i nie wszystko
jeszcze działa; podstawowe kodowanie DVD do DivX wydaje się działać.

%prep
%setup -q -n %{name}-%{version}%{_rc}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static plugins, *.la shouldn't be needed (libgmodule used)
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{la,a}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUG* ChangeLog README TODO
%attr(755,root,root) %{_bindir}/drip
%attr(755,root,root) %{_bindir}/dripencoder
%attr(755,root,root) %{_bindir}/gnomedrip
%attr(755,root,root) %{_libdir}/libdripspu.so.*.*.*
%attr(755,root,root) %{_libdir}/libdrip_*filter.so.*.*.*
%attr(755,root,root) %{_libdir}/libdrip_*filter.so
%{_pixmapsdir}/drip
