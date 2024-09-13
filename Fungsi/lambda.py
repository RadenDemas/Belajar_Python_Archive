#fungsi lambda atau fungsi anonimus
#fungsi lambda bisa disebut fungsi anonimus dikarenakan
#lambda merupakan fungsi yang tidak memiliki nama

#fungsi biasa

def pangkat(angka):
    return angka**2

print(f"hasil pangkat = {pangkat(2)}")

#fungsi lambda
#variabel = lambda argument:return
pangkat = lambda angka:angka**2

print(f"hasil pangkat = {pangkat(4)}")

#jadi maksud dari penggunaan dari lambda disini itu
#untuk mempersingkat fungsi pada umumnya
#sebagai contoh diatas
#kasus diatas dapat dituliskan f(x) = x^2
#jadi ketika kita mengimputkan suatu angka kedalam fungsi tersebut
#angka tersebut akan masuk sebagai argument (kita sebut x)
#kemudian argument tersebut selanjutnya akan dieksekusi ke dalam rumus x^2
#jadi urutannya:
#argument masuk -> eksekusi sesuai badadn fungsi -> selesai 





##sorting data list
data_list = ["demas", "syahrul", "waldi", "ajef", "eja"]
#sorting normal
data_list.sort()
print(data_list)

##sorting berdasarkan panjang
#cara normal
data_list = ["demas", "syahrul", "waldi", "ajef", "eja"]
data_list.sort(key=len)
print(f"\n sort normal = \n {data_list}")

#cara fungsi biasa
data_list = ["demas", "syahrul", "waldi", "ajef", "eja"]
def sort(data):
    return len(data)
data_list.sort(key=sort)
print(f"\n sort fungsi biasa = \n {data_list}")

#cara fungsi lambda 
data_list = ["demas", "syahrul", "waldi", "ajef", "eja"]
data_list.sort(key=lambda data:len(data))
print(f"\n sort fungsi lambda = \n {data_list}")

#jadi maksud dari fungsi disini yaitu
#pertama tama data list tersebut masuk terlebih dahulu ke dalam fungsi
#kemudian setelah masuk ke dalam argument suatu fungsi akan dieksekusi di badang fungsi
#setelah dieksekusi, data list tersebut di"return" kembali ke dalam data list.sort
#data list -> masuk ke argument suatu fungsi -> dieksekusi di badan fungsi -> di"return" -> hasilnya kembali ke data list.sort

##filter
#filter disini merupakan suatu cara menyaring data yang diinginkan pada suatu data list

data_angka = [1,2,4,5,6,7,8,9]

#mengambil data kurang dari tujuh
#menggunakan fungsi biasa
def filter_kurang_dari_lima(angka):
    return angka < 7

data_angka_baru = list(filter(filter_kurang_dari_lima, data_angka))
print(f"data kurang dari tujuh = {data_angka_baru}")

#jadi pada maksud fungsi disini yaitu
#secara rumus terlebih dahulu
#variabel baru = list(filter(fungsi,data list))
#jadi ketika kita telah menuliskan fungsi
#kemudian pada nantinya si data list tersebut akan masuk kedalam argument pada fungsi
#setelah itu masuk kedalam badan fungsi dan kemudian dieksekusi
#kemudian data tersebut nantinya akan di"return" ke dalam variabel data list baru
#proses:
#data list -> masuk ke dalam argument fungsi -> diproses didalam badan fungsi -> di"return" ke dalam data list baru

#mengambil data kurang dari empat
#menggunakan lambda
data_angka_baru_2 = list(filter(lambda x:x<4,data_angka))
print(f"data kurang dari empat = {data_angka_baru_2}")

#kurang lebih cara kerja nya sama seperti pada fungsi biasa, namun lebih singkat
#data list masuk ke dalam argumen x, dan untuk x itu kurang dari 4
#jadi nantinya data baru tersebut akan menghasilkan angka yang bernilai kurang dari 4

#mengambl data genap&ganjil
data_genap = list(filter(lambda x:(x%2==0),data_angka))
data_ganjil = list(filter(lambda x:(x%2 != 0), data_angka))

print(f"angka genap = {data_genap}")
print(f"angka ganjil = {data_ganjil}")

#fungsi anonimus/currying
#secara sederhana, kita dapat memasukkan fungsi lambda langsung kedalam suatu fungsi tanpa nama
#itulah mengapa fungsi lambda sering disebut juga fungsi anonimus

#fungsi biasa
def pangkat_2(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(pangkat_2(2,3))

#fungsi anonimus/currying
def pangkat_lambda(pangkat):
    return lambda angka:angka**pangkat

hasil_lambda = pangkat_lambda(2) #<- memasukan argument biasa
print(hasil_lambda(4)) #<- memasukan argument lambda

print(pangkat_lambda(3)(3)) #<- kurung pertama merupakan argument fungsi biasa dan yang kedua merupakan argument fungsi lambda

#jadi pada saat kita menggunakan fungsi biasa, kita menggunakan 2 argument secara bersamaan
#namun pada fungsi anonimus kita menggunakan 2 argument yang berbeda
#yang satu menggunakan argument fungsi biasa dan satu lagi argument lambda
#jadi pada saat pengisian argument kita menggunakan dua kali kurung
#urutannya argument fungsi kemudian argument anonimus
#setelah itu fungsi dapat dieksekusi

#proses:
#argument fungsi -> masuk ke dalam badan fungsi (pangkat) -> argument lambda -> masuk ke dalam badan fungsi (angka) -> kemudian setelah itu fungsi dapat dieksekusi dan di"return"
