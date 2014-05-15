Name:       ams
Summary:    Alsa Modular Synth

Version:    2.1.1
Release:    1

URL:        http://alsamodular.sourceforge.net/
Source:     http://sourceforge.net/projects/alsamodular/files/alsamodular/2.1.1/%{name}-%{version}.tar.bz2
License:    GPLv2
Group:      Sound

Requires:   cmt
Requires:   swh-plugins
Requires:   VCO-plugins
Requires:   rev-plugins
Requires:   mcp-plugins
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  qt4-devel
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  ladspa-devel
BuildRequires:  zita-alsa-pcmi-devel

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
%doc README THANKS
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/ams.1.*
%{_datadir}/pixmaps/ams_32.xpm
#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure --with-ladspa-path=%{_libdir}/ladspa
%make

%install
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