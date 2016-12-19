#!/bin/sh

DEST=$1
DPRT=$2
LPRT=$3
SPRT=$3
SUSR=$4

if [ -z "${DEST}" -o -z "${DPRT}" -o -z "${SPRT}" ] ; then
	echo "Usage: sshsrcport.sh <DEST> <DPRT> <SPRT> [SUSR]" ; exit 1
fi

#pass in log proto tcp from any port {SPRT} to port {DPRT}
echo "ncat -l ${LPRT} --sh-exec \"ncat ${DEST} ${DPRT} -p ${SPRT}\""
ncat -l ${LPRT} --sh-exec "ncat ${DEST} ${DPRT} -p ${SPRT}"

#if [ "x${SUSR}" != "x" ]; then
#	ssh ${SUSR}@127.0.0.1 -p ${LPRT}
#else
#	ssh 127.0.0.1 -p ${LPRT}
#fi

