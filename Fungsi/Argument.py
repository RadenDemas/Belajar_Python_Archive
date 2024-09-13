#fungsi dengan argument
#argument disini dapat berarti input

#template fungsi dengan argument

#def nama_fungsi(argument/parameter/input):
    #badan fungsi

#pada bagian parameter dapat diisi apa saja, dan untuk menambahkan data input gunakan tanda koma(,)

def halo(nama):
    print(f"halo wahai {nama}")

halo("demas")

#jadi pada tanda kurung pada eksekusi halo merupakan input yang akan kita isi
#kemudian data input tersebut masuk kedalam (nama) yang kemudian akan dieksekusi pada badan fungsi

def tambahan(angka1,angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambahan(10,5)

#pada data input disebutkan (angka1,angka2)
#pada tanda kurung yang akan dieksekusi dapat diartikan menjadi
#data_eksekusi(angka1,angka2)
#kemudian data input tersebut akan masuk kedalam program yang berada di dalam badan fungsi

def istri(list_waifu):
    daftar_waifu = list_waifu.copy()
    for waifu in daftar_waifu:
        print(f"halo wahai {waifu} ku tercinta")

nama_waifu = ["chino", "maya", "megu"]

istri(nama_waifu)

#pada data input disebutkan (data_list)
#pada data_list yang berada pada fungsi perlu mengambil data di luar badan fungsi
#oleh karena itu kita perlu membuat terlebih dahulu data_list_luar di luar badan fungsi
#kemudian setelah data_list_luar terbuat kita perlu membuat sebuah copy di dalam badan fungsi menggunakan data_list
#copy disini berguna agar ketika ada index yang ingin kita rubah, maka tidak akan terubah pada data_list_luar
#kemudian untuk mengeksekusi tiap tiap index
#kita perlu mengambil mengambilnya dari data variabel yang di badan fungsi
#kemudian kita dapat eksekusi menggunakan for loop

#template nya
#list_luar = (list)
#def nama_fungsi(list_dalam):
    #nama_variabel_data = list_dalam.copy()
    #for nama_loop in nama_variabel_data:
        #eksekusi yang kita inginkan
