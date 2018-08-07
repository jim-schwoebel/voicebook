'''
generate_password.py

Generate a strong password from a list of dictionary elements.

Inspired from post here:
http://code.activestate.com/recipes/578169-extremely-strong-password-generator/
'''
from os import urandom
import random 

def generate_password(length):
    char_set = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
    password=''
    for i in range(length):
        password=password+random.choice(char_set)
    password=password.encode('utf-8')
    return password 

# how to implement - just specify length you need 
# print(generate_password(24))
