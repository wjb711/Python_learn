#!/bin/bash
export PATH=/bin
echo "start now, current location is "
echo "" >/tmp/log.log
pwd
echo "*********************************"
echo "zip file list is here "
echo "*********************************"
ls *.zip
for i in *.zip;
do
unzip -l $i |awk '{print $4}'|sed '1,3d'|sed '$d'|sed '$d' >>/tmp/log.log
done
echo "***********same file*********************"
sort /tmp/log.log|uniq -d
read -p "*****press any key to end********" n1
