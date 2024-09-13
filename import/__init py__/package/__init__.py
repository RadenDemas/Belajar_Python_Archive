from . import mtk
# titik (.) disini merupakan folder yang sedang kita gunakan
#disini kita ingin mengimport module mtk
#jadi maksud diatas adalah;
#untuk . (folder package) import module mtk

from .persegi import luas

#kita dapat langsung juga menghubungkan program secara langsung
#jadi maksud diatas;
#untuk folder pada package dengan modul persegi mengimport program luas

from .persegi_panjang import luas,keliling

#kita juga dapat menghubungkan banyak progra secara langsung
#ini disebut dengan chaining

from . import sub_package

from .sub_package import operasi_mtk



#__all__ = [
#    "mtk"
#]

#ketika kita menggunakan sistem import all
#kita tidak dapat menjalankan sistem import satu satu
#jika kita gunakan maka file akan error