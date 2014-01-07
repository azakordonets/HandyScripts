#!/usr/bin/env python
import subprocess
import optparse
import re

#Iterates over list, running statements for each item in the list
#Note, that whitespace is absolutely critical and that a consistent indent must be maintained for the code to work properly
cmd = "python -V"
def checkPythonVersion(cmd):
    p = subprocess.Popen(cmd, shell = True,
    	stdout=subprocess.PIPE,
	    stderr=subprocess.STDOUT)
    out = p.stdout.read().strip()
    return out  #This is the stdout from the shell command
mkdir = "mkdir tmp"
cd_tmp = "cd tmp"
wget = "wget http://python.org/ftp/python/2.7.2/Python-2.7.2.tgz"
tar = "xvfz Python-2.7.2.tgz"
cd_python = "Python-2.7.2"
configure = "./configure --prefix=/opt/python2.7 --enable-shared"
make = "make"
make_alt_install = "make altinstall"
echo = "echo "/opt/python2.7/lib" >> /etc/ld.so.conf.d/opt-python2.7.conf"
ldconfig = "ldconfig"
cd = "cd .."
remove = "rm -rf tmp"
cmds = [mkdir,cd_tmp,wget,tar,cd_python,configure,make, make_alt_install,
echo,ldconfig,cd,cd,remove]

if checkPythonVersion(cmd) != "Python 2.7.2":
	for cmd in cmds:
	install = subprocess.check_call(cmd, shell=True)


