""" import CRUD as crud

user_input = input("Masukan Opsi: ")
match user_input:
    case "1" : crud.read_console()
    case "2" : print("CREATE DATA")
    case "3" : print("UPDATE DATA")
    case "4" : print("DETELETE DATA")
 """

""" gabung = ["kono" "sekai" "wa" "utsukushi"]
gabung_str = f"{gabung}"
pisahkan = gabung_str.split(",")
print(str(gabung) + " |menjadi --->| " + str(pisahkan))
input = input("")
 """

""" import sys
for i in sys.path:
    print(i) """
""" import CRUD as curd
test = dir(curd)

print(test) """

""" def buka():
    with open("data.txt","r") as file:
        content = file.readlines()
        return content

hasil_data = buka()
for index,data in enumerate(hasil_data): 
    data_break = data.split(",")
    total = data_break[3]
    total_strip = total.replace(" ", "")
    #jumlah_total = (sum(i) for i in zip(total))
    reslist = []
    for i in range(0,len(total_strip)):
        reslist.append(total_strip[i])
    print(f"resultan list is : {str(reslist)}") """

""" with open("data.txt", "r") as file:
    data = file.read()
    data_jadi_list = data.replace(" ", "").split("\n")
    data1 = data_jadi_list[0]
    data2 = data_jadi_list[1]
    data3 = data_jadi_list[2]
    data4 = data_jadi_list[3]
    data5 = data_jadi_list[4]
    reslist = [sum(i) for i in zip(data1,data2)]
    print(reslist) """
    
""" nama = "akang"

with open("nama.txt","a",encoding="utf-8") as file:
    file.write(f"{nama}\n")
    file.write("aduch")
    file.write(nama+"\n") """

""" with open("data.txt","r") as file:
    baca = file.read()
    print(len(baca)) """

test = "vFOEqa,23000                                                                                                                                                                                                                                                          ,3000                                                                                                                                                                                                                                                           ,20000                                                                                                                                                                                                                                                          ,2023 - 05 - 15"
print(len(test))