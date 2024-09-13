    ##Width and Multiline

    #Data umum
nama = "Raden Demas"
kelas = "XII IPA 4"
umur = "18 tahun"

    #String umum
print("Menyatukan string".center(20, "="))
data = f"Nama : {nama}, Kelas : {kelas}, Umur : {umur}"
print(data)

    #String multiline command /n
print("\n","MULTILINE \\n".center(20, "="))
data = f"Nama :{nama},\nKelas : {kelas}, \nUmur : {umur}"
print(data)

    #String multiline triplets
print("\n","MULTILINE TRIPLETS".center(20,"="))
data = f"""Nama : {nama}
Kelas : {kelas}
Umur : {umur}
"""
print(data)