import time
import string
import random
import os

DATABASE = "data.txt"
template = {
    "key" : "XXXXXX",
    "pendapatan" : 255*" ",
    "pengeluaran" : 255*" ",
    "total" : 255*" ",
    "tanggal" : "dd/mm/yyyy"
}

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
            data["pendapatan"] = pendapatan_str + template["pendapatan"][len(pendapatan_str):]
            data["pengeluaran"] = pengeluaran_str + template["pengeluaran"][len(pengeluaran_str):]
            data["total"] = total_str + template["total"][len(total_str):]
            data["tanggal"] = time.strftime("%Y - %m - %d")

            #print
            seluruh_data = f'{data["key"]},{data["pendapatan"]},{data["pengeluaran"]},{data["total"]},{data["tanggal"]}'
            print(len(seluruh_data))
            file.write(seluruh_data)


def read_data(**kwargs) -> str: #<- menunjukan fungsi menjadi str (string)
    with open(DATABASE,"r") as file:
        content = file.readlines() #membaca file database menjadi berupa sebuah data dict
        #print(content) -> akan diprint menjadi sebuah data dict
        jumlah_data = len(content) #<- mengecek berapa banyak jumlah data
        if "index" in kwargs: #<- jika key index didalam kwargs
            index_data = kwargs["index"]-1
            if index_data < 0 or index_data > jumlah_data: #<- untuk membatasi input index
                return False #mengembalikan hasil menjadi false atau 0
            else: #mengembalikan hasil menjadi true (1)
                return content[kwargs["index"]-1] #<- untuk mengambil kwargs pada key index kemudian mengambil data pada index tertentu pada data.txt . dikarenakan index dimulai dari 0, kita perlu mengurangi index yang diinput. misal mengambil data pertama, berarti index input = 1 dikurangi 1 menjadi 0
            
        else: #<- digunakan untuk membaca saja
            return content #akan dikembalikan menjadi sebuah data string
        
        
""" def update(no_data,pk,pemasukan,pengeluaran,total,tanggal):
    #casting to str
    pendapatan_str = str(pemasukan)
    pengeluaran_str = str(pengeluaran)
    total_str = str(total)

    #data dict
    data = template.copy()
    data["key"] = pk
    data["pendapatan"] = pendapatan_str + template["pendapatan"][len(pendapatan_str):]
    data["pengeluaran"] = pengeluaran_str + template["pengeluaran"][len(pengeluaran_str):]
    data["total"] = total_str + template["total"][len(total_str):]
    data["tanggal"] = tanggal

    #print
    seluruh_data = f'{data["key"]},{data["pendapatan"]}, {data["pengeluaran"]}, {data["total"]},{data["tanggal"]}'
    #print(seluruh_data)
    #print(len(seluruh_data))
    panjang_data = len(seluruh_data)
    #panjang_aa = panjang_data*(no_data-1)
    #print(panjang_data) 
    try:
        with open(DATABASE, "r+", encoding="utf-8") as file:
            #content = file.readlines()
            #jumlah_data = len(content)
            file.seek(panjang_data*(no_data-1))
            #test = file.seek(panjang_aa*(no_data-1)) #untuk memindahkan kursor ketika mengedit, jika tidak maka data yang diedit merupakan data yang pertama
            file.write(seluruh_data)
    except:
        print("Terjadi error")
    #file.write(seluruh_data) """
    
def update(data_ganti,pk,pemasukan,pengeluaran,total,tanggal):
        #casting to str dan int
    pendapatan_str = str(pemasukan)
    pengeluaran_str = str(pengeluaran)
    total_str = str(total)
    data_ganti = int(data_ganti)

        #data dict
    data = template.copy()
    data["key"] = pk
    data["pendapatan"] = pendapatan_str + template["pendapatan"][len(pendapatan_str):]
    data["pengeluaran"] = pengeluaran_str + template["pengeluaran"][len(pengeluaran_str):]
    data["total"] = total_str + template["total"][len(total_str):]
    data["tanggal"] = tanggal
    
        #print
    seluruh_data = f'{data["key"]},{data["pendapatan"]},{data["pengeluaran"]},{data["total"]},{data["tanggal"]}'
    print(len(data['key']))
    print(len(data['pendapatan']))
    print(len(data['pengeluaran']))
    print(len(data['total']))
    print(len(data['tanggal']))
    print(len(seluruh_data))
    panjang_data = len(seluruh_data)
    
    with open(DATABASE,"r+",encoding="utf-8") as file:
        if data_ganti == 1:
            file.seek(0)
        elif data_ganti == 2:    
            file.seek(panjang_data*(data_ganti-1)+data_ganti)
        elif data_ganti > 2:
            file.seek(panjang_data*(data_ganti-1)+data_ganti+(data_ganti-2))
        #print(panjang)
        #file.write(seluruh_data)
        print("Data telah diganti")
        
def delete(no_data):
    try:
        with open(DATABASE,"r") as file:
            counter = 0 #<- menghitung readline keberapa yang ingin kita hapus
            while True:
                content = file.readline() #membaca data dalam satu baris
                if len(content) == 0:
                    break #<- jika panjang data 0, maka secara otomatis program akan berhenti
                elif counter == no_data - 1:
                    pass
                    #ketika counter memiliki jumlah yang sama
                    #maka data yang pada barisan counter itu akan diskip/dilewati
                    #nanti nya pada saat melakukan pencopy-an data terhadap temp_file
                    #data yang ingin dihapus tidak ikut tercopy
                else:
                    with open("data_temp.txt","a",encoding="utf-8") as temp_file:
                        temp_file.write(content)
                        #temp_file atau temporary file digunakan sebagai buffer
                        #data yang berada di DATABASE akan dipindahkan ke file temp_file
                        #
                counter += 1
    except:
        print("data gagal dihapus")
    
    os.replace("data_temp.txt",DATABASE) #<- untuk mengubah nama file data_temp.txt menjadi DATABASE

if __name__ == "__main__":
    #read_data()
    #update()
    Membuat_database_pertama()
    























if __name__ == "__main__":
  """   try:
      with open(DATABASE, mode="r") as file:
            print("Mengecek database")
            content = file.read()
            print(content)
    except:
      print("database tidak ditemukan")
      Membuat_database_pertama()
      print("database telah dibuat") """
  read_data()
