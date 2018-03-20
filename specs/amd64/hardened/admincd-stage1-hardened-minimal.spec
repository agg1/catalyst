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
	-awt -bindist -branding -debug -consolekit -dbus -kdbus -policykit -pam -systemd -oss -pulseaudio -udisks -upower -upnp -upnp-av -avahi -gvfs -gtk3 -qt4 -qt5 -gnome-keyring -libnotify -jit -orc -gnome -kde -java -ruby -python -test hardened urandom ipv6 crypt sasl ssl libressl curl_ssl_libressl -gnutls -nettle socks5 -system-mitkrb5 -system-heimdal usb threads nptl nls unicode bzip2 lzo lzma xz zlib readline static-libs
	-udev
	-accessibility
	-X
	-doc
	-gtk
	minimal

livecd/packages:
	net-dialup/picocom
	net-misc/dhcp
	net-misc/dhcpcd
	net-misc/iputils
#	sys-apps/busybox
#	sys-apps/coreutils
	sys-apps/dmidecode
	sys-apps/gptfdisk
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/lsb-release
#	sys-apps/net-tools
#	sys-apps/util-linux
	#sys-apps/clrngd
	sys-apps/rng-tools
	sys-devel/bc
	dev-libs/libressl
	sys-fs/e2fsprogs
	sys-fs/lvm2
