import os #untuk membersihkan data terminal secara keseluruhan. gunakan cls untuk windows dan clear untuk mac dan linux
import random #memberikan data random
import string #menuliskan data string berdasarkan ASCII


#latihan
template_data = {
    "nama":"nama",
    "kelas":"kelas",
    "absen" : "absen",
    "nilai" : "nilai"
}

data_ulangan ={}

while True:


    os.system("cls")
    print(f"{'DATA SISWA':^30}")

    siswa = dict.fromkeys(template_data.keys()) #dapat menggunakan dict.fromkeys ataupun menggunakan data kosong.fromkeys
    siswa["nama"] = input("Nama : ")
    siswa["kelas"] = str(input("Kelas : "))
    siswa["absen"] = int(input("Absen : "))
    siswa["nilai"] = int(input("Nilai : "))
    print(f"{'KEY':<9}  {'NAMA':<8} {'kelas':<8} {'ABSEN':<3} {'NILAI':<3}")
    print("="*50)

    KEY = ''.join((random.choice(string.ascii_uppercase) for key_random in range(6)))
    data_ulangan.update({KEY:siswa})

#program akan terus saling tindih dikarenakan data yang diambil memiliki key yang sama secara terus menerus
#oleh karena itu kita harus menggenerate key agar data data tersebut tidak saling tumpang tindah
#penggenerate-an key tersebut dilakukan secara acak melali data import random dan string

    for siswa in data_ulangan:
        key = siswa

        nama = data_ulangan[key]['nama']
        kelas= data_ulangan[key]['kelas']
        absen = data_ulangan[key]['absen']
        nilai = data_ulangan[key]['nilai']

    print(f"{key:<9} {nama:<8} {kelas:<8} {absen:<3} {nilai:<3}")
    print('\n')
    lanjut = input("apakah akan dilanjut (y/n): ")
    if lanjut == "n":
        break

