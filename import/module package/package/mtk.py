def tambah(*data):
    bilangan = 0
    for tambah in data:
        bilangan += tambah

    return bilangan

def kali(*data):
    bilangan = 0
    for kali in data:
        bilangan *= kali

    return bilangan

def pangkat(pangkat):
    return lambda x:x**pangkat

