'''
decrypt_file.py

decrypt a file with a key.

From following this pycrypto tutorial:
https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
'''
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

decrypt_file('piano2.wav.enc')