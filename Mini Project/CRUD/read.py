from .operasi1 import read_data

def read_console():
    data_read = read_data()
    
    #header
    index = "No"
    pemasukan = "Pemasukan"
    pengeluaran = "Pengeluaran"
    total = "Total"
    tanggal = "Tanggal"

    print("\n" + "="*100)
    print(f"{index:4} | {pemasukan:16} | {pengeluaran:16} | {total:16} | {tanggal:8}")
    print("-"*100)

    #data
    for index,data in enumerate(data_read):
        data_break = data.split(",") #jika tidak menggunakan split, database akan berupa string bukan berupa data dict
        pk = data_break[0]
        pemasukan = data_break[1]
        pengeluaran = data_break[2]
        total = data_break[3]
        tanggal  = data_break[4]

        print(f"{index+1:<4} | {pemasukan:.16} | {pengeluaran:.16} | {total:.16} | {tanggal:<8}", end="")

    #footer
    print("\n" + "="*100)

if __name__ == "__main__":
    read_console()

