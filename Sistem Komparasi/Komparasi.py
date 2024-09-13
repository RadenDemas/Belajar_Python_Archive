#Komparasi atau perbandingan adalah suatu sistem membandingkan satu nilai dengan nilai lainyna
#Setiap hasil dari Operasi komparasi akan menghasilkan boolean

#komparasi terdiri atas
'''
1. lebih besar <
2. lebih kecil >
3. lebih besar sama dengan >=
4. lebih kecil sama dengan <=
5. sama dengan absolut (nilai nya pasti) ==
6. tidak sama dengan !=
7. is (membandingkan suatu value dengan value lainnya dengan nilai yang sama)
8. is not (membandingkan suat value dewngan value lainnya dengan nilai yang tidak sama)
'''
#Hasil dari komparasi hanya akan menghasilkan True dan False

a = 6
b = 4

#Lebih Besar >
print("===LEBIH BESAR===")

hasil = a > 3
print("a > 3", '=', hasil)

hasil = a > 6
print("a > 6", '=', hasil)

hasil = b > 2
print("b > 2", '=', hasil)

hasil = b > 4
print("b > 4", '=', hasil)

#lebih kecil <
print("===LEBIH KECIL===")

hasil = a < 6
print("a < 6", '=', hasil)

hasil = a < 7
print("a < 7", '=', hasil)

hasil = b < 4
print("b < 4", '=', hasil)

hasil = b < 5
print("b < 5", '=', hasil)

#lebih besar sama dengan >=
print("===LEBIH BESAR SAMA DENGAN===")

hasil = a >= 3
print("a >= 3", '=', hasil)

hasil = a >= 6
print("a >= 6", '=', hasil)

hasil = b >= 2
print("b >= 2", '=', hasil)

hasil = b >= 4
print("b >= 4", '=', hasil)

#lebih kecil sama dengan <=
print("===LEBIH KECIL SAMA DENGAN===")

hasil = a <= 6
print("a <= 6", '=', hasil)

hasil = a <= 7
print("a <= 7", '=', hasil)

hasil = b <= 4
print("b <= 4", '=', hasil)

hasil = b <= 5
print("b <= 5", '=', hasil)

#SAMA DENGAN ABSOLUT ==
print("===SAMA DENGAN ABSOLUT===")

hasil = a == 6
print("a == 6 =", hasil)

hasil = a == 4
print("a == 4 =", hasil)

#Tidak sama dengan !=
print("===TIDAK SAMA DENGAN===")

hasil = a != 6
print("a != 6 =", hasil)

hasil = a != 4
print("a != 4 =", hasil)

#'is' sebagai komparasi object identity
# object identity merupakan identitas objek pada memori
# untuk melihat identitas objek dapat dilakukan menggunakan id(objek) 
# hex(id(objek)) merupakan identitas objek dalam bahasa java
print("===OBJECT IDENTITY (IS)===")

x = 9 #ini merupakan assigment untuk membuat object
y = 9

print('nilai x =', x , ', id =', hex(id(x)))
#0x229186c01f0 merupakan identitas objek dari x

print('nilai y =', y , ', id =', hex(id(y)))
#0x229186c01f0 merupakan identitas objek dari y
#kedua identitas tersebut dapat sama dikarenakan kedua objek tersebut memiliki value yang sama

hasil = x is y
print ('x is y', '=', hasil)

x = 9 
y = 6

print('nilai x =', x , ', id =', hex(id(x)))
#0x229186c01f0 merupakan identitas objek dari x

print('nilai y =', y , ', id =', hex(id(y)))
#0x2cdbe200190 merupakan identitas objek dari y
#kedua identitas tersebut berbeda, dikarenakan kedua objek tersebut memiliki value yang berbeda

hasil = x is y
print ('x is y', '=', hasil)

#hasil nya menjadi false, dikarenakan kedua objek memiliki identitas yang berbeda


#'is not'
#tidak seperti 'is'
#'is not' membandingkan kedua objek dengan melihat value yang berbeda
print("===OBJECT IDENTITY (IS NOT)===")

x = 7
y = 5

print('nilai x =', x , ', id =', hex(id(x)))
#0x1cb77e601b0 merupakan identitas objek dari x

print('nilai y =', y , ', id =', hex(id(y)))
#0x1cb77e60170 merupakan identitas objek dari y
#kedua objek memiliki identitas yang berbeda, ini dikarenakan kedua objek tersebut memiliki value yang berbeda

hasil = x is not y
print ('x is y', '=', hasil)

#hasil nya akan menjadi true, dikarenakan kedua objek memiliki identitas yang berbeda

x = 7
y = 7

print('nilai x =', x , ', id =', hex(id(x)))
#0x2cdbe2001b0 merupakan identitas objek dari x

print('nilai y =', y , ', id =', hex(id(y)))
#0x2cdbe2001b0 merupakan identitas objek dari y
#kedua identitas tersebut dapat sama dikarenakan kedua objek tersebut memiliki value yang sama

hasil = x is not y
print ('x is y', '=', hasil)

#hasil nya akan menjadi false, dikarenakan kedua objek memiliki identitas yang sama
