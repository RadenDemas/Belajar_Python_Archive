#module package
#merupakan suatu tempat dimana kita dapat menyimpan program ataupun file external .py
#nantinya module package ini dapat dieksekusi di module utama
#hal yang perlu diperhatikan dalam penggunaan module package ini
#yaitu module package tersebut harus berada dalam satu folder, bukan folder package

import package.mtk
#     package module
from package import kimia
#    package        module
from package.fisika import gaya
#   package  module     program variabel 

tambahan = package.mtk.tambah(1,2,3,4,5)
print(f"\nhasil = {tambahan} ")

mol = kimia.mol(180,18)
print(f"\nhasil = {mol}")

gaya_fisika = gaya(5,8)
print(f"\nhasil = {gaya_fisika}")

#dapat dilihat diatas, kita dapat mengimport suatu package
#dengan cara yang berbeda beda
#tiap jenis mengimport suatu package dapat mempermudah saat pengambilan module
#atau disisi lain dapat memastikan program variabel berasal dari module mana