%define name	ams
%define version	1.8.7
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Alsa modular synth
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/alsamodular/%{name}-%{version}.tar.bz2
URL:		http://alsamodular.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot

Requires:	cmt swh-plugins vco-plugins rev-plugins mcp-plugins
BuildRequires:	fftw2-devel qt3-devel jackit-devel alsa-lib-devel
BuildRequires:	ladspa-devel clalsadrv-devel

%description
AlsaModularSynth is a realtime modular synthesizer and effect processor.
It features:
    * MIDI controlled modular software synthesis
    * Realtime effect processing with capture from e.g. "Line In" or "Mic In".
    * Full control of all synthesis and effect parameters via MIDI.
    * Integrated LADSPA Browser with search capability
    * JACK Support

NOTE: Example files are in /usr/share/ams

%prep
%setup -q
perl -p -i -e "s|-O2|$RPM_OPT_FLAGS||g" Makefile
perl -p -i -e 's/BASE_DIR\)\/lib/BASE_DIR\)\/%{_lib}/g' Makefile
perl -p -i -e 's/usr\/X11R6\/lib/usr\/X11R6\/%{_lib}/g' Makefile
perl -p -e -e 's/lib\/ladspa/${_lib}\/ladspa/g' Makefile

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name
cp %name $RPM_BUILD_ROOT/%_bindir
# examples files move to demos ?
cp demos/*.ams $RPM_BUILD_ROOT/%_datadir/%name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="sound_section.png" needs="x11" title="Alsa Modular Synth" longtitle="Modular Synthesizer for ALSA" section="Multimedia/Sound" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Alsa Modular Synth
Comment=Modular Synthesizer for ALSA
Exec=%{_bindir}/%{name} 
Icon=sound_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;AudioVideoEditing;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README THANKS
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop

