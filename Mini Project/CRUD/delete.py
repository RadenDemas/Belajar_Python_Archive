from .operasi1 import read_data,delete
from .read import read_console

def delete_console():
    read_console()
    while True:
        data_ganti = int(input("Silahkan pilih data yang akan diganti: "))
        info_data = read_data(index=data_ganti)
        
        if info_data: #dikarenakan fungsi tersebut berupa true(1), maka data pun dapat dieksekusi
            pass #while loop akan dihentikan secara paksa
        else: #dikarenakan sebelumnya fungsi dikembalikan menjadi false (0), maka else akan dieksekusi
            print("Nomor tidak valid")
        data_break = info_data.split(",") #jika tidak menggunakan split, database akan berupa string bukan berupa data dict
        pk = data_break[0]
        pemasukan = data_break[1]
        pengeluaran = data_break[2]
        total = data_break[3]
        tanggal  = data_break[4] #<- untuk menghapus \n diakhir barisan pada data.txt
        
        print("="*100)
        print(f"Pendapatan = {pemasukan}")
        print(f"Pengeluaran = {pengeluaran}")
        print(f"total = {total}")
        print(f"tanggal = {tanggal}")
        print("="*100)
        
        berakhir = input("Apakah data yang ingin diganti sudah benar (y/n): ")
        if berakhir == "y" or berakhir == 'Y': 
            break
        
    delete(data_ganti)
    
if __name__ == "__main__":
    delete_console()