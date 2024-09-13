#tipe data: angka variabel asli (integer)
data_integer = 500
print ("data : ", data_integer)
print ("-bertipe : ", type(data_integer))

#tipe data: angka desimal (float)
data_float = 1.35 #penggunaan koma (,) diganti mnejadi titik (.)
print ("data : ", data_float)
print ("-bertipe : ", type(data_float))

#tipe data: kumpulan karakter (string/str)
data_string = "chino" #harus menggunakan tanda kutip ("")
print ("data : ", data_string)
print ("-bertipe : ", type(data_string))

#tipe data: biner true/false (boolean)
data_bool = True
print ("data : ", data_bool)
print ("-bertipe : ", type(data_bool))

##tipe data khusus

#tipe data: kompleks
#digunakan untuk mencari nilai imaginer (i/j)
data_complex = complex (3,9)
print ("data : ", data_complex)
print ("-bertipe : ", type(data_complex))

#tipe data: berasal dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.583)
print ("data : ", data_c_double)
print ("-bertipe : ", type(data_c_double))
