#data = ['kucing', 'kodok', 'burung', 'beruang', 'paus,', [1,2,3]]
#print(data)
#nilai = (85.68 + 86.81 + 88.6 + 90.87 + 91.33)/5
#print(nilai)


""" def input_user():
    pertanyaan = input("siapa disana:")


if input() == "aku":
    print("halo aku")
else:
    print("saha maneh") """

""" import time

tanggal = time.strftime("%Y - %m - %d")
print(tanggal) """

import random
import string
import time

template = {
    "key" : "XXXXXX",
    "pendapatan" : 255*" ",
    "pengeluaran" : 255*" ",
    "total" : 255*" ",
    "tanggal" : "dd/mm/yyyy"
}
#input
""" kelas = int(input(""))
kelas_str = str(kelas) """
pendapatan = int(input("Berapa nilai pemasukan : "))
pengeluaran = int(input("Berapa nilai pengeluaran : "))
total = pendapatan - pengeluaran

#casting to str
pendapatan_str = str(pendapatan)
pengeluaran_str = str(pengeluaran)
total_str = str(total)

""" while True:
    
    data = template.copy()
    
    data["key"] = ''.join((random.choice(string.ascii_letters)for key_random in range(6)))
    data["Kata"] = "Demas" + template["Kata"][len("Demas"):]
    data["kelas"] = kelas_str + template["kelas"][len("kelas"):]
    data["Apa"] = "naon"
    print(data)
    break """

while True:

    data = template.copy()
    data["key"] = ''.join((random.choice(string.ascii_letters)for key_random in range(6)))
    data["pendapatan"] = pendapatan_str + template["pendapatan"][len("pendapatan"):]
    data["pengeluaran"] = pengeluaran_str + template["pengeluaran"][len("pengeluaran"):]
    data["total"] = total_str + template["total"][len("total"):]
    data["tanggal"] = time.strftime("%Y - %m - %d")
    print(data)
    break