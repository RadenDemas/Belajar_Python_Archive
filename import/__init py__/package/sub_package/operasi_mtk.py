def tambah(*data):
    hasil = 0
    for angka in data:
        hasil += angka

    return hasil

def kurang(*data):
    hasil = 0
    for angka in data:
        hasil -= angka

    return hasil

def kali(*data):
    hasil = 1
    for angka in data:
        hasil *= angka

    return hasil

def pangkat(pangkat):
    return lambda x:x**pangkat