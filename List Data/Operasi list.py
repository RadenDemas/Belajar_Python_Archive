data_angka = [1,4,2,5,6,3,6,2,3,6,0,6,9,4,1,2,8,2,2,3]
data_nama = ["demas","rifki", "syahrul", "ajef", "waldi"]

#Counting, menghitung berapa banyak angka tertentu dalam suatu list
jumlah_data_1 = data_angka.count(1)
jumlah_data_2 = data_angka.count(2)
print(f"jumlah angka 1 pada list = {jumlah_data_1}")
print(f"jumlah angka 2 pada list = {jumlah_data_2}")

print("\n")
#mengambil/melihat posisi objek pada list (index)
posisi_demas = data_nama.index("demas")
posisi_ajef = data_nama.index("ajef")
print(f"posisi demas pada list = {posisi_demas}")
print(f"posisi ajef pada list = {posisi_ajef}")

print("\n")
#mengurutkan list secara teratur (mulai paling kecil)
print(f"data angka sebelum disort = \n{data_angka}")
data_angka.sort()
print(f"data angka setelah disort = \n{data_angka}")
print(f"data angka sebelum disort = \n{data_angka}")
data_nama.sort()
print(f"data nama setelah disort = \n{data_nama}")

print("\n")
#mengurutkan list secara terbalik (mulai paling besar)
print(f"data angka sebelum direverse = \n{data_angka}")
data_angka.reverse()
print(f"data angka setelah direverse = \n{data_angka}")
print(f"data nama sebelum direverse = \n{data_nama}")
data_nama.reverse()
print(f"data nama setelah direvers = \n{data_nama})")