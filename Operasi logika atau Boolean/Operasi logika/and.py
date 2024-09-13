#Operasi logika atau boolean
#not, or, and, xor
#NOT = Kebalikan data awal
#OR = jika ada True maka True #pada logika matematika atau tabel kebenaran disebut dengan disjungsi inklusif
#AND = jika ada False maka False #pada logika matematika atau tabel kebenaran disebut dengan kongjungsi
#XOR = jika beda maka True #pada logika matematika atau tabel kebenaran disebut dengan disjungsi ekslusif

#AND
#'AND' dalam logika matematika atau tabel kebenaran disebut dengan kongjungsi
#Tabel kebenaran kongjungsi harus benar (true) semua baru hasilnya bisa disebut benar
#Jika salah satu pernyataan salah (false) maka hasilnya akan salah (false)

print("===AND===")
a = True
b = True
c = a and b

print(a, 'and', b, '=', c)

a = True
b = False
c = a and b

print(a, 'and', b, '=', c)

a = False
b = True
c = a and b

print(a, 'and', b, '=', c)

a = False
b = False
c = a and b

print(a, 'and', b, '=', c)