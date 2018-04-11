#cd /home/autobuild ; git clean -df .
#git crypt unlock key.gcr; cd -
#cd /home/extra_overlay ; git clean -df .
#git crypt unlock key.gcr; cd -

0) create or update gpg signing key
	- autobuild-gentkey.sh
1) create directories and manually prepare catalyst if required with initial build
	- /home/seeds
	- /home/autolog
	- check make.conf settings match portage tree version (python etc), revert when done
	- emerge -vb catalyst from appropriate portage tree, mount --bind distfiles, unmount when done
	- emerge shc compiler
	- consider manually mounting TMP to /var/tmp
	- rm -f /tmp/.prepared /tmp/.relda
2) rm -f /tmp/.relda /tmp/.prepared ; ./autobuild-all.sh 2>&1 | tee -a /home/autolog/build.log
3) rm -f /tmp/.relda /tmp/.prepared ; ./autobuild-all_vm.sh 2>&1 | tee -a /home/autolog/build.log
4) rm -f /tmp/.relda /tmp/.prepared ; ./autobuild-update.sh LATEST-RELDA 2>&1 | tee -a /home/autolog/build.log
	- update build may break with a kernel update involved
	  in that case a build against an old init-stage3 with autobuild-all.sh instead may help
	  just place a symlink for RELDA on init stage
	- there is three variants to build a release
		a) autobuild-all.sh
			- adapt MAKEFLAGS -jN and load-average  for parallel jobs according to nCPU present
			- adapt SWITCH_CTARGET according to target compiler
		b) autobuild-all.sh beginning against previous init stage3 from a)
		c) autobuild-update.sh against previous stage1 of the individual flavor
			- this is known to break with kernel update involved
			  iptables and ip link not autoloading kernel modules any longer
			- a flawless minimal flavor stage is required for all virtual machine flavors
			- admin, desktop and full flavor must be considered likewise wether init stage3
			  or previous flavor stage1 can be utilized
