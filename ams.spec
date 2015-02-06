Name:       ams
Summary:    Alsa Modular Synth
Version:    2.0.1
Release:    5

URL:        http://alsamodular.sourceforge.net/
Source:     http://prdownloads.sourceforge.net/alsamodular/%{name}-%{version}.tar.bz2
Patch0:     ams-2.0.1-fix-strfmt.patch
License:    GPLv2
Group:      Sound

Requires:   cmt
Requires:   swh-plugins
Requires:   VCO-plugins
Requires:   rev-plugins
Requires:   mcp-plugins
BuildRequires:  fftw2-devel
BuildRequires:  qt4-devel
BuildRequires:  jackit-devel
BuildRequires:  libalsa-devel
BuildRequires:  ladspa-devel
BuildRequires:  clalsadrv-devel

%description
AlsaModularSynth is a realtime modular synthesizer and effect processor.
It features:
    * MIDI controlled modular software synthesis
    * Realtime effect processing with capture from e.g. "Line In" or "Mic In".
    * Full control of all synthesis and effect parameters via MIDI.
    * Integrated LADSPA Browser with search capability
    * JACK Support

NOTE: Example files are in /usr/share/ams


%files
%defattr(-,root,root)
%doc README THANKS
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/ams.1.*
%{_datadir}/pixmaps/ams_32.xpm
#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p1

%build
LDFLAGS="-ldl" %configure2_5x --with-ladspa-path=%{_libdir}/ladspa
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#menu
mkdir -p %{buildroot}/%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Alsa Modular Synth
Comment=Modular Synthesizer for ALSA
Exec=%{_bindir}/%{name}
Icon=%{_datadir}/pixmaps/ams_32.xpm
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;AudioVideoEditing;
EOF


%changelog
* Thu May 03 2012 Frank Kober <emuse@mandriva.org> 2.0.1-4
+ Revision: 795369
- bump release
- rebuild after re-importing VCO-plugins

* Sat Jul 24 2010 Frank Kober <emuse@mandriva.org> 2.0.1-3mdv2011.0
+ Revision: 558123
- rebuild for new libclalsadrv

* Mon Mar 01 2010 Frank Kober <emuse@mandriva.org> 2.0.1-2mdv2010.1
+ Revision: 513062
- rebuild
- fix desktop icon, cleanup spec

* Tue Jan 05 2010 Stéphane Téletchéa <steletch@mandriva.org> 2.0.1-1mdv2010.1
+ Revision: 486316
- Source fix

  + Frank Kober <emuse@mandriva.org>
    - new upstream version 2.0.1, strfmt patch generated from upstream cvs
    - strfmtfix patch dropped since it caused runtime errors
    - update to new version 2.0.0

* Wed May 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2.0.0-0.rc1.2mdv2010.0
+ Revision: 380172
- Bump release
- Fix previous patch

* Wed May 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2.0.0-0.rc1.1mdv2010.0
+ Revision: 380165
- Update to 2.0.0 Rc1 ( qt4 based)

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.8.7-3mdv2009.0
+ Revision: 218429
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 1.8.7-3mdv2008.1
+ Revision: 135820
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import ams


* Tue Sep 12 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.8.7-3mdv2007.0
- Use mkrel
- XDG

* Thu Nov 10 2005 Austin Acton <austin@mandriva.org> 1.8.7-2mdk
- lib64 fix

* Wed Aug 24 2005 Austin Acton <austin@mandriva.org> 1.8.7-1mdk
- 1.8.7
- source URL
- buildrequires clalsadrv

* Sat Sep 11 2004 Austin Acton <austin@mandrake.org> 1.8.5-2mdk
- require mcp-plugins

* Thu Jul 8 2004 Austin Acton <austin@mandrake.org> 1.8.5-1mdk
- 1.8.5

* Sun May 9 2004 Austin Acton <austin@mandrake.org> 1.8.1-1mdk
- 1.8.1
- require vco and rev plugins for included patches

* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 1.7.7-1mdk
- 1.7.7

* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 1.7.3-1mdk
- 1.7.3

* Sun Jan 25 2004 Franck Villaume <fvill@freesurf.fr> 1.7.2-2mdk
- fix BuildRequires : fftw2-devel

* Fri Jan 23 2004 Austin Acton <austin@mandrake.org> 1.7.2-1mdk
- 1.7.2
- remove epoch tag (0 is implied)
- back to sane versioning
- use opt flags

* Fri Jan 23 2004 Franck Villaume <fvill@freesurf.fr> 20040107-2mdk
- epoch tag = 0

* Fri Jan 09 2004 Franck Villaume <fvill@freesurf.fr> 20040107-1mdk
- cvs 20040107
- the examples files moved to demos directory
- fix buildrequires : 64bits + ladspa-devel

* Sat Aug 30 2003 Austin Acton <aacton@yorku.ca> 1.5.12-1mdk
- 1.5.12

* Fri May 23 2003 Austin Acton <aacton@yorku.ca> 1.5.9-2mdk
- change menu title

* Wed May 21 2003 Austin Acton <aacton@yorku.ca> 1.5.9-1mdk
- initial package
