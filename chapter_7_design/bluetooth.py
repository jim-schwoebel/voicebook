'''
================================================ 
##            VOICEBOOK REPOSITORY            ##      
================================================ 

repository name: voicebook 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/voicebook 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: a book and repo to get you started programming voice applications in Python - 10 chapters and 200+ scripts. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-09-28 

This code (voicebook) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
##               LICENSE TERMS                ##      
================================================ 

Copyright 2018 NeuroLex Laboratories, Inc. 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

================================================ 
##               SERVICE STATEMENT            ##        
================================================ 

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in Kafka distributed architectures, microservices 
built on top of Node.js / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
##                 BLUETOOTH.PY               ##    
================================================ 

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
