#Menduplikasi list
a = ["demas", "syahrul", "rifki"]
b = a #pass reference/menduplikasi data secara referensi

print(f"a = {a}")
print(f"b = {b}")

#merubah salah satu objek

a[2] = "ajef"
print(f"a = {a}")
print(f"b = {b}")
#data pada kedua list akan sama, ini dikarenakan address yang dimiliki yang dimiliki kedua list tersebut memiliki kemiripan

#address kedua list
print(f"adress list a = {hex(id(a))}")
print(f"adress list b = {hex(id(b))}")


print("\n")
#Copy list
c = a.copy() #full duplicate/secara full diduplikasi

print(f"adress list a = {hex(id(a))}")
print(f"adress list b = {hex(id(b))}")
print(f"adress list c = {hex(id(c))}")

c[0] = "siti"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

a[1] = "karina"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

#dapat dilihat list a dan b sama dikarenakan address list yang sama
#sedangkan address list c berbeda, maka ketika objek list pada list c diganti tidak akan berpengaruh pada list b dan a
#sebaliknya ketika objek pada list a dan b dirubah, maka list c tidak akan berubah 
#