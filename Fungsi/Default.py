#default argument
#seperti nama nya, default argument berarti sebuah argument yang sudah ada bawaan dari sana nya
#semisal jika nama_fungsi(argument)
#pada jenis argument biasa kita harus mengisi argument tersebut, jika tidak maka fungsi tidak akan berjalan
#sedangkan dalam default argument, ditulis nama_fungsi(argument = nilai)
#pada jenis default argument, ketika argument tersebut tidak diisi program akan tetap berjalan
#ini dikarenakan fungsi tersebut sudah memiliki nilai di dalam nya

#normal argument

def halo(kepada, salam):
    print(f"halo {kepada}, {salam}")

halo("demas", "salam kenal")

#default argument
def halo(kepada, salam = "salam kenal"):
    print(f"halo {kepada}, {salam}")

halo("demas")
halo("waldi", "apa kabar?")

#seperti pada fungsi diatas, pada default argument kita dapat mengosongkan argument (salam)
#ini dikarenakan argument (salam) sudah memiliki default argument nya
#sehingga kita fungsi tersebut dieksekusi, argument salam tinggal mengeksekusi nilai di dalam nya
#selain itu kita dapat menimpa nya dengan nilai yang baru

def hitungan(angka_1, angka_2 = 3):
    hasil = angka_1 * angka_2
    return hasil

print(hitungan(2,5))
print(hitungan(angka_2 = 10, angka_1 = 5))
print(hitungan(angka_1=5))

#pada fungsi diatas, telah diketahui nilai fungsi bawaan angka_2 yaitu 3
#sehingga jika kita mengisi nilai argument angka_1 saja, otomotis nilai angka_2 akan menjadi 3
#selain itu kita dapat mengedit/memodifikasi nilai tersebut dengan cara yang bebas, asalkan:
#nama_argument = nilai
#kita harus mengetahui dulu nama argument yang kita tulis, dengan itu kita dapat mengedit/memodifikasi nilai argumnet tersebut
#kemudian jika ada suatu argument tidak ada nilai nya, maka fungsi tidak akan berjalan

def banyak_hitungan(angka_1 = 1, angka_2 = 2, angka_3 = 3, angka_4 = 4, angka_5 = 5):
    hasil = angka_1 + angka_2 + angka_3 + angka_4 + angka_5
    return hasil

banyak_hitungan()
print(banyak_hitungan(angka_5 = 10))

#melanjutkan fungsi yang sebelumnya,
#kita dapat mengedit/memodifikasi nilai suatu argument dengan cara menarik nama argument nya
#sebagai contoh, kita menarik angka_5 diubah menjadi 10
#maka nilai awal angka_5 = 5 menjadi angka_5 = 10