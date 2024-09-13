data_pelajaran = {
    "mtk" : "matematika",
    "bio" : "biologi",
    "sb" : "seni budaya",
}

mata_pelajaran = data_pelajaran.copy()
mata_pelajaran_not_copy = data_pelajaran

print(f"data asli : \n{data_pelajaran}")
print(f"data not copy : \n{mata_pelajaran_not_copy}")
print(f"data copy : \n{mata_pelajaran}")

#Melihat adresss data dict asli, not copy, dan copy
print("\n", "Adress".center(20,"="))

print(f"adrees asli : {hex(id(data_pelajaran))}")
print(f"adrees not copy : {hex(id(mata_pelajaran_not_copy))}")
print(f"adrees copy : {hex(id(mata_pelajaran))}")
print("data asli: ", hex(id(data_pelajaran["mtk"])))
print("data not copy: ",hex(id(mata_pelajaran_not_copy["mtk"])))
print("data copy: ",hex(id(mata_pelajaran["mtk"])))

#data dilihat pada address data asli dan not copy memiliki address yang sama
#sedangkan address pada data copy memiliki address yang berbeda
#kemudian pada address tiap tiap objek memiliki adrdress yang sama
#dapat disimpulkan bahwa data dict copy memiliki kemiripan seperti data list copy

#mengupdate data dict asli dan copy
print("\n", "Update".center(20,"="))

data_pelajaran["mtk"] = "math"
mata_pelajaran["bio"] = "biology"

print(f"data asli : \n{data_pelajaran}")
print(f"data not copy : \n{mata_pelajaran_not_copy}")
print(f"data copy : \n{mata_pelajaran}")

#dapat dilihat pada hasil menunjukkan bahwa
#data asli dan not copy saling melakukan update ketika data asli diupdate sedangkan data copy tidak
#ini dikarenakan address data asli dan not copy sama sedangkan data copy beda
#sebaliknya ketika data copy diupdate, hanya data cope saja yang terupdate
#ini karenaka kita hanya mengupdate pada data satu address

#Pop atau menghilangkan adata
print("\n", "Pop".center(20,"="))

data_pelajaran.pop("bio")
print(f"data asli : \n{data_pelajaran}")
print(f"data not copy : \n{mata_pelajaran_not_copy}")
print(f"data copy : \n{mata_pelajaran}")

#untuk menghilangkan suatu objek
#kita hanya perlu menuliskan key nya saja pada kurung pop

print("\n")

mata_pelajaran.popitem()
print(f"data asli : \n{data_pelajaran}")
print(f"data not copy : \n{mata_pelajaran_not_copy}")
print(f"data copy : \n{mata_pelajaran}")

#untuk menghilagkan objek terakhir
#kita hanya perlu menuliskan .popitem()
#maka objek paling terakhir akan dihapus