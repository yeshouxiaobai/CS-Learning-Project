# MIT Missing Semester Demo 1

第一课是关于 Shell 的。这节课介绍了 Shell 的基本操作。

```bash
echo hello

# when there is a space
echo "Hello World"
echo 'Hello World'
echo Hello\ World

echo $PATH

which echo
whereis echo

# present working directory
pwd

cd /home

# four special directories
cd ..
cd .
cd -
cd ~

# show the files
ls
ls -l

# help or documents of softwares
ls --help
man ls

# about the informations
lrwxrwxrwx.  1 root root     7 Mar 16  2021 bin -> usr/bin
dr-xr-xr-x.  5 root root  4096 Mar 29  2021 boot
drwxr-xr-x  19 root root  3000 Dec 27 07:09 dev
drwxr-xr-x. 78 root root  4096 Dec 27 07:27 etc
drwxr-xr-x.  2 root root  4096 Dec 27 07:27 home
lrwxrwxrwx.  1 root root     7 Mar 16  2021 lib -> usr/lib
lrwxrwxrwx.  1 root root     9 Mar 16  2021 lib64 -> usr/lib64
drwx------.  2 root root 16384 Mar 16  2021 lost+found
drwxr-xr-x.  2 root root  4096 Apr 11  2018 media
drwxr-xr-x.  2 root root  4096 Apr 11  2018 mnt
drwxr-xr-x.  3 root root  4096 Mar 29  2021 opt
dr-xr-xr-x  83 root root     0 Dec 27 07:09 proc
dr-xr-x---.  3 root root  4096 Dec 27 07:25 root
drwxr-xr-x  23 root root   640 Dec 27 07:26 run
lrwxrwxrwx.  1 root root     8 Mar 16  2021 sbin -> usr/sbin
drwxr-xr-x.  2 root root  4096 Apr 11  2018 srv
dr-xr-xr-x  13 root root     0 Dec 27 07:09 sys
drwxrwxrwt.  9 root root  4096 Dec 28 03:41 tmp
drwxr-xr-x. 13 root root  4096 Mar 16  2021 usr
drwxr-xr-x. 19 root root  4096 Mar 16  2021 var

# rename and copy
mv [FILE] [FILE]
cp [FILE] [FILE]

# redirect
echo hello > hello.txt
echo hello >> hello.txt
cat < hello.txt > hello2.txt
ls -l / | tail -n1 > ls.txt
curl --head --silent google.com | grep -i content-length
curl --head --silent google.com | grep -i content-length | cut --delimiter=' ' -f2

# an important directory
cd /sys
ls
cd ./class/backlight/intel_backliight
ls
cat brightness
# this will not work
sudo echo 500 > brightness
# this will work
sudo su
echo 500 > brightness
exit
# or in this way
echo 1060 | sudo tee brightness
```

