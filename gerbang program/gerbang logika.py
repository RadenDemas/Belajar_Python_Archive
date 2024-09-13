#__main___ -> merupakah sebuah top level environment

#__name__ == "__main__" hanya akan terjadi bila kita menjalankan program di file utama


#__name__ pada file program utama
print(f"__name__ pada program ini = {__name__}") #-> ketika kita mengeprint program ini di file yang kita gunakan saat ini, maka akan menghasilkan __main__
#yang artinya bahwa kita sedang menggunakan program ini sebagai file utama

#__name__ pada file program eksternal (module)
import fungsi
import tambah_module
#ketika kita mengiprint __name__ pada program eksternal
#maka hasil yang akan keluar adalah nama dari si file yang kita jalankan
#namun ketika kita menajalankan program tersebut pada file nya, maka akan berubah menjadi __main__
# python fungsi.py

#contoh penggunaann

#deklarasi
def tambah(a,b):
    return a+b
#fungsi utama
print(f"__name__ tambah_module = {tambah_module.__name__}")
if __name__ == "__main__":
    angka1 = 10
    angka2 = 15
    hasil = tambah(angka1,angka2)
    print(hasil)

#jika pada file external
if tambah_module.__name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = tambah_module.tambah(angka1,angka2)
    print(hasil)

#ketika kita menjalankan suatu program dari luar file utama dengan syarat program tersebut harus "__main__"
#file tersebut tidak akan berjalan

#__name__ pada package
import package

#ketika kita mengiport sebuah package dengan untuk mencari tahu __name__
#kita tidak dapat menjalankannya
#kita hanya dapat menjalankan program tersebut di dalam foldernya