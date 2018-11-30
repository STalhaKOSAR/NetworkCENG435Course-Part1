import socket
from thread import *
import threading
import ntplib
import time

print_lock = threading.Lock()

def thread(port):
    UDP_PORT1 = port

    sock = socket.socket(socket.AF_INET, 
                        socket.SOCK_DGRAM)
    sock.bind(('', UDP_PORT1))

    for i in range(0,10):
		time.sleep(1)
		for y in range(0,10):
			data, addr = sock.recvfrom(18)
			c = ntplib.NTPClient()
			response = c.request('time.google.com')
			timer = response.tx_time
			dataFloat = float(data)
			print "diff",timer-dataFloat

def Main(): 
    print_lock.acquire() 

    start_new_thread(thread,(12004,))
    start_new_thread(thread,(12005,))
    while True:
        pass
  
if __name__ == '__main__': 
    Main() 