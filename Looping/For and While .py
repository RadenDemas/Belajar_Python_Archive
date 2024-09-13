    #Jika dilakukan dengan manual
#nilai = 1
#print(nilai)
#nilai = nilai + 1
#print(nilai)
#nilai = nilai + 1
#print(nilai)
#nilai = nilai + 1
#print(nilai)

    #Jika dilakukan dengan cara looping (for)
#nilai = 0
#while nilai < 5: 
#    nilai += 1
#    print(nilai)
#   if nilai == 4:
         #break

    ###Looping (for)
    #Looping for biasa nya digunakan untuk looping data yang bertipe kan list
    ## For (list)
print("FOR LIST".center(20,"="))
nilai = [1, 2, 3, 4, 5]

for hasil in nilai:
    print(hasil)

    ## For (range)
    #range akan menghitung jarak dari angka yang diminta dengan syarat (< angka) dan (>= angka, < angka)
print("\n","FOR RANGE".center(20,"="))
nilai = range(1,6)
#nilai jarak artinya >= 1 dan < 6

for hasil in nilai:
    print(hasil)

    ###While
    #Sedangkan While biasa nya digunakan dengan looping data yang memiliki batasan
    #Batasan tersebut bisa merupakan tanda <, >, <=, >=
print("\n","WhILE".center(20,"="))
nilai = 0

while nilai < 5:
    nilai += 1
    print(nilai)
#Jika looping while tidak akan menemui batasan, maka program akan terus berjalan
#Ini dikarenakan bahwa command yang diberika bersifat true
#Oleh karena nya looping akan terus berjalan hingga mencapai nilai false

