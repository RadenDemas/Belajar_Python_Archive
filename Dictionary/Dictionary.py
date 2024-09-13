#list (list)
#data list meruapakan suatu data yang berupa suatu barisan list yang dapat berisi list ataupun objek
#data list diambil dengan cara mengambil index
#            index  index  index  index
#              0      1      2      3
data_list = ["demas", 1, "syahrul", 2]

print(data_list[0])

#dictonary (dict)
#data dictionary meruapakan suatu data yang dapat berisi berbagai macam data, dapat berupa list, dict, ataupun objek
#data dictionary diambil dengan cara mengambil key (kata kunci) dan akan hasil nya akan berupa value

#data_dict = {"dem":"demas", "rul":"syahrul"}

data_dict = {
    #key    #value
    "dem" : "demas",
    "rul" : "syahrul",
    "num" : 1,
    "list" : data_list
}

print(data_dict["rul"], 
      data_dict["num"]
      )

#Untuk mengecek keys pada data
print("\n")
keys = data_dict.keys()
print(keys)

#untuk mengecek values pada data
print("\n")
values = data_dict.values()
print(values)

#untuk mengecek items pada data
print("\n")
items = data_dict.items()
print(items)
