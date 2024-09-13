#Penggunaan list ditandai dengan []

    #Kumpulan data angka
print("KUMPULAN DATA ANGKA".center(35,"="))
data = [1, 3, 5, 7, 9]
print(data)

    #Kumpulan data string
print("\n","KUMPULAN DATA STRING".center(35,"="))
data = ["kimi", "wa", "suki","da"]
print(data)
#untuk menghilangkan tanda baca
ileng = ' '.join(data)
print(ileng)

    #Kumpulan data boolean
print("\n","KUMPULAN DATA BOOLEAN".center(35,"="))
data = [False, False, True]
print(data)

    #Kumpulan Campuran
print("\n","KUMPULAN DATA CAMPURAN".center(35,"="))
data = [1, 'otak otak', True, 2, 'batagor', False]
print(data)

    ##Cara alternatif membuat list
    #Kumpulan range
print("\n","KUMPULAN DATA RANGE".center(35,"="))
data_range = range(0, 11)
print(data_range)
data_range_list = list(data_range)
print(data_range_list)

    #Kumpulan for (list comperhasion)
print("\n","KUMPULAN DATA FOR".center(35,"="))
data_for = [data for data in range(0,11)]
print(data_for)
    #cara hitungan operasi(+ - * / ** // %) data list
data_for = [data*2 for data in range(0,11)]
print(data_for)

    #Kumpulan for if
print("\n","KUMPULAN DATA FOR IF".center(35,"="))
list_por_if = [data for data in range(0,11) if data != 3] # != 3 menghilangkan angka 3
print(list_por_if)

    #mencari data list nilai genap
list_por_if = [data for data in range(0,11) if data%2 == 0]
print(list_por_if)

    #mencari data list nilai ganjil
list_por_if = [data for data in range(0,11) if data%2 == 1]
print(list_por_if)
