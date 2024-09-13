#Casting data adalah merubah satu data menjadi satu data yang lain
#Tipe data python: str, int, boolean, dan float

#INTEGER
print("===INTEGER===")

data_int = 13
print("Data : ", data_int, ",Data tipe : ", type(data_int))

data_float = float(data_int)
print("Data : ", data_float, ",Data tipe : ", type(data_float))

data_str = str(data_int)
print("Data : ", data_str, ",Data tipe : ", type(data_str))

data_bool = bool(data_int) #akan false jika data int berupa 0
print("Data : ", data_bool, ",Data tipe : ", type(data_bool))

#float
print("===FLOAT===")

data_float = 18.36
print("Data : ", data_float, ",Data tipe : ", type(data_bool))

data_int = int(data_float) #akan dibulatkan kebawah berapa pun nilai desimal nya
print("Data : ", data_int, ",Data tipe : ", type(data_int))

data_str = str(data_int) 
print("Data : ", data_str, ",Data tipe : ", type(data_str))

data_bool = bool(data_float) #akan false jika float berupa 0
print("Data : ", data_bool, ",Data tipe : ", type(data_bool))

#String
print("===STRING===")

data_str = "4"
print("Data : ", data_str, ",Data tipe : ", type(data_str))

data_int = int(data_str) 
print("Data : ", data_int, ",Data tipe : ", type(data_int))
#akan error jika data str tidak berisi

data_float = float(data_str) 
print("Data : ", data_float, ",Data tipe : ", type(data_float))
#akan error jika data str tidak berisi
#akan error jika data str bukan angka

data_bool = bool(data_str) #akan berupa false jika data str tidak berisi
print("Data : ", data_bool, ",Data tipe : ", type(data_bool)) 

#Boolean
print("===BOOLEAN===")

data_bool = False
print("Data : ", data_bool, ",Data tipe : ", type(data_bool))

data_int = int(data_bool) 
print("Data : ", data_int, ",Data tipe : ", type(data_int))
#nilai int akan bernilai 1 jika data bool berupa true
#nilai int akan bernilai 0 jika data bool berupa false

data_float = float(data_bool)
print("Data : ", data_float, ",Data tipe : ", type(data_float))
#nilai float akan bernilai 1 jika data bool berupa true
#nilai flaot akan bernilai 0 jika data bool berupa false

data_str = str(data_bool) 
print("Data : ", data_str, ",Data tipe : ", type(data_str))


#seluruh data str akan menulis ulang data yang sebelumnya dan tidak berubah
