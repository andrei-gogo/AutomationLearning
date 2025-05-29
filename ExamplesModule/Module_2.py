# print ("Tipuri de date")
#
# a = 10 #Int
# b = 99.12 #Float
# c = 'Eu sunt Python Expert now' #String
# d = True
# e = None
#
# print ("Examples:", a,b,c,d,e)
# input("\n Apasa enter pentru a continua ...")
#
#
# # ========
# #Operators
# # adunare +
# # scădere -
# # înmulțire *
# # împărțire /
# # restul împărțirii %
# # putere **
# # ========
#
# print("\n Jocul Operatiilor")
#
# x = float (input("\n Primul numar:"))
#
# y = float (input("\n Al doilea numar:"))
#
# op = input ("\n Introdu un operator ca string")
#
# operatii = {
#     "+" : x + y,
#     "-" : x - y,
#     "/": x / y,
#     "//": x + y,
#     "*": x + y,
#     "%": x % y,
#     "**": x ** y,
# }
#
#
# rezultat = operatii.get(op, "Operator Necunoascut")
#
# print (f"\n Rezultatul este: {rezultat}")
# input("\n Apasa enter pentru a continua....")

# =====
# Asserions
# # =====
#
# a1 = int(input("\n Primul numar:"))
# b2 = int(input("\n Al doile numar:"))
#
# print("assert a == b ...")
#
# # assert a1==b2, " X ! Error a nu este egal cu b "
#
# assert a1 > 100 , "Este adevarat"
# assert b2 < 10 "nu este adevarat"
# assert a1 != b2
# assert

# String Game

print("My Stirng")
name = input("numele meu:")
salut = "Salut" + name
litere = len(name)
mare = name.upper()
mic = name.lower()

print(salut)
print("numale meu are", litere, "litere")
print("Cu majuscule", mare)
print("Cu litere mici", mic)