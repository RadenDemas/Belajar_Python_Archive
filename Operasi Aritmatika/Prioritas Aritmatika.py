#Untuk prioritas aritmatika menggunakan sebuah tangga matematika
'''
1. Tanda kurung ()
2. eksponen atau pangkat **
3. perkalian, pembagian, modulus, dan floor *, /, %, //
4. pertambahan dan perkalian + -
'''
#Contoh
x = 3
y = 1
z = 5

hasil = x + y + z * x + x ** z / z 
print(x,'+',y,'+',z,'*',x,'+',x,'**',z,'/',z,'=',hasil)

hasil = (x + y) * z
print('(',x, '+', y,')', '*', z , '=',hasil)