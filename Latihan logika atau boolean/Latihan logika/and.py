#latihan gabungan area rentang dari angka
#contoh and atau kongjungsi (irisan)

#-----2+++++8-----
jawaban = float(input("Masukan nilai >2 dan <8 : "))

#-----2++++
jika_lebih = (jawaban > 2)
print("lebih dari 2 : ", jika_lebih)

#+++++8-----
jika_kurang = (jawaban < 8)
print("kurang dari 8 : ", jika_kurang)

#-----2+++++8-----
hasil = jika_kurang and jika_lebih
print("Maka jawaban nya : ", hasil)