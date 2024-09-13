    ###1. cara membuat string
'''
    1. dengan menggunakan single quote (tanda kutip satu) '...'
    2. dengan menggunakan double quote (tanda kutip dua) "..."
'''

data = 'ini adalah single quote'
print(data, type(data))

data = "ini adalah duoble quote"
print(data, type(data))
#kedua assigment tersebut merupakan string

print('"halo apa kabar')
#dapat digunaan keduanya untu tidak terjadi error

#print('hari jum'at')
#ini dapat error dikarenakan terjadi error pada command ' pada 'at
#solusinya dapat menggunakan duoble quote "..."

print("hari jum'at")

#menggunakan tanda \
#membuat tanda' menjadi string

#print('hari ini hari jum'at)
#maka akan terjadi error
#untu mengatasinya, tambahkan \ sebelum 'at

print('hari ini hari jum\'at') 

    ##backslash (\\)
#print("C:\user/Bambang")
#maka aan terjadi error
#ini karea program akan bingung atas command \u
#untuk mengatasinya, tambahan \ sebelum (\u) agar (\u) menjadi string

print('C:\\user/Bambang')

    ##tab (\t)
#untuk memberika space pada kelimat

print("halo apa kabar \t\tkamu yang disana")

    ##backspace(\b)
#untuk menghapus space pada klaimat

print("aku berada \bdidekat mu")

    ##newline (garis baru)
#\n -> LF -> Line Feed -> untuk linux dan MacOs
#\r -> CR -> Carriage Return -> untuk os lama
#\r\n -> Line Feed Carriage Return -> untuke windows

print("aku berada\ndiatas mu")

    ###3. string literal atau raw (r'...'
# string raw aan mengubah seluruh comand yang berada didalam nya menjadi string normla

#print('C:\new folder\hari jum'at)
#ini aan error dikarenaan ada beberapa command yang error
#cara mengatasi nya dengan menambahkan r sebelum quote

print(r"C:\newfolder\harijum'at")

    ##multiline literal string ('''   ''')
#untu membuat lebih dari satu baris pada satu string

print("""
    Nama : Demas
    Kelas : XII IPA 4
    Umur : 18 tahun
""")

    ##multiline literal string raw (r""" """")
print(r"""
    Nama : Demas
    Kelas : XII \IPA \4
    Umur : 18 \tahun
""")