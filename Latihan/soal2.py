total = 0
kelipatan = 2
while total < 100:
    total = (kelipatan)
    kelipatan = (kelipatan)
    #print(total)

#print("\n")
hasil = [total*3+1 for total in range(2,100) if total%2 ==0]

for total in hasil:
    if total >= 100:
        break
    #print(total)

hasil_1 = [total for total in range (1,100,2)]

#print(hasil_1)

hasil_2 = [total for total in range (1, 100, 4)]

#print(hasil_2)