#Port scanner

 
import sys
import socket

#specify target
ip = '192.168.1.6'

#declare empty array
open_ports =[] 

#specify port range
ports = range(1, 65535)

'''
In this example we have all TCP ports using the range.
Could use common list to save time/reduce noise:
ports = {21, 22, 23, 53, 80, 135, 443, 445}
'''

#Tries to connect to port
def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result

#loop for the ports we have listed
for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    
#print out the results
if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")