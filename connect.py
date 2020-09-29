#!/usr/bin/python3

print("content-type: text/html")
print("location: http://192.168.43.117/f.html")

print()

import cgi
import subprocess as sp

a = ["priyanka"]
b = ["redhatos"]

form = cgi.FieldStorage()
user = form.getvalue('user')
passwd = form.getvalue('pass')

if(user in a):
	if(passwd in b):
		final = sp.getoutput("cat /var/www/html/f.html")
	else:
		print("invalid password")
else:
	print("invalid username")
