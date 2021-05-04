keyK = [1, 2, 3, 6]
plaintextP = [1, 2, 2, 2]
vectorS = [0, 1, 2, 3, 4, 5, 6, 7]
temporaryVectorT = [1, 2, 3, 6, 1, 2, 3, 6]
C = []
t = 0
k = 0

j = 0

for i in range(0, 8):
    j = (j + vectorS[i] + temporaryVectorT[i]) % 8
    print("i = " + str(i))
    print("j = " + str(j))
    vectorS[i], vectorS[j] = vectorS[j], vectorS[i]
    print(vectorS)
    print("\n")

i = 0
j = 0

for n in range(plaintextP.__len__()):
    i = (i + 1) % 8
    j = (j + vectorS[i]) % 8
    vectorS[i], vectorS[j] = vectorS[j], vectorS[i]
    t = (vectorS[i] + vectorS[j]) % 8
    k = vectorS[t]
    C.append(k ^ plaintextP[n])

print("CypherText: " + str(C))