from mtk import tambah as tbh
from mtk import kurang as kur
from mtk import kali as x
from mtk import pangkat as pngkt

pertambahan = tbh(2,4,5)
pengurangan = kur(-20,5,3)
perkalian = x(5,2,3)
perpangkatan = pngkt(2)(5) #<- 2 merupakan argument fungsi dan 5 merupakan argument lambda
print(pertambahan)
print(pengurangan)
print(perkalian)
print(perpangkatan)

#pada penggunaan module alias ini
#berguna untuk kita menyederhanakan suatu data variabel
#agar kita mudah mengingat
