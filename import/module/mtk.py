def tambah(*data):
    bilangan = 0
    for hasil in data:
        bilangan += hasil
    return bilangan

def kurang(*data):
    bilangan = 0
    for hasil in data:
        bilangan -= hasil
    return bilangan

def kali(*data):
    bilangan = 1
    for hasil in data:
        bilangan *= hasil
    return bilangan

def bagi(*data):
    bilangan = 1
    for hasil in data:
        bilangan /= hasil
    return bilangan

def pangkat(pangkat):
    return lambda x:x**pangkat
