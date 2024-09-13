#Operasi logika atau boolean
#not, or, and, xor
#NOT = Kebalikan data awal
#OR = jika ada True maka True #pada logika matematika atau tabel kebenaran disebut dengan disjungsi inklusif
#AND = jika ada False maka False #pada logika matematika atau tabel kebenaran disebut dengan kongjungsi
#XOR = jika beda maka True #pada logika matematika atau tabel kebenaran disebut dengan disjungsi ekslusif

#XOR
#'XOR' dalam logika matematika atau tabel kebenaran disebut dengan disjungsi ekslusif
#tabel kebenarang disjungsi ekslusif hanya salah satu pernyataan yang berbeda maka hasilnya akan benar (true)
#jika hasil pernyataan kedua itu sama, maka hasilnya akan salah

print("===XOR===")
a = True
b = True
c = a ^ b

print(a, 'xor', b, '=', c)

a = True
b = False
c = a ^ b

print(a, 'xor', b, '=', c)

a = False
b = True
c = a ^ b

print(a, 'xor', b, '=', c)

a = False
b = False
c = a ^ b

print(a, 'xor', b, '=', c)
