subarch: amd64
version_stamp: latest
target: livecd-stage2
rel_type: hardened
profile: hardened/linux/amd64/no-multilib
snapshot: latest
source_subpath: hardened/livecd-stage1-amd64-latest.tar.bz2
portage_confdir: /home/catalyst/etc/portage/
portage_overlay: /home/catalyst/extra_overlay/

livecd/volid: Hardened Desktop Live System
livecd/type: generic-livecd
livecd/iso: amd64-latest.iso
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --mdadm --makeopts=-j24 --config=/etc/portage/genkernel.conf --no-oldconfig
livecd/cdtar: /usr/share/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/bootargs: dokeymap nodhcp memory_corruption_check=1
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
	crypt
	sound
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
	cryptsetup
	hardened
	ipv6
	livecd
	loop-aes
	extra-ciphers
	jpg
	keyscrub
	lvm1
	midi
	fluidsynth
	mng
	modules
	ncurses
	nls
	nptl
	nptlonly
	threads
	png
	readline
	socks5
	ssl
	truetype
	iconv
	unicode
	urandom
	usb
	doc
	latex
	static-libs
	python_targets_python2_7
	python_targets_python3_4
	mmx
	sse
	sse2
	cairo
	gtk
#	opencl
#	llvm
	gallium
	xvfb
	X
	-video_cards_qxl
	-video_cards_virtualbox
	-video_cards_vmware

#boot/kernel/gentoo/packages:
#	sys-kernel/linux-firmware
#	sys-block/iscsitarget

#livecd/unmerge:
#	sys-libs/pam
#	sys-auth/pambase

livecd/rm:
	/lib/firmware/*
	/boot/System*
	/boot/initr*
	/boot/kernel*
	/etc/make.conf*
	/etc/make.globals
	/etc/make.profile
	/var/tmp/gentoo.config
	/var/tmp/genkernel/initramfs*

#livecd/empty:
