import iptools
import validators
import socket
import sys
import os
file_path = r"C:\Users\robosalmon\Documents\progransb\outputs\portscanoutputs.txt"
print("enter URL / IP to prefrom portscan")
x = input()

valip = iptools.ipv4.validate_ip(x)
valurl = validators.url(x)
with open(file_path, 'w') as fp:
    if valurl is True:
        print ("Valid URL: ", x)
        fp.write(str("Valid URL: ")+"\n")
        fp.write(x+"\n")
        #y= socket.gethostbyname(x)
        #print("IP of URL:", y)
        print("starting scan of url")
        fp.write("starting scan of url"+"\n")

    else:
        if valip is True:
            print("Valid IP: ", x)
            print("starting scan of ip")
            fp.write("Valid IP: "+"\n")
            fp.write(x+"\n")
            fp.write("starting scan of ip"+"\n")

        else:
            print("Invalid URL/ IP: ", x)
            fp.write("Invalid URL/ IP: "+"\n")
            fp.write(x+"\n")
            sys.exit

    for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            r = s.connect_ex((x,port))
            if r ==0:
                print("Port {} is open".format(port))
                fp.write("Port {} is open".format(port))
            s.close()


        
        