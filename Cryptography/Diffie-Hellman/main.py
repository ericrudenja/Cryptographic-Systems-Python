def DiffieHellman(primeP, primitiveRootG, alicePrivateValueA, bobPrivateValueB):
    aliceGeneratedKeyX = pow(primitiveRootG, alicePrivateValueA) % primeP
    bobGeneratedKeyY = pow(primitiveRootG, bobPrivateValueB) % primeP
    print("aliceGeneratedKeyX: " + aliceGeneratedKeyX.__str__())
    print("bobGeneratedKeyY: " + bobGeneratedKeyY.__str__())

    aliceGeneratedSecretKeyKa = pow(bobGeneratedKeyY, alicePrivateValueA) % primeP
    bobGeneratedSecretKeyKb = pow(aliceGeneratedKeyX, bobPrivateValueB) % primeP
    print("aliceGeneratedSecretKeyKa: " + aliceGeneratedSecretKeyKa.__str__())
    print("bobGeneratedSecretKeyKb: " + bobGeneratedSecretKeyKb.__str__())

    if aliceGeneratedSecretKeyKa == bobGeneratedSecretKeyKb: print ("Success, aliceGeneratedSecretKeyKa equals bobGeneratedSecretKeyKb!")


DiffieHellman(846, 3, 17, 72)




