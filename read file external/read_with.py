#sama hal seperti sebelumnya
#kita dapat membuka file txt namun dengan cara yang paling singkat dengan menggunakan with

with open("teks.txt", mode="r") as file: #as disini merupakan kita ingin menyebut si teks ini sebagai apa
    content = file.read()
    print(content)
print(f"apakah file ditutup = {file.closed}")

#jadi maksud diatas
#dengan membuka file teks.txt dengan mode read dengan sebagai file
#pada data variabel content kita membaca file yang merujuk pada file teks.txt

#dengan menggunakan with, kita tidak perlu menutup file txt lagi
#karena dengan with, kita hanya dapat mengakses file txt pada bagian isi with tersebut saja
#dengan itu ketika kita membuka file txt di luar with, maka file txt tidak akan terbaca