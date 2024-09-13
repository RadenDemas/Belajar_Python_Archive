#mode write
with open("teks_1.txt","w",encoding="utf-8") as file:
    file.write("raden demas")
with open("teks_1.txt","w",encoding="utf-8") as file:
    file.write("syahrul diemas")

#dengan menggunakan mode write, kita dapat membuat sebuah file txt baru
#kemudian kita juga dapat langsung menambahkan suatu data secara langsung ke ke file txt
#namun ketika kita membuat sebuah code dengan file txt yang sama
#data tersebut akan secara sengaja menimpa file txt yang sebelum nya

#mode append
#mode append merupakan sebuah mode dimana kita
#dapat menambahkan suatu data ke dalam file txt dan langsung membuat file txt

with open("teks_2.txt","a",encoding="utf-8") as file:
    file.write("raden demas\n")
    file.write("syahrul diemas")

#data yang tambahkan secara otomatis akan berada di 1 baris yang sama
#meskipun kita membuat code di barisan yang berbeda
#jika ingin membuat data tersebut di baris yang baru, gunakan "\n" pada akhir kalimat

#mode r+
#mode r+ merupakan sebuah gabungan dari mode r dan w
#dengan mode ini kita dapat sekaligus membaca dan menulis file txt
#namun tidak seperti mode write biasa nya
#pada mode r+ tidak secara langsung membuat file txt kita dijalankan

with open("teks_3.txt","r+",encoding="utf-8") as file:
    print(f"apakah file ini dapat dibaca = {file.readable()}")
    print(f"apakah file ini dapat ditulis = {file.writable()}")

with open("teks_3.txt","r+",encoding="utf-8") as file:
    file.write("raden demas\n")
    file.write("syahrul diemas\n")
    file.write("rifki nur cahya")
    print(file.read())

#bisa dilihat ketika kita mencoba untuk membuka file txt pada satu bagian isi with
#file txt tersebut tidak dapat terbaca
#oleh karena itu kita harus membuat code yang sama lagi untuk membaca file txt

print("\n")

with open("teks_3.txt","r+",encoding="utf-8") as file:
    print(file.read())

with open("teks_3.txt","r+",encoding="utf-8") as file:
    file.write("siti\n")
    file.write("karina\n")

#ketika kita menulis ulang menggunakan r+
#jika pada mode write data akan secara langsung dihapus dan ditulis ulang
#pada mode r+ data akan secara otomatis menimpa data sebelumnya sesuai panjang data

print("\n")

with open("teks_3.txt","r+",encoding="utf-8") as file:
    print(file.read())