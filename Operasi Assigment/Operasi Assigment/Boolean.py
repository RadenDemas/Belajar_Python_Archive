#Operasi boolean
#OR (&)
print("===OR===")
data = True
print("Hasil dari data asli adalah : ", data)
data |= True
print("Hasil Or True adalah : ", data)

data = True
print("\nHasil dari data asli adalah : ", data)
data |= False
print("Hasil Or False adalah : ", data)

data = False
print("\nHasil dari data asli adalah : ", data)
data |= True
print("Hasil Or True adalah : ", data)

data = False
print("\nHasil dari data asli adalah : ", data)
data |= False
print("Hasil Or False adalah : ", data)

#data boolean or akan menjadi false bila kedua nya false


#AND (&)
print("\n===AND===")
data = True
print("Hasil dari data asli adalah : ", data)
data &= True
print("Hasil And True adalah : ", data)

data = True
print("\nHasil dari data asli adalah : ", data)
data &= False
print("Hasil And False adalah : ", data)

data = False
print("\nHasil dari data asli adalah : ", data)
data &= True
print("Hasil And True adalah : ", data)

data = False
print("\nHasil dari data asli adalah : ", data)
data &= False
print("Hasil dAnd False adalah : ", data)

#boolean and akan menjadi false bila salah satu nya mempunyai false


#XOR (^)
print("\n===XOR===")
data = True
print("Hasil dari data asli adalah : ", data)
data ^= True
print("Hasil Xor True adalah : ", data)

data = True
print("\nHasil dari data asli adalah : ", data)
data ^= False
print("Hasil XOR False adalah : ", data)

data = False
print("\nHasil dari data asli adalah : ", data)
data ^= True
print("Hasil Xor False adalah : ", data)

data = False
print("\nHasil dari data asli adalah : ", data)
data ^= False
print("Hasil Xor True adalah : ", data)

#data boolean xor akan menjadi false bila kedua nya false dan true nya sama