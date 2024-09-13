#latihan gabungan area rentang dari angka
#contoh or atau Disjungsi ekslusif (gabungan lepas)

#++++3----7++++
jawaban = float(input("masukan nilai <3 atau >7 : "))

#+++3-----
jika_kurang = (jawaban < 3)
print("kurang dari 3 :", jika_kurang)

#----7++++
jika_lebih = (jawaban > 7)
print("lebih dari 7 :", jika_lebih)

#++++3----7++++
hasil = jika_kurang ^ jika_lebih
print("Maka jawaban nya :  ", hasil)