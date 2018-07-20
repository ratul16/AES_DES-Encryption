from Crypto.Cipher import AES
import binascii

filer = open
key = "qwertyu iopl kjh"
cipher = AES.new(key)
plain = open("plaint.txt","w")
decryptxt = cipher.decrypt(ciphertxt)
demo = str(binascii.unhexlify(decryptxt))
plain.write(demo)
print (demo)