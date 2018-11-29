#!/usr/bin/env python

import socket


TCP_PORT = 12001

UDP_IP = "127.0.0.1"
UDP_IP2 = "127.0.0.1"

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
    data = conn.recv(17)
    print "received data:", data 
    sock.sendto(data, (UDP_IP, UDP_PORT1))
    sock.sendto(data, (UDP_IP2, UDP_PORT2))
conn.close()


