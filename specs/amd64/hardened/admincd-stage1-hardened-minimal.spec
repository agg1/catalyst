subarch: amd64
version_stamp: latest
target: livecd-stage1
rel_type: hardened
profile: hardened/linux/amd64/no-multilib
snapshot: latest
source_subpath: hardened/stage3-amd64-latest.tar.bz2
portage_confdir: /home/catalyst/etc/portage/
portage_overlay: /home/catalyst/extra_overlay/

livecd/use:
	-avahi
	-consolekit
	-doc
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
	-X
	-udev
	minimal
	bzip2
	cryptsetup
	hardened
	ipv6
	livecd
	loop-aes
	extra-ciphers
	keyscrub
	lvm1
	modules
	ncurses
	nls
	nptl
	nptlonly
	readline
	ssl
	unicode
	urandom
	usb
	static-libs
	mmx
	sse
	sse2

livecd/packages:
	net-misc/dhcp
	net-misc/iputils
	sys-apps/gptfdisk
	sys-apps/iproute2
	sys-apps/lsb-release
	sys-devel/bc
	sys-fs/lvm2
