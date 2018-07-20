from Crypto.Cipher import  DES
import binascii

key = "hello123"

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


des = DES.new(key, DES.MODE_ECB)
text = "Python is the best !"
paddedtxt = pad(text)
ciphertxt = des.encrypt(paddedtxt)
encrypedtxt = str(binascii.hexlify(ciphertxt),'utf-8')
print (encrypedtxt)

a=str(des.decrypt(encrypedtxt))
print (a)