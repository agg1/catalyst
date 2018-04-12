#!/bin/sh -e
# Copyright aggi 2016,2017,2018

export LATEST=$1
[ -z "${LATEST}" ] && echo "LATEST not set" && exit 1

if [ -f /tmp/.relda ]; then
	export RELDA=$(cat /tmp/.relda)
	export NOCLEAN="true"
else
	:> /home/autolog/build.log
fi

source /home/autobuild/autobuild.sh
prepare_system

export PKDIR="/home/packages/minimal/${LATEST}"
update_livecd_minimal

export CKERN=true
export PKDIR="/home/packages/admin/${LATEST}"
update_livecd_admin

export CKERN=true
export PKDIR="/home/packages/desktop/${LATEST}"
update_livecd_desktop

export CKERN=true
export PKDIR="/home/packages/full/${LATEST}"
update_livecd_full

sign_release
