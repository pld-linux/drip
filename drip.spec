Summary:	DVD to Div/X-Encoder
Summary(pl):    dekoder formatu dvd do divx
Name:		drip
Version:	0.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}.tar.gz
URL:		http://drip.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	avifile >= 0.6.0 libdvdcss >= 1.0.0 libdvdread lame
Buildrequires:	libdvdread-devel libdvdcss >= 1.0.0 avifile >= 0.6.0 avifile-devel gtk+-devel ORBit-devel  lame

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
You'll need decss for handling of the DVD mpeg2 streams, and avifile
for divx;-) encoding. Dont forget to install the windows dll files for
avifile. A patched version of mpeg2divx is hooked into drip for
wrapping libmpeg3 and avifile. Also have DVD support in your OS, like
linux 2.4. Good luck backing up your stuff.

Drip is not yet finished, it has bugs and not all of the features are
implemented. Basic dvd to divx ripping seems to work.

%description -l pl
Bedziesz potrzebowal biblioteki do odkodowania DVD-Video 
dla obslugi strumienia DVD mpeg2 i kodowania avifile dla divx;-).
Nie zapomnij zainstalowac windowsowych plikow dla dla avifile.
drip nie jest jeszcze skonczonym projektem.


%prep

%setup -q

%build
%configure2_13 --prefix=%{_prefix} --mandir=%{_mandir} --with-gnome=/usr/X11R6
%{__make}

%install

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig  


gzip -9nf AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_prefix}/bin/drip
%attr(755,root,root) %{_prefix}/bin/dripencoder
%attr(755,root,root) %{_prefix}/bin/gnomedrip
%attr(755,root,root) %{_prefix}/lib/libdripspu.a
%attr(755,root,root) %{_prefix}/lib/libdripspu.la
%attr(755,root,root) %{_prefix}/lib/libdripspu.so
%attr(755,root,root) %{_prefix}/lib/libdripspu.so.0
%attr(755,root,root) %{_prefix}/lib/libdripspu.so.0.1.0
%attr(755,root,root) %{_prefix}/share/gnome/help/drip/C/figs/drip.png
%attr(644,root,root)%{_prefix}/share/gnome/help/drip/C/index.html
%attr(644,root,root)%{_prefix}/share/gnome/help/drip/C/topic.dat
%attr(644,root,root)%{_prefix}/share/pixmaps/drip/drip.png
%attr(644,root,root)%{_prefix}/share/pixmaps/drip/drip_logo.jpg
