#
# Regular cron jobs for the zbackup package
#
0 4	* * *	root	[ -x /usr/bin/zbackup_maintenance ] && /usr/bin/zbackup_maintenance
