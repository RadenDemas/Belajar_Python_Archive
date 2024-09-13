data_0 = [2,4]
data_1 = [6,8]
data_list_biasa = [2,4,6,8]

print(f"data list biasa = {data_list_biasa}")
data_list_gabungan = [data_0,data_1]
print(f"data list gabungan = {data_list_gabungan}")

#Jadi guna dari nested list ini yaitu untuk menggabungkan 1 atau lebih list kedalam suatu list lain

#contoh
peserta_a = ["demas", 18, "matematika"]
peserta_b = ["karin", 17, "inggris"]
peserta_c = ["ajef", 18, "debat"]

seluruh_peserta = [peserta_a, peserta_b, peserta_c]

print(f"list seluruh peserta = \n {seluruh_peserta}")

#untuk membagi tiap tiap objek kedalam data yang diinginkan dapat dilakukan dengan cara

for peserta in seluruh_peserta:
    #print(f"Nama \t\t: {peserta[0]}")
    #print(f"Umur \t\t: {peserta[1]}")
    #print(f"Mata Lomba \t: {peserta[2]}\n")
    #atau
    print(f"""
    Nama : {peserta[0]}
    Umur : {peserta[1]}
    Mata Lomba : {peserta[2]}
    """)