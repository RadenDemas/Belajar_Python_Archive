#__init__.py
#init merupakan suatu file yang haus ada pada suatu package
#fungsi dari file ini yaitu mengeksekusi ketika mengimport folder package
#jadi ketika kita mengimport folder tersebut
#file init akan otomatis tereksekusi terlebih dahulu

#import package

#hasil_mtk = package.mtk.tambah(1,2,3,4,5)
#print(hasil_mtk)

#jika kita mengimport package seperti biasa, maka package tidak memiliki modul
#ini dikarenakan module mtk masih belum terhubung ke dalam package

import package.mtk

hasil_mtk = package.mtk.tambah(1,2,3,4,5)
print(hasil_mtk)

#kita masih dapat mengeksekusi program tersebut dengan mengimport
#folder package bersamaan dengan module nya
#namun, jika dengan cara ini, maka ketika kita memiliki banyak sub package
#maka code untuk mengimport nya juga semakin panjang

#untuk mengatasi ini, maka dari itu kita harus menggunakan file init
#karena file init ini berjalan terlebih dahulu sebelum file module akan dijalankan

import package

hasil_mtk = package.mtk.tambah(1,2,3,4,5)
print(hasil_mtk)

luas_persegi = package.luas(5,5)
print(luas_persegi)
 
#pada saat penulisan code nya pada saat module program secara langsung terhubung dengan init
#nanti nya kita tidak perlu menuliskan file dari module tersebut
#kita hanya perlu menuliskan folder package bersama dengan program saja


luas_bangun_ruang = package.sub_package.bangun_ruang.luas_persegi_panjang(4,5)
print(luas_bangun_ruang)

hasil_tambah_2 = package.sub_package.tambah(5,15,20,10)
print(hasil_tambah_2)