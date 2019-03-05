echo 欢迎使用本监控程序， 可以监控cpu，内存，硬盘等
echo 优点是占用内存小，实时监控，有输出，能告警
echo 有问题，找xxx
echo 注意参数设置
echo 格式为python.exe monitor.py 间隔时间（秒） 阈值百分比 告警保存位置文件夹
echo 例如python monitor.py 60 95 \\10.102.10.13\tools\100.tmp\123\logs
cd /d %~dp0
python.exe monitor.py 60 95 \\10.102.10.13\tools\100.tmp\123\logs
