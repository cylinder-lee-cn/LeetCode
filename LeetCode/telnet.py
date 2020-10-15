from telnetlib import Telnet
from time import sleep

host = "10.1.0.241"
port = 23

# connect telnet host
tn = Telnet(host, port)
# input username
tn.read_until(b"login: ")
tn.write(b"ht\r\n")
# input password
tn.read_until(b"Password: ")
tn.write(b"!Q2w3e4r\r\n")

# waitting for the prompt
tn.read_until(b"#")
# input the command
tn.write(b"?\r\n")
# wait 1 second
sleep(1)
# output the command response
print(tn.read_very_eager().decode('ascii'))

tn.close()
