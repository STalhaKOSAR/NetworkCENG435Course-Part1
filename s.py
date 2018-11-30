import socket
import time
import ntplib

TCP_IP = "10.10.1.2"
TCP_PORT = 12001

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))  
c = ntplib.NTPClient()                  
for i in range (0,10):
    for y in range (0,10):
        response = c.request('time.google.com')
        timer = response.tx_time
        MESSAGE = repr(timer)
        sock.send(MESSAGE)
    time.sleep(1)

sock.close()