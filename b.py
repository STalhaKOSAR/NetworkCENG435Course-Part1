#!/usr/bin/env python

import socket


TCP_PORT = 12001

UDP_IP = "10.10.2.2" #r1
UDP_IP2 = "10.10.4.2" #r2

UDP_PORT1 = 12002
UDP_PORT2 = 12003 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_DGRAM) 
s.bind(('', TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
for i in range(0,10):
    data = conn.recv(18)
    print "received data:", data 
    sock.sendto(data, (UDP_IP, UDP_PORT1))
    sock.sendto(data, (UDP_IP2, UDP_PORT2))
conn.close()


