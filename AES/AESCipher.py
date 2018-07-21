import base64
import hashlib

from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-s[-1]]


class AESCipher:

    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

key = open("key.txt",'r')
cipher = AESCipher(key.read())
#a =  key.read()
#print(a)


choice = input("Press 'e' to Encrypt : \nPress 'd' to Decrypt : \n")
if choice == 'e' :
    filer = open("input.txt",'r')
    filew = open("cipher.txt",'w')
    inputtxt = filer.read()
    encrypted = cipher.encrypt(inputtxt)
    filew.write(str(encrypted))

elif choice == 'd' :
    filer = open("input.txt",'r')
    filew = open("plain.txt",'w')
    inputtxt = filer.read()
    encrypted = cipher.encrypt(inputtxt)
    decrypted = cipher.decrypt(encrypted)
    filew.write(str(decrypted))
