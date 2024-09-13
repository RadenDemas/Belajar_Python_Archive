from operasi import DATABASE
from operasi import Membuat_database_pertama

def init_console():
    try:
        with open(DATABASE,mode="r") as file:
            print("Mengecek file...")
            content = file.read()
            print(content)
    except:
        with open(DATABASE,mode="w",encoding="utf-8") as file:
            print("Database tidak ditemukan, proses membuat database...")
            Membuat_database_pertama()
            print("Database telah dibuat")

if __name__ == "__main__":
    init_console()
