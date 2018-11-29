import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 12002
UDP_PORT2 = 12004

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_DGRAM) 
sock2 = socket.socket(socket.AF_INET, 
                        socket.SOCK_DGRAM) 
sock.bind(('', UDP_PORT))

for i in range(0,10):
    data, addr = sock.recvfrom(17) 
    print "received message:", data
    sock2.sendto(data, (UDP_IP, UDP_PORT2))