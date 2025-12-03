
#number = 20
#number2 = 30
# judul
#print (number)
#print ("rise & shine!")
#print ("taco" + "cat")
#rint ("taco " + "cat")
#print (2*4)
#print (3,"iyah")

#message= "welcome to python!"
#print(message)
#print(number , message)
#length = 1
#high =34
#print (length * high)
#print (10 // 2)
#print (100 % 2)

#-------------------------------------------------------------------------------------
#LEARN FROM YT (MODULUS OPERATOR)


#friends =  10

#friends =  friends + 1
#friends += 3
#friends -= 7
#friends *= 10
#friends /= 2
#friends **= 2
#remainder = friends % 4
#print(remainder)

#SIMPLE ARITHMATIC

# x = 2.14
# y = -5000000
# z = 3.20

#result = round(z)
#result = abs(y) 
#result = max(x, y, z)
#result = min(x, y, z)

#AMAZINNNG IMPORT MATH WITH POPULAR FORMULA!
#import math

#x = 9.2

#print (math.pi)
#print (math.e)

#print (math.ceil(x))
#print(math.floor(x))

#import math: KELILING LINGKARAN
#QUESTION
#print('Bintang has a round of a wheel, and he curious to cound the circumference.')
#print('How much does the circumference of the wheel has?')
#radius = float(input('If the Radius of the wheel  is ... :'))


# circumference = 2 * math.pi * radius YOUTUBE GUIDE
#circumference = 10 * math.pi * radius

#print(f" The circumference of the wheel is { round (circumference)}cm")

# print(f"The circumference is: {circumference}") FIRST
# print(f"The circumference is {round(circumference, 2)} cm")

#LUAS LINGKARAN
# import math

#radius = float(input("The radius of the circle"))

#area = math.pi * pow(radius, 2)

#print(f"The area of circle is {round(area, 3)} cm^2")

#VOLUME TABUNG
#import math

#radius = float(input("Radius tabung memiliki jari-jari:"))

#volume = math.pi * pow(radius, 2)

#print(f"volume tabung nya adalah: {round(volume,  1)}")

#SEARCH FOR HYPOTENUSE OF A RIGHT TRIANGLE

#(failll)

#import math

#try:
    #print("Hitung sisi miring segitiga siku-siku dengan rumus Pythagoras")
    #a = float(input("Masukkan panjang sisi A (cm): "))
    #b = float(input("Masukkan panjang sisi B (cm): "))
    #c = math.sqrt(a**2 + b**2)
   # print(f"Sisi miring segitiga siku-siku adalah {c:.2f} cm")
#except ValueError:
    #print("Input tidak valid. Harap masukkan angka.")

#-------------------------------------------------------------------------------------

#Title: if statement 
#if = Do some code only IF some condition is true
#   else do something else

#age = int(input("How old are you"))

#if age >= 100:
    #print("You are too OLDDD!")

#elif age >= 18:
    #print("Congratulations! you have signed up")

#elif age < 0:
    #print("OH HELL NAH, YOU HAVEN'T BORN YET")

#else:
   # print("sorry bro you have to be great than 17!")

#-----------------


#response = input("Would you like to order a food? (Y/N)")

#if response == "Y":
   # print("Okay! what would you like to order?")

#elif response == "N":
    #print("so why you're here?")

#else:
    #print("what dyou mean?")

#-----------------

#name = input("What's your name sweethear?")

#if name == "":
    #print("Just answer the damn question")

#else:
    #print(f"Welcome King {name}! it's good to see you")

#online = False / True

#if online:
   # print("The user is now online")

#else:
    #print("Oops, the user is offline")

#-------------------------------------------------------------------------------------

#CALCULATORRRRSS BY ME
#FAILEDD


# Meminta input operasi
#operasi = input("Masukkan operasi (+, -, *, /, **): ")

# Meminta input angka pertama
#Angka1 = float(input("Angka pertama: "))

# Validasi operasi
#operasi = input("+, -, *, /, **")

#Angka1 = float(input("Angka pertama: "))

#if operasi == "**":
   # Hasil = Angka1 **2
    #print(Hasil)

#else: 

    #Angka2= float(input("Angka kedua: "))
    #if operasi  == "+":
        #Hasil = Angka1 + Angka2
        #print(Hasil)

   # elif operasi == "-":
        #Hasil = Angka1 - Angka2
        #print(Hasil)

    #elif operasi == "*":
        #Hasil = Angka1 * Angka2
       # print(Hasil)

    #elif operasi == "/":
        #if Angka2 == 0:
           # print("Tidak terdefinisi")

      #  else:
           # Hasil = Angka1 / Angka2
            #print(Hasil)

    #else: 
        #print(f"{operasi} tidak valid")

#bilangan1 = float(input("bilangan1: "))

#operasi = input("+, -, *, /")

#bilangan2 = float(input("bilangan2: "))

#if operasi == "+":
   #hasil = bilangan1 + bilangan2
    #print(hasil)

#elif operasi == "-":
    #hasil = bilangan1 - bilangan2
    #print(hasil)

#elif operasi == "*":
   # hasil = bilangan1 * bilangan2
    #print(hasil)

#elif operasi == "/":
    #hasil = bilangan1 / bilangan2
    #print(hasil)

#else:
    #print(f"That ain't right, {operasi}? ")

#-------------------------------------------------------------------------------------

#WEIGHT CONVERTER

#weight = float(input("Input your weight: "))
#unit = input("Kgs or Lbs? (K/L): ")

#if unit == "K":
   # weight = weight * 2.205
    #unit = "Lbs."
    #print(f"your weight in {unit} is {weight} {unit}")

#elif unit == "L":
   # weight = weight / 2.205
    #unit = "Kgs"
    #print(f"your weight in {unit} is {weight} {unit} ")

#else:
    #print(f" That {unit} isn't avaliable")

#KESALAHAN: KESALAHAN DI BAGIAN VARIABLE YANG DIAPAKAI UNTUK FUNCTION IF, ELIF

#unit = input("Farenheit or Celcius? (F/C) ")
#temp = float(input("How much the temperature: "))

#if unit == "C":
    #temp = round((temp * 9 ) / 5 + 32, 2 )
    #print(f"your celcius temperature is {temp} F")

#elif unit == "F":
    #temp = round((temp - 32) * 5 / 9, 2)
   # print(f"your farenheit temperature is {temp} C")

#else:
    #print(f"That {unit} isn't available")
#-------------------------------------------------------------------------------------
#LOGICAL OPERATOR
#temp = 45
#is_raining = False

#if temp >35 or temp <0 or is_raining:
   # print("It's not a good day to go outside")
#else:
    #print("It's a good day to go outside")
#-------------------------------------------------------------------------------------

# temp = 24
# is_sunny = True

# if temp > 30 and is_sunny:
#     print ("its a hot day")
#     print("you should drink water")

# elif 25 > temp >0 and  is_sunny:
#     print("it's a warm day")
#     print("you should drink water")

# elif temp <= 0:
#     print("its a cold day")
#     print("you should drink water")

# if temp > 30 and not is_sunny:
#     print ("its a hot day")
#     print("you should drink warm water")

# elif 25 > temp >0 and not is_sunny:
#     print("it's a warm day")
#     print("you should drink warm water")

# elif temp <= 0 and not is_sunny:
#     print("its a cold day")
#     print("you should drink warm water")
#-------------------------------------------------------------------------------------

 #conditinal statement
# common use = X if condition else Y

# num = 0
# a = 100
# b= 1000
# # age = 35
# description = "married"
# # temperature =  30
# user_role = "admin"

# # # print( "positive" if num >= 0 else 'negative')
# # # print("even" if num % 2 == 0 else "odd")
# # # max_num = a if a >b else b
# # # min_num = a if a < b else b
# # status = "adult" if age >= 18 else "child"
# # deskripsi = "masha allah" if description is "married" else "insha allah"
# # weather = "HOT " if temperature > 32  else "cold" 
# # question: how can i add some elif function because between 30 - 35 it's normal weather
# apa_aja = "full access" if user_role == "admin" else "Limites acces"


# # # if a > b:
# # #     print("a")
# # # else :
# # #     print("b")
# # # print(status)
# # # print(deskripsi)
# # print(weather)
# print(apa_aja)
# # #-------------------------------------------------------------------------------------

#STRING METHODS

# phone_number = input("What's yput number?")

#yang ini start angka 1
# result = len(name)

#yg ini start angka 0
# result = name.find ('n')
# result = name.rfind ('n')
# name = name.capitalize( )
# name = name.upper()
# name  = name.lower()
# name = name.isdigit()
# name  = name.isalpha()

# result = phone_number.count("-")
# phone_number = phone_number.replace("-", "")

# print(phone_number)

# name = input("What's your name?")
# username.find("")

# if len(name) >5:
#     print("please use shorter name")

# else: 
#     print(f"Welcome {name}!")
# print(result)

