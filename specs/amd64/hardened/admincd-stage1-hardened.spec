subarch: amd64
version_stamp: latest
target: livecd-stage1
rel_type: hardened
profile: hardened/linux/amd64/no-multilib
snapshot: latest
source_subpath: hardened/stage4-amd64-latest.tar.bz2
portage_confdir: /home/catalyst/etc/portage/
#portage_overlay: /home/source/portage/proj/musl
#chost: TARCH-gentoo-linux-musl
cflags: -O3 -pipe -march=nehalem -mtune=nehalem
cxxflags: -O3 -pipe -march=nehalem -mtune=nehalem

#-udev
livecd/use:
	-consolekit
	-policykit
	-pam
	-systemd
	-kdbus
	-dbus
    -pulseaudio
    -bindist
	-branding
	-gvfs
	-gnome-keyring
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
	bzip2
#	deprecated
	fbcon
#	fbcondecor
    hardened
	ipv6
	livecd
	loop-aes
	extra-ciphers
	keyscrub
	lvm1
	midi
	mng
	modules
	ncurses
	nls
	nptl
	nptlonly
	png
#	portaudio
	readline
	socks5
	ssl
	truetype
	unicode
	urandom
	usb
#    doc
#    latex
#	static

livecd/packages:
#    app-doc/doxygen
	app-admin/bastille
	app-admin/checksec
	app-admin/chroot_safe
	app-admin/chrootuid
	app-admin/chrpath
	app-admin/clog
	app-admin/conky
	app-admin/conkyforecast
	app-admin/cpulimit
	app-admin/denyhosts
	app-admin/dio
#	app-admin/diradm
	app-admin/eselect
	app-admin/evtxtools
	app-admin/fam
	app-admin/fetchlog
	app-admin/hardening-check
	app-admin/hddtemp
	app-admin/ide-smart
#	app-admin/kedpm
#	app-admin/keepass
#	app-admin/keepassx
#	app-admin/kpcli
	app-admin/lnav
	app-admin/logcheck
	app-admin/logmon
	app-admin/logrotate
#	app-admin/logsentry
	app-admin/lsat
	app-admin/makepasswd
	app-admin/mcelog
	app-admin/mktwpol
	app-admin/multilog-watch
	app-admin/pass
	app-admin/passook
	app-admin/passwordsafe
	app-admin/pprocm
#	app-admin/procinfo
	app-admin/procinfo-ng
	app-admin/psmon
	app-admin/pwcrypt
	app-admin/pwgen
	app-admin/quickswitch
	app-admin/sshguard
	app-admin/superadduser
	app-admin/syslog-ng
	app-admin/syslog-summary
	app-admin/sysstat
	app-admin/testdisk
	app-admin/tmpwatch
	app-admin/tripwire
	app-admin/usbview
	app-admin/vault
	app-admin/verynice
#	app-admin/webmin
	app-admin/whowatch
	app-admin/xtail
#	app-antivirus/clamav
#	app-antivirus/clamav-unofficial-sigs
	app-arch/alien
	app-arch/bzip2
	app-arch/cpio
	app-arch/dpkg
	app-arch/gzip
#	PATH_MAX rumble
	app-arch/mt-st
	app-arch/p7zip
	app-arch/pbzip2
	app-arch/rar
	app-arch/tar
	app-arch/unrar
	app-arch/unzip
	app-backup/duplicity
	app-benchmarks/cpuburn
	app-benchmarks/bonnie
	app-benchmarks/bonnie++
	app-benchmarks/dbench
	app-benchmarks/httperf
	app-benchmarks/i7z
	app-benchmarks/iozone
	app-benchmarks/stress
	app-benchmarks/tiobench
    app-cdr/bashburn
	app-cdr/bin2iso
	app-cdr/cdrdao
#	app-cdr/cdrkit
    app-cdr/cdrtools
    app-cdr/dvd+rw-tools
	app-cdr/nrg2iso
    app-cdr/xcdroast
	app-crypt/aescrypt
	app-crypt/aespipe
	app-crypt/bcrypt
	app-crypt/bcwipe
	app-crypt/gnupg
	app-crypt/pinentry
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
	#stardict
	app-doc/abs-guide
	app-doc/autobook
#	app-doc/cppman
#	app-doc/devmanual
#	app-doc/phrack-all
	app-editors/bluefish
#	app-editors/emacs
	app-editors/hexcurse
	app-editors/hexedit
	app-editors/mg
	app-editors/vim
#	app-emacs/ebuild-mode
#	app-emulation/cloud-init
#	app-emulation/xen-tools
	app-emulation/qemu
#	app-emulation/spice
	app-emulation/virt-manager
#	app-emulation/wine
	app-eselect/eselect-mesa
	app-eselect/eselect-opengl
	app-eselect/eselect-opencl
	app-eselect/eselect-timezone
	app-forensics/afl
	app-forensics/aide
#	app-forensics/air
	app-forensics/autopsy
	app-forensics/chkrootkit
#	app-forensics/cmospwd
	app-forensics/memdump
	app-forensics/rkhunter
	app-forensics/sleuthkit
	app-forensics/unhide
	app-forensics/volatility
	app-forensics/zzuf
#	app-laptop/i8kutils
#	app-leechcraft
	app-misc/ca-certificates
#	app-misc/beagle
	app-misc/colordiff
	app-misc/mc
#	app-misc/pax-utils
	app-misc/screen
#	app-misc/splitvt
	app-misc/tmux
	app-misc/vlock
	app-mobilephone/smsclient
	app-mobilephone/smssend
	app-mobilephone/smstools
	app-office/dia
#	app-office/gnucash
#	app-office/gnumeric
	app-office/libreoffice
	app-office/libreoffice-l10n
#	app-office/scribus
#	app-pda/gtkpod
#	app-pda/ipodslave
	app-portage/eix
	app-portage/genlop
	app-portage/gentoolkit
	app-portage/gentoolkit-dev
	#app-portage/herdstat
	app-portage/layman
	app-portage/mirrorselect
	app-portage/portage-utils
	app-portage/porthole
	app-portage/repoman
	app-portage/ufed
	app-shells/bash
	app-shells/dash
	app-shells/bash-completion
	app-shells/gentoo-bashcomp
#	app-shells/zsh
#	app-text/evince
#	app-text/tetex
	app-text/tree
	app-text/stardict
	app-text/dos2unix
	app-text/wgetpaste
	app-vim/gentoo-syntax
	dev-lang/perl
	dev-lang/python
	dev-libs/openssl
#	dev-libs/libressl
#	dev-util/anjuta
	dev-util/ccache
	dev-util/catalyst
	dev-util/cmake
	dev-util/codeblocks
	dev-util/indent
#	dev-util/kdbg
	dev-util/ltrace
	dev-util/strace
	dev-util/valgrind
#	dev-vcs/cvs
	dev-vcs/git
	dev-vcs/git-crypt
#	dev-vcs/subversion
#	lxde-base/lxappearance
##	lxde-base/lxappearance-obconf
#	lxde-base/lxde-common
#	lxde-base/lxde-icon-theme
#	lxde-base/lxde-meta
#	lxde-base/lxdm
#	lxde-base/lxinput
#	lxde-base/lxlauncher
#	lxde-base/lxmenu-data
#	lxde-base/lxpanel
#	lxde-base/lxrandr
#	lxde-base/lxsession
#	lxde-base/lxsession-edit
#	lxde-base/lxshortcut
#	lxde-base/lxtask
#	lxde-base/lxterminal
#	lxde-base/menu-cache
#	mail-client/alpine
	mail-client/mutt
	mail-client/thunderbird
	mail-client/mailx
	mail-client/mailx-support
#	mail-filter/procmail
#	mail-filter/clamassassin
#	mail-filter/spamassassin
#	mail-mta/courier
#	mail-mta/exim
#	mail-mta/msmtp
#	mail-mta/postfix
#	mail-mta/sstmp
	media-gfx/blender
#	media-gfx/digikam
	media-gfx/fbida
	media-gfx/feh
	media-gfx/fbgrab
	media-gfx/gimp
	media-gfx/gtkam
	media-gfx/inkscape
	media-gfx/xsane
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-libs/gstreamer
	media-libs/openal
	media-libs/libsdl
	media-libs/libsdl2
	media-libs/mesa
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
	media-plugins/gst-plugins-a52dec
	media-plugins/gst-plugins-alsa
#	media-plugins/gst-plugins-amr
#	media-plugins/gst-plugins-annodex
#	media-plugins/gst-plugins-assrender
#	media-plugins/gst-plugins-bluez
	media-plugins/gst-plugins-cdio
	media-plugins/gst-plugins-cdparanoia
#	media-plugins/gst-plugins-dash
#	media-plugins/gst-plugins-dtls
#	media-plugins/gst-plugins-dts
#	media-plugins/gst-plugins-dv
#	media-plugins/gst-plugins-dvb
#	media-plugins/gst-plugins-dvdread
#	media-plugins/gst-plugins-faac
#	media-plugins/gst-plugins-faad
	media-plugins/gst-plugins-ffmpeg
	media-plugins/gst-plugins-flac
#	media-plugins/gst-plugins-gconf
#	media-plugins/gst-plugins-gdkpixbuf
#	media-plugins/gst-plugins-gio
	media-plugins/gst-plugins-gl
#	media-plugins/gst-plugins-gsm
#	media-plugins/gst-plugins-hls
#	media-plugins/gst-plugins-ivorbis
#	media-plugins/gst-plugins-jpeg
	media-plugins/gst-plugins-ladspa
	media-plugins/gst-plugins-lame
	media-plugins/gst-plugins-libav
#	media-plugins/gst-plugins-libde265
#	media-plugins/gst-plugins-libmms
#	media-plugins/gst-plugins-libnice
	media-plugins/gst-plugins-libpng
#	media-plugins/gst-plugins-libvisual
#	media-plugins/gst-plugins-mad
	media-plugins/gst-plugins-meta
#	media-plugins/gst-plugins-modplug
	media-plugins/gst-plugins-mpeg2dec
	media-plugins/gst-plugins-mpeg2enc
#	media-plugins/gst-plugins-mplex
#	media-plugins/gst-plugins-musepack
#	media-plugins/gst-plugins-neon
#	media-plugins/gst-plugins-ofa
	media-plugins/gst-plugins-ogg
	media-plugins/gst-plugins-openh264
#	media-plugins/gst-plugins-opus
	media-plugins/gst-plugins-oss
#	media-plugins/gst-plugins-pango
#	media-plugins/gst-plugins-raw1394
#	media-plugins/gst-plugins-resindvd
#	media-plugins/gst-plugins-rtmp
#	media-plugins/gst-plugins-schroedinger
#	media-plugins/gst-plugins-shout2
#	media-plugins/gst-plugins-sidplay
#	media-plugins/gst-plugins-smoothstreaming
#	media-plugins/gst-plugins-soundtouch
#	media-plugins/gst-plugins-soup
#	media-plugins/gst-plugins-speex
#	media-plugins/gst-plugins-taglib
#	media-plugins/gst-plugins-theora
#	media-plugins/gst-plugins-twolame
#	media-plugins/gst-plugins-uvch264
#	media-plugins/gst-plugins-v4l2
#	media-plugins/gst-plugins-vaapi
#	media-plugins/gst-plugins-voaacenc
#	media-plugins/gst-plugins-voamrwbenc
	media-plugins/gst-plugins-vorbis
	media-plugins/gst-plugins-vp8
	media-plugins/gst-plugins-vpx
	media-plugins/gst-plugins-wavpack
	media-plugins/gst-plugins-x
	media-plugins/gst-plugins-x264
#	media-plugins/gst-plugins-x265
#	media-plugins/gst-plugins-ximagesrc
	media-plugins/gst-plugins-xvid
	media-plugins/gst-plugins-xvideo
	media-sound/alsa-tools
	media-sound/alsa-utils
	media-sound/alsaplayer
#	media-sound/audacious
	media-sound/audacity
#	media-sound/easytag
#	media-sound/grip
#	media-sound/hydrogen
#	media-sound/rhythmbox
#	media-tv/w_scan
	media-video/dvdrip
	media-video/lsdvd
	media-video/mplayer
#	media-video/smplayer
#	media-video/vlc
	media-video/xine-ui
#	net-analyzer/alive
	net-analyzer/amap
	net-analyzer/angst
	net-analyzer/argus
	net-analyzer/argus-clients
	net-analyzer/arpoison
	net-analyzer/arptools
	net-analyzer/arpwatch
	net-analyzer/authforce
	net-analyzer/bing
	net-analyzer/bmon
	net-analyzer/braa
	net-analyzer/bro
	net-analyzer/bwm-ng
	net-analyzer/cbm
	net-analyzer/cryptcat
	net-analyzer/cutter
	net-analyzer/dhcp_probe
	net-analyzer/dhcpdump
	net-analyzer/dnstracer
#	net-analyzer/dosdetector
	net-analyzer/driftnet
	net-analyzer/dsniff
#	net-analyzer/egressor
#	net-analyzer/etherape
	net-analyzer/ettercap
	net-analyzer/fail2ban
	net-analyzer/ffp
	net-analyzer/firewalk
	net-analyzer/fping
	net-analyzer/fragroute
	net-analyzer/ftester
#	net-analyzer/fwlogwatch
#	net-analyzer/gnu-netcat
	net-analyzer/hping
	net-analyzer/httping
	net-analyzer/hunt
	net-analyzer/hydra
	net-analyzer/ifmetric
	net-analyzer/ifstat
	net-analyzer/ifstatus
	net-analyzer/iftop
	net-analyzer/ike-scan
	net-analyzer/ipguard
	net-analyzer/iptraf-ng
	net-analyzer/iptstate
#	net-analyzer/ipv6-toolkit
	net-analyzer/isic
	net-analyzer/knocker
#	net-analyzer/lft
	net-analyzer/linkchecker
	net-analyzer/macchanger
	net-analyzer/masscan
#	net-analyzer/metasploit
#	net-analyzer/monitoring-plugins
#	net-analyzer/nagios
	net-analyzer/namebench
	net-analyzer/nessus
#	net-analyzer/net-snmp
#	net-analyzer/netcat
#	net-analyzer/netcat6
	net-analyzer/netwox
	net-analyzer/ngrep
	net-analyzer/nikto
	net-analyzer/nipper
#	net-analyzer/nmbscan
	net-analyzer/nmap
	net-analyzer/ntop
	net-analyzer/ntopng
	net-analyzer/openvas
	net-analyzer/p0f
	net-analyzer/packit
#	net-analyzer/portbunny
	net-analyzer/portsentry
	net-analyzer/rrdtool
#	net-analyzer/sarg
	net-analyzer/scanlogd
	net-analyzer/scanssh
	net-analyzer/scli
	net-analyzer/snort
	net-analyzer/ssldump
	net-analyzer/sslscan
#	net-analyzer/sslsniff
	net-analyzer/synscan
	net-analyzer/tcpdump
	net-analyzer/tcptraceroute
#	uint16_t not found???
	net-analyzer/testssl
	net-analyzer/traceroute
	net-analyzer/traceroute-nanog
	net-analyzer/tcpdump
	net-analyzer/mtr
	net-analyzer/wireshark
#	net-dialup/globespan-adsl
	net-dialup/mingetty
	net-dialup/minicom
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-dns/bind-tools
	net-dns/ddclient
	net-dns/dnsmasq
#	net-dns/dnstop
	net-dns/pdns
	net-firewall/arptables
	net-firewall/conntrack-tools
	net-firewall/ebtables
#	net-firewall/fwanalog
	net-firewall/fwbuilder
	net-firewall/fwipsec
	net-firewall/fwknop
	net-firewall/ipsec-tools
#	net-firewall/ipset
#	net-firewall/ipt_netflow
	net-firewall/iptables
	net-firewall/itval
	net-firewall/nfacct
#	net-firewall/nftables
#	net-firewall/nufw
	net-firewall/psad
#	net-firewall/pftop
#	net-firewall/shapecfg
#	net-firewall/ufw
	net-firewall/ufw-frontends
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-fs/samba
	net-fs/sshfs
	net-ftp/filezilla
	net-ftp/ftp
	net-ftp/ncftp
#	net-ftp/vsftpd
	net-im/pidgin
	net-irc/hexchat
	net-irc/irssi
	net-irc/weechat
	net-irc/znc
#	net-mail/dovecot
	net-misc/bridge-utils
	net-misc/curl
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ndisc6
	net-misc/ntp
#	net-misc/openntpd
	net-misc/openssh
	net-misc/openvpn
	net-misc/radvd
	net-misc/rdate
	net-misc/rdesktop
	net-misc/rsync
	net-misc/socat
#	net-misc/spice-gtk
	net-misc/sstp-client
#	net-misc/telnet-bsd
	net-misc/tightvnc
	net-misc/tor
	net-misc/vconfig
	net-misc/vpnc
	net-misc/wakeonlan
	net-misc/wget
	net-misc/whois
	net-misc/youtube-dl
	net-misc/youtube-viewer
#	net-nds/ypserv
#	net-nds/openldap
#	net-news/
	net-p2p/transmission
	net-print/cups
	net-proxy/dante
	net-proxy/privoxy
	net-proxy/squid
	net-proxy/torsocks
	net-proxy/tsocks
#	net-proxy/ziproxy
#	net-voip/
#	net-wireless/aircrack-ng
#	net-wireless/airpwn
	net-wireless/airsnort
	net-wireless/airtraf
	net-wireless/b43-fwcutter
	net-wireless/cpyrit-opencl
#	net-wireless/bcm43xx-fwcutter
	net-wireless/horst
	net-wireless/hostap-utils
	net-wireless/hostapd
	net-wireless/iw
#	net-wireless/kismet
#	net-wireless/lorcon
	net-wireless/mdk
	net-wireless/mfoc
	net-wireless/pyrit
	net-wireless/rfkill
	net-wireless/wepattack
	net-wireless/wepdecrypt
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
#	net-wireless/prism54-firmware
#	net-wireless/ipw2100-firmware
#	net-wireless/ipw2200-firmware
#	net-wireless/zd1201-firmware
#	net-wireless/zd1211-firmware
#	sci-*/
#	sys-apps/apmd
	sys-apps/arrayprobe
	sys-apps/acl
	sys-apps/attr
	sys-apps/busybox
	sys-apps/cciss_vol_status
	sys-apps/chname
	sys-apps/coreutils
	sys-apps/dcfldd
	sys-apps/diffutils
	sys-apps/dmidecode
	sys-apps/dstat
	sys-apps/ethtool
	sys-apps/file
	sys-apps/findutils
	sys-apps/flashrom
	sys-apps/fxload
	sys-apps/gawk
	sys-apps/gptfdisk
#	sys-apps/gradm
	sys-apps/grep
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/ipmitool
	sys-apps/iproute2
	sys-apps/less
	sys-apps/lsb-release
	sys-apps/man
	sys-apps/man-pages
	sys-apps/man-pages-posix
	sys-apps/memtester
	sys-apps/mlocate
#	sys-apps/netplug
	sys-apps/pciutils
#	sys-apps/pcmciautils
#	sys-apps/pcsc-lite
#	sys-apps/pmount
	sys-apps/sdparm
	sys-apps/sed
	sys-apps/setserial
	sys-apps/sg3_utils
#	sys-apps/slocate
	sys-apps/smartmontools
	sys-apps/usbutils
	sys-apps/util-linux
	sys-apps/which
	sys-apps/x86info
	sys-apps/portage
	sys-block/aoetools
	sys-block/disktype
	sys-block/fio
	sys-block/gparted
#	sys-block/mpt-status
	sys-block/mtx
	sys-block/open-iscsi
	sys-block/parted
	sys-block/partimage
#	sys-block/qla-fc-firmware
	sys-block/tw_cli
#	sys-boot/grub
	sys-boot/syslinux
	sys-boot/winusb
	sys-devel/autoconf
	sys-devel/autogen
	sys-devel/automake
	sys-devel/bc
    sys-devel/binutils-config
#    sys-devel/clang
#	sys-devel/distcc
    sys-devel/gcc-config
	sys-devel/gdb
	sys-devel/libtool
#	sys-devel/llvm
	sys-devel/make
#	sys-fabric/
#	sys-firmware/
#	sys-firmware/iwl3945-ucode
#	sys-firmware/iwl4965-ucode
#	sys-firmware/iwl5000-ucode
#	sys-freebsd/
#	sys-fs/eudev
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
	sys-fs/squashfs-tools
	sys-fs/sysfsutils
#	sys-fs/xfsprogs
	sys-kernel/linux-docs
	sys-kernel/linux-firmware
	sys-libs/gpm
	sys-libs/libsmbios
#	sys-power/acpid
#	sys-power/apcupsd
	sys-power/cpupower
#	sys-power/pm-quirks
#	sys-power/pm-utils
	sys-power/powertop
#	sys-process/acct
	sys-process/at
	sys-process/atop
	sys-process/audit
	sys-process/cronie
	sys-process/ftop
	sys-process/htop
	sys-process/lsof
	sys-process/memwatch
	sys-process/nmon
	sys-process/iotop
	sys-process/procps
	sys-process/psmisc
	#virtual/opengl
	virtual/pkgconfig
#	www-apache/
#	www-apps/
	www-client/firefox
	www-client/links
	www-client/w3m
#	www-misc/
#	www-plugins/
	www-servers/apache
	www-servers/fnord
#	www-servers/lighttpd
	www-servers/nginx
#	www-servers/tomcat
	x11-apps/appres
	x11-apps/bitmap
	x11-apps/editres
	x11-apps/mesa-progs
	x11-apps/xauth
	x11-apps/xbacklight
	x11-apps/xcalc
	x11-apps/xclipboard
	x11-apps/xclock
	x11-apps/xcmsdb
	x11-apps/xclock
	x11-apps/xconsole
	x11-apps/xcursorgen
	x11-apps/xdm
	x11-apps/xdriinfo
	x11-apps/xev
	x11-apps/xf86dga
	x11-apps/xfd
	x11-apps/xfontsel
	x11-apps/xgamma
	x11-apps/xhost
	x11-apps/xinit
	x11-apps/xinput
	x11-apps/xkbcomp
#	x11-apps/xkbevd
	x11-apps/xkbprint
	x11-apps/xkbutils
	x11-apps/xkill
	x11-apps/xload
	x11-apps/xlogo
	x11-apps/xman
	x11-apps/xmessage
	x11-apps/xmodmap
	x11-apps/xmore
	x11-apps/xrandr
	x11-apps/xrdb
	x11-apps/xset
	x11-apps/xsetroot
#	x11-apps/xsm
#	x11-apps/xstdcmap
#	x11-apps/xtrap
#	x11-apps/xvfb-run
#	x11-apps/xvidtune
	x11-apps/xvinfo
	x11-apps/xwd
	x11-apps/xwininfo
#	x11-apps/xwud
	x11-base/xorg-drivers
	x11-base/xorg-server
	x11-base/xorg-x11
#	x11-drivers/
	x11-drivers/xf86-input-synaptics
	# remove at-spi-atk dependency to avoid pulling in dbus
	x11-libs/gtk+
	x11-misc/xautolock
	x11-misc/xlockmore
	x11-misc/i3status
#	x11-plugins/
#	x11-proto/
	x11-terms/xterm
	x11-wm/i3
#	xfce-base/
#	xfce-extra/
