Summary:	DVD to DivX-Encoder
Summary(pl):    Koder formatu DVD do DivX
Name:		drip
Version:	0.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://drip.sourceforge.net/files/%{name}-%{version}.tar.gz
URL:		http://drip.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	avifile-devel >= 0.6.0
BuildRequires:	gtk+-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libdvdcss-devel >= 1.0.0
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
%setup -q

%build
%configure2_13 \
	--with-gnome=/usr/X11R6

%{__make}

%install

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog INSTALL NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT;

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig  

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/drip
%attr(755,root,root) %{_bindir}/dripencoder
%attr(755,root,root) %{_bindir}/gnomedrip
%attr(755,root,root) %{_libdir}/libdripspu.la
%attr(755,root,root) %{_libdir}/libdripspu.so.0.1.0
%dir %{_datadir}/gnome/help/drip
%dir %{_datadir}/gnome/help/drip/C
%dir %{_datadir}/gnome/help/drip/C/digs
%{_datadir}/gnome/help/drip/C/figs/drip.png
%{_datadir}/gnome/help/drip/C/index.html
%{_datadir}/gnome/help/drip/C/topic.dat
%dir %{_pixmapsdir}/drip
%{_pixmapsdir}/drip/drip.png
%{_pixmapsdir}/drip/drip_logo.jpg
