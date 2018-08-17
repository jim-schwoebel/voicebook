*This section documents all the scripts in the chapter_9_security folder.*

## decrypting files
decrypt_file.py
```python3
import os, random, struct, json, pickle
from Crypto.Cipher import AES

def decrypt_file(in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """

    # load public key from a pickle file 
    keyfile=in_filename[0:-8]+'_key.pickle'
    try:
        key=pickle.load(open(keyfile,'rb'))
    except:
        print('please put %s in current directory'%(keyfile))

    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

#decrypt_file('piano2.wav.enc')
```
## encrypting files 
encrypt_file.py
```python3
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


#password = gp.generate_password(24)
#key = hashlib.sha256(password).digest()
#print(key)
#encrypt_file(key, 'piano2.wav', out_filename=None, chunksize=64*1024)
```
## generating passwords
generate_password.py
```python3
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
```

## Resources
If you are interested to read more on any of these topics, check out the documentation below.

* [Pycryptodome](https://www.pycryptodome.org/en/latest/src/cipher/cipher.html)
