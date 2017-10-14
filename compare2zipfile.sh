export PATH=/bin
echo $PATH
ls $PATH
unzip -l $1 >/tmp/1.txt
unzip -l $2 >/tmp/2.txt
diff /tmp/1.txt /tmp/2.txt
read n1
