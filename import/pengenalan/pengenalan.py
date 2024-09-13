#import statement
#import statement merupakan sebuah sebuah pernyataan
#yang dimana fungsi nya yaitu untuk mengambil suatu program dari file external berbentuk .py
#perlu diingat, pada saat pembuatan nama file penggunaan spasi harus dihindarkan
#sebagai ganti nya dapat menggunakan underscore (_)

#   1. untuk menyambungkan program dari external .py
print("halo dunia")
import hello_world

#perlu diingat, untuk file yang akan diimport nanti yang akan dijalankan
#merupakan file yang disimpan paling terakhir kali

#   2. import menggunakan data variabel
import halo_saya
print(halo_saya.data)

#tuliskan nama data variabel pada namespace variabel
#namespace variabel yaitu adalah file .py yang akan kita import
import waifu
print(waifu.istri)

#   3. import fungsi
import mtk
hasil = mtk.kali(4,5)

print(hasil)

#untk import suatu fungsi
#kita dapat mengisi argument fungsi external tersebut disini

#   4. import input
import input_1
input_1.data

#pycahce
#ketika kita telah mengeksekusi suatu package
#nanti setelah selesai akan membuat sebuah folder __pycahce__
#di dalam folder __pycahce__ berisi berupa perintah mesin untuk mengeksekusi module
#guna dari folder ini yaitu untuk mempercepat proses mengekseksi suatu module
