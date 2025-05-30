<<<<<<< HEAD
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


# # String Game
#
# print("My String")
#
# name = input("numele meu:")
#
# salut= "salut " + name
# litere = len(name)
# mare = name.upper()
# mic = name.lower()
#
# print(salut)
# print("Numele meu are", litere, "litere")
# print("Cu majusucle", mare)
# print("Cu litere mici", mic)
# #=======

# 🎓 Python - Modul Interactiv pentru Începători (Fără bucle sau condiții)

# =========================
# 1. Data Types
# =========================
print("📘 1. TIPURI DE DATE")
a = 5
b = 3.14
c = "Hello"
d = True
e = None
print("✅ Exemple: ", a, b, c, d, e)
input("\n🔹 Apasă Enter pentru a continua...")

a = 5              # int
b = 3.14           # float
c = "Hello"        # str
d = True           # bool
e = None           # NoneType

# =========================
# 2. Operators Game
# =========================
print("\n🎮 2. JOCUL OPERATORILOR")
x = float(input("📥 Introdu primul număr: "))
y = float(input("📥 Introdu al doilea număr: "))
op = input("⚙️ Introdu operatorul (+, -, *, /, %, **): ")

operatii = {
    "+": x + y,
    "-": x - y,
    "*": x * y,
    "/": x / y,
    "%": x % y,
    "**": x ** y
}
rezultat = operatii.get(op, "Operator necunoscut")
print(f"✅ Rezultatul este: {rezultat}")
input("\n🔹 Apasă Enter pentru a continua...")

# =========================
# 3. Assertion Game
# =========================
print("\n🕵️‍♂️ 3. TESTĂM ASSERT")
a = int(input("📥 Introdu valoarea lui a: "))
b = int(input("📥 Introdu valoarea lui b: "))
print("Facem assert că a == b...")
assert a == b, "❌ Eroare: a NU este egal cu b!"
print("✅ Bravo! a == b este adevărat!")
print("Facem acum un assert că a > 20...")
assert a > 20, "❌ Eroare: a NU este mai mare decât 20!"
print("✅ Wow! a este mai mare decât 20!")
input("\n🔹 Apasă Enter pentru a continua...")

# =========================
# 4. String Game
# =========================
print("\n🎉 4. STRINGURI INTERACTIVE")
nume = input("📥 Introdu-ți numele: ")
salut = "Salut, " + nume
litere = len(nume)
mare = nume.upper()
mic = nume.lower()
print("👋 " + salut)
print("🔢 Numele tău are", litere, "litere.")
print("🔠 Cu MAJUSCULE:", mare)
print("🔡 Cu litere mici:", mic)
input("\n🔹 Apasă Enter pentru a continua...")
#>>>>>>> a176bb7a33575878736b4a8fddcc628bd3c895ac

