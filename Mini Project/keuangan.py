import os
import CRUD as crud
def header():
    print("SELAMAT DATANG".center(100))
    print("ANDA SEKARANG SEDANG MENGAKSES".center(100))
    print("DATABASE KEUANGAN".center(100))
    print("="*100)
    print("""
        1. Read Data
        2. Create Data
        3. Update Data
        4. Delete
        """)

sistem_operasi = os.name


if __name__ == "__main__":
    header()
    match sistem_operasi:
        case "Posix": os.system("clear") #-> posix digunakan untuk linux dan kode nya clear untuk membersihkan data terminal
        case "nt": os.system("cls") #-> nt digunakan untuk windows dan kode nya clear untuk membersihkan data terminal
        #Mengecek database
    crud.init_console()

    while True:
        match sistem_operasi:
            case "Posix": os.system("clear") #-> posix digunakan untuk linux dan kode nya clear untuk membersihkan data terminal
            case "nt": os.system("cls") #-> nt digunakan untuk windows dan kode nya clear untuk membersihkan data terminal
        header()
        print("="*100)
        user_input = input("Masukan Opsi: ")

        match user_input:
            case "1" : crud.read_console()
            case "2" : crud.create_console()
            case "3" : crud.update_console()
            case "4" : crud.delete_console()
            case _: print("Permintaan yang diinginkan tidak vaild") #case _ -> digunakan bila input tidak sesuai yang diinginkan atau pada daftar, maka program akan selesai

        berakhir = input("Apakah sudah selesai (y/n)? ")

        if berakhir == "y" or berakhir == "Y":
            break