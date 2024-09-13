import os

def pemilihan():
    """"Fungsi Pemilihan Kepada User"""
    print("""
Pemilihan persoalan yang akan dicari:
1. Perubahan titik didih (satu)
2. Mencari titik didih larutan (dua)
3. Mencari titik didih pelarut (tiga)
4. Mencari Kb larutan (empat)
5. Mencari mol (lima)
6. Mencari gram (enam)
7. Mencari Volume (tujuh)
Syarat Syarat:
    - Tolong jawab dengan nomor yang tertera menggunakan huruf)
    - Jika suatu nilai tidak diketahui, tolong jawab 0 saja
    """)

def header():
    """""Fungsi Header"""

    print(f"{'PROGRAM KENAIKAN TITIK DIDIH':^40}")
    print(f"{'-'*40}")

#Rumus rumus
def perubahan_suhu():
    """""Mencari perubahan suhu jika diketahui tb larutan dan tb pelarut"""
    pertanyaan = input("Apakah diketahui nilai tb pelarut dan larutan (y/n): ")
    if pertanyaan == "y":
        tb_pelarut = float(input("Berapakah tb pelarut: "))
        tb_larutan = float(input("Berapakah tb larutan: "))
        hasil = tb_pelarut - tb_larutan
        print(f"{tb_pelarut} - {tb_larutan} = {hasil:.5f}")
    else:
        mencari_purbahan_suhu()

def mencari_purbahan_suhu():
    """Mencari perubahan titik didih"""
    kb = float(input("Berapakah nilai kb: "))
    mol = float(input("Berapakah nilai mol: "))
    if mol == 0:
        nilai_mol = mencari_mol()
        hasil = kb * nilai_mol
        print(f"{kb} x {nilai_mol} = {hasil:.05f}")
        return hasil
    else:
        hasil = kb*mol
        print(f"{kb} x {mol} = {hasil:.05f}")
        return hasil
    
def mencari_mol():
    """Mencari nilai mol pada suatu zat dengan diketahui nya gram, mr, dan volume"""
    gr = float(input("Berapakah gram zat pelarut: "))
    mr = float(input("Berapakah mr zat pelarut: "))
    vol = float(input("Berapakah nilai volume larutan: "))
    hasil = (gr/mr)*(1000/vol)
    return hasil

def mencari_tb_larutan():
    pertanyaan = input("Apakah diketahui perubahan titik didih (y/n): ")
    print("\n")
    if pertanyaan == "y":
        perubahan_suhu = float(input("Berapakah nilai perubahan titik didih: "))
        tb_pelarut = float(input("Berapakah niali tb pelarut: "))
        hasil = perubahan_suhu + tb_pelarut
        print(f"{perubahan_suhu} + {tb_pelarut} = {hasil:.05f}")
    else:
        nilai_perubahan_suhu = mencari_purbahan_suhu()
        tb_pelarut = float(input("Berapakah niali tb pelarut: "))
        hasil = nilai_perubahan_suhu + tb_pelarut
        print(f"{nilai_perubahan_suhu} + {tb_pelarut} = {hasil:.05f}")

def mencari_tb_pelarut():
    pertanyaan = input("Apakah diketahui perubahan titik didih (y/n): ")
    print("\n")
    if pertanyaan == "y":
        perubahan_suhu = float(input("Berapakah nilai perubahan titik didih: "))
        tb_larutan = float(input("Berapakah niali tb larutan: "))
        hasil = perubahan_suhu + tb_larutan
        print(f"{perubahan_suhu} + {tb_larutan} = {hasil:.05f}")
    else:
        nilai_perubahan_suhu = mencari_purbahan_suhu()
        tb_larutan = float(input("Berapakah niali tb larutan: "))
        hasil = nilai_perubahan_suhu + tb_larutan
        print(f"{nilai_perubahan_suhu} + {tb_larutan} = {hasil:.05f}")

def mencari_kb():
    pertanyaan = input("Apakah diketahui nilai perubahan titik didih (y/n): ")
    if pertanyaan == "y":
        nilai_perubahan_suhu = float(input("Berapakah nilai perubahan titik didih: "))
        pertanyaan_2 = input("Apakah diketahui nilai mol (y/n): ")
        print("\n")
        if pertanyaan_2 == "y":
            nilai_mol = float(input("Berapakah nilai mol"))
            hasil = nilai_perubahan_suhu/nilai_mol
            print (f"{nilai_perubahan_suhu} / {nilai_mol} = {hasil:.05f}")
        else:
            nilai_mol = mencari_mol()
            hasil = nilai_perubahan_suhu/nilai_mol
            print (f"{nilai_perubahan_suhu} / {nilai_mol} = {hasil:.05f}")
    else:
        tb_pelarut = float(input("Berapakah tb pelarut: "))
        tb_larutan = float(input("Berapakah tb larutan: "))
        nilai_perubahan_suhu = tb_pelarut - tb_larutan
        print(f"{tb_pelarut} - {tb_larutan} = {nilai_perubahan_suhu:.5f}")
        print("\n")
        pertanyaan_2 = input("Apakah diketahui nilai mol (y\n): ")
        if pertanyaan_2 == "y":
            nilai_mol = float(input("Berapakah nilai mol"))
            hasil = nilai_perubahan_suhu/nilai_mol
            print (f"{nilai_perubahan_suhu} / {nilai_mol} = {hasil:.05f}")
        else:
            nilai_mol = mencari_mol()
            hasil = nilai_perubahan_suhu/nilai_mol
            print (f"{nilai_perubahan_suhu} / {nilai_mol} = {hasil:.05f}")

def mencari_mol_2():
    """"Mencari mol dengan diketahuinya nilai perubahan titik didih dan kb"""
    pertanyaan = input("Apakah diketahui nilai perubahan titik didih (y/n): ")
    if pertanyaan == "y":
        nilai_perubahan_suhu = float(input("Berapakah nilai perubahan titik didih: "))
        nilai_kb = float(input("Berapakah nilai Kb: "))
        hasil = nilai_perubahan_suhu/nilai_kb
        print(f"{nilai_perubahan_suhu} / {nilai_kb} = {hasil:.05f}")
    else:
        tb_pelarut = float(input("Berapakah tb pelarut: "))
        tb_larutan = float(input("Berapakah tb larutan: "))
        nilai_kb = float(input("Berapakah nilai Kb: "))
        nilai_perubahan_suhu = tb_pelarut - tb_larutan
        print(f"{tb_pelarut} - {tb_larutan} = {nilai_perubahan_suhu:.5f}")
        hasil = nilai_perubahan_suhu/nilai_kb
        print(f"{nilai_perubahan_suhu} / {nilai_kb} = {hasil:.05f}")

def mencari_gr():
    pertanyaan = input("Apakah diketahui nilai perubahan titik didih (y/n): ")
    if pertanyaan == "y":
        nilai_perubahan_suhu = float(input("Berapakah nilai perubahan titik didih: "))
        nilai_kb = float(input("Berapakah nilai Kb: "))
        nilai_mr = float(input("Berapakah nilai Mr: "))
        nilai_vol = float(input("Berapakah nilai Volume: "))
        hasil = (nilai_perubahan_suhu/nilai_kb) * nilai_mr * (nilai_vol/1000)
        print(f"({nilai_perubahan_suhu} / {nilai_kb}) x {nilai_mr} x ({nilai_vol}/1000) = {hasil:.05f}")
    else:
        tb_pelarut = float(input("Berapakah tb pelarut: "))
        tb_larutan = float(input("Berapakah tb larutan: "))
        nilai_perubahan_suhu = tb_pelarut - tb_larutan
        nilai_kb = float(input("Berapakah nilai Kb: "))
        nilai_mr = float(input("Berapakah nilai Mr: "))
        nilai_vol = float(input("Berapakah nilai Volume: "))
        hasil = (nilai_perubahan_suhu/nilai_kb) * nilai_mr * (nilai_vol/1000)
        print(f"{tb_pelarut} - {tb_larutan} = {nilai_perubahan_suhu:.5f}")
        print(f"({nilai_perubahan_suhu} / {nilai_kb}) x {nilai_mr} x ({nilai_vol}/1000) = {hasil:.05f}")

def mencari_vol():
    pertanyaan = input("Apakah diketahui nilai perubahan titik didih (y/n): ")
    if pertanyaan == "y":
        nilai_perubahan_suhu = float(input("Berapakah nilai perubahan titik didih: "))
        nilai_kb = float(input("Berapakah nilai Kb: "))
        nilai_mr = float(input("Berapakah nilai Mr: "))
        nilai_gr = float(input("Berapakah nilai gr: "))
        hasil = (nilai_kb/nilai_perubahan_suhu) * 1000 * (nilai_gr/nilai_mr)
        print(f"({nilai_kb}/{nilai_perubahan_suhu}) * 1000 * ({nilai_gr/nilai_mr}) = {hasil:.05f}")
    else:
        tb_pelarut = float(input("Berapakah tb pelarut: "))
        tb_larutan = float(input("Berapakah tb larutan: "))
        nilai_perubahan_suhu = tb_pelarut - tb_larutan
        nilai_kb = float(input("Berapakah nilai Kb: "))
        nilai_mr = float(input("Berapakah nilai Mr: "))
        nilai_gr = float(input("Berapakah nilai gr: "))
        hasil = (nilai_kb/nilai_perubahan_suhu) * 1000 * (nilai_gr/nilai_mr)
        print(f"{tb_pelarut} - {tb_larutan} = {nilai_perubahan_suhu:.5f}")
        print(f"({nilai_kb}/{nilai_perubahan_suhu}) * 1000 * ({nilai_gr/nilai_mr}) = {hasil:.05f}")
    

#Program Inti

while True:
    os.system("cls")
    header()
    pemilihan()
    pilih = input("Apa yang anda cari? ")
    print("\n")
    if pilih == "1" or pilih == "satu":
        perubahan_suhu()
    elif pilih == "2" or pilih == "dua":
        mencari_tb_larutan()
    elif pilih == "3" or pilih == "tiga":
        mencari_tb_pelarut()
    elif pilih == "4" or pilih == "empat":
        mencari_kb()
    elif pilih == "5" or pilih == "lima":
        mencari_mol_2()
    elif pilih == "6" or pilih == "enam":
        mencari_gr()
    elif pilih == "7" or pilih == "tujuh":
        mencari_vol()
    else:
        print("Tolong isi sesuai syarat!")

    print("\n")
    lanjut = input("apakah akan lanjut(y/n): ")
    if lanjut == "n":
        break

print("Terimakasih telah menggunakan jasa kami ^_^")