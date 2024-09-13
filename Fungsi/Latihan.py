import os

def header():
    """Fungsi Header"""
    print(f"{'PROGRAM MENCARI LUAS':^20}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^20}")
    print(f"{'-'*30:^20}")

def input_user():
    """Fungsi Input User"""
    panjang = float(input("Berapakah nilai panjang = "))
    lebar = float(input("Berapakah nilai lebar =  "))
    return panjang,lebar

def pemilihan():
    """Fungsi Pemilihan Kepada User"""
    print("""
    1. Mencari Luas
    2. Mencari Keliling
    """)

def rumus_luas(panjang,lebar):
    """Fungsi Rumus Luas"""
    hasil = panjang*lebar
    print(f"{hasil:.05f}")
    #return panjang*lebar

def rumus_keliling(panjang,lebar):
    """Fungsi Rumus Keliilng"""
    return 2*(panjang + lebar)

def display(value = ""):
    """Fungsi Display"""
    print(f"hasil = {value}")
    


while True:
    os.system("cls")
    header()
    pemilihan()
    pilih = input("Mana yang anda cari: ")

    if pilih == "1" or pilih == "satu":
        panjang,lebar = input_user()
        hasil = rumus_luas(panjang,lebar)
        display(hasil)

    elif pilih == "2" or pilih == "dua":
        panjang,lebar= input_user()
        hasil = rumus_keliling(lebar,panjang)
        display(hasil)

    else:
        print("Tolong Pilih Yang Benar")

    lanjut = input("Apakah masih dilanjut (y/n): ")
    if lanjut == "n":
        break
