#exception merupakan istilah ketika program tidak memiliki error
#namun pada saat runtime terjadi error

#angka = 0
#hasil = 5/angka
#print(hasil)

#contoh di atas merupakan salah satu jenis exception
#dimana 5 tidak dapat dibagi dengan 0

#untuk menghindari ini agar program tetap terus berjalan
#kita harus menggunakan try dan error

#angka = int(input("berapa angka tersebut :"))

""" try:
    hasil = 5/angka
    print(hasil)
except:
    print(f"hasil tidak dapat dibagi") """

#contoh ketika membuat sebuah program aplikasi
#contoh 1
""" while True:
    angka = int(input("Berapa angka tersebut: "))
    try:
        hasil = 5/angka
        print(f"hasil = {hasil}")
    except:
        print("hasil tidak dapat dibagi")
    lanjut = input("apakah akan lanjut (y/n): ")
    if lanjut == "n":
        break """

#contoh 2
try:
    with open("data.txt","r") as file:
        print(file.read())
except:
    print("file txt tidak ditemukan \nmembuat data baru .....")
    with open("data.txt","w",encoding="utf-8") as file:
        file.write("ini adalah data baru")