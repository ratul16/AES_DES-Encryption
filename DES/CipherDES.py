from Crypto.Cipher import  DES
import base64

keyfile = open ("key.txt","r")
key = keyfile.read()

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

des = DES.new(key, DES.MODE_ECB)


choice = input("Press 'e' to Encrypt : \nPress 'd' to Decrypt : \n")

if choice == 'e' :
    filer = open("input.txt","r")
    filew = open("cipher.txt","w")
    plaintxt = filer.read()
    paddedtxt = pad(plaintxt)
    ciphertxt = des.encrypt(paddedtxt)
    encrypt = str(base64.b64encode(ciphertxt))
    filew.write(encrypt)

elif choice == 'd' :
    filer = open("cipher.txt","r")
    filew = open("plain.txt","w")
    ciphertxt = filer.read()
    paddedtxt = pad(ciphertxt)
    decipher = des.decrypt(paddedtxt)
    decrypt =str(base64.b64decode(decipher))
    filew.write(decrypt)