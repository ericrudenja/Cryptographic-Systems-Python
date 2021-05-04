import hashlib
# a very simple case

plaintext1 = "101011"
plaintext2 = "100000"
plaintext3 = "001111"
initializationVector = "101110"

# print(plaintext1 ^ initializationVector)
ciphertextList = []
decryptedList = []

print "Initialization vector: " + initializationVector + "\n"

def encryptDecrypt(plaintext, key, whichWay):

    if len(plaintext) == len(key):
        ciphertext = ""
        for l, i in zip(plaintext, key):
            if l == " " or i == " ":
                ciphertext = ciphertext + (" ")
            elif (int(l) + int(i)) == 2:
                ciphertext = ciphertext + ("0")
            else:
                ciphertext = ciphertext + str((int(l) + int(i)))

        if whichWay == 1:
            ciphertextList.append(ciphertext)
        elif whichWay == 2:
            decryptedList.append(ciphertext)

encryptDecrypt(plaintext1, initializationVector, 1)
encryptDecrypt(plaintext2, ciphertextList[-1], 1)
encryptDecrypt(plaintext2, ciphertextList[-2], 1)
encryptDecrypt(plaintext2, ciphertextList[-3], 1)


print "dec"
encryptDecrypt(ciphertextList[-1], plaintext1, 2)
encryptDecrypt(ciphertextList[-2], plaintext2, 2)
encryptDecrypt(ciphertextList[-3], plaintext2, 2)
encryptDecrypt(ciphertextList[-4], initializationVector, 2)

print ciphertextList
print decryptedList
# last one of the decryptedList should be the original plaintext value whatever the original value was

# same thing done with sha256
class cbc:
    def __init__(self, hashPrevious, upcoming):
        self.upcoming = upcoming
        self.hashPrevious = hashPrevious
        stringToBeConvertedToHash = "".join(upcoming) + hashPrevious
        #give a plaintext string to the hash and then encode it from into utf-8
        self.hashcbc = hashlib.sha256(stringToBeConvertedToHash.encode()).hexdigest()

# so if I change the first InitalizationVector, the further ones change too, let's test that

initializationVector = cbc("HelloMyNameIsEricAndThisIsInitializationVector", "Hello One")

secondcbc = cbc(initializationVector.hashcbc, ["Hello Two"])


print(initializationVector.hashcbc)

print(secondcbc.hashcbc)

# this wouldn't really be reversible because it's sha256 and that'd take a while


