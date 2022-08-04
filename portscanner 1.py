import iptools, validators, socket, sys, os, threading, time
from queue import Queue
print("enter URL / IP to prefrom portscan")
file_path = r"C:\Users\robosalmon\Documents\progransb\outputs\portscanoutputs.txt"

y = input()
valip = iptools.ipv4.validate_ip(y)
valurl = validators.url(y)
print_lock = threading.Lock()
q = Queue()


with open(file_path, 'w') as fp:
    if valurl is True:
        print ("Valid URL: ", y)
        fp.write(str("Valid URL: ")+"\n")
        fp.write(y+"\n")
        y= socket.gethostbyname(socket.gethostname(y))
        print("IP of URL:", y)
        print("starting scan of url")
        fp.write("starting scan of url"+"\n")

    else:
        if valip is True:
            print("Valid IP: ", y)
            print("starting scan of ip")
            fp.write("Valid IP: "+"\n")
            fp.write(y+"\n")
            fp.write("starting scan of ip"+"\n")

        else:
            print("Invalid URL/ IP: ", y)
            fp.write("Invalid URL/ IP: "+"\n")
            fp.write(y+"\n")
            sys.exit(0)



def scan(port): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((y, port))
        with print_lock:
            print("Port {} is open".format(port))
            fp.write("Port {} is open".format(port))
        con.close()
    except:
        pass
def threader():
    while True:
        worker = q.get()
        scan(worker)
        q.task_done()



for i in range(400):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 65535):
    q.put(worker)

q.join()




 #       for port in range(1,65535):
 #           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 #           socket.setdefaulttimeout(1)
 #           r = s.connect_ex((x,port))
 #           if r ==0:
 #              print("Port {} is open".format(port))
 #           fp.write("Port {} is open".format(port))
 #           s.close()
