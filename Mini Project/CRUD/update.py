from .operasi1 import read_data,update
from .read import read_console
def update_console():
    #membaca data yang ada
    read_console()
    
    #Memilih data yang akan diganti
    while True:
        data_ganti = int(input("Silahkan pilih data yang akan diganti: "))
        info_data = read_data(index=data_ganti)
        
        if info_data: #dikarenakan fungsi tersebut berupa true(1), maka data pun dapat dieksekusi
            break #while loop akan dihentikan secara paksa
        else: #dikarenakan sebelumnya fungsi dikembalikan menjadi false (0), maka else akan dieksekusi
            print("Nomor tidak valid")
    
    data_break = info_data.split(",") #jika tidak menggunakan split, database akan berupa string bukan berupa data dict
    pk = data_break[0]
    pemasukan = data_break[1]
    pengeluaran = data_break[2]
    total = data_break[3]
    tanggal  = data_break[4] #<- untuk menghapus \n diakhir barisan pada data.txt
    print("="*100)
    
    # Memilih jenis data yang akan diubah
    while True:
        print(f"Pendapatan = {pemasukan}")
        print(f"Pengeluaran = {pengeluaran}")
        print(f"total = {total}")
        print(f"tanggal = {tanggal}")
        print("="*100)
        
        print("""1. Pemasukan
2. Pengeluaran
""")
        permintan_ganti = input("Silahkan pilih data yang akan diganti: ")
        
        match permintan_ganti:
            case "1" : pemasukan = (input("Pemasukan:"))
            case "2" : pengeluaran = (input("Pengeluaran: "))
            case _: print("Permintaan yang diinginkan tidak vaild") #case _ -> digunakan bila input tidak sesuai yang diinginkan atau pada daftar, maka program akan selesai
        total = int(pemasukan) - int(pengeluaran)
        #print(len(str(total)))
        print(len(tanggal))
        #print(len(pengeluaran))
        berakhir = input("Apakah data yang ingin diganti sudah benar (y/n): ")
        if berakhir == "y" or berakhir == 'Y': 
            break
    #Membaca kembali setelah data diganti
    update(data_ganti,pk,pemasukan,pengeluaran,total,tanggal)
    #read_console()
if __name__ == "__main__":
    update_console()