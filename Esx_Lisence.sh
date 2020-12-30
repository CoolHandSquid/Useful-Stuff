#!/bin/sh
#Script to renew evaluation license for ESXI
#
###install###
#Place this script in /opt/Esx_Lisence.sh
#chmod +x
#
###add cron job###
#vi /var/spool/cron/crontabs/root
#5 0 * * 6 /opt/Esx_Lisence.sh
#


rm -r /etc/vmware/license.cfg
cp /etc/vmware/.#license.cfg /etc/vmware/license.cfg
/etc/init.d/vpxa restart
