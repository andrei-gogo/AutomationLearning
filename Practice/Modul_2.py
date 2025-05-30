# print("Tipuri de date")
#
# a= 10 #int
# b= 99.12 #float
# c= "this is python training" #string
# d= True #boolean
# e= None #non-type
#
# print(f"Examples:",{a},{b},{c},{d},{e})
# #input("\n Apasa enter pentru a continua ...")
#
# ########
# #Operators
# ########
#
# # adunare +
# # scădere -
# # înmulțire *
# # împărțire /
# # restul împărțirii %
# # putere **
#
# print("\n Jocul Operatiilor")
#
# x = float(input("\n Scrie valoare pt X: "))
#
# y = float(input("\n Scrie valoare pt Y: "))
#
# op = input("\n Introdu operator: ")
#
# operatii = {
#     "+" : x+y,
#     "-" : x-y,
#     "*" : x*y,
#     "/" : x/y,
#     "%" : x%y,
#     "**" : x**y,
# }
#
# rezultat = operatii.get(op, "Operator Necunoscut")
#
# print(f"\n Rezultatul este: {rezultat}")
# input("\n Apasa enter pentru a continua ...")

########
#Assertions
########

# a1 = int(input("\n Primul nr: "))
#
# b1 = int(input("\n Al doilea nr: "))
#
# print("Assertia a este egal cu b ...")
# #multiple rules can be done for 1 assert
# #assert a1==b1 , "Eroare, a nu este egal cu b"
# #
# # assert a1>100 , "Este adevarat"
# # assert b1<10 , "hai ca mai poti"
#
# assert a1==b1 and a1 > 100 or b > 50, "Eroare, a nu este egal cu b"


########
#String Game
########

print("My String")
name = input("numele meu: ")

salut = "Salut " + name + "!"

litere = len(name)
mare = name.upper()
mic = name.lower()

print(salut)
print("Numele meu are", litere, "litere.")
print("Cu majuscule", mare)
print("Cu litere mici ", mic)