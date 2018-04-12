#!/bin/sh -e
# Copyright aggi 2016,2017,2018

export LATEST=$1
[ -z "${LATEST}" ] && echo "LATEST not set" && exit 1

#export NOCLEAN="true"
if [ -f /tmp/.relda ]; then
	export RELDA=$(cat /tmp/.relda)
else
	:> /home/autolog/build.log
fi

source /home/autobuild/autobuild.sh
prepare_system

# minimal
export PKDIR="/home/packages/minimal/${LATEST}"
clean_stage
update_livecd_stage1 minimal
update_livecd_stage2 minimal
archive_kerncache

# admin
export CKERN=true
export PKDIR="/home/packages/admin/${LATEST}"
clean_stage
compile_csripts default
update_livecd_stage1 admin
update_livecd_stage2 admin

# desktop
export CKERN=true
export PKDIR="/home/packages/desktop/${LATEST}"
clean_stage
compile_csripts default
update_livecd_stage1 desktop
# keep portage tree for package updates on desktop ISO
cp ${TMPDR}/catalyst/snapshots/* ${CADIR}/tmp/buildoverlay
update_livecd_stage2 desktop

# full
export CKERN=true
export PKDIR="/home/packages/full/${LATEST}"
clean_stage
compile_csripts default
update_livecd_stage1 full
# keep portage tree for package updates on desktop ISO
cp ${TMPDR}/catalyst/snapshots/* ${CADIR}/tmp/buildoverlay
update_livecd_stage2 full

sign_release
