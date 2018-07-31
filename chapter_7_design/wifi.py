'''
wifi.py

Various wifi scripts that are useful
https://pypi.org/project/wireless/
https://github.com/joshvillbrandt/wireless
'''

from wireless import Wireless

# connect to wireless network 
wireless=Wireless()
ssid='I_am_cool'
password='password'
wireless.connect(ssid='ssid', password='password')

# various things you can get 
print(wireless.current())
print(wireless.interfaces())
print(wireless.interface())
print(wireless.power())
print(wireless.driver())
