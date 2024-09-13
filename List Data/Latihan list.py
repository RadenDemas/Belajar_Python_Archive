#Membuat program sederhana list buku
list_buku = []

while True:
    print("masukkan data buku: ")
    Judul = input("Judul buku \t: ")
    Penulis = input("Penulis buku \t: ")

    data_buku = [Judul,Penulis]
    list_buku.append(data_buku)

    print("\n","LIST BUKU".center(20,"="))

    for index,buku in enumerate(list_buku):
        print(f"total: {index+1} | Judul: {buku[0]} | Penulis: {buku[1]}")
    
    print("\n","=".center(19,"="))

    pertanyaan = input("Apakah masih ada: (y/n)")
    if pertanyaan=="n":
        break