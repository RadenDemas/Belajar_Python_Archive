""" from operasi import DATABASE,string,random,template,time        
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

print(len(data['key'])) #6
print(len(data['pendapatan'])) #255
print(len(data['pengeluaran'])) #255
print(len(data['total'])) #255
print(len(data['tanggal'])) #14
            
        #print
seluruh_data = f'{data["key"]},{data["pendapatan"]},{data["pengeluaran"]},{data["total"]},{data["tanggal"]}'
print(len(seluruh_data)) """

nama = "demas"
nama_tambah = "a"
with open("file.txt","r+", encoding="utf-8") as file:
        file.seek(9) 
        #baris awal = 0
        #baris kedua = panjang baris awal + 2
        #maksud nya yang pertama itu garis baru dan satu lagi untuk masuk ke barisan awal (0)
        file.write(f"{'poeh':.16}")
""" with open("file.txt","a", encoding="utf-8") as file:
        file.write("\n"+f"{'wengi':.16}") """