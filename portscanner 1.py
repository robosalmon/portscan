import iptools
import validators
import socket
import sys

print("enter URL / IP to prefrom portscan")
x = input()

valip = iptools.ipv4.validate_ip(x)
valurl = validators.url(x)

if valurl is True:
    print ("Valid URL: ", x)
    #y= socket.gethostbyname(x)
    #print("IP of URL:", y)
    print("starting scan of url")
    
else:
        if valip is True:
            print("Valid IP: ", x)
            print("starting scan of ip")
        else:
            print("Invalid URL/ IP: ", x)
            sys.exit(0)

for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        r = s.connect_ex((x,port))
        if r ==0:
            print("Port {} is open".format(port))
        s.close()

   