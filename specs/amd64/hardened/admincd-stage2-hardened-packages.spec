subarch: amd64
version_stamp: latest
target: livecd-stage2
rel_type: hardened
profile: hardened/linux/amd64/no-multilib
snapshot: latest
source_subpath: hardened/livecd-stage1-amd64-latest.tar.bz2
portage_confdir: /home/autobuild/etc/portage/
portage_overlay: /usr/local/portage

boot/kernel: linux
boot/kernel/linux/sources: ck-sources
boot/kernel/linux/config: /home/autobuild/etc/portage/kconfig

boot/kernel/linux/use:
	#minimal
	#-doc
	-bindist -branding -debug -test -pam -systemd -consolekit -policykit -dbus -kdbus -oss -pulseaudio hardened urandom ipv6 sasl ssl libressl curl_ssl_libressl -gnutls -nettle threads nptl nls unicode bzip2 lzo lzma xz zlib readline fortran clang gmp openmp ghc smp static-libs
	-udev -udisks -upower -upnp -upnp-av -avahi usb
	-system-mitkrb5 -system-heimdal -kerberos
	-java -ruby -python
	#-lua -php
	-X -gtk -gtk2 -gtk3 -qt4 -qt5
	-gvfs -gconf -gtk3 -gnome-keyring -gnome -kde -accessibility -wayland -introspection
	-libinput -libnotify
	-jit -orc
	acl caps seccomp skey smartcard xattr
	#ldap nis radius
	### DESKTOP
	X gtk gtk2 xcb xkb
	sqlite
	truetype fontconfig cups gnuplot pdf latex jadetex xetex xml iconv spell icu
	vim-syntax bash-completion
	scanner joystick
	socks5
	#snmp
	sdl sdl2 cdparanoia cdr encode
	gd djvu bmp gif jpeg jpeg2k mng png apng svg tiff cairo imlib wmf xpm
	sound jack sox speex fluidsynth midi gstreamer a52 aac flac gsm lame ladspa lash ogg openal vorbis wav mad mp3 sndfile cdda cddb dts timidity
	video -vlc mplayer mp4 mpeg mjpeg theora ffmpeg xvid x264 h323 v4l matroska vcd css dvb dvd dvdr dv quicktime
	alsa
	alsa_pcm_plugins_adpcm
	alsa_pcm_plugins_alaw
	alsa_pcm_plugins_asym
	alsa_pcm_plugins_copy
	alsa_pcm_plugins_dmix
	alsa_pcm_plugins_dshare
	alsa_pcm_plugins_dsnoop
	alsa_pcm_plugins_empty
	alsa_pcm_plugins_extplug
	alsa_pcm_plugins_file
	alsa_pcm_plugins_hooks
	alsa_pcm_plugins_iec958
	alsa_pcm_plugins_ioplug
	alsa_pcm_plugins_ladspa
	alsa_pcm_plugins_lfloat
	alsa_pcm_plugins_linear
	alsa_pcm_plugins_meter
	alsa_pcm_plugins_mmap_emul
	alsa_pcm_plugins_mulaw
	alsa_pcm_plugins_multi
	alsa_pcm_plugins_null
	alsa_pcm_plugins_plug
	alsa_pcm_plugins_rate
	alsa_pcm_plugins_route
	alsa_pcm_plugins_share
	alsa_pcm_plugins_shm
	alsa_pcm_plugins_softvol
	#directfb fbcon
	#egl
	#gles
	#gles2
	#gles3
	opengl gallium glamor uxa sna dri dri2 dri3 vaapi vdpau xa xv xvmc
	video_cards_amdgpu
	video_cards_apm
	video_cards_ast
	video_cards_chips
	video_cards_cirrus
	video_cards_dummy
	video_cards_epson
	video_cards_fbdev
	video_cards_glint
	video_cards_i128
	video_cards_i740
	video_cards_intel
	video_cards_i915
	video_cards_i965
	video_cards_mach64
	video_cards_mga
	video_cards_neomagic
	video_cards_nouveau
	video_cards_nv
	video_cards_r128
	video_cards_radeon
	video_cards_radeonsi
	video_cards_rendition
	video_cards_s3
	video_cards_s3virge
	video_cards_savage
	video_cards_siliconmotion
	video_cards_sisusb
	video_cards_tdfx
	video_cards_tga
	video_cards_trident
	video_cards_tseng
	video_cards_vesa
	video_cards_via
	video_cards_voodoo
	video_cards_nvidia
	-video_cards_fglrx
	-video_cards_geode
	-video_cards_freedreno
	-video_cards_omap
	-video_cards_omapfb
	-video_cards_qxl
	-video_cards_sunbw2
	-video_cards_suncg14
	-video_cards_suncg3
	-video_cards_suncg6
	-video_cards_sunffb
	-video_cards_sunleo
	-video_cards_suntcx
	-video_cards_tegra
	-video_cards_virtualbox
	-video_cards_vmware
	input_devices_acecad
	input_devices_aiptek
	input_devices_elographics
	input_devices_fpit
	input_devices_hyperpen
	input_devices_joystick
	input_devices_keyboard
	-input_devices_libinput
	input_devices_mouse
	input_devices_mutouch
	input_devices_penmount
	input_devices_tslib
	input_devices_vmmouse
	input_devices_void
	input_devices_synaptics
	input_devices_wacom
	-input_devices_evdev

boot/kernel/linux/packages:
##app-accessibility
##app-admin
	app-admin/chrootuid
	app-admin/grubconfig
	app-admin/ide-smart
	app-admin/logsentry
	app-admin/lsat
	app-admin/perl-cleaner
	#app-admin/python-updater
	app-admin/sudo
	#app-admin/mktwpol
	#app-admin/tripwire
	app-admin/ulogd
	app-admin/whowatch
##app-antivirus
	app-antivirus/clamav
	app-antivirus/clamav-unofficial-sigs
##app-arch
	#app-arch/alien
	#app-arch/rpm
##app-backup
	app-backup/amanda
	#app-backup/bacula
	#app-backup/bareos -> crypto_openssl.c
##app-benchmarks
	#app-benchmarks/httperf
##app-cdr
##app-crypt
	app-crypt/aescrypt
	app-crypt/bcwipe
	#app-crypt/efitools
	#app-crypt/gpa
	#app-cdr/graveman
	#app-crypt/johntheripper
##app-dicts
	#app-dicts/stardict*
##app-doc
	#app-doc/cppman
	app-doc/abs-guide
	app-doc/autobook
	app-doc/devmanual
	app-doc/elisp-manual
	app-doc/linkers-and-loaders
	app-doc/linux-device-drivers
	app-doc/linuxfromscratch
	app-doc/single-unix-specification
	app-doc/selfhtml
	app-doc/tldp-howto
	app-doc/phrack-all
##app-editors
	app-editors/hexedit
	#app-editors/emacs
##app-emacs
##app-emulation
	#app-emulation/fuse
	#app-emulation/fuse-utils
	#app-emulation/ganeti
##app-eselect
##app-forensics
	app-forensics/foremost
	app-forensics/mac-robber
	#app-forensics/autopsy
	#app-forensics/cmospwd
	app-forensics/examiner
	app-forensics/memdump
	#app-forensics/openscap
	app-forensics/pasco
	#app-forensics/libewf
	#app-forensics/rdd
	#app-forensics/rkhunter
	#app-forensics/rdd
	app-forensics/scalpel
	app-forensics/volatility
	app-forensics/yasat
##app-i18n
##app-laptop
	#app-laptop/radeontool
##app-leechcraft
	# patch required to drop dbus dependency
	#app-leechcraft/leechcraft-meta
##app-misc
	#app-misc/jail
	#app-misc/xmind
##app-mobilephone
	app-mobilephone/anyremote
	#app-mobilephone/smssend
##app-office
	app-office/dia2code
	#app-office/openerp
	#app-office/planner
	#app-office/gnumeric
	#app-office/skrooge
	#app-office/scribus
	#app-office/texmacs -> guile1.9 conflicts with latest guile required by autogen
	#app-office/texmaker -> qtwebkit -> ruby
	#app-office/texstudio -> various conflicts and inconsistencies to be analyzed separately
##app-officeext
	#app-officeext/ooo2gd
	app-officeext/barcode
	app-officeext/dmaths
	app-officeext/sun-templates
	app-officeext/texmaths
##app-pda
	#app-pda/gtkpod
	#app-pda/ipodslave
##app-portage
	#app-portage/porthole
##app-shells
##app-text
	#app-text/pandoc
##app-vim
##app-xemacs
##dev-ada
##dev-cpp
	dev-cpp/clucene
	dev-cpp/lucene++
##dev-db
	#dev-db/mysql
	#dev-db/sqlitestudio
##dev-dotnet
##dev-embedded
##dev-erlang
##dev-games
##dev-go
##dev-haskell
##dev-java
	#dev-java/ant
	#dev-java/icedtea
	#dev-java/icedtea-web
	#virtual/jre
	#virtual/jdk
##dev-lang
	dev-lang/php
	dev-lang/swig
##dev-libs
##dev-lisp
##dev-lua
##dev-ml
##dev-perl
##dev-php
##dev-python
##dev-qt
##dev-ros
##dev-ruby
##dev-scheme
##dev-tcltk
##dev-tex
##dev-texlive
##dev-util
	dev-util/indent
##dev-vcs
##distfiles
##eclass
##games-action
##games-arcade
##games-board
##games-emulation
##games-engines
##games-fps
	games-fps/darkplaces
	games-fps/freespace-scp
	games-fps/xonotic
	games-fps/yamagi-quake2
##games-kids
##games-misc
##games-mud
##games-puzzle
##games-roguelike
##games-rpg
##games-server
##games-simulation
	games-simulation/flightgear
	games-simulation/lincity-ng
	games-strategy/widelands
##games-sports
##games-strategy
	games-strategy/0ad
	games-strategy/asc
	games-strategy/crimson
	games-strategy/warzone2100
	games-strategy/wesnoth
	games-strategy/widelands
##games-util
##gnome-base
##gnome-extra
##gnustep-apps
##gnustep-base
##gnustep-libs
##header.txt
##java-virtuals
##kde-apps
##kde-frameworks
##kde-misc
##kde-plasma
##licenses
##lxde-base
##lxqt-base
##mail-client
##mail-filter
##mail-mta
##mate-base
##mate-extra
##media-fonts
	#media-fonts/corefonts
##media-gfx
##media-libs
##media-plugins
##media-radio
##media-sound
	#media-sound/grip
	media-sound/mumble
	#media-sound/musescore
	#media-sound/rhythmbox
##media-tv
	#media-tv/w_scan
##media-video
##metadata
##net-analyzer
	#net-analyzer/aimsniff
	#net-analyzer/amap
	net-analyzer/authforce
	net-analyzer/bing
	net-analyzer/bmon
	#net-analyzer/bro
	#net-analyzer/bsnmp
	net-analyzer/bwm-ng
	net-analyzer/calamaris
	net-analyzer/cnet
	#net-analyzer/dsniff
	net-analyzer/ethloop
	net-analyzer/fail2ban
	net-analyzer/ftester
	net-analyzer/fwlogwatch
	#net-analyzer/httping
	#net-analyzer/hydra
	net-analyzer/ifstat
	#net-analyzer/ipgen
	net-analyzer/iplog
	net-analyzer/ipsumdump
	#net-analyzer/ipv6toolkit
	net-analyzer/isic
	net-analyzer/macchanger
	#net-analyzer/metasploit
	#net-analyzer/nagircbot
	#net-analyzer/nagvis
	#net-analyzer/nrpe
	#net-analyzer/namebench
	#net-analyzer/ndsad
	#blocks nessus-core
	#net-analyzer/nessus
	#net-analyzer/nessus-bin
	#net-analyzer/nessus-client
	#net-analyzer/nessus-core
	#net-analyzer/nessus-libraries
	#net-analyzer/nessus-plugins
	#net-analyzer/libnasl
	net-analyzer/nettop
	net-analyzer/netwatch
	#net-analyzer/nikto
	#net-analyzer/openvas
	#net-analyzer/ospd
	#net-analyzer/portbunny
	net-analyzer/portmon
	net-analyzer/sarg
	#net-analyzer/ssldump
	#net-analyzer/sslscan
	#net-analyzer/sslsniff
	net-analyzer/synscan
	#net-analyzer/tcpreplay
	#net-analyzer/testssl
	#net-analyzer/thc-ipv6
##net-dialup
	#net-dialup/wvdial
##net-dns
	net-dns/pdnsd
	#conflict with nfs-utils
	#net-nds/portmap
	#net-nds/ypbind
	#broken
	#net-nds/yp-tools
##net-firewall
	#net-firewall/fwbuilder
	#net-firewall/ipset
	#net-firewall/ipt_netflow
	#https://bugs.gentoo.org/show_bug.cgi?id=583608
	#net-firewall/nftables
	#net-firewall/nufw
	net-firewall/shapecfg
	#net-firewall/xtables-addon
##net-fs
##net-ftp
##net-im
	#net-im/silc-server
	#net-im/skype
	#net-im/toxic
	#net-im/utox
##net-irc
##net-libs
	#net-libs/tox
##net-mail
##net-misc
	#net-misc/connman
	#net-misc/socat
##net-nds
	#net-nds/lat
##net-news
##net-nntp
##net-p2p
##net-print
	#net-print/foomatic-filters
	#net-print/foomatic-gui
##net-proxy
	#net-proxy/ziproxy
##net-voip
	#net-voip/blink
	#net-voip/ekiga
##net-vpn
##net-wireless
	#net-wireless/airpwn
	#net-wireless/hostap-utils
	#net-wireless/hostapd
	#net-wireless/kismet
	#net-wireless/kismet-ubertooth
	#net-wireless/lorcon
	net-wireless/mfoc
	net-wireless/rfkill
##packages
##perl-core
##profiles
##ros-meta
##sci-astronomy
##sci-biology
##sci-calculators
	sci-calculators/pcalc
	sci-calculators/units
	sci-calculators/wcalc
	#sci-calculators/calcoo
	#sci-calculators/calculator
	#sci-calculators/tiemu
	sci-calculators/tilp2
##sci-chemistry
##sci-electronics
##sci-geosciences
##sci-libs
##sci-mathematics
##sci-misc
##sci-physics
##sci-visualization
##scripts
##sec-policy
##skel.ebuild
##skel.metadata.xml
##sys-apps
##sys-auth
##sys-block
##sys-boot
##sys-cluster
##sys-devel
##sys-fabric
##sys-firmware
##sys-freebsd
##sys-fs
##sys-kernel
##sys-libs
##sys-power
##sys-process
	sys-process/memwatch
	sys-process/nmon
##virtual
##www-apache
##www-apps
##www-client
##www-misc
##www-plugins
##www-servers
	www-servers/apache
##x11-apps
##x11-base
##x11-drivers
##x11-libs
##x11-misc
##x11-plugins
##x11-proto
##x11-terms
##x11-themes
##x11-wm
##xfce-base
##xfce-extra
