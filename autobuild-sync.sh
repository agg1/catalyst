#!/bin/sh -e

# rsync distfiles
[ -e /home/distfiles/ -a -e /media/backup/distfiles/ ] && \
rsync -av /home/distfiles/ /media/backup/distfiles/
rsync -av /media/backup/distfiles/ /home/distfiles/

cd /home/seeds
git pull --rebase origin master
git push --tags origin master

for d in autobuild extra_overlay portage ; do
	cd /home/${d}
	git fsck
	git pull --rebase origin master
	git push --tags origin master
done

for d in autobuild extra_overlay portage ; do
	cd /home/${d}
	sg lanout -c "git push --tags www02 master || true" || true
done
for d in autobuild extra_overlay portage ; do
	cd /home/${d}
	sg wanout -c "git push --tags github master || true" || true
done
