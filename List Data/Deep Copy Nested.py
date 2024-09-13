data_0 = [1,3]
data_1 = [5.7]

#Shallow Copy
#Shallow copy merupakan cara mengcopy suatu nested list, 
#namun tidak dapat merubah list yang berada pada isi list
#hanya dapat merubah list biasa

data_gabungan = [data_0, data_1, 9]
data_copy = data_gabungan.copy()

print(f"Data gabungan = {data_gabungan}")
print(f"Data copy = {data_copy}")

print(f"\naddress data list")
print(f"Data gabungan = {hex(id(data_gabungan))}")
print(f"Data copy = {hex(id(data_copy))}")

print(f"\naddress data list tiap dalam list")
print(f"Data gabungan = {hex(id(data_gabungan[0]))}")
print(f"Data copy = {hex(id(data_copy[0]))}")

print(f"\nmengubah data list")

data_gabungan[2] = 8
print(f"Data gabungan = {data_gabungan}")
print(f"Data copy = {data_copy}")

print("\n")

data_copy[0][0] = 2
print(f"Data gabungan = {data_gabungan}")
print(f"Data copy = {data_copy}")

#list pada data masing masing akan berubah, ini dikarenakan data list memiliki address yang berbeda
#sedangkan list pada data list kedua nya sama sama berubah, ini dikarenan data list memiliki data list yang berbeda

#Deepcopy 
#Deep copy merupakan suatu cara untuk mencopy data list secara keseluruhan
#tidak seperti shallow copy, deep coppy dapat merubah list dalam data list

print(f"\ndeepcopy")
data_0 = [1,3]
data_1 = [5.7]
from copy import deepcopy
data_gabungan = [data_0, data_1, 9]
data_copy = data_gabungan.copy()
data_deep = deepcopy(data_gabungan)

print(f"Data gabungan = {data_gabungan}")
print(f"Data copy = {data_copy}")
print(f"Data deep = {data_deep}")

print(f"\naddress data list")
print(f"Data gabungan = {hex(id(data_gabungan))}")
print(f"Data copy = {hex(id(data_copy))}")
print(f"Data deep = {hex(id(data_deep))}")

print(f"\naddress data list tiap dalam list")
print(f"Data gabungan = {hex(id(data_gabungan[0]))}")
print(f"Data copy = {hex(id(data_copy[0]))}")
print(f"Data deep = {hex(id(data_deep[0]))}")

#dapat dilihat perbedaan address data list tiap dalam list nya
print("\n")
data_gabungan[0][0] = 2
data_deep[0][1] = 4

print(f"Data gabungan = {data_gabungan}")
print(f"Data copy = {data_copy}")
print(f"Data deep = {data_deep}")

#dapat dilihat, hasil menunjukkan data gabungan dan data copy tetap saling menyalin
#sedangkan pada data deep, data tersebut tidak menyalin data gabungan dan data copy