#fungsi return (kembalian)
#fungsi return ini dimaksud kan untuk dikembalikan kepada data nama_fungsi
#dalam matematika kita sering menemukan dengan fungsi y = f(x) = x .... 
#y merupakan data yang akan mengeksekusi fungsi, 
#f(x) disini merupakan data nama_fungsi dan,
#x disini merupakan badan fungsi

#lalu apa yang dimaksud dengan return?
#maksud rentrun disini yaitu ketika fungsi f(x) ini telah mengeksekusi x yang berada di badan fungsi
#setelah itu hasil nya dikembali ke y

def kuadrat(input_angka):
    outputkuadrat = input_angka**2 + 1
    return outputkuadrat

y = kuadrat(2)
print(y)

#Kalau kita simpulkan pada program diatas, dapat dinyatakan
#f(x) = x^2 + 1
#y = f(2)
#f(2) = 2^2 +1 =5
#y = f(2) = 5

def operasi_aritmatika(bilangan_1,bilangan_2):
    tambah = bilangan_1 + bilangan_2
    kurang = bilangan_1 - bilangan_2
    kali = bilangan_1 * bilangan_2
    bagi = bilangan_1 / bilangan_2
    return tambah, kurang, kali, bagi

fungsi_x = operasi_aritmatika(3,2)
print(fungsi_x)

ta,ku,ka,ba = operasi_aritmatika(3,2)
print(f"hasil tambah = {ta} ")
print(f"hasil kurang = {ku}")
print(f"hasil kali = {ka}")
print(f"hasil bagi = {ba}")

#kalau kita nyatakan program diatas kedalam operai matematika
#f(x1,x2), dimana f(x1,x2) terdiri atas
#1. tambah = x1 + x2
#2. kurang = x1 - x2
#3. kali = x1 . x2
#4. bagi = x1 / x2

#pada operasi diatas, terdapat 4 jenis operasi, yaitu tambah kurang dan kali
#y = f(x1,x2)
#y = f(3,2)
#setelah kita mengisi nilai x pada f(x), selanjut x akan dimasukkan kedalam tiap tiap operasi
#f(3,2) :
#1. f(3,2) = 3 + 2 = 5
#2. f(3,2) = 3 - 2 = 1
#3. f(3,2) = 3 . 2 = 6
#4. f(3,2) = 3 / 2 = 1.5
#y = f(3,2) = himpunan penyelesaian{5,1,6,1.5}

#pada fungsi return, kita dapat memanggil salah satu operasi yang kita inginkan
#misalkan jika kita memanggil no.1 tambah, maka hanya akan mengeksekusi fungsi tambahan

