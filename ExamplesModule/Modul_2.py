# print ("Tipuri de date")
#
# a= 10 #int
# b= 99.12 #float
# c= "eu sunt python" #string
# d= True #bool
# e= None #NoneType
#
# print ("Example: " ,a, b, c, d, e)
# input("\n Apasa enter pentru a continua...")
#
# # =======
# # Operators
# # adunare +
# # scădere -  #
# # înmulțire *
# # împărțire /
# # restul împărțirii %  #
# # putere **
# #======
#
# print("\n Jocul Operatiilor")
# x= float(input("\n Primul numar:"))
#
# y= float(input("\n Al doilea numar:"))
#
# op= input("\n Introdu operator")
#
# operatii= {
#     "+" : x + y,
#     "-" : x - y,
#     "*" : x * y,
#     "/" : x / y,
#     "//" : x//y,
#     "%" : x % y,
#     "**" : x ** y,
# }
#
# rezultat = operatii.get(op, "Operator necunoscut")
#
# print(f"\n Rezultateul este {rezultat}")
# input("\n Apasa enter pentru a continua...")

# # ============
# #Assersions
# #============
#
# a1 = int(input("\n Primul numar:"))
#
# b2 = int(input("\n Al doilea numar:"))
#
# print("Assert a == b ...")
# #assert a1==b2 , "Error a nu este egal cu b"
# # assert a1==b2 and a1 > 100 or a1 < 10
# #assert a1 > 100, "a1 < 100"
# assert b2 < 10, "b2 > 10"


# String Game

print("My String")

name = input("numele meu:")

salut= "salut " + name
litere = len(name)
mare = name.upper()
mic = name.lower()

print(salut)
print("Numele meu are", litere, "litere")
print("Cu majusucle", mare)
print("Cu litere mici", mic)

