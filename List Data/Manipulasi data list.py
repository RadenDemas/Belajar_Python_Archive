#Index
#         0/-3     1/-2    2/-1
data = ["demas", "rifki", "syahrul"]
print(data)

#mengambil data dari list
data_pertama = data[0]
print(f"data pertama nya adalah = {data_pertama}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_tengah = data[1] #bisa menggunakan 1 atau -2
print(f"data tengah nya adalah = {data_tengah}")

#menghitung jumlah data pada list
panjang_data = len(data)
print(f"panjang data nya adalah = {panjang_data}")

#menambah item pada list sesuai posisi
print(f"sebelum data ditambah = {data}")

#untuk rumusnya
#data.insert(posisi_item)
#item adalah nama data yang akan ditambahkan
#posisi merupakan mau berada dimanakah item yang akan disimpan
data.insert(2,"ajef")
print(f"sesudah data ditambah = {data}")

#menambah data diakhir list
#menggunakan data.append(item)
data.append("reza")
print(f"data terakhir ditambah = {data}")

#menambahkan list baru kedalam list
#menggunakan list lama.extend(list baru)
data_baru = ["iqbal", "fauzan"]
data.extend(data_baru)
print(f"data yang ditambahkan list = {data}")

#merubah item data
#cara nya dengan nama list[posisi] = item baru
data[1] = "alya"
print(f"list kedua diganti menjadi = {data}")

#meremove/menghapus data
#menggunakan nama list.remove(item)
#syarat nya adalah nama item dengan nama yang ingin dihapus harus sama
data.remove("alya")
print(f"data yang menghilang = {data}")

#meremove/menghapus data paling terakhir
#cara nya hanya menggunakan nama list.pop
fauzan_menghilang = data.pop()
print(f"data terakhir menghilang = {data}")

#untuk mengetahui item apa yang hilang dapat dicek dengan menggunakan string yang digunakan
print(f"data yang menghilang = {fauzan_menghilang}")
