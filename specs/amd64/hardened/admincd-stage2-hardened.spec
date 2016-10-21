subarch: amd64
version_stamp: latest
target: livecd-stage2
rel_type: hardened
profile: hardened/linux/amd64/no-multilib
snapshot: latest
source_subpath: hardened/livecd-stage1-amd64-latest.tar.bz2
portage_confdir: /home/catalyst/etc/portage-desktop
cflags: -O3 -pipe -march=nehalem -mtune=nehalem
cxxflags: -O3 -pipe -march=nehalem -mtune=nehalem

livecd/volid: Linux Hardened Live System
livecd/type: generic-livecd
livecd/iso: admincd-amd64-latest.iso
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --mdadm --makeopts=-j16 --config=/etc/portage/genkernel.conf --no-oldconfig
livecd/cdtar: /usr/share/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/bootargs: dokeymap docache memory_corruption_check=1 modprobe.blacklist=asix,mcs7830
# ubsan_handle=OEAINVBSLF
# ubsan_handle=ELNVBSLF
livecd/rcdel: keymaps|boot netmount|default
#dhcpcd
#livecd/rcadd:
livecd/root_overlay: /home/catalyst/rootfs
#livecd/xdm:

boot/kernel: gentoo

boot/kernel/gentoo/sources: vanilla-sources
boot/kernel/gentoo/config: /home/catalyst/etc/portage/kconfig
#-udev
boot/kernel/gentoo/use:
	-*
	-avahi
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
	-gtk3
	-jit
	-orc
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
	fbcon
	hardened
	ipv6
	livecd
	loop-aes
	extra-ciphers
	jpg
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
	readline
	socks5
	ssl
	truetype
	unicode
	urandom
	usb
	doc
	latex
	static-libs

#boot/kernel/gentoo/packages:
#	sys-kernel/linux-firmware
#	sys-block/iscsitarget

#livecd/unmerge:
#	sys-libs/pam
#	sys-auth/pambase

livecd/rm:
	/lib/firmware
	/boot/System*
	/boot/initr*
	/boot/kernel*
	/etc/make.conf*
	/etc/make.globals
	/etc/make.profile
	/var/tmp/gentoo.config
	/var/tmp/genkernel/initramfs*
#	/etc/*-
#	/etc/*.old
#	/etc/default/audioctl
#	/etc/dispatch-conf.conf
#	/etc/env.d/05binutils
#	/etc/env.d/05gcc
#	/etc/etc-update.conf
#	/etc/hosts.bck
#	/etc/issue*
#	/etc/genkernel.conf
#	/etc/man.conf
#	/etc/resolv.conf
#	/lib*/*.a
#	/lib*/*.la
#	/lib*/cpp
#	/root/.bash_history
#	/root/.viminfo
#	/sbin/*.static
#	/sbin/fsck.cramfs
#	/sbin/fsck.minix
#	/sbin/mkfs.bfs
#	/sbin/mkfs.cramfs
#	/sbin/mkfs.minix
#	/usr/bin/addr2line
#	/usr/bin/ar
#	/usr/bin/as
#	/usr/bin/audioctl
#	/usr/bin/c++*
#	/usr/bin/cc
#	/usr/bin/cjpeg
#	/usr/bin/cpp
#	/usr/bin/djpeg
#	/usr/bin/ebuild
#	/usr/bin/emerge
#	/usr/bin/elftoaout
#	/usr/bin/f77
#	/usr/bin/g++*
#	/usr/bin/g77
#	/usr/bin/gcc*
#	/usr/bin/genkernel
#	/usr/bin/gprof
#	/usr/bin/i?86-gentoo-linux-uclibc-*
#	/usr/bin/i?86-pc-linux-*
#	/usr/bin/jpegtran
#	/usr/bin/ld
#	/usr/bin/libpng*
#	/usr/bin/nm
#	/usr/bin/objcopy
#	/usr/bin/objdump
#	/usr/bin/piggyback*
#	/usr/bin/portageq
#	/usr/bin/ranlib
#	/usr/bin/readelf
#	/usr/bin/repoman
#	/usr/bin/size
#	/usr/bin/strip
#	/usr/bin/tbz2tool
#	/usr/bin/xpak
#	/usr/bin/yacc
#	/usr/lib*/*.a
#	/usr/lib*/*.la
#	/usr/lib*/perl5/site_perl
#	/usr/lib*/gcc-lib/*/*/libgcj*
#	/usr/sbin/archive-conf
#	/usr/sbin/dispatch-conf
#	/usr/sbin/emaint
#	/usr/sbin/emerge-webrsync
#	/usr/sbin/env-update
#	/usr/sbin/fb*
#	/usr/sbin/fixpackages
#	/usr/sbin/quickpkg
#	/usr/sbin/regenworld
#	/usr/share/consolefonts/1*
#	/usr/share/consolefonts/7*
#	/usr/share/consolefonts/8*
#	/usr/share/consolefonts/9*
#	/usr/share/consolefonts/A*
#	/usr/share/consolefonts/C*
#	/usr/share/consolefonts/E*
#	/usr/share/consolefonts/G*
#	/usr/share/consolefonts/L*
#	/usr/share/consolefonts/M*
#	/usr/share/consolefonts/R*
#	/usr/share/consolefonts/a*
#	/usr/share/consolefonts/c*
#	/usr/share/consolefonts/dr*
#	/usr/share/consolefonts/g*
#	/usr/share/consolefonts/i*
#	/usr/share/consolefonts/k*
#	/usr/share/consolefonts/l*
#	/usr/share/consolefonts/r*
#	/usr/share/consolefonts/s*
#	/usr/share/consolefonts/t*
#	/usr/share/consolefonts/v*
#	/usr/share/misc/*.old

#livecd/empty:
#	/etc/cron.daily
#	/etc/cron.hourly
#	/etc/cron.monthly
#	/etc/cron.weekly
#	/etc/logrotate.d
#	/etc/modules.autoload.d
#	/etc/runlevels/single
#	/etc/skel
#	/lib/dev-state
#	/lib/udev-state
#	/lib64/dev-state
#	/lib64/udev-state
#	/root/.ccache
#	/tmp
#	/usr/diet/include
#	/usr/diet/man
#	/usr/i?86-gentoo-linux-uclibc
#	/usr/i?86-pc-linux-uclibc
#	/usr/lib/X11/config
#	/usr/lib/X11/doc
#	/usr/lib/X11/etc
#	/usr/lib/awk
#	/usr/lib/ccache
#	/usr/lib/gcc-config
#	/usr/lib/gconv
#	/usr/lib/nfs
#	/usr/lib/perl5/site_perl
#	/usr/lib/portage
#	/usr/lib64/X11/config
#	/usr/lib64/X11/doc
#	/usr/lib64/X11/etc
#	/usr/lib64/awk
#	/usr/lib64/ccache
#	/usr/lib64/gcc-config
#	/usr/lib64/gconv
#	/usr/lib64/nfs
#	/usr/lib64/perl5/site_perl
#	/usr/lib64/portage
#	/usr/local
#	/usr/portage
#	/usr/share/aclocal
#	/usr/share/baselayout
#	/usr/share/binutils-data
#	/usr/share/consolefonts/partialfonts
#	/usr/share/consoletrans
#	/usr/share/dict
#	/usr/share/et
#	/usr/share/gcc-data
#	/usr/share/genkernel
#	/usr/share/gettext
#	/usr/share/glib-2.0
#	/usr/share/gnuconfig
#	/usr/share/gtk-doc
#	/usr/share/i18n
#	/usr/share/info
#	/usr/share/lcms
#	/usr/share/libtool
#	/usr/share/locale
#	/usr/share/man
#	/usr/share/rfc
#	/usr/share/ss
#	/usr/share/state
#	/usr/share/texinfo
#	/usr/share/unimaps
#	/usr/share/zoneinfo
#	/usr/src
#	/var/cache
#	/var/empty
#	/var/lib/portage
#	/var/log
#	/var/spool
#	/var/state
#	/var/tmp
