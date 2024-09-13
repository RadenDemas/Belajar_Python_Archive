from mtk import tambah,kurang,kali,pangkat
#pada penggunaan import ini, kita dapat memasukkan program yang ingin kita masukkan
#namun kita dapat menambahkan semua program dengan menggunakan tanda *
from mtk import *
#namun ada kekurangan pada penggunaan penambahan semua program ini
#yaitu kita tidak tahu dari mana program itu berasa
#jika kita menggunakan banyak module

pertambahan = tambah(2,4,5)
pengurangan = kurang(-20,5,3)
perkalian = kali(5,2,3)
perpangkatan = pangkat(2)(5) #<- 2 merupakan argument fungsi dan 5 merupakan argument lambda
print(pertambahan)
print(pengurangan)
print(perkalian)
print(perpangkatan)

#jika kita menggunakan module from
#kita tidak memerlukan nama dari module external tersebut
#kita dapat menjalankan program dengan hanya menggunakan program variabel nya saja
