data_dict = {
    "mtk":"matematika",
    "bio":"biologi",
    "sb":"seni budaya"
}
print(data_dict)
# Melihat panjang data dictionary
#Jika pada data list panjang suatu data dihitung tiap index
#Pada data dict, panjang dihitung setiap satu key dan value
lendict= len(data_dict)
print(f"panjang data dict: {lendict}")

#Mengecek ada nya suatu key
key_1 = "mtk"
key_2 = "pkn"
mengecek_key_1 = key_1 in data_dict
print(f"apakah {key_1} ada: {mengecek_key_1}")
mengecek_key_2 = key_2 in data_dict
print(f"apakah {key_2} ada: {mengecek_key_2}")

#mengakses value dengan menggunakan get
#jika kita mengakses value dengan cara biasa
#maka jika objek tidak ada maka program akan error
#sebaliknya jika kita menggunakan get
#maka program akan menunjukan bahwa objek tersebut tidak ada
print("\n", "Mengakses Value".center(15,"="))
print(data_dict["mtk"])

print(data_dict.get("mtk"))
print(data_dict.get("pkn"))

#Menambah/mengupdate suatu data dictionary
#pada data dict dapat mengubah suatu objek dengan cara
#menuliskan terlebih dahulu key yang sudah ditentukan
#dan untuk menambah suatu objek hanya perlu mengisi key dan value
print("\n", "Update Data Dict".center(15,"="), "\n")
data_dict['mtk'] = "math"
print(data_dict)

data_dict["pjok"] = ["olahraga"]
print(data_dict)

data_dict.update({"mtk":"matematika"})
print(data_dict)

data_dict.update({"pkn":"pendidikan negara"})
print(data_dict)
#untuk menambah/mengupdate suatu data dictionary dapat menggunakan data.update
#untuk eksekusinya kurang lebih akan sama seperti pada biasa nya

#Menghapus objek pada data dictionary
#untuk mengahpus objek pada data dictionary hanya diperlukan key saja
print("\n", "Menghapus Data Dict".center(15,"="), "\n")
del data_dict["pkn"]
print(data_dict)