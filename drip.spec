Summary:	DVD to DivX-Encoder
Summary(pl):	Koder formatu DVD do DivX
Name:		drip
Version:	0.9.0
Release:	0.RC1.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://drip.sourceforge.net/files/%{name}-%{version}-RC1.tar.gz
# Source0-md5:	1bc27dbb4080da18e6153253a5087156
URL:		http://drip.sourceforge.net/
BuildRequires:	ImageMagick-devel
BuildRequires:	ORBit-devel
BuildRequires:	a52dec-libs-devel >= 0.7.4
BuildRequires:	avifile-devel >= 0.7.22
BuildRequires:	esound-devel
BuildRequires:	gcc-c++ >= 3.0.0
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libdvdcss-devel >= 1.2.2
BuildRequires:	libdvdread-devel >= 0.9.3
BuildRequires:	libxml2-devel
BuildRequires:	mpeg2dec-devel >= 0.3.1
Requires:	avifile >= 0.7.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You'll need DeCSS for handling of the DVD MPEG-2 streams, and avifile
for DivX ;-) encoding. Don't forget to install the Windows DLL files
for avifile. A patched version of mpeg2divx is hooked into drip for
wrapping libmpeg3 and avifile. Also have DVD support in your OS, like
Linux 2.4. Good luck backing up your stuff.

Drip is not yet finished, it has bugs and not all of the features are
implemented. Basic DVD to DivX ripping seems to work.

%description -l pl
Drip u¿ywa DeCSS do obs³ugi strumieni DVD MPEG-2 oraz avifile do
kodowania DivX ;-). Potrzebuje plików DLL z Windows dla avifile.
Do obs³ugi p³yt DVD trzeba mieæ wsparcie w systemie (np. Linuksie
2.4).

Uwaga: Drip jeszcze nie jest skoñczony, ma b³êdy i nie wszystko
jeszcze dzia³a; podstawowe kodowanie DVD do DivX wydaje siê dzia³aæ.

%prep
%setup -q -n %{name}-%{version}-RC1

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
