import paramiko
import cmd
import pychart 
import csv
from datetime import datetime
import time



for i in range(0,70):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('10.1.20.55', username='root', 
        password='123456')
    stdin, stdout, stderr = ssh.exec_command("netstat -lanpe --protocol=inet | grep TIME_WAIT | wc -l")
    output = stdout.read() 
    print str(i) + " " +str(int(output))
    with open('eggs.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([i] + [int(output)])
    stdin.close()
    ssh.close()
    time.sleep(60)
