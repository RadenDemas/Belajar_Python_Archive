##args
#args merupakan singkatan dari arguments
#args berfungsi untuk membuat argument pada pada berbentuk data list
#pada penulisan args harus menggunakan tanda "*", jadi penulisan nya=
#nama_fungsi(*args): """nama args dapat diganti dengan nama lain"""

#fungsi biasa
def list(nama, kelas, absen ):
    print(f"nama = {nama}, kelas = {kelas}, absen = {absen}")

list("demas", 12, 21)

#fungsi list
def list_fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    kelas = data[1]
    absen = data[2]
    print(f"nama = {nama}, kelas = {kelas}, absen = {absen}")

list_fungsi(["syahrul", 12, 27])
#pada list fungsi seperti ini harus menggunakan penulisan data list
#nama_fungsi([data list])

#fungsi args
def list_args(*args):
    nama = args[0]
    kelas = args[1]
    absen = args[2]
    print(f"nama = {nama}, kelas = {kelas}, absen = {absen}")

list_args("rifki", 12, 24)
#jadi penulisan pada fungsi list args ditulis sesuai index
#jadi saat fungsi tersebut dilist, argument otomatis akan tersusun sesuai urutan penulisan argument
#list_args(rifki, 12, 24)
#index =     0    1   2

#jadi fungsi asli dari args ini yaitu misal nya kita menemui sebuah program
#yang dimana program itu membutuhkan banyak sekali objek
#disini kita menggunakan args untuk menyingkat pada bagian argument kepada bentuk list
#contoh

def penambahan(*data):
    bilangan = 0
    for angka in data:
        bilangan += angka
    return bilangan

hasil = penambahan(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

##kwars
#kwars merupakan singkatan dari key words arguments 
#args berfungsi untuk membuat argument pada fungsi berbentuk data dict
#pada penulisan args harus menggunakan tanda "**", jadi penulisan nya=
#nama_fungsi(**kwargs): """nama args dapat diganti dengan nama lain"""

#melihat kerja fungsi dict kwargs

def kumpulang_data(**kwargs):
    print(kwargs)
kumpulang_data(nama = "udin", kelas = 12, absen = 31, attitude = "minus")
#jadi pada fungsi diatas kita dapat melihat cara kerja dari fungsi kwargs
#jadi pada argument kita harus mengisi masih masing key dan value
#kumpulang_data(nama = "udin", kelas = 12, absen = 31, attitude = "minus")
#               key     value   key  value  key  value   key       value
#jadi pada argument nanti kita harus mengisi key dan value secara sekaligus 

#fungsi dict kwargs
def fungsi_kwargs(**kwargs):
    nama = kwargs["nama"]
    kelas = kwargs["kelas"]
    absen = kwargs["absen"]
    print(f"nama = {nama}, kelas = {kelas}, absen = {absen}")

fungsi_kwargs(nama = "waldi", kelas = 12, absen = 35)

#sesuai pada bagian melihat kerja fungsi dict kwargs
#pada bagian argument kita harus mengisi key dan value secara sekaligus
#kemudian pada bagian badan fungsi kita dapat memanggil si key nya

#campuran args dan kwargs
def operasi_math(*args,**kwargs):
    if kwargs["opsi"] == "tambah":
        bilangan = 1
        for angka in args:
            bilangan += angka
    elif kwargs["opsi"] == "kurang":
        bilangan = 1
        for angka in args:
            bilangan -= angka
    elif kwargs["opsi"] == "kali":
        bilangan = 1
        for angka in args:
            bilangan *= angka
    elif kwargs["opsi"] == "bagi":
        for angka in args:
            bilangan = 1
            bilangan *= angka
    else:
        print("tolong isi data yang benar")
    return bilangan

hasil = operasi_math(1,2,3,4,5, opsi = "tambah")
print(f"hasil = {hasil}")
hasil = operasi_math(1,2,3,4,5, opsi = "kurang")
print(f"hasil = {hasil}")
hasil = operasi_math(1,2,3,4,5, opsi = "kali")
print(f"hasil = {hasil}")
hasil = operasi_math(1,2,3,4,5, opsi = "none")
print(f"hasil = {hasil}")

#jadi pada fungsi diatas kita memiliki
#key = opsi
#value = tambah, kurang, kali, bagi
#data list = 1,2,3,4,5

#Jadi pada data diatas kita menggunakan data percabangan if, elif, dan else
#kita memiliki acuan nya kita memiliki key pada kwargs yaitu opsi
#nah pada bagian opsi ini yang akan berguna untuk menentukan hasil dari data percabangan
#kemudian data list (1,2,3,4,5) nanti kita gunakan for loop untuk operasi nya
#jadi awalnya kita harus menentukan terlebih dahulu bilangan sebelum for loop dimulai
#pada contoh tambahan kita memiliki bilangan = 1
#nanti pada jalan nya ekseksui:
# bilangan + data_list[awal] + ... + data_list[terakhir]

#untuk sistematika jalan nya:
#1. awal nya value pada key kwargs akan melihat opsi pada data percabangan
#2. data percabangan menemukan value yang sesuai dengan yang diinginkan
#3. pada data yang diinginkan kita dapat menjalankan hal yang kita inginkan, pada contoh ini kita menggunkan tambahan
#4. kita masukkan output bilangan awal
#5. kemudian kita masukkan data_list kepada data for loop
#6. tulis code sesuai program yang diinginkan

#perlu dicatat, untuk setiap operasi pada fungsi return harus pada paling bawah dan tidak boleh pada opsi lain
