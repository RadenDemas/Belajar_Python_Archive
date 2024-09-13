import time
import string
import random

DATABASE = "data.txt"
template = {
    "key" : "XXXXXX",
    "pendapatan" : 255*" ",
    "pengeluaran" : 255*" ",
    "total" : 255*" ",
    "tanggal" : "dd/mm/yyyy"
}

#Membuat Database
def Membuat_database_pertama():
    with open(DATABASE,"w",encoding="utf-8") as file:
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
            data["pendapatan"] = pendapatan_str + template["pendapatan"][len("pendapatan"):]
            data["pengeluaran"] = pengeluaran_str + template["pengeluaran"][len("pengeluaran"):]
            data["total"] = total_str + template["total"][len("total"):]
            data["tanggal"] = time.strftime("%Y - %m - %d")

            #print
            seluruh_data = f'{data["key"]}, {data["pendapatan"]}, {data["pengeluaran"]}, {data["total"]}, {data["tanggal"]}'
            print(seluruh_data)
            file.write(seluruh_data)


#Read Data
def read_data():
    with open(DATABASE,"r") as file:
        content = file.readlines() #membaca file database menjadi berupa sebuah data dict
        #print(content) -> akan diprint menjadi sebuah data dict
        return content #akan dikembalikan menjadi sebuah data string 

""" try:
      with open(DATABASE, mode="r") as file:
            print("Mengecek database")
            content = file.read()
            print(content)
except:
      print("database tidak ditemukan")
      Membuat_database_pertama()
      print("database telah dibuat")
 """