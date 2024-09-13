#latihan gabungan area rentang dari angka
#contoh or atau Disjungsi inklusif (gabungan tidak lepas)


#+++++5----------9++++++
# maksudnya <5 atau >9

inputuser = float(input("masukan nilai <5 atau >9 : "))

#+++++5-----
jika_kurang = (inputuser < 5)
print("kurang dari 3 : ", jika_kurang)

#-----9+++++
jika_lebih = (inputuser > 9)
print("lebih dari tiga : ", jika_lebih)

#+++++5----------9++++++
hasil = jika_kurang or jika_lebih
print("maka jawaban nya adalah : ", hasil)