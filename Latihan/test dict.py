import random
import string

template_data = {
    "nama":"nama",
    "kelas":"kelas",
    "absen" : "absen",
    "nilai" : "nilai"
}

data_ulangan ={}


while True:

    siswa = dict.fromkeys(template_data.keys())
    siswa["nama"] = input("Nama : ")
    siswa["kelas"] = str(input("Kelas : "))
    siswa["absen"] = int(input("Absen : "))
    siswa["nilai"] = int(input("Nilai : "))

    key = "".join(random.choice(string.ascii_uppercase) for i in range(6))

    data_ulangan.update({key:siswa})

    for siswa in data_ulangan:
        key = siswa
    
        nama = data_ulangan[key]['nama']
        kelas= data_ulangan[key]['kelas']
        absen = data_ulangan[key]['absen']
        nilai = data_ulangan[key]['nilai']

        print(key , nama, kelas, absen, nilai)
    
        lanjut = input("apakah akan lanjut (y/n): ")
        if lanjut == "n":
            break