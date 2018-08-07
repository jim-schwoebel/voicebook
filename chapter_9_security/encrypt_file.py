'''
encrypt_file.py

Take in a file and encrypt it.

From following this pycrypto tutorial:
https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
'''
import hashlib, pickle
import os, random, struct
from Crypto.Cipher import AES
import generate_password as gp
from os import urandom

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = urandom(16)
    
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            
            while True:
                print('hi2')
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '.encode('utf-8') * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

    # make sure to output the key in pickle format 
    picklefile=open(in_filename[0:-4]+'_key.pickle', 'wb')
    pickle.dump(key, picklefile)
    picklefile.close()


password = gp.generate_password(24)
key = hashlib.sha256(password).digest()
print(key)
encrypt_file(key, 'piano2.wav', out_filename=None, chunksize=64*1024)
