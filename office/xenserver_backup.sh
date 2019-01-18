#本程序是用来自动备份xen虚拟机
#使用方法 本脚本.sh 虚机名称 备份的路径
#例如 backvm.sh vm1 /tmp
#结束后就会在/tmp目录下生成vm1+日期时间.xva的备份文件

vm=$1
#虚机名是第一个参数

saved_location=$2
#保存位置是第二个参数

date0=`date +'%Y%m%d%H%M'`
#日期加时间

snapshot_uuid=`xe vm-snapshot vm=$1 new-name-label=${vm}_${date0}`
#快照uuid是自动生成的

xe template-param-set is-a-template=false ha-always-run=false uuid=${snapshot_uuid}
#转化快照为虚机

xe vm-export vm=${snapshot_uuid} filename=${saved_location}/${vm}${date0}.xva
#导出虚机

xe snapshot-destroy snapshot-uuid=${snapshot_uuid}
#删除快照，节省空间
