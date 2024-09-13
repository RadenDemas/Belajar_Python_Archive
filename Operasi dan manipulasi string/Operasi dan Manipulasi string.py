    ###1. menyatukan tiap tiap string (+)
judul = "Menyatukan string".center(20, "=")
print("\n" + judul)

Nama_Belakang = ("Raden")
Nama_Tengah = ("Demas")
Nama_Depan = ("Amirul Plawirakusumah")

Data = Nama_Belakang + " "+ Nama_Tengah +" "+ Nama_Depan
Data_2 = Nama_Belakang, Nama_Tengah, Nama_Depan
#Memakai tanda + atau , untuk menyatukan tiap string menjadi assigment
#Memakai tambahkan " " untuk memberikan spasi pada assigement baru

print(Data, type(Data))
print(Data_2)

    ###2. Menghitung panjang string (len)
#untuk menghitung berapa banyak huruf yang digunakan pada suatu string
judul = "len".center(20, "=")
print("\n" + judul)

panjang = len(Data)
print("Jadi banyak huruf pada data : " + str(panjang))

    ###3. mengecek apakah ada komponen karakter pada string (in/in not)
#in untuk mengecek komponen karakter tersebut ada pada sting
#not in untuk mengecek bahwa komponen karakter tersebut tidak ada pada string
judul = "IN/IN NOT".center(20,"=")
print("\n" + judul)

d = "d"
status = d in Data
print(d + " ada di " + Data + '= ' + str(status)) #untuk mengubah status dari boolean menjadi string

d = "d"
status = d not in Data
print(d + " ada di " + Data + '= ' + str(status))

    ##pengulangan karakter
#print ("Mata ne "*10)

    ##indexing ([])
#untuk melihat huruf apa yang berada pada nomor index
#untuk penomoran nya dimulai dari 0
judul = "INDEXING".center(20, "=")
print("\n" + judul)
'''
Raden
R = 0
a = 1
d = 2
e = 3
n = 4
'''
#untuk spasi dihitung juga dalam index
print('index ke 0 : ' + Data[0])
print('index ke 4 : ' + Data[4])
print('index ke 5 : ' + Data[5])
print('index ke 10 : ' + Data[10])

#item/karakter paling kecil (min)
#dihitung dalam binary atau ascii code paling kecil
print('paling kecil : ' + min(Data))

#item/karakter paling besar (max)
#dihitung dalam binary atau ascii code paling besar
print('paling besar :' + max(Data))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah ", str(ascii_code))

ascii_code = ord("w")
print('ASCII code untuk "w" adalah ', str(ascii_code))

    ###4. Merubah Cast string
    ## Merubah seluruh assigment menjadi upper case
judul = "MERUBAH CAST STRING".center(21, "=")
print("\n" + judul)

lower = "kimi no koto ga suki desu!!"
print(lower)

upper = lower.upper()
print(upper)

    ## Meruba seluruh asigment menjadi lower case
random = "AanOoo.... Go... GOmenn..."
print("\n" + random)

lower = random.lower()
print(str(lower))

    ###5. Pengecekan isx method
    ##islower() <-- untuk mengecek huruf kecil pada assigment
judul = "ISX METHOD".center(20, "=")
print("\n" + judul)


kecil = "aduh sangat pusing sekali"
mengecek = kecil.islower()
print(kecil + " itu kecil : ", mengecek)
#bisa menggunakan tanda + untuk run , namun perlu mengubah nya menjadi str

besar = "HADEUH ADA APA SIH SAMA KAMU"
mengecek = besar.islower()
print( besar + " itu kecil : " + str(mengecek))

    ##isupper() <-- untuk mengecek huruf besar pada assigment

mengecek = kecil.isupper()
print("\n" + kecil + " itu besar : " + str(mengecek))

mengecek = besar.isupper()
print(besar + " itu besar : ", mengecek)

    ##isalpha() <-- untuk mengecek huruf secara keseluruhan

huruf = "jikasepertiini"
mengecek = huruf.isalpha()
print ("\n" + huruf + ", itu huruf semua : ", mengecek)

huruf = "jika seperti ini"
mengecek = huruf.isalpha()
print (huruf + ", itu huruf semua : ", mengecek)


#tanda spasi pun dimasukan sebagai bagian dari bukan alfabet, maka hasil nya pun false

    ##isalnum() <-- untuk mengecek huruf dan angka
    #tidak ada boelh space
huruf_angka = "jikaXadalah1"
mengecek = huruf_angka.isalnum()
print("\n " + huruf_angka + " itu angka dan huruf : "+ str(mengecek))

huruf_angka = "jika X adalah 1"
mengecek = huruf_angka.isalnum()
print(huruf_angka + " itu angka dan huruf : "+ str(mengecek))

    ##isdecimal() <-- untuk mengecek angka
    #tidak ada boleh space dan huruf
angka = "20.19942"
mengecek = angka.isdecimal()
print("\n" + angka + " itu angka : ", mengecek)

    ##isspace() <-- untuk mengecek space, tab, garis baru
    #tidak boleh ada huruf dan angka
kosong = "     "
mengecek = kosong.isspace()
print("\n" + "'" +  kosong + "'" + " apakah kosong : ", mengecek)

    ##istittle() <-- semua kata dimulai dengan huruf besar
besar = "Aku Sepertinya Sudah Besar"
mengecek = besar.istitle()
print("\n" + besar + " Apakah benar : ", mengecek)

kecil = "Aku sepertinya masih kecil"
mengecek = kecil.istitle()
print(kecil + " Apakah benar : ", mengecek )

    ###6. penggabungan komponen join() dan split()
    #join() yaitu untuk menggabung komponen kelompok data
    #split() yaitu untuk memisahkan komponen kelompok data
#untuk membuat data join diperlukan kelompok data dengan tanda [] didalam nya
judul = "PENGGABUNGAN KOMPONEN".center(30, "=")
print("\n" + judul)

pisah = ["kono", "sekai", "wa", "utsukushi"]
gabungkan = ' '.join(pisah)
print ( str(pisah) + " |menjadi --->| " + gabungkan)

gabung = "kono sekai wa utsukushi"
pisahkan = gabung.split()
print(str(gabung) + " |menjadi --->| " + str(pisahkan))

    ###7. alokasi karakter rjust(), ljust(), center(), dan strip()
    #rjust untuk mengalokasikan kata menjadi disebelah kanan
    #ljust untuk mengalokasikan kata menjadi disebelah kiri
    #center untuk mengalokasikan kata menjadi di tengah
    #strip untuk menghilangkan tanda
judul = "ALOKASI DATA".center(20, "=")
print("\n" + judul)


kanan = "kanan".rjust(20, "!") #dapat menggunakan :>
print( kanan)

kiri = "kiri".ljust(19,"!") #dapat menggunakan :<
print(kiri)

tengah = "tengah".center(20,"-") #dapat menggunakan :^
print(tengah)

dihilangkan = "----hilang----".strip("-")
print(dihilangkan)