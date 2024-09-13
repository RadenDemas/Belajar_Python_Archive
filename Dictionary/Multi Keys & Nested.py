siswa_1 = {
    "nama":"Demas",
    "absen":"21",
    "nilai":90,
    "tuntas":True
}

siswa_2 = {
    "nama":"Syahrul",
    "absen":"28",
    "nilai":80,
    "tuntas":True
}

siswa_3 = {
    "nama":"Rifki",
    "absen":"24",
    "nilai":75,
    "tuntas":False
}

#Nested data dict
#kurang lebih sama seperti nested list dimana list dapat disimpan di list lagi
#maka data dict juga dapat disimpan juga di dalam data dict lagi

data_ulangan = {
    "SISWA001":siswa_1,
    "SISWA002":siswa_2,
    "SISWA003":siswa_3
}

#mengisi data mirip seperti data base
print(f"{'KEY':<9}  {'NAMA':<8} {'ABSEN':<3} {'NILAI':<3} {'TUNTAS':<5}")

print("="*50)

for data in data_ulangan:
    key = data
    nama = data_ulangan[key]["nama"]
    absen = data_ulangan[key]["absen"]
    nilai = data_ulangan[key]["nilai"]
    tuntas = data_ulangan[key]["tuntas"]
    print(f"{key:<9}  {nama:<8} {absen:<5} {nilai:<5} {tuntas:<5}")
