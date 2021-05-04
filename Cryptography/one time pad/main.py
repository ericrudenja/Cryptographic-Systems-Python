import binascii
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# a function that creates text files with relevant hex data
def writeFile(cipher, tag, ciphertext, filename):
    file_out = open(filename, "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()

# upload image and convert it to hex with the binascii module
def encryptAndDecrypt():
    ############################################################
    # ENCRYPT
    ############################################################

    with open("imageToEncrypt.png", 'rb') as n:
        imageHex = binascii.hexlify(n.read())
    print("Data to encrypt: " + imageHex.__str__())

    # set an arbitrary 16 byte key from the cryptodome module
    key = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(imageHex)

    writeFile(cipher, tag, ciphertext, "cipher.txt")

    ############################################################
    # DECRYPT
    ############################################################

    file_in = open("cipher.txt", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    writeFile(cipher, tag, ciphertext, "decrypted.txt")

    print("Decrypted data:  " + data.__str__())

    ############################################################
    # CONVERT DECRYPTED DATA BACK TO IMAGE FORMAT
    ############################################################

    data = data.strip()
    data = binascii.a2b_hex(data)
    with open('test3.png', 'wb') as image_file:
        image_file.write(data)

encryptAndDecrypt()


