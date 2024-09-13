    ### Format String
    #Format string merupakan suatu command untuk membuat semua assigement menjadi format yang berbentuk string

    #contoh
nama = "pipit"
data = "nama dia " + nama
print("",data + ", dan tipe tipe data :  ", type(data))

format = f"nama dia {nama}, dan tipe data : "
print("\n",format, type(format))

    ##angka
    #merubah integer menjadi string
angka = 2004
format = f"angkanya : {angka}, dan bertipe :"
print("\n", format, type(format))

    ##boolean
    #mengubah boolean menjadi string
bool = True
format = f"true atau false : {bool}, dan bertipe"
print("\n", format, type(format))

    ##bilangan bulat
    #mengubah bilangan bulat yang berbentuk integer menjadi string
    #tidak dapat mengubah float menjadi string
bilangan = -15
format = f"berapa angka bilangan : {bilangan:d}"
print ("\n", format, type(format))

    ##desimal
    #mengubah bilangan desimal yang berbentuk float dan int menjadi string
    #dan dapat menentukan berapa banyak angka dibelakang koma yang dibutuhkan
desimal = 15.56732
format = f"berapa angka desimal : {desimal:.1f}" 
print("\n", format, type(format))
#gunakan . dan berapa banyak angka dibelakang koma yang diinginkan
#pembulatan nya akan diturunkan ke atas

    ##Memberikan titik sebagai penanda ribuan
    #Gunakan koma (,) sebagai penanda nya
    #jika menggunakan titik (.) akan error
harga = 20000
format = f"Rp {harga:,}"
print("\n", format, type(format))

    ##Leading zero
    #untuk memberi batas berapa banyak karakter yang diinginkan
    #untuk sisa karakter yang tersisa akan dijadikan space
desimal = 15.56732
format = f"berapa angka desimal : {desimal:05.1f}" 
print("\n", format, type(format))
'''
penandaan leading zero ditandai dengan
1. titik dua didepan angka real untuk menentukan berapa banyak batas
2. jika dibelakang angka real kosong, maka hanya akan menyimpan space
3. jika dibelakang angka real ada angka 0, maka sisa batas yang tersisa akan
digunakan oleh 0
'''

    ##Menampilkan tanda negative dan positive
angka_plus = 13
angka_minus = -15

format_plus = f"Angka : {angka_plus:+d}"
format_minus = f"Angka : {angka_minus:+d}"

print( "\n",format_plus + " dan " + format_minus)

    ##Memformat persentase  (%)
    #Mengubah angka desimal menjadi persen
persentase = 0.1525
format = f"Berapa persen : {persentase:.2%}"
print("\n" , format , type(persentase))
#gunakan titik belakang persen untuk memberikan batas angka

    ## Operasi Aritmatika sederhana
harga = 5000
jumlah = 15
total = f"Gatot : Rp. {harga*jumlah:,}"
print("\n", total, type(total))

    ##Mengatur lebar
    #Digunakan untuk mengatur jarak tiap data
nama = "Raden Demas"
kelas = "XII IPA 4"
data = f'''
Nama : {nama:>12}
Nama : {nama}
Kelas : {kelas:>11}
Kelas : {kelas}
'''
print(data,type(data))

    ##Format menjadi binary, octal, dan hex

angka = int(format(255, 0))

#format_binary = f"Binary : {bin(angka)}"
#format_octal = f"Octal : {oct(angka)}"
format_hex = f"Hex : {hex(angka)}"

#print("\n",format_binary, type(format_binary))
#print(format_octal, type(format_octal))
print(format_hex, type(format_hex))

