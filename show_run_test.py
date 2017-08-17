import getpass
import sys
import telnetlib

HOST = "192.168.122.114"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("terminal length 0\n")
tn.write("show running-config\n")
tn.write("exit\n")

print tn.read_all()
