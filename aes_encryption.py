from Crypto.Cipher import AES
import binascii

#Encryption method
filer = open("input.txt","r")
filew = open("output.txt","w")
key = "qwertyu iopl kjh"
plaintxt = filer.read()
cipher = AES.new(key)
ciphertxt = cipher.encrypt(plaintxt)
encryptxt = str(binascii.hexlify(ciphertxt),'ascii')
filew.write(encryptxt)

decryptxt = cipher.decrypt(ciphertxt)
print (decryptxt)


