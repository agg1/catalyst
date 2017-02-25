subarch: amd64
version_stamp: latest
target: livecd-stage1
rel_type: hardened
profile: hardened/linux/amd64/no-multilib
snapshot: latest
source_subpath: hardened/stage3-amd64-latest.tar.bz2
portage_confdir: /home/autobuild/etc/portage/
portage_overlay: /usr/local/portage

livecd/use:
	-awt -bindist -branding -debug -consolekit -dbus -kdbus -policykit -pam -systemd -pulseaudio -udisks -upower -upnp -upnp-av -avahi -gvfs -gtk3 -qt4 -qt5 -gnome-keyring -libnotify -gnome -kde -java -ruby -python -test hardened urandom ipv6 crypt sasl ssl openssl libressl curl_ssl_libressl -gnutls -nettle socks5 system-mitkrb5 usb threads nptl nls unicode bzip2 lzo lzma xz zlib xml static-libs
	-udev
	-wayland
	-gconf
	smp
	clang
	X
	doc
	gtk
	xcb
	xkb
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
	icu
	djvu
	bmp
	gif
	jpeg
	jpeg2k
	mng
	png
	apng
	svg
	tiff
	fluidsynth
	midi
	gstreamer
	a52
	aac
	flac
	gsm
	lame
	ladspa
	ogg
	openal
	vorbis
	wav
	mad
	mp3
	mp4
	mpeg
	speex
	theora
	ffmpeg
	xvid
	x264
	h323
	v4l
	cdda
	cddb
	css
	dvb
	dvd
	oss
	sdl
	scanner
	joystick
	sound
	video
	egl
	gles
	gles2
	gles3
	opengl
	gallium
	glamor
	uxa
	sna
	dri
	dri2
	dri3
	vaapi
	vdpau
	xa
	xv
	xvmc
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
	input_devices_libinput
	input_devices_mouse
	input_devices_mutouch
	input_devices_penmount
	input_devices_tslib
	input_devices_vmmouse
	input_devices_void
	input_devices_synaptics
	input_devices_wacom
	-input_devices_evdev
	mmx
	sse
	sse2
	ntfsprogs
	-ntfsdecrypt
	libusb
	cairo
	imlib
	sqlite
	truetype
	xetex
	fortran

livecd/packages:
	app-admin/apache-tools
	app-admin/checksec
	app-admin/chroot_safe
	app-admin/chrootuid
	app-admin/chrpath
	app-admin/cpulimit
	app-admin/diradm
	app-admin/eselect
	app-admin/evtxtools
	app-admin/genromfs
	app-admin/grubconfig
	app-admin/hddtemp
	app-admin/ide-smart
	app-admin/lnav
	app-admin/logrotate
	app-admin/logsentry
	app-admin/lsat
	app-admin/mcelog
	app-admin/pass
	app-admin/passook
	app-admin/passwordsafe
	app-admin/paxtest
	app-admin/procinfo-ng
	app-admin/perl-cleaner
	app-admin/python-updater
	#app-admin/qtpass
	app-admin/rsyslog
	app-admin/sshguard
	app-admin/superadduser
	app-admin/syslog-summary
	app-admin/testdisk
	app-admin/tmpwatch
	app-admin/mktwpol
	app-admin/tripwire
	#app-admin/ulogd
	app-admin/verynice
	app-admin/whowatch
	app-antivirus/clamav
	app-antivirus/clamav-unofficial-sigs
	app-arch/bzip2
	app-arch/cpio
	app-arch/dpkg
	app-arch/gzip
	app-arch/mt-st
	app-arch/p7zip
	app-arch/pbzip2
	app-arch/rar
	app-arch/sharutils
	app-arch/tar
	app-arch/unrar
	app-arch/unzip
	app-backup/bareos
	app-benchmarks/bonnie++
	app-benchmarks/stress-ng
	app-cdr/bashburn
	app-cdr/bin2iso
	app-cdr/burncdda
	app-cdr/ccd2iso
	app-cdr/cdrdao
	app-cdr/cdrtools
	app-cdr/cuetools
	app-cdr/dvd+rw-tools
	app-cdr/nrg2iso
	app-cdr/pburn
	app-cdr/poweriso
	app-cdr/xdvdfs-tools
	app-crypt/aescrypt
	app-crypt/aespipe
	app-crypt/bcrypt
	app-crypt/bcwipe
	#app-crypt/efitools
	#app-crypt/gcr
	app-crypt/gnupg
	#app-crypt/gpa
	app-crypt/hashalot
	app-crypt/md5deep
	app-crypt/md6sum
	app-crypt/pinentry
	app-crypt/signify
	app-dicts/aspell-de
	app-dicts/aspell-de-alt
	app-dicts/aspell-en
	app-dicts/aspell-es
	app-dicts/aspell-it
	app-dicts/aspell-fr
	app-dicts/aspell-ru
	app-dicts/myspell-de
	app-dicts/myspell-de_1901
	app-dicts/myspell-en
	app-dicts/myspell-es
	app-dicts/myspell-it
	app-dicts/myspell-fr
	app-dicts/myspell-ru
	app-doc/doxygen
	app-editors/bluefish
	app-editors/hexcurse
	app-editors/hexedit
	app-editors/nano
	#app-editors/padre
	dev-perl/List-MoreUtils
	app-editors/vim
	app-editors/wxmedit
	app-emulation/qemu
	app-emulation/spice
	#app-emulation/wine
	app-eselect/eselect-mesa
	app-eselect/eselect-opengl
	app-eselect/eselect-opencl
	app-eselect/eselect-timezone
	app-eselect/eselect-vi
	app-forensics/afl
	app-forensics/chkrootkit
	app-forensics/foremost
	app-forensics/mac-robber
	app-forensics/magicrescue
	app-forensics/ovaldi
	app-forensics/sleuthkit
	app-forensics/unhide
	app-forensics/zzuf
	app-misc/abook
	app-misc/banner
	app-misc/ca-certificates
	app-misc/rmlint
	app-misc/mc
	app-misc/tmux
	#app-misc/xmind
	app-misc/zisofs-tools
	app-mobilephone/anyremote
	app-mobilephone/gammu
	app-mobilephone/smsclient
	app-mobilephone/smstools
	app-office/dia
	app-office/homebank
	app-office/libreoffice
	app-office/libreoffice-l10n
	app-office/texmacs
	app-portage/cfg-update
	app-portage/eix
	app-portage/esearch
	app-portage/genlop
	app-portage/gentoolkit
	app-portage/gentoolkit-dev
	app-portage/layman
	app-portage/metagen
	app-portage/mirrorselect
	app-portage/portage-utils
	app-portage/porthole
	app-portage/repoman
	app-portage/ufed
	app-shells/bash
	app-shells/bash-completion
	app-shells/gentoo-bashcomp
	app-shells/zsh
	app-shells/zsh-completions
	app-shells/gentoo-zsh-completions
	app-text/dos2unix
	app-text/ghostscript-gpl
	app-text/gtkspell
	app-text/stardict
	app-text/tree
	app-text/wgetpaste
	app-text/xpdf
	app-text/docx2txt
	app-text/html2text
	app-text/html-xml-utils
	app-text/odt2txt
	app-text/texi2html
	#app-text/pandoc
	app-text/rfcutil
	app-text/htmltidy
	app-vim/ackvim
	app-vim/airline
	app-vim/align
	app-vim/alternate
	app-vim/ansiesc
	#app-vim/ant_menu
	app-vim/autoalign
	app-vim/bash-support
	app-vim/bnf-syntax
	app-vim/brainfuck-syntax
	app-vim/breakpts
	app-vim/bufexplorer
	app-vim/c-support
	app-vim/calendar
	app-vim/cctree
	app-vim/cfengine-syntax
	app-vim/checkattach
	app-vim/closetag
	app-vim/cmdalias
	app-vim/colorschemes
	app-vim/colorsel
	app-vim/csv
	app-vim/ctrlp
	app-vim/cvsmenu
	app-vim/dbext
	app-vim/detectindent
	app-vim/dhcpd-syntax
	app-vim/diffchar
	app-vim/dirdiff
	app-vim/easy-align
	app-vim/easytags
	app-vim/ebnf-syntax
	app-vim/emmet
	app-vim/eruby-syntax
	app-vim/eselect-syntax
	app-vim/extra-syntax
	app-vim/foldutil
	app-vim/fugitive
	app-vim/fuzzyfinder
	app-vim/genindent
	app-vim/gentoo-syntax
	app-vim/genutils
	app-vim/gist
	app-vim/git-patch-tags
	app-vim/gitgutter
	app-vim/gitlog
	app-vim/gitolite-syntax
	app-vim/gitv
	app-vim/gnupg
	app-vim/greputils
	app-vim/gtk-syntax
	app-vim/help-extra-syntax
	#app-vim/html5
	app-vim/increment
	app-vim/info
	app-vim/json
	app-vim/l9
	app-vim/locateopen
	app-vim/matrix
	app-vim/merginal
	app-vim/minibufexpl
	app-vim/multiplesearch
	app-vim/multvals
	app-vim/neocomplcache
	app-vim/nerdcommenter
	app-vim/nerdtree
	app-vim/nerdtree-tabs
	app-vim/nginx-syntax
	app-vim/notes
	app-vim/ntp-syntax
	app-vim/omnicppcomplete
	app-vim/pam-syntax
	app-vim/pathogen
	app-vim/pdv
	app-vim/perl-support
	app-vim/pgn-syntax
	app-vim/phpdocs
	app-vim/project
	app-vim/pushpop
	app-vim/pyclewn
	app-vim/pydiction
	app-vim/pydoc
	app-vim/pytest
	app-vim/python-mode
	app-vim/rails
	app-vim/rainbow_parentheses
	app-vim/repeat
	app-vim/reload
	app-vim/recover
	app-vim/rust-mode
	app-vim/scala-syntax
	app-vim/searchcomplete
	app-vim/securemodelines
	app-vim/selinux-syntax
	app-vim/session
	#app-vim/showmarks
	#app-vim/splice
	app-vim/supertab
	app-vim/surround
	app-vim/syntastic
	app-vim/tagbar
	app-vim/taglist
	app-vim/tcomment
	app-vim/thlnk
	app-vim/tmpl
	app-vim/tt2-syntax
	app-vim/txtfmt
	app-vim/udev-syntax
	app-vim/vcscommand
	app-vim/vim-misc
	app-vim/vimbuddy
	#app-vim/vimclojure
	app-vim/vimcommander
	app-vim/vimoutliner
	#app-vim/vimpress
	app-vim/vimpython
	app-vim/vimtex
	app-vim/webapi
	app-vim/wikipedia-syntax
	app-vim/xquery-syntax
	app-vim/xsl-syntax
	app-vim/yankring
	#app-vim/youcompleteme
	app-vim/vim-spell-cs
	app-vim/vim-spell-da
	app-vim/vim-spell-de
	app-vim/vim-spell-el
	app-vim/vim-spell-en
	app-vim/vim-spell-es
	app-vim/vim-spell-fr
	app-vim/vim-spell-he
	app-vim/vim-spell-hu
	app-vim/vim-spell-it
	app-vim/vim-spell-nl
	app-vim/vim-spell-pl
	app-vim/vim-spell-pt
	app-vim/vim-spell-ru
	dev-db/unixODBC
	dev-db/sqlite
	dev-db/pgadmin3
	dev-db/postgresql
	dev-db/redis
	dev-lang/perl
	dev-lang/python
	# broken with EGL dependency
	dev-libs/DirectFB
	dev-libs/libbsd
	dev-libs/libusb-compat
	dev-libs/gmp
	dev-libs/libxml2
	dev-libs/mpfr
	dev-libs/libressl
	dev-python/pycrypto
	dev-util/ccache
	dev-util/catalyst
	dev-util/cloc
	dev-util/cmake
	dev-util/codeblocks
	dev-util/geany
	dev-util/geany-plugins
	dev-util/indent
	dev-util/ltrace
	dev-util/pkgconfig
	dev-util/shc
	dev-util/strace
	dev-util/valgrind
	dev-vcs/cvs
	dev-vcs/git
	dev-vcs/git-crypt
	dev-vcs/subversion
	games-util/joystick
	lxde-base/lxdm
	lxde-base/lxde-meta
	mail-client/mutt
	mail-client/thunderbird
	mail-client/mailx
	mail-client/mailx-support
	mail-filter/dovecot-antispam
	mail-filter/dovecot_deleted_to_trash
	mail-filter/clamassassin
	mail-filter/procmail
	mail-filter/spamassassin
	mail-filter/opensmtpd-extras
	mail-mta/opensmtpd
	#media-fonts/corefonts
	media-fonts/croscorefonts
	media-fonts/dejavu
	media-fonts/freefont
	media-fonts/freefonts
	media-fonts/font-adobe-100dpi
	media-fonts/font-adobe-75dpi
	media-fonts/font-bitstream-100dpi
	media-fonts/font-bitstream-75dpi
	media-fonts/font-bitstream-type1
	media-fonts/font-ibm-type1
	media-fonts/font-schumacher-misc
	media-fonts/ubuntu-font-family
	media-fonts/font-xfree86-type1
	media-fonts/ttf-bitstream-vera 
	media-gfx/fbida
	media-gfx/feh
	media-gfx/gimp
	media-gfx/gtkam
	media-gfx/imagemagick
	media-gfx/inkscape
	media-gfx/gqview
	media-gfx/sane-frontends
	media-gfx/xsane
	media-gfx/xv
	media-libs/libextractor
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-libs/gstreamer
	media-libs/gst-plugins-bad
	media-libs/gst-plugins-base
	media-libs/gst-plugins-good
	media-libs/gst-plugins-ugly
	media-libs/openal
	media-libs/libsdl
	media-libs/libsdl2
	media-libs/mesa
	media-libs/netpbm
	media-libs/sdl-gfx
	media-libs/sdl-image
	media-libs/sdl-mixer
	media-libs/sdl-net
	media-libs/sdl-pango
	media-libs/sdl-sound
	media-libs/sdl-terminal
	media-libs/sdl-ttf
	media-libs/sdl2-gfx
	media-libs/sdl2-image
	media-libs/sdl2-mixer
	media-libs/sdl2-net
	media-libs/sdl2-ttf
	media-libs/sdlmm
	media-sound/alsa-tools
	media-sound/alsa-utils
	media-sound/alsaplayer
	media-sound/aumix
	media-sound/cdparanoia
	media-sound/mpc
	media-sound/mpd
	media-video/dvdrip
	media-video/lsdvd
	media-video/mplayer
	#media-video/vlc
	net-analyzer/aimsniff
	net-analyzer/angst
	net-analyzer/argus
	net-analyzer/argus-clients
	net-analyzer/arpoison
	net-analyzer/arp-scan
	net-analyzer/arptools
	net-analyzer/arpwatch
	net-analyzer/barnyard2
	net-analyzer/braa
	net-analyzer/cryptcat
	net-analyzer/cutter
	net-analyzer/dhcp_probe
	net-analyzer/dhcpdump
	net-analyzer/dnstracer
	net-analyzer/dosdetector
	net-analyzer/driftnet
	net-analyzer/egressor
	net-analyzer/ettercap
	net-analyzer/fail2ban
	net-analyzer/ffp
	net-analyzer/firewalk
	net-analyzer/fping
	net-analyzer/fragroute
	net-analyzer/gnu-netcat
	net-analyzer/hping
	net-analyzer/hunt
	net-analyzer/ifmetric
	net-analyzer/ifstat
	net-analyzer/ifstatus
	net-analyzer/iftop
	net-analyzer/ike-scan
	net-analyzer/ipaudit
	net-analyzer/ipcad
	net-analyzer/ipguard
	net-analyzer/iptraf-ng
	net-analyzer/iptstate
	net-analyzer/ipv6-toolkit
	net-analyzer/knocker
	net-analyzer/labrea
	net-analyzer/lft
	net-analyzer/linkchecker
	net-analyzer/macchanger
	net-analyzer/masscan
	net-analyzer/mbrowse
	net-analyzer/mping
	net-analyzer/mrtg
	net-analyzer/mtr
	net-analyzer/nagios
	net-analyzer/nagios-check_glsa2
	net-analyzer/nagios-plugin-check_raid
	net-analyzer/monitoring-plugins
	net-analyzer/nagios-plugins-snmp
	net-analyzer/nbtscan
	net-analyzer/netcat6
	net-analyzer/netperf
	net-analyzer/net-snmp
	net-analyzer/netwag
	net-analyzer/netwox
	net-analyzer/ngrep
	net-analyzer/nipper
	net-analyzer/nmap
	net-analyzer/nmbscan
	net-analyzer/ntop
	#net-analyzer/ntopng
	net-analyzer/p0f
	net-analyzer/packit
	net-analyzer/portsentry
	net-analyzer/ripe-atlas-tools
	net-analyzer/rrdtool
	net-analyzer/sbd
	net-analyzer/scanlogd
	net-analyzer/scanssh
	net-analyzer/scli
	net-analyzer/suricata
	net-analyzer/oinkmaster
	net-analyzer/snort
	net-analyzer/tcpdump
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-analyzer/traceroute-nanog
	net-analyzer/upnpscan
	net-analyzer/wapiti
	#net-analyzer/wireshark
	net-dialup/dial
	net-dialup/diald
	net-dialup/freeradius
	net-dialup/mingetty
	net-dialup/minicom
	net-dialup/picocom
	net-dialup/pptpclient
	net-dialup/pptpd
	net-dialup/pppconfig
	net-dialup/rp-pppoe
	#net-dialup/wvdial
	net-dns/bind-tools
	net-dns/ddclient
	net-dns/dnsmasq
	net-dns/dnstop
	net-dns/libidn
	net-firewall/arptables
	net-firewall/conntrack-tools
	net-firewall/ebtables
	#net-firewall/fwipsec
	net-firewall/fwknop
	net-firewall/ipsec-tools
	net-firewall/iptables
	net-firewall/itval
	net-firewall/nfacct
	#net-firewall/nftables
	net-firewall/psad
	net-firewall/shapecfg
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-ftp/ncftp
	net-ftp/oftpd
	net-ftp/vsftpd
	net-im/bitlbee
	net-im/pidgin
	#net-im/toxic
	#net-im/utox
	net-irc/anope
	net-irc/hexchat
	net-irc/ircd-hybrid
	net-irc/irssi
	net-irc/irssi-fish
	net-irc/irssi-otr
	net-irc/znc
	net-libs/libotr
	#net-libs/tox
	net-mail/dovecot
	net-mail/isync
	net-mail/notmuch
	net-mail/notmuchfs
	net-mail/muchsync
	net-mail/qprint
	net-misc/asterisk
	net-misc/bridge-utils
	net-misc/curl
	net-misc/dhcp
	net-misc/iputils
	net-misc/mosh
	net-misc/mrouted
	net-misc/ndisc6
	net-misc/netkit-bootparamd
	net-misc/netkit-bootpd
	net-misc/netkit-fingerd
	net-misc/netkit-routed
	net-misc/netkit-rsh
	net-misc/netkit-rusers
	net-misc/netkit-rwall
	net-misc/netkit-rwho
	net-misc/netkit-talk
	net-misc/netkit-telnetd
	net-misc/netkit-timed
	net-misc/ntp
	#net-misc/openntpd
	net-misc/openssh
	net-misc/openvpn
	net-misc/quagga
	net-misc/radvd
	net-misc/rdate
	net-misc/rdesktop
	net-misc/rsync
	net-misc/socat
	net-misc/spice-gtk
	net-misc/sstp-client
	net-misc/tightvnc
	net-misc/tor
	net-misc/urlview
	net-misc/vconfig
	net-misc/vde
	net-misc/vpnc
	net-misc/wol
	net-misc/wget
	net-misc/whois
	net-misc/WendzelNNTPd
	net-misc/yatb
	net-misc/youtube-dl
	net-misc/youtube-viewer
	net-nds/adtool
	net-nds/openldap
	net-nds/ypserv
	net-p2p/transmission
	net-print/cups
	net-print/cups-filters
	net-print/cups-pdf
	net-print/foomatic-db
	net-print/foomatic-db-engine
	net-print/foomatic-db-ppds
	#net-print/foomatic-filters
	#net-print/foomatic-gui
	net-print/gutenprint
	#net-print/lprng
	net-proxy/dante
	net-proxy/polipo
	net-proxy/privoxy
	net-proxy/squid
	net-proxy/torsocks
	net-proxy/tsocks
	net-voip/gnugk
	net-voip/linphone
	net-voip/yate
	net-wireless/aircrack-ng
	net-wireless/airsnort
	net-wireless/airtraf
	net-wireless/b43-fwcutter
	net-wireless/horst
	net-wireless/iw
	net-wireless/mdk
	net-wireless/pyrit
	net-wireless/cpyrit-opencl
	net-wireless/wepattack
	net-wireless/wepdecrypt
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sci-mathematics/octave
	sci-mathematics/octave-epstk
	sci-visualization/gnuplot
	sys-apps/arrayprobe
	sys-apps/acl
	sys-apps/attr
	sys-apps/cciss_vol_status
	sys-apps/chname
	sys-apps/coreutils
	sys-apps/dcfldd
	sys-apps/net-tools
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/dmidecode
	sys-apps/dstat
	sys-apps/ethtool
	sys-apps/file
	sys-apps/findutils
	sys-apps/gawk
	sys-apps/gptfdisk
	sys-apps/grep
	sys-apps/groff
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/i2c-tools
	#sys-apps/ipmitool
	#sys-apps/ipmiutil
	sys-apps/iproute2
	#sys-apps/irqbalance
	sys-apps/keyutils
	sys-apps/less
	sys-apps/lshw
	sys-apps/lsb-release
	sys-apps/man-db
	sys-apps/man-pages
	sys-apps/man-pages-posix
	sys-apps/memtester
	sys-apps/miscfiles
	sys-apps/mlocate
	sys-apps/net-tools
	sys-apps/pciutils
	sys-apps/pcmciautils
	sys-apps/pcsc-lite
	sys-apps/pmount
	sys-apps/portage
	sys-apps/sdparm
	sys-apps/sed
	sys-apps/setserial
	sys-apps/sg3_utils
	sys-apps/smartmontools
	sys-apps/systrace
	sys-apps/texinfo
	sys-apps/usbutils
	sys-apps/util-linux
	sys-apps/vbetool
	sys-apps/which
	#sys-apps/clrngd
	sys-apps/rng-tools
	sys-auth/skey
	sys-block/aoetools
	sys-block/vblade
	sys-block/fio
	sys-block/mpt-status
	sys-block/mtx
	sys-block/open-iscsi
	sys-block/parted
	sys-block/tw_cli
	sys-boot/grub
	sys-boot/syslinux
	sys-boot/winusb
	sys-devel/autoconf
	sys-devel/autoconf-wrapper
	sys-devel/autogen
	sys-devel/automake
	sys-devel/automake-wrapper
	sys-devel/bc
	sys-devel/binutils
	sys-devel/binutils-config
	sys-devel/bison
	sys-devel/gcc
	sys-devel/gcc-config
	sys-devel/flex
	sys-devel/clang
	sys-devel/distcc
	sys-devel/gcc
	sys-devel/gcc-config
	sys-devel/gettext
	sys-devel/gdb
	sys-devel/gnuconfig
	sys-devel/libtool
	sys-devel/m4
	sys-devel/llvm
	sys-devel/make
	sys-devel/patch
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/ddrescue
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/ext3grep
	sys-fs/extundelete
	sys-fs/f2fs-tools
	sys-fs/hfsutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/quota
	sys-fs/reiserfsprogs
	sys-fs/sshfs
	sys-fs/squashfs-tools
	sys-fs/sysfsutils
	sys-fs/xfsprogs
	sys-kernel/genkernel
	sys-kernel/linux-docs
	sys-kernel/linux-headers
	sys-libs/db
	sys-libs/gdbm
	sys-libs/gpm
	sys-libs/libkudzu
	sys-libs/libsmbios
	sys-power/acpid
	sys-process/at
	sys-process/atop
	sys-process/audit
	sys-process/cronie
	sys-process/ftop
	sys-process/htop
	sys-process/lsof
	sys-process/procps
	sys-process/psmisc
	sys-process/schedtool
	#dev-java/ant
	#dev-java/icedtea
	#dev-java/icedtea-web
	#virtual/jre
	#virtual/jdk
	virtual/opengl
	virtual/pkgconfig
	www-apps/ikiwiki
	dev-perl/Perl-Tidy
	dev-perl/Search-Xapian
	dev-perl/Digest-SHA1
	dev-perl/Mail-Sendmail
	dev-perl/XML-Writer
	dev-perl/Sort-Naturally
	dev-perl/Text-CSV
	dev-perl/Text-WikiFormat
	dev-perl/HTML-Tree
	app-text/tesseract
	app-text/texlive
	app-text/xapian-omega
	www-client/firefox
	www-client/lynx
	www-client/w3m
	www-servers/fnord
	www-servers/nginx
	x11-apps/appres
	x11-apps/editres
	x11-apps/mesa-progs
	x11-apps/xauth
	x11-apps/xbacklight
	x11-apps/xcalc
	x11-apps/xcmsdb
	x11-apps/xconsole
	x11-apps/xcursorgen
	x11-apps/xdriinfo
	x11-apps/xev
	x11-apps/xf86dga
	x11-apps/xfd
	x11-apps/xfontsel
	x11-apps/xgamma
	x11-apps/xhost
	x11-apps/xinit
	x11-apps/xkbcomp
	x11-apps/xkbprint
	x11-apps/xkbutils
	x11-apps/xmodmap
	x11-apps/xrandr
	x11-apps/xrdb
	x11-apps/xset
	x11-apps/xsetroot
	x11-apps/xvinfo
	x11-base/xorg-drivers
	x11-base/xorg-server
	x11-base/xorg-x11
	x11-libs/gtk+extra
	x11-libs/libva
	x11-misc/i3status
	x11-misc/openbox-menu
	x11-misc/pcmanfm
	x11-misc/xautolock
	x11-misc/xcalib
	x11-misc/xtrlock
	x11-terms/xterm
	x11-wm/i3
	x11-wm/openbox
