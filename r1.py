import socket
import time

UDP_IP = "10.10.3.2"
UDP_PORT = 12002
UDP_PORT2 = 12004

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_DGRAM) 
sock2 = socket.socket(socket.AF_INET, 
                        socket.SOCK_DGRAM) 
sock.bind(('', UDP_PORT))

for i in range(0,10):
    time.sleep(1)
    for y in range (0,10):
        data, addr = sock.recvfrom(18) 
        print "received message:", data
        sock2.sendto(data, (UDP_IP, UDP_PORT2))