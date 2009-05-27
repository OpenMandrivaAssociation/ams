%define name	ams
%define version	2.0.0
%define release %mkrel 0.rc1.2

Name: 	 	%{name}
Summary: 	Alsa modular synth
Version: 	%{version}
Release: 	%{release}

URL:		http://alsamodular.sourceforge.net/
Source:     http://prdownloads.sourceforge.net/alsamodular/%{name}-%{version}-rc1.tar.bz2
Patch0:     ams-2.0.0-rc1-fix-strings-errors.patch
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot

Requires:	cmt 
Requires:   swh-plugins 
Requires:   vco-plugins 
Requires:   rev-plugins 
Requires:   mcp-plugins
BuildRequires:	fftw2-devel 
BuildRequires:  qt4-devel 
BuildRequires:  jackit-devel 
BuildRequires:  alsa-lib-devel
BuildRequires:	ladspa-devel 
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
%setup -q -n %name-%version-rc1
%patch0 -p0

%build
%configure2_5x
%make

%install
make DESTDIR=%buildroot install
#menu

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
