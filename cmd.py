#!/usr/bin/python3

print("content-type: text/html\n")

print()
import cgi
import subprocess
import sys
from datetime import date
import webbrowser
form = cgi.FieldStorage()
cmd = form.getvalue("c")

if ('run' in cmd) or ('what'in cmd) or ('date'in cmd):
	res = subprocess.getoutput('date')
	print(res)

elif ('calender' in cmd) or ('cal' in cmd):
	res=subprocess.getoutput('cal')
	print(res)
elif ('ram' in cmd) or ('usage' in cmd):
	res=subprocess.getoutput('free -m')
	print(res)
elif ('hadoop' in cmd):
	res=subprocess.getoutput('hadoop')
	print(res)
elif ('present' in cmd) or ('where'in cmd):
	res=subprocess.getoutput('pwd')
	print(res)
elif ('dir' in cmd) or ('list'in cmd):
	res=subprocess.getoutput('ls')
	print(res)
elif ('docker' in cmd):
	res=subprocess.getoutput('docker')
	print(res)
elif('active' in cmd)or('process'in cmd):
	res=subprocess.getoutput('ps -x')
	print(res)
elif('reboot' in cmd):
	res=subprocess.getoutput('init 6')
	print(res)
elif('ip' in cmd):
	res=subprocess.getoutput('ifconfig')
	print(res)
elif('espeak-ng'in cmd):
	res=subprocess.getoutput(cmd)
elif ('stop' in cmd) and ('firewall'in cmd):
	res=subprocess.getoutput('systemctl stop firewalld')
	print('firewall stoped sucessfully')

elif ('start' in cmd) and ('firewall'in cmd):
	res=subprocess.getoutput('systemctl start firewalld')
	print('firewall stoped sucessfully')

else:
	res=subprocess.getoutput(cmd)
	print(res)
#choice = cmd
