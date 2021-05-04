publicPartN = 0

# Let's say plaintext message is HI, these two letters alphabetically stand for numbers 8 and 9 respectfully.

def generatePrivateKey(primeNumberP,primeNumberQ, exponentE, someIntegerK):
    global publicPartN
    publicPartN = primeNumberP * primeNumberQ

    for i in range(1, publicPartN + 1):
        if (publicPartN % i == 0 and i == exponentE) or type(exponentE) != int:
            raise Exception("Check the exponent!")

    convertN = (primeNumberP - 1) * (primeNumberQ - 1)

    privateKeyD = (someIntegerK * convertN + 1) / exponentE

    encryptedDataC = pow(89, exponentE) % publicPartN
    print "Encrypted data that says HI in a form of a number: " + encryptedDataC.__str__()

    decryptedDataC = pow(encryptedDataC, privateKeyD) % publicPartN
    print "Decrypted data that says HI from the number: " + decryptedDataC.__str__()





generatePrivateKey(53, 59, 3, 2)
