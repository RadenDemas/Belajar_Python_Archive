print(f''' Apakah yang dicari? (Tolong jawab dengan nomor yang tertera menggunakan huruf)
1. Perubahan titik didih (satu)
2. Mencari titik didih larutan (dua)
3. Mencari titik didih pelarut (tiga)
4. Mencari Kb larutan (empat)
5. Mencari mol (lima)
6. Mencari gram (enam)
7. Mencari Volume (tujuh)
''')

pilih = (input("Tolong piliah salah satu yang diatas : "))
#pertanyaan pertama
if pilih== "satu" or pilih == "1" :
    pertanyaan = input("Apakah ada nilai Tb larutan dan pelarut? ")
    if pertanyaan=="ya":
        Tb_larutan = float(input("Berapakah nilai Tb larutan? "))
        Tb_pelarut = float(input("Berapakah nilai Tb pelarut? "))
        hasil = Tb_larutan - Tb_pelarut
        print(f"{Tb_pelarut} - {Tb_larutan} = {hasil:.05f}")
    else:
        Kb = float(input("Berapakah nilai Kb larutan? "))
        Mol = float(input("Berapakah mol larutan tersebut? "))
        hasil = Kb * Mol
        if Mol == 0:
            gram = float(input("Berapakah gram zat pelarut? "))
            Mr = float(input("Berapakah Mr zat pelarut? "))
            Volume = float(input("Berapakah  Volume larutan? "))
            Mol = (gram/Mr)*(1000/Volume)
            hasil = Kb * Mol
        print(f"{Kb} x {Mol} = {hasil:.05f}")

#pertanyaa kedua
elif pilih==("dua") or pilih == "2" :
    Kb = float(input("Berapakah nilai Kb larutan? "))
    Mol = float(input("Berapakah mol larutan tersebut? "))
    perubahan_titik_didih = Kb * Mol
    pembatas = (f"{perubahan_titik_didih:0.5f}")
    if Mol < 0.000000000000000000000000000000000000000000000000000000000000001:
        gram = float(input("Berapakah gram zat pelarut? "))
        Mr = float(input("Berapakah Mr zat pelarut? "))
        Volume = float(input("Berapakah  Volume larutan? "))
        Mol = (gram/Mr)*(1000/Volume)
        perubahan_titik_didih = Kb * Mol
        pembatas = (f"{perubahan_titik_didih:0.5f}")
    print(f"{Kb} x {Mol} = {pembatas}")
    Tb_pelarut = float(input("Berapakah nilai Tb pelarut nya? "))
    hasil = perubahan_titik_didih + Tb_pelarut
    print (f"{pembatas} + {Tb_pelarut} = {hasil}")

#pertanyaan ketiga
elif pilih==("tiga") or pilih == "3":
    Kb = float(input("Berapakah nilai Kb larutan? "))
    Mol = float(input("Berapakah mol larutan tersebut? "))
    perubahan_titik_didih = Kb * Mol
    pembatas = (f"{perubahan_titik_didih:0.5f}")
    if Mol < 0.000000000000000000000000000000000000000000000000000000000000001:
        gram = float(input("Berapakah gram zat pelarut? "))
        Mr = float(input("Berapakah Mr zat pelarut? "))
        Volume = float(input("Berapakah  Volume larutan? "))
        Mol = (gram/Mr)*(1000/Volume)
        perubahan_titik_didih = Kb * Mol
        pembatas = (f"{perubahan_titik_didih:0.5f}")
    print(f"{Kb} x {Mol} = {pembatas}")
    Tb_larutan = float(input("Berapakah nilai Tb larutan nya? "))
    hasil = perubahan_titik_didih + Tb_larutan
    print (f"{pembatas} + {Tb_larutan} = {hasil}")

#pertanyaan keempat
elif pilih==("empat") or pilih=="4":
    Tb_larutan = float(input("Berapakah nilai Tb larutan? "))
    Tb_pelarut = float(input("Berapakah niali Tb pelarut? "))
    Perbuahan_titik_didih = Tb_larutan - Tb_pelarut
    print(f"{Tb_larutan} - {Tb_pelarut} = {Perbuahan_titik_didih}")
    Mol = float(input("Berapakah nilai Mol larutan? "))
    if Mol < 0.000000000000000000000000000000000000000000000000000000000000001:
        gram = float(input("Berapakah gram zat pelarut? "))
        Mr = float(input("Berapakah Mr zat pelarut? "))
        Volume = float(input("Berapakah  Volume larutan? "))
        Mol = (gram/Mr)*(1000/Volume)
    hasil = Perbuahan_titik_didih / Mol
    pembatas = (f"{hasil:.05f}")
    print(f"{Perbuahan_titik_didih} : {Mol} = {pembatas}")

#pertanyaan kelima
elif pilih==("lima") or pilih=="5":
    Tb_larutan = float(input("Berapakah nilai Tb larutan? "))
    Tb_pelarut = float(input("Berapakah niali Tb pelarut? "))
    perubahan_titik_didih = Tb_larutan - Tb_pelarut
    pembatas_1 = (f"{perubahan_titik_didih:.05f}")
    print(f"{Tb_larutan} - {Tb_pelarut} = {pembatas_1}")
    Kb = float(input("Berapakah nilai Kb? "))
    hasil = perubahan_titik_didih / Kb
    pembatas_2 = (f'{hasil:.05f}')
    print (f"{pembatas_1} : {Kb} = {pembatas_2}")

#pertanyaan keenam
elif pilih==("enam") or pilih=="6":
    Tb_larutan = float(input("Berapakah nilai Tb larutan? "))
    Tb_pelarut = float(input("Berapakah niali Tb pelarut? "))
    perubahan_titik_didih = Tb_larutan - Tb_pelarut
    pembatas_1 = (f"{perubahan_titik_didih:.05f}")
    print(f"{Tb_larutan} - {Tb_pelarut} = {pembatas_1}")
    Kb = float(input("Berapakah nilai Kb? "))
    Mr = float(input("Berapakah nilai Mr pelarut? "))
    Volume  = float(input("Berapakah Volume larutan? "))
    hasil_perubahan = perubahan_titik_didih / Kb
    mencari_gram = hasil_perubahan*(Mr/(1000/Volume))
    print(mencari_gram)

#pertanyaan ketujuh
elif pilih==("tujuh") or pilih=="7":
    Tb_larutan = float(input("Berapakah nilai Tb larutan? "))
    Tb_pelarut = float(input("Berapakah niali Tb pelarut? "))
    perubahan_titik_didih = Tb_larutan - Tb_pelarut
    pembatas_1 = (f"{perubahan_titik_didih:.05f}")
    print(f"{Tb_larutan} - {Tb_pelarut} = {pembatas_1}")
    Kb = float(input("Berapakah nilai Kb? "))
    Mr = float(input("Berapakah nilai Mr pelarut? "))
    gram  = float(input("Berapakah Gram pelarut? "))
    hasil_perubahan = perubahan_titik_didih / Kb
    mencari_volume = (hasil_perubahan/1000)*(gram/Mr)
    print(mencari_volume)

else:
    print("Coba baca lagi yang bener!!")