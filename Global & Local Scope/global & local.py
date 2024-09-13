#global dan local scope adalah suatu sistem pada program
#global merupakan sebuah sistem yang berada di luar sistem looping ataupun logika
#local scope adalah sebuah sistem yang berada di dalam sistem looping ataupun logika

#global scope
a = 2
def pertambahan():
    bilangan_tambah = 10
    tambah = a + bilangan_tambah
    return tambah

tambah = a + 10
print(tambah)

print(pertambahan())

#Jadi pada global scope kita dapat menentukan suatu variabel
#kemudian variabel tersebut dapat diakses/dieksekusi pada sistem manapun

#local scope

def kurang():
    c = 5
    d = 2
    kurang = c - d
    return kurang

print(kurang())

kali = c * d 
print(kali)

#dapat dilihat pada variabel diatas
#ketika variabel yang berada di dalam def kemudian ingin diakses diluar def tersebut
#maka variabel tersebut akan error
#karena variabel tersebut hanya akan mengesekusi pada lingkupan def tersebut

def bagi():
    dibagi = c/d
    return dibagi

print(bagi())

#sama hal nya seperti sistem diatas
#ketika kita ingin mengeksekusi variabel tersebut
#meskipun kita membuat sistem yang sama (dalam hal ini kita menggunakan def)
#sistem tersebut tetap tidak akan berjalan
#ini dikarenakan variabel tersebut hanya akan berjalan di satu lingkup sistem

