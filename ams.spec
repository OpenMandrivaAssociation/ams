Summary:		Alsa Modular Synth
Name:	ams
Version:	   2.2.1
Release:		2
License:	GPLv2+
Group:	Sound
Url:	https://alsamodular.sourceforge.net/
Source0:	https://sourceforge.net/projects/alsamodular/files/alsamodular/%{version}/%{name}-%{version}.tar.xz
# Provide a desktop file
Patch0:	ams-2.2.1-add-desktop-file.patch
BuildRequires:	qt5-linguist-tools
BuildRequires:	clalsadrv-devel
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblo) >= 0.26
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Widgets)
Requires:	cmt
Requires:	mcp-plugins
Requires:	rev-plugins
Requires:	swh-plugins
Requires:	vco-plugins

%description
AlsaModularSynth is a realtime modular synthesizer and effect processor.
It features:
* MIDI controlled modular software synthesis.
* Realtime effect processing with capture from e.g. "Line In" or "Mic In".
* Full control of all synthesis and effect parameters via MIDI.
* Integrated LADSPA Browser with search capability.
* JACK Support.
NOTE: Example files are kept in %{_datadir}/ams.

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_datadir}/pixmaps/%{name}_32.xpm

#--------------------------------------------------------------------

%prep
%autosetup -p1


%build
# Fix "missing too old" message
autoreconf -vfi
export CXXFLAGS="%{optflags} -std=gnu++11"
%configure
%make_build


%install
%make_install

# Install the source provided desktop file
mkdir -p %{buildroot}/%{_datadir}/applications
install -m 0644 %{name}.desktop %{buildroot}/%{_datadir}/applications
