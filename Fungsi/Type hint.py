#type hint
#merupakan suatu command untuk memberi tahu jenis fungsi yang harus dimasukkan
#type hint terdiri dari:
#string = str
#integer = int 
#float = float
#boolean = bool
#peran nya type hint ini untuk memberi tahu kepada pengguna
#apa yang harus dimasukkan ke dalam argument pada fungsi

def perkalian(angka1,angka2):
    hasil = angka1*angka2
    return hasil

print(perkalian(5,2))
print(perkalian(2.5,3))
#print(perkalian(udin,dadang))

#Jika kita mengisi argument pada fungsi diatas
#untuk jenis argument bertipekan integer dan float tetap jalan
#sedangkan argument bertipekan string tidak jalan
#nah guna dari type hint ini untuk memberi tahu pengguna
#apa jenis argument yang harus diisi pada fungsi

def pertambahan(angka1 = int,angka2 = int)  -> int:
    hasil = angka1+angka2
    return hasil

print(pertambahan(3,2))

#seperti fungsi diatas
#kita memberi tanda bahwa pada fungsi angka 1 dan 2 merupakan integer
#maka dari itu kita harus mengisi argument tersebut dengan integer
#selain itu kita dapat memberi tanda dengan menggunakan tanda panah (->)

def halo(nama=str,pengirim=str) -> str:
    print(f"halo {nama}, ini {pengirim}")

print(halo("udin", "dadang"))