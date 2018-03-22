subarch: amd64
version_stamp: latest
target: livecd-stage2
rel_type: hardened
profile: hardened/linux/amd64/no-multilib
snapshot: latest
source_subpath: hardened/livecd-stage1-amd64-latest.tar.bz2
portage_confdir: /home/autobuild/etc/portage/
portage_overlay: /usr/local/portage

livecd/volid: Hardened Desktop Live System
livecd/type: generic-livecd
livecd/iso: amd64-latest.iso
livecd/fstype: none
livecd/gk_mainargs: --config=/etc/portage/genkernel.conf
livecd/cdtar: /home/autobuild/etc/portage/catalyst/livecd/cdtar/isolinux-3.86-cdtar.tar.bz2
livecd/bootargs: net.ifnames=0 dokeymap nodhcp memory_corruption_check=1
livecd/rcdel: keymaps|boot netmount|default
livecd/rcadd: cronie|default rsyslog|default
# sshd|default sshguard|default
livecd/root_overlay: /home/autobuild/rootfs/default
livecd/overlay: /home/autobuild/rootfs/desktop
#livecd/xdm:

boot/kernel: linux
boot/kernel/linux/sources: ck-sources
boot/kernel/linux/config: /home/autobuild/etc/portage/kconfig

boot/kernel/linux/use:
	minimal
	-doc
	-bindist -branding -debug -test -pam -systemd -consolekit -policykit -dbus -kdbus -oss -pulseaudio hardened urandom ipv6 crypt sasl ssl libressl curl_ssl_libressl -gnutls -nettle threads nptl nls unicode bzip2 lzo lzma xz zlib readline fortran clang gmp openmp ghc smp static-libs
	-udev -udisks -upower -upnp -upnp-av -avahi usb
	-system-mitkrb5 -system-heimdal -kerberos
	-java -ruby -python
	#-lua -php
	#-X -gtk -qt4 -qt5
	-gvfs -gconf -gtk3 -gnome-keyring -gnome -kde -accessibility -wayland -introspection
	-libinput -libnotify
	-jit -orc
	#acl caps seccomp skey smartcard xattr
	#ldap nis radius

boot/kernel/linux/packages:
	app-admin/sudo
	#app-arch/alien
	#app-arch/rpm
	app-backup/amanda
	#app-backup/bacula
	#app-benchmarks/httperf
	#app-cdr/graveman
	#app-crypt/johntheripper
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
	#app-dicts/stardict*
	#app-editors/emacs
	#app-emacs/
	#app-emulation/fuse
	#app-emulation/fuse-utils
	#app-emulation/ganeti
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
	# patch required to drop dbus dependency
	#app-leechcraft/leechcraft-meta
	#app-misc/jail
	#app-misc/pax-utils
	#app-mobilephone/smssend
	app-office/dia2code
	#app-office/openerp
	#app-office/planner
	#app-office/gnumeric
	#app-office/skrooge
	#app-office/scribus
	#app-officeext/ooo2gd
	app-officeext/barcode
	app-officeext/dmaths
	app-officeext/sun-templates
	app-officeext/texmaths
	#app-pda/gtkpod
	#app-pda/ipodslave
	#app-xemacs/
	#dev-ada
	#dev-cpp
	dev-cpp/clucene
	dev-cpp/lucene++
	#dev-db/
	#dev-db/mysql
	#dev-db/sqlitestudio
	#dev-dotnet/
	#dev-embedded/
	#dev-erlang/
	#dev-games/
	#dev-go/
	#dev-haskell/
	#dev-java/
	dev-lang/php
	dev-lang/swig
	#dev-libs/
	#dev-lisp/
	#dev-lua/
	#dev-ml/
	#dev-perl/
	#dev/php/
	#dev-python/
	#dev-qt/
	#dev-ros/
	#dev-ruby/
	#dev-scheme/
	#dev-tcltk/
	#dev-tex/
	#dev-texlive/
	#dev-util/
	#dev-vcs/
	#games-action/
	#games-arcade/
	#games-board/
	#games-emulation/
	#games-engines/
	games-fps/darkplaces
	games-fps/freespace-scp
	games-fps/xonotic
	games-fps/yamagi-quake2
	games-simulation/flightgear
	games-simulation/lincity-ng
	games-strategy/widelands
	#games-kids/
	#games-misc/
	#games-mud/
	#games-puzzle/
	#games-roguelike/
	#games-rpg/
	#games-server/
	#games-simulation/
	#games-sports/
	games-strategy/0ad
	games-strategy/asc
	games-strategy/crimson
	games-strategy/warzone2100
	games-strategy/wesnoth
	games-strategy/widelands
	games-util/jstest-gtk
	#gnome-base/
	#gnome-extra/
	#gnustep-apps/
	#gnustep-base/
	#gnustep-libs/
	#java-virtuals/
	#kde-apps/
	#kde-base/
	#kde-frameworks/
	#kde-misc/
	#kde-plasma/
	#lxde-base/
	#lxqt-base/
	#mail-client/
	#mail-filter/
	#mail-mta/
	#mate-base/
	#mate-extra/
	#media-fonts/
	#media-libs/
	#media-plugins/
	#media-radio/
	#media-sound/grip
	media-sound/mumble
	#media-sound/rhythmbox
	#media-tv/
	#media-tv/w_scan
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
	net-analyzer/ftester
	net-analyzer/fwlogwatch
	#net-analyzer/httping
	#net-analyzer/hydra
	net-analyzer/ifstat
	#net-analyzer/ipgen
	net-analyzer/iplog
	net-analyzer/ipsumdump
	net-analyzer/isic
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
	#net-dialup/wvdial
	net-dns/pdnsd
	#net-firewall/fwbuilder
	#net-firewall/ipset
	#net-firewall/ipt_netflow
	#https://bugs.gentoo.org/show_bug.cgi?id=583608
	#net-firewall/nufw
	#net-firewall/xtables-addon
	#net-fs/
	#net-im/silc-server
	#net-im/skype
	#net-misc/connman
	#net-misc/socat
	#net-nds/lat
	#conflict with nfs-utils
	#net-nds/portmap
	#net-nds/ypbind
	#broken
	#net-nds/yp-tools
	#net-news/
	#net-nntp/
	#net-p2p/
	#net-print/
	#broken
	#net-proxy/ziproxy
	#net-voip/blink
	#net-voip/ekiga
	#net-wireless/airpwn
	#net-wireless/hostap-utils
	#net-wireless/hostapd
	#net-wireless/kismet
	#net-wireless/kismet-ubertooth
	#net-wireless/lorcon
	net-wireless/mfoc
	net-wireless/rfkill
	#perl-core/
	#ros-meta/
	#sci-astronomy/
	#sci-biology/
	sci-calculators/pcalc
	sci-calculators/units
	sci-calculators/wcalc
	#sci-chemistry/
	#sci-electronics/
	#sci-geosciences/
	#sci-libs/
	#sci-mathematics/
	#sci-misc/
	#sci-physics/
	#sci-visualization/
	#sci-calculators/calcoo
	#sci-calculators/calculator
	#sci-calculators/tiemu
	sci-calculators/tilp2
	#sec-policy/
	#sys-apps/
	#sys-auth/skey
	#sys-block/
	#sys-boot/
	#sys-cluster/
	#sys-devel/
	#sys-fabric/
	#sys-firmware/
	#sys-freebsd/
	#sys-fs/
	#sys-kernel/
	#sys-libs/
	#sys-power/
	#sys-process/
	sys-process/memwatch
	sys-process/nmon
	#www-apache/
	#www-apps/
	#www-client/
	#www-misc/
	#www-plugins/
	#www-servers/
	www-servers/apache
	#x11-apps/
	#x11-base/
	#x11-drivers/
	#x11-libs/
	#x11-misc/
	#x11-plugins/
	#x11-proto/
	#x11-terms/
	#x11-themes/

#livecd/unmerge:
#	sys-libs/pam
#	sys-auth/pambase

livecd/rm:
	#/lib/firmware/*
	/boot/System*
	/boot/initr*
	/boot/kernel*
	/etc/make.conf*
	/etc/make.globals
	/etc/make.profile
	/var/tmp/gentoo.config
	/var/tmp/genkernel/initramfs*
	/usr/src/linux

#livecd/empty:

livecd/fsscript: /home/autobuild/finalize_target.sh
