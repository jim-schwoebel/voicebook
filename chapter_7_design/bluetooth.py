'''
bluetooth.py

Taken from tutorial:
http://blog.kevindoran.co/bluetooth-programming-with-python-3/

More info from repo:
https://github.com/karulis/pybluez
'''
import bluetooth
from bluetooth.ble import DiscoveryService

###############################################################
##                      MAIN SCRIPT                          ## 
###############################################################

# The MAC address of a Bluetooth adapter on the server.
# The server might have multiple Bluetooth adapters.
hostMACAddress = '00:1f:e1:dd:08:3d'
serverMACAddress = hostMACAddress
# 3 is an arbitrary choice. However, it must match the port used by the client.
port = 3
    
def get_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))
    for addr, name in nearby_devices:
        print("  %s - %s" % (addr, name))
    
    return nearby_devices 

def bluetooth_send(serverMACAddress, port, data):
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((serverMACAddress, port))
    s.send(data)
    sock.close()

def bluetooth_receive(hostMACAddress, port):
    # receive data 
    backlog = 1
    size = 1024
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((hostMACAddress, port))
    s.listen(backlog)
    try:
        client, clientInfo = s.accept()
        while 1:
            data = client.recv(size)
            if data:
                print(data)
                client.send(data) # Echo back to client
    except:	
        print("Closing socket")
        client.close()
        s.close()

###############################################################
#        CREATING CLIENT_SERVER APPLICATIONS                 ## 
###############################################################

### # For the Server
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.bind(("192.168.1.17",50001)) # The Bluetooth MAC Address and RFCOMM port is replaced with an IP Address and a TCP port.
##
### For the Client
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect(("192.168.1.17",50001))
##
### Note: these are arbitrary IP addresses and TCP ports.
