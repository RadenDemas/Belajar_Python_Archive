data = input("Masukan data :")
print("data", data, ", Tipe data :", type(data))
#data yang keluar pasti string

#untuk mengubah string ke integer, input perlu dimasukan setelah int
data_int = int(input("masukan nilai: "))
print("Data :", data_int, ", Tipe data : ", type(data_int))

#untuk mengubah string ke float, input perlu dimasukan setelah float
data_float = float(input("masukan nilai desimal: "))
print("Data : ", data_float, ", Tipe data :", type(data_float))

#untuk input boolean tidak selalu true, diperlukan input int terlebih dahulu
#input akan menjadi true jika nilai > 0
#input akan menjadi false jika nilai = 0
data_bool = bool(int(input("Benar atau salah: ")))
print("Data :", data_bool, ", Tipe data :", type(data_bool))

#penggunaan nama data tidak perlu selalu mengggunakan data_data apa
Nilai = int(input("Berapa nilai nya: "))
print("Nilai nya adalah", Nilai)