#ini merupakan file module utama yang kedua
#pada modul utama yang kedua ini kita akan mencoba untuk membuat
#seluruh package pada modul dapat diakses dengan mudah

from package import *

#tanda bintang itu dapat diartikan all (semuanya)
#jadi maksud diatas;
#untuk folder package mengimport semua module

#kemudian pada file init juga kita perlu mengimport seluruh program program
#yang terdapat pada modul modul didalam pacage

hasil_tambah = mtk.tambah(1,2,3,4,5)
print(hasil_tambah)

#pada saat penulisan, kita tidak perlu untuk menulis kan folder package
#karena akan secara otomatis masuk kedalam code, dan kita hanya perlu menulis file modul dan program
