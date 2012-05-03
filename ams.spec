Name:       ams
Summary:    Alsa Modular Synth
Version:    2.0.1
Release:    4

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
