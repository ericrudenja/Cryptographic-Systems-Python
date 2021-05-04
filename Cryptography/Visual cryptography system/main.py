import binascii
from Crypto.Cipher import AES

# upload image and convert it to hex with the binascii module
def encrypt():
    with open("image.png", 'rb') as n:
        imageHex = binascii.hexlify(n.read())
    print(imageHex)

    # cipher = AES.new(imageHex, AES.MODE_EAX)

encrypt()

