#Operasi logika atau boolean
#not, or, and, xor
#NOT = Kebalikan data awal
#OR = jika ada True maka True #pada logika matematika atau tabel kebenaran disebut dengan disjungsi inklusif
#AND = jika ada False maka False #pada logika matematika atau tabel kebenaran disebut dengan kongjungsi
#XOR = jika beda maka True #pada logika matematika atau tabel kebenaran disebut dengan disjungsi ekslusif

#OR
#'OR' dalam logika matematika atau tabel kebenaran disebut dengan disjungsi
#tabel kebenarang disjungsi inklusif salah satu pernyataan harus benar (true) maka hasilnya dapat disebut 
#benar (true)
#Jika kedua pernyataan salah (false) maka akan disebut salah (false)

print("===OR===")
a = True
b = True
c = a or b

print(a, 'or', b, '=', c)

a = True
b = False
c = a or b

print(a, 'or', b, '=', c)

a = False
b = True
c = a or b

print(a, 'or', b, '=', c)

a = False
b = False
c = a or b

print(a, 'or', b, '=', c)