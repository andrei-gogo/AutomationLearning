# print("Tipuri de date")
#
# a= 10 # int
# b= 22, 33 # float
# c= "Test modul" # string
# d= True # bool
# e= None # none type
#
# print ("Examples:",a,b,c,d,e)
# input("\n Press Enter to continue...")
#
# # =======
# #Operators
# # adunare +
# # scădere -
# # înmulțire *
# # împărțire /
# # restul împărțirii %
# # putere **
# # =======
#
# print ("\n Jocul Operatiilor")
#
# x= float(input("\n Primul Numar "))
#
# y= float(input("\n Al doilea numar "))
#
# op= input("\n Introdu un operator ca si string")
#
# operatii = {
#     "+" : x + y,
#     "-" : x - y,
#     "*" : x * y,
#     "/" : x / y,
#     "%" : x % y,
#     "**" : x ** y,
# }
#
# rezultat = operatii.get(op, "Operator Necunoscut")
#
# print(f"\n Rezultatul este : {rezultat}")
input("\n Press Enter to continue...")

# =====
#Assertions
# =====

# a1 = int(input("\n Primul Numar "))
#
# b2 = int(input("\n Al doilea numar "))
#
# print("Ce facem azi...")
#
# # assert a1==b2, "X ! Error a nu este egal cu b"
#
# assert a1 > 100, "Este adevarat"
# assert b2 < 10, "Nu este adevarat"
#
# assert a1 != b2
#

# String Game

print("My String")

name = input("numele meu:")
salut = "Salut" + name
litere = len(name)
mare = name.upper()
mic = name.lower()

print(salut)
print("Numele meu are", litere , "litere")
print("Cu majuscule", mare)
print("Cu litere mici", mic)