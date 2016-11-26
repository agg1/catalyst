subarch: amd64
version_stamp: latest
target: livecd-stage1
rel_type: hardened
profile: hardened/linux/amd64/no-multilib
snapshot: latest
source_subpath: hardened/stage3-amd64-latest.tar.bz2
portage_confdir: /home/catalyst/etc/portage/
portage_overlay: /usr/local/portage

livecd/use:
	-awt -bindist -branding -debug -consolekit -dbus -kdbus -policykit -pam -systemd -pulseaudio -udisks -upower -upnp -upnp-av -avahi -gvfs -gtk3 -qt4 -qt5 -gnome-keyring -libnotify -gnome -kde -ruby -test hardened urandom ipv6 sasl ssl openssl libressl curl_ssl_libressl -gnutls -nettle socks5 system-mitkrb5 usb threads nptl nls unicode bzip2 lzo lzma xz zlib readline xml static-libs
	-udev
	-X
	-doc
	-gtk
	-ntfsdecrypt
	ntfsprogs

livecd/packages:
	app-admin/checksec
	app-admin/eselect
	app-admin/genromfs
	app-admin/grubconfig
	app-admin/hddtemp
	app-admin/ide-smart
	app-admin/passook
	app-admin/perl-cleaner
	app-admin/python-updater
	app-admin/syslog-ng
	app-admin/testdisk
	app-benchmarks/bonnie++
	app-benchmarks/stress-ng
	app-arch/bzip2
	app-arch/cpio
	app-arch/gzip
	app-arch/mt-st
	app-arch/p7zip
	app-arch/pbzip2
	app-arch/rar
	app-arch/tar
	app-arch/unrar
	app-arch/unzip
	app-cdr/cdrdao
	app-cdr/cdrtools
	app-cdr/dvd+rw-tools
	app-crypt/bcwipe
	app-crypt/gnupg
	app-crypt/hashalot
	app-crypt/md5deep
	app-crypt/pinentry
	app-crypt/signify
	app-editors/nano
	app-editors/vim
	app-misc/ca-certificates
	app-misc/pax-utils
	app-misc/tmux
	app-misc/zisofs-tools
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
	app-portage/repoman
	app-portage/ufed
	app-shells/bash-completion
	app-shells/gentoo-bashcomp
	app-text/tree
	app-text/dos2unix
	app-text/wgetpaste
	app-vim/gentoo-syntax
	dev-lang/perl
	dev-lang/python
	dev-libs/libressl
	dev-python/pycrypto
	dev-util/catalyst
	dev-util/pkgconfig
	dev-util/shc
	dev-vcs/git
	mail-client/mailx
	mail-mta/msmtp
	net-analyzer/gnu-netcat
	net-analyzer/macchanger
	net-analyzer/netcat6
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-analyzer/traceroute-nanog
	net-analyzer/tcpdump
	net-dialup/mingetty
	net-dialup/minicom
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-dns/bind-tools
	net-firewall/iptables
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-ftp/ncftp
	net-misc/bridge-utils
	net-misc/curl
	net-misc/dhcp
	net-misc/iputils
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-misc/telnet-bsd
	net-misc/vconfig
	net-misc/wol
	net-misc/wget
	net-misc/whois
	net-wireless/b43-fwcutter
#	net-wireless/iw
#	net-wireless/rfkill
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
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
	sys-apps/ethtool
	sys-apps/file
	sys-apps/findutils
#	sys-apps/flashrom
#	sys-apps/fxload
	sys-apps/gawk
	sys-apps/gptfdisk
	sys-apps/grep
	sys-apps/groff
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/less
	sys-apps/lsb-release
	sys-apps/lshw
	sys-apps/man-db
	sys-apps/man-pages
	sys-apps/man-pages-posix
	sys-apps/memtester
	sys-apps/miscfiles
	sys-apps/pciutils
	sys-apps/pcmciautils
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
	sys-apps/which
	sys-boot/syslinux
	sys-block/mpt-status
	sys-block/mtx
	sys-block/open-iscsi
	sys-block/parted
	sys-block/tw_cli
	sys-boot/grub
	sys-boot/syslinux
	sys-devel/autoconf
	sys-devel/autoconf-wrapper
	sys-devel/automake
	sys-devel/automake-wrapper
	sys-devel/bc
	sys-devel/binutils-config
	sys-devel/bison
	sys-devel/flex
	sys-devel/gcc
	sys-devel/gcc-config
	sys-devel/gettext
	sys-devel/gnuconfig
	sys-devel/libtool
	sys-devel/m4
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
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/sshfs
	sys-fs/squashfs-tools
	sys-fs/sysfsutils
	sys-fs/xfsprogs
	sys-kernel/genkernel
	sys-kernel/linux-headers
	sys-libs/gpm
	sys-libs/libkudzu
	sys-libs/libsmbios
	sys-power/acpid
	sys-process/lsof
	sys-process/procps
	sys-process/psmisc
	virtual/pkgconfig
	www-client/links
