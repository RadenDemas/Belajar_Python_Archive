import datetime as tanggal

    ## membuat Tanggal
hari_ini = tanggal.date.today()

print(f'''Tanggal : {hari_ini}
Hari : {hari_ini:%A}
''')

    ##menginput data user manual
tahun = 1945
bulan = 8
hari = 17
#data = int(input(tahun, bulan, hari))
tanggal_user = tanggal.date(tahun, bulan, hari)
umur_hari = hari_ini - tanggal_user
umur_tahun = umur_hari.days // 365

print(f'''Tanggal lahir : {tanggal_user}
Hari : {tanggal_user}
Umur : {umur_tahun} tahun
''')

    ##menginput data user secara otomatis


tahun = int(input("Tahun berapa? "))
bulan = int(input("Bulan apa? "))
hari = int(input("Hari apa? "))
tanggal_user = tanggal.date(tahun, bulan, hari)
umur_hari = hari_ini - tanggal_user
umur = umur_hari.days // 365
bulan_sisa = (umur_hari.days % 365) // 30
hari_sisa = (umur_hari.days % 365) // 12

print(f'''
Tangal = {tanggal_user}
Hari : {tanggal_user:%A}
Umur : {umur} tahun
Ulang tahun selanjutnya : {bulan} bulan dan {hari_sisa} hari
''')