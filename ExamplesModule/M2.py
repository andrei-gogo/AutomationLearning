# print("Tipuri de date")
#
# a= 10 #int
# b= 99.12 #float
# c= "Mesaj despre Python" #string
# d= True #bool
# e= None #None Type
#
# print("Examples:" ,a,b,c,d,e)
# input("\n Press Enter to continue...")


# =====
#Operators
# =====

# print("\n Jocul Operatiilor")
#
# x = float(input("\n Primul numar: "))
# y = float(input("\n Second numar: "))
# op = input("\n Introdu un operator: ")
#
# operatii ={
#     "+": x+y,
#     "-": x-y,
#     "*": x*y,
#     "/": x/y,
#     "//": x//y,
#     "**": x**y,
#     "%": x%y,
# }
#
# rezultat = operatii.get(op, "Operator Necunoscut")
#
# print(f"\n Rezultatul este: {rezultat}")
# input("\n Press Enter to continue...")


# =========
# Jocul Asertiilor
# ========

# print("\n TESTĂM ASSERT")
#
# a = int(input(" Introdu valoarea lui a: "))
# b = int(input(" Introdu valoarea lui b: "))
#
# print("Facem assert că a == b...")
#
# assert a == b or a>60, " Eroare: a NU este mai mare decât 60!"
#
# input("\n Apasă Enter pentru a continua...")

#String game

print("My string")

name =input("numele meu:")

salut= "Salut " + name
litere = len(name)
mare = name.upper()
mic = name.lower()

print( salut)
print( "Numele meu are" ,litere, "litere")
print("Cu Majuscule",mare)
print("Cu litere mici",mic)