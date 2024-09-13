    ##if else dan elif(else if)
    #Merupakan suatu sistem untuk membuat percabangan pada program

    ##if
#nama = str(input("Siapa nama anda? "))

#1. input data user
#2. kondisi if, jika true akan diproses dan jika false akan dilewat
#3. program selesai

#if nama=="Demas":
   # print("Halo demas")

#print("program selesai")
#If hanya akan memproses kondisi dimana input bersifat true pada apa yang dikondisikan, dan jika false akan dilewat

    ##else

#1. input data user
#2. kondisi if, jika true akan diproses dan jika false akan dilempar ke else
#3. else akan memperoses input yang false tadi
#4. program selesai

#nama = str(input("Siapa nama anda? "))

#if nama=="Demas":
   # print("Halo demas")
#else:
    #print("Kamu siapa ya?")
#print("program selesai")
#jika sebelumnya kondisi bersifat false akan dilewat, dengan ada nya else kondisi false akan diproses

    ##elif (else if)

#1. input data user
#2. kondisi if, jika true akan diproses dan jika false akan dilempar ke elif
#3. jika kondisi elif bersifat true, maka elif akan diproses, dan jika false akan dilempar ke else
#3. else akan memperoses input yang false tadi
#4. program selesai

nama = str(input("Siapa nama anda? "))

if nama=="Demas":
    print("Halo demas")
elif nama=="Udin":
    print("Halo udin teman nya demas")
else:
    print("Kamu siapa ya?")
print("program selesai")
#elif akan membuat sebuah percabangan yang baru
#jika if itu false, maka akan dilempar ke elif untuk diproses
#jika kondisi bersifat true maka akan diproses dan jika false akan dilempar ke else