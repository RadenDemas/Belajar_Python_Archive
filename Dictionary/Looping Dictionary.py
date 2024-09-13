data_pelajaran = {
    "mtk" : "matematika",
    "bio" : "biologi",
    "sb" : "seni budaya",
}

#Looping secara biasa

print("Looping biasa".center(16,"="))

for pelajaran in data_pelajaran:
    print(pelajaran)

#Pada looping biasa, data yang terambil hanya berupa key saja

#Looping menggunakan .keys .values. items
#.keys --> untuk mengambil data dari data dict hanya berupa keys
#.values --> untuk mengambil data dari data dict hanya berupa value
#.items --> untuk mengambil data dari data dict berupa keys dan values

print("\n", "Looping Keys".center(20,"="))

keys = data_pelajaran.keys()

for pelajaran in keys:
    print(f" key pada data: {pelajaran}")

#Cara memasukkan value dalam looping keys

print("\n")
for pelajaran in data_pelajaran.keys():
    print(f"value: {data_pelajaran.get(pelajaran)}")

print("\n", "Looping Values".center(20,"="))

values = data_pelajaran.values()

for pelajaran in values:
    print(f"value pada data: {pelajaran}")

print("\n", "Looping Items".center(20,"="))

items = data_pelajaran.items()

for pelajaran in items:
    print(f"items pada data: {pelajaran}")

#mengambil keys dan values menggunakan .items

print("\n")
for keys,values in items:
    print(f"key: {keys} dan value: {values}")
