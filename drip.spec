Summary:	DVD to Div/X-Encoder
Name:		drip
Version:	0.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}.tar.gz
URL:		http://drip.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	avifile >= 0.6.0 libdvdcss >= 1.0.0 libdvdread orbitcpp lame
Buildrequires:	libdvdcss >= 1.0.0 avifile >= 0.6.0 gtk+-devel ORBit-devel orbitcpp lame

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

%prep

%setup -q

%build
CFLAGS="%{rpmcflags}" ./configure --prefix=%{_prefix} --mandir=%{mandir} --with-gnome=/usr/X11R6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
[ "$RPM_BUILD_ROOT" = "/var/tmp/%{name}-%{version}-%{release}" ] && rm -rf $RPM_BUILD_ROOT;

%{__make} DESTDIR=$RPM_BUILD_ROOT install

/sbin/ldconfig -n $RPM_BUILD_ROOT

#find $RPM_BUILD_ROOT -type f -o -type l |sed -e "s|$RPM_BUILD_ROOT||g" > filelist

%clean
[ "$RPM_BUILD_ROOT" = "/var/tmp/%{name}-%{version}-%{release}" ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_prefix}/bin/drip
%{_prefix}/bin/dripencoder
%{_prefix}/bin/gnomedrip
%{_prefix}/lib/libdripspu.a
%{_prefix}/lib/libdripspu.la
%{_prefix}/lib/libdripspu.so
%{_prefix}/lib/libdripspu.so.0
%{_prefix}/lib/libdripspu.so.0.1.0
%{_prefix}/help/drip/C/figs/drip.png
%{_prefix}/help/drip/C/index.html
%{_prefix}/help/drip/C/topic.dat
%{_prefix}/share/pixmaps/drip/drip.png
%{_prefix}/share/pixmaps/drip/drip_logo.jpg
%{_prefix}/share/pixmaps/drip/phosphor-persistence.gif
