#for loop
print("\nmenggunakan for")
kumpulan_angka = [1,4,5,2,3,6,7]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

print("\n")

peserta = ["demas", "syahrul", "ajef", "waldi"]

for nama in peserta:
    print(f"Nama = {peserta}")

#for and range loop
print("\nfor and range loop")
kumpulan_angka2 = [1,4,5,2,3,6,7]

panjang = len(kumpulan_angka2)
for i in range(panjang):
    print(f"Angka = {i}")

#while loop
print("\nwhile loop")
kumpulan_angka = [1,4,5,2,3,6,7]
panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {i}")
    i+=1

#list comperhension
print(f"\nlist comperhension")
data = ["demas",1,2,3,"chino"]

[print (f"data = {i}") for i in data]

kumpulan_angka = [1,2,3,4,5]
angka_kuadrat = [i**2 for i in kumpulan_angka]
print(f"angka = {angka_kuadrat}")

#enumerate
print("\nenumerate")
data_list = ["demas", "syahrul", "ajef", "waldi"]
for Index,data in enumerate(data_list):
    print(f"index = {Index}, data = {data}")