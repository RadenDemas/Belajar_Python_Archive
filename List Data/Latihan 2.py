#membuat program sederhana memasukkan list peserta lomba
list_peserta =[]


while True:
    print("Masukkan data data dibawah!")
    nama_peserta = input("Nama \t: ")
    no_peserta = input("Nomor Peserta \t:")
    umur_peserta = input("Umur \t: ")

    data_peserta = [nama_peserta, no_peserta, umur_peserta]
    list_peserta.append(data_peserta)
    
    print("\n", "List Peserta".center(20,"="))
    for index,data in enumerate(list_peserta):

        print(f"No : {index+1}, Nama : {data[0]}, Nomor Peserta : {data[1]}")

        print("\n", "=".center(19,"="))

    lanjutkan = input("Apakah masih ada peserta : (y/n)")
    if lanjutkan=="n":
        break