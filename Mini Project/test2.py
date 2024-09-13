import os
import time
import string
import random
""" 
def header():
    print("SELAMAT DATANG".center(100))
    print("ANDA SEKARANG SEDANG MENGAKSES".center(100))
    print("DATABASE KEUANGAN".center(100))
    print("="*100)
    print("""
        #1. Read Data
        #2. Create Data
        #3. Update Data
        #4. Delete
        #""")
    

""" template = {
    "kata":255*".",
    "huruf":255*"."
}
nama = input("")
huruf = input("") """

"""data = template.copy()
panjang_kata_str = f"{data['kata']:.16}"
panjang_huruf_str = f"{data['huruf']:.16}"
data["kata"] = nama + template["kata"][len(panjang_kata_str):]
data["huruf"] = huruf + template["huruf"][len(panjang_huruf_str):]
seluruh_data = f"{panjang_kata_str:.16},{panjang_huruf_str:.16}"
print(len(panjang_kata_str))
print(len(panjang_huruf_str))
print(len(data["kata"]))
print(len(data["huruf"]))
print(len(template["huruf"][len(huruf):]))
print(len(template["kata"][len(nama):]))
print(len(nama+(template["kata"][len(nama):]))) """


""" data = template.copy()
panjang_kata_str = f"{data['kata']:.16}"
panjang_huruf_str = f"{data['huruf']:.16}"
print("="*100)
print(f"len kata = {len(panjang_kata_str)}")
print(f"len huruf = {len(panjang_huruf_str)}")
print("="*100)

data["kata"] = nama + template["kata"][len(nama):]
data["huruf"] = huruf + template["huruf"][len(huruf):]
print("\n"+"="*100)
print(f"len data kata = {len(data['kata'])}")
print(f"len data huruf = {len(data['huruf'])}")
print("="*100)

format = f"{data['kata']},{data['huruf']}"
print(format)
print(f"len format = {len(format)}") """



template = {
    "key" : "XXXXXX",
    "pendapatan" : 255*" ",
    "pengeluaran" : 255*" ",
    "total" : 255*" ",
    "tanggal" : "dd/mm/yyyy"
}

        #input
pendapatan = int(input("Berapa nilai pemasukan : "))
pengeluaran = int(input("Berapa nilai pengeluaran : "))
total = pendapatan - pengeluaran

        #casting to str
pendapatan_str = str(pendapatan)
pengeluaran_str = str(pengeluaran)
total_str = str(total)

        #data dict
data = template.copy()
data["key"] = ''.join((random.choice(string.ascii_letters)for key_random in range(6)))
data["pendapatan"] = pendapatan_str + template["pendapatan"][len(pendapatan_str):]
data["pengeluaran"] = pengeluaran_str + template["pengeluaran"][len(pengeluaran_str):]
data["total"] = total_str + template["total"][len(total_str):]
data["tanggal"] = time.strftime("%Y - %m - %d")
    
        #print
seluruh_data = f'{data["key"]}, {data["pendapatan"]}, {data["pengeluaran"]}, {data["tanggal"]}, {data["tanggal"]}'
print(len(data["pendapatan"])) #255
print(len(data["pengeluaran"])) #255
print(len(data["total"])) #255
print(len(seluruh_data)) #553

