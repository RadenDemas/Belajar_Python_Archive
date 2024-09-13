#Bitwise merupakan operasi yang digunakan khusus untuk menangani operasi logika biner/binary
#sama hal nya dengan operasi boolean, operasi bitwise juga terdiri dari and, or, xor, not
'''
1. or |
2. and &
3. xor ^
4. not ~
5. Shift right >>
6. Shift left <<
'''
#kerja operasi bitwise ini dengan cara membandingan tiap tiap angka pada binary
'''
a = 000000101 = 5
b = 000001001 = 9
c = a | b

a = 000000101
b = 000001001
c = 000001101 = 13
'''

a = 3
b = 8

print('nilai a :', a, 'binary : ', format(a, '08b'))
print('nilai b :', b, 'binary : ', format(b, '08b'))

print('======OR=====')

c = a | b
print('nilai c :', c, 'binary : ', format(c, '08b'))
