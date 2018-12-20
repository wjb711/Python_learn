#本程序是在linux下监控文件夹，通过观察文件夹的修改时间，如果有变化，触发邮件通知
#使用的格式 sh 本程序.sh 监控文件夹 监控时间（秒）触发的邮箱地址
d0=`stat -c %z $1`
time0=`date +%s -d "${d0:0:19}"`
time1=`date +%s`
#time_delta=`expr $time0 - $time1 `
time_delta=` expr $time1 - $time0 `
echo $time0,$time1,$time_delta
#a=$time_delta
#echo $a
if [[ $time_delta -lt $2 ]];
then
echo 'g'
content=`ls -alF $1`
/usr/local/bin/sendEmail -f $3 -t $3 -u $1 -m "$content" -s 10.4.172.3 -o message-charset=UTF-8
else
echo 'no',$time_delta
fi
