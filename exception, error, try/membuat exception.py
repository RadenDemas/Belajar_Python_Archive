#cara membuat exception
#kita membutuhkan exception agar program yang kita ingin kan itu menjadi satu jalan
from numbers import Number


#contoh
""" def tambah(a,b):
    return a+b

print("a","b") """

#kita tidak ingin program kita dapat menambahkan string
#maka dari itu kita harus membuat exception
#exception disini kita hanya memperbolehkan menginput angka

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number): #(argument, data yang kita inginkan)
        raise "Input harus berupa angka"
    return a+b

print(tambah(5,5))
print(tambah("a",5))

#ketika kita membuat program khusus angka dengan exception
#ketika input menambahkan berupa string, program akan secara otomatis error
#ini berguna kita tidak ingin adanya kesalahan pada hasil ketika saat program dijalankan