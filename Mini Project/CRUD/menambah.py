from .operasi1 import read_data, DATABASE, template,random,time,string
from .read import read_console
#from read import read_console

def create_console():
    with open(DATABASE,mode="a", encoding="utf-8") as file:
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
        file.write(seluruh_data+'\n')
    
    print("Data baru telah ditambahkan, menampilkan data baru....")
    read_console()

if __name__ == "__main__":
    create_console()
    #read_data()