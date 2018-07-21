from Crypto.Cipher import  DES
import base64

keyfile = open ("key.txt","r")
key = keyfile.read()

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

des = DES.new(key, DES.MODE_ECB)

chioce = input("1.Press 'e' to Encrypt:\n2.Press 'd' to Decrypt:\n")

if chioce == 'e' :
    text = open("input.txt",'r')
    textw = open("cipher.txt",'w')
    inputtxt = text.read()
    cipher = pad(inputtxt)
    encrypted = des.encrypt(cipher)
    textw.write(str(encrypted))
    print ("Encrypted Text :"+str(encrypted))

elif chioce == 'd' :
    text = open("input.txt",'r')
    textw = open("plain.txt",'w')
    inputtxt = text.read()
    cipher = pad(inputtxt)
    encrypted = des.encrypt(cipher)
    decrypted = des.decrypt(encrypted)
    textw.write(str(decrypted))
    print ("Decrypted Text :"+str(decrypted))


