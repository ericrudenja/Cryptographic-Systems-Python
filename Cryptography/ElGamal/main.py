cOne = 0
cTwo = 0

def encrypt(largePrimeP, specialNumberG, publicKeyB, messageM, randomNumberK):
    global cOne
    global cTwo
    cOne = pow(specialNumberG, randomNumberK) % largePrimeP
    cTwo = (messageM * pow(publicKeyB, randomNumberK)) % largePrimeP

    print "cOne: " + cOne.__str__()
    print "cTwo: " + cTwo.__str__()

encrypt(283, 60, 216, 101, 36)

def decrypt(cOne, cTwo, largePrimeP, privateKeyb):
    decryptedMessage = pow(cOne, largePrimeP - privateKeyb - 1) * cTwo % largePrimeP
    print "Decrypted Message: " + decryptedMessage.__str__()

decrypt(cOne, cTwo, 283, 7)