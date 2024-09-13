##membaca sebuah teks file txt pada python
file = open("teks.txt", mode="r")
#mode = "r" -> read
#mode = "w" -> write
#bila kita mengobah mode menjadi write
#secara otomatis seluruh tulisan file pada txt akan terhapus

#untuk mengecek apakah file txt tersebut dapat dibaca atau ditulis
print(f"status file = {file.readable()}")
print(f"status file = {file.writable()}")


#membaca seluruh file (read)
#print(file.read())
#file akan secara otomatis akan membaca seluruh teks pada file


#membaca perbaris (readline)
#print(file.readline(), end="")
#print(file.readline(), end ="")

#secara otomatis ketika kita membuka pada baris pertama
#maka ketika kita mengeprint file selanjutnya
#akan secara otomatis akan membuka pada baris kedua
#dan secara akan otomatis akan memberikan "\n" pada setiap akhir barisan
#untuk menghilangkan "\n" pada akhir barisan
#caranya dengan end="", string harus kosong jika ingin menghilangkan "\n"
#namun kita juga dapat menambahkan apapun yang ingin kita tambahkan

#mengubah menjadi bentuk data list 
print(file.readlines())
#file akan secara otomatis mengubah file teks string menjadi data list

#untuk diingat setiap kita membuka file txt kita harus selalu menutup nya kembali
#kenapa harus ditutup? agar tidak terjadi error ketika kita membuka kembali

print(f"apakah file ditutup = {file.closed}")
file.close()
print(f"apakah file ditutup = {file.closed}")