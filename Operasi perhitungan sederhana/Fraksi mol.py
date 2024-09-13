#Pertama
#menghitung mol tiap masing masing senyawa
Massa_1 = float(input("Berapakah massa senyawa pertama? "))
Mr_1 = float (input("Berapakah Mr senyawa pertama? "))
mol_1 = Massa_1 / Mr_1

Massa_2 = float(input("Berapakah massa senyawa kedua ? "))
Mr_2 = float (input("Berapakah Mr senyawa kedua? "))
mol_2 = Massa_2 / Mr_2

print("Mol 1 ", '=', Massa_1, '/', Mr_1, '=', mol_1)

print("Mol 2 ", '=', Massa_2, '/', Mr_2, '=', mol_2)


#Kedua
#Menghitung Fraksi mol yang kedua mol
X_mol_1 = (mol_1)/(mol_1 + mol_2)

print("X mol 1 ", '=', mol_1, '/' , '(', mol_1, '+', mol_2, ')', '=', X_mol_1)

X_Mol_2 = (mol_2)/(mol_1 + mol_2)

print("X mol 2 ", '=', mol_2, '/' , '(', mol_1, '+', mol_2, ')', '=', X_Mol_2)


#Ketiga
#Menjumlahkan seluruh fraksi mol untuk mencari fraksi total
#Jika fraksi total = < 1 = False
#Jika fraksi total = 1 = True
X_total = X_mol_1 + X_Mol_2

print("X Total", '=', X_mol_1, '+', X_Mol_2, '=', X_total)
