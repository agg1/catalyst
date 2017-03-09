subarch: amd64
version_stamp: latest
target: livecd-stage2
rel_type: hardened
profile: hardened/linux/amd64/no-multilib
snapshot: latest
source_subpath: hardened/livecd-stage1-amd64-latest.tar.bz2
portage_confdir: /home/autobuild/etc/portage/
portage_overlay: /usr/local/portage

livecd/volid: Hardened Admin Live System
livecd/type: generic-livecd
livecd/iso: amd64-latest.iso
livecd/fstype: squashfs
livecd/gk_mainargs: --mdadm --makeopts=-j16 --config=/etc/portage/genkernel.conf --no-oldconfig
livecd/cdtar: /home/autobuild/etc/portage/catalyst/livecd/cdtar/isolinux-3.86-cdtar.tar.bz2
livecd/bootargs: dokeymap nodhcp nosound memory_corruption_check=1 pbsleep console=ttyS0,115200 console=tty0
livecd/rcdel: keymaps|boot netmount|default
livecd/rcadd: cronie|default rsyslog|default
#sshd|default sshguard|default
livecd/root_overlay: /home/autobuild/rootfs
#livecd/xdm:

boot/kernel: linux
boot/kernel/linux/sources: ck-sources
boot/kernel/linux/config: /home/autobuild/etc/portage/kconfig

boot/kernel/linux/use:
	-awt -bindist -branding -debug -consolekit -dbus -kdbus -policykit -pam -systemd -pulseaudio -udisks -upower -upnp -upnp-av -avahi -gvfs -gtk3 -qt4 -qt5 -gnome-keyring -libnotify -gnome -kde -java -ruby -python -test hardened urandom ipv6 crypt sasl ssl openssl libressl curl_ssl_libressl -gnutls -nettle socks5 system-mitkrb5 usb threads nptl nls unicode bzip2 lzo lzma xz zlib xml static-libs
	-udev
	-X
	-doc
	-gtk
	-ntfsdecrypt
	ntfsprogs

#boot/kernel/linux/packages:
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
	/var/tmp/genkernel
	/usr/src/linux

#livecd/empty:

livecd/fsscript: /home/autobuild/finalize_target.sh

