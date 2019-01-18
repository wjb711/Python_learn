直接写为backvm.sh w7d0 NFS1  即可


#本程序是用来自动备份xen虚拟机
#使用方法 本脚本.sh 虚机名称 存储的名字
#例如 backvm.sh vm1 存储名称
#结束后就会在存储目录下生成vm1+日期时间.xva的备份文件

vm=$1
#虚机名是第一个参数

nfs_uuid=`xe sr-list name-label=$2|grep uuid |cut -d":" -f2`
#echo ${nfs_uuid}
saved_location='/var/run/sr-mount/'
echo ${saved_location}
saved_location=${saved_location}${nfs_uuid/ /''}
echo ${saved_location}
#保存nfs存储名称是第二个参数

date0=`date +'%Y%m%d%H%M'`
#日期加时间

snapshot_uuid=`xe vm-snapshot vm=$1 new-name-label=${vm}_${date0}`
#快照uuid是自动生成的

xe template-param-set is-a-template=false ha-always-run=false uuid=${snapshot_uu                                                                                                                     id}
#转化快照为虚机

xe vm-export vm=${snapshot_uuid} filename=${saved_location}/${vm}${date0}.xva
#导出虚机

xe snapshot-destroy snapshot-uuid=${snapshot_uuid}
#删除快照，节省空间
