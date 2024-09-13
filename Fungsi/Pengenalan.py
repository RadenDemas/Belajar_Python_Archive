#pengenalan fungsi
#fungsi dalam python digunakan untuk menyederhanakan suatu program
#fungsi biasa nya dinyatakan menggunakan def

#penulisan program secara biasa
print("biasa".center(20,"="))

print("hello world")
print("hello world")
print("hello world")

#penulisan program menggunakan fungsi
print("fungsi".center(20,"="))
def hellow_world():
    print("hello world")

hellow_world()
hellow_world()
hellow_world()

#dalam fungsi, kita dapat menyimpan berbagai program dalam satu baris fungsi
print("\n")
def halo():
    print("hello demas")
    print("welcome to python")
    print("press start to play")

halo()

#kita tidak dapat menjalankan fungsi sebelum kita membuat program fungsi
print("\n")
#selamat_datang()

def selamat_datang():
    print("selamat datang")
    print("silahkan bersantai terlebih dahulu")