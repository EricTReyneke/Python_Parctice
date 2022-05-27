#INTEGERS
#numb = 4*4
#numb2 = 4
#print(numb + numb2)
#print(2 ** 2) #Tot die mag
#print(5 // 4) #Ront af to die laagste heel getal
#print(6 % 4) #Wys die res wwarde
#print(bin(5)) Print die binary number

#MATH FUNCTIONS
#print(round(3.6)) Rond af tot die naste heel getal
#print(abs(-20)) Maak die getal n positieve getal

#OPERATOR PRECEDENCE
#()
# **
# * /
# + -

#CONSTANTS moet altyf in blok letters geskryf word
#GOOD PRACTICE WITH VARIABLES moet altyf klein letters wees en mag nie met n nommer begin nie

#a,b,c = 1, "Lekker", 2
#print(a)
#print(b)
#print(c)

#Type conversion word gedoen deur om net die data type se afkortin te se voor n hakkie bv str() of int() en nie ().ToString nie

#String Excape scequances... die \ word gerbuik om te wys dat die volgende Character n string is en nie n function nie.
#print("Ek is \"Nogals\" moeg")
#\t en \n word nogsteeds dieselfde gebruik soos in ander tale

#Waar ons die $ sign gebruik om te trancate gebruik ons die letterl "f" in Python

# name = "Eric"
# age = 20
# print("Your name is {new_name} and you are {new_age} years old".format(new_name = "Arie", new_age = 20))
# print(f"Your name is {name} and you are {age} years old.")

#indexing [start:stop:stepover]
#name = "Eric Reyneke"
#kry net my naam
#print(name[:4])
#Die defualt is 0
#NBNBNBNB Om n - by te sit begin jy by die laaste index.
#Gan gebruik word om die string om te ruil.                     NB!!!!!
#print(name[::-1])

#Exersice to find how old a persone is.
# import datetime
# birth_year = int(input("Please enter the year you where born in: "))
# getting = datetime.datetime.now()
# current_year = int(getting.strftime("%Y"))
# age = current_year - birth_year
# print(f"You are {str(age)} years old.")

#Exercise Prompt for a users username and password. After you need to get the length and display the password in *
# user_name = input("Please enter your user name: ")
# password = input("Please enter your password: ")
# lenght = len(password)
# hide_password = "*" * lenght
# print(f"{user_name}, your password {hide_password} is {lenght} letters long")




# Scope belangrik
count = 0;

def Counter1():
  global count;
  count = 100;
  return count;

print(Counter1())
print(count)

# output
# 100
# 100

#-------------------

count = 0;

def Counter1(count):
  return count;

print(Counter1(count))
print(count)
#output 
#100
#0