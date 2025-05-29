print("Tipuri de date")


a= 10 # Int
b= 99.12 # Float
c= "Eu sunt Python" # String
d= True # Boolean
e= None # NoneType

print("Examples:",a,b,c,d,e)
input("\n Apasa enter pentru a continua...")

# ======
#Operators
# adunare +
# scădere -
# înmulțire *
# împărțire /
# restul împărțirii %
# putere **
# ======

print("\n Jocul Operatiilor")
x = float(input("\n Primul numar:"))

y = float(input("\n Al doilea numar:"))

op = input("\n Introdu un operator ca si string:")

operatii = {
    "+" : x + y,
    "-" : x - y,
    "*" : x * y,
    "/" : x / y,
    "//" : x // y,
    "%" : x % y,
    "**" : x ** y,
}

rezultat = operatii.get(op, "Operator necunoscut")

print(f"\n Rezultat este: {rezultat}")
input("\n Apasa enter pentru a continua...")


# ======
# Assertions
# ======

a1 = int(input("\n Primul numar:"))
b2 = int(input("\n Al doilea numar:"))

print("Ce facem azi")

assert a1 == b2 , " X ! Error a nu este egal cu b"

assert b2 < 10, "Nu este adevarat"



# String Game

print("My String")

name = input("\n numele meu:")
salut = "Salut" + name
litere = len(name)
mare = name.upper()
mic = name.lower()

print(salut)
print("Numele meu are", litere, "litere")
print("Cu Majuscule", mare)
print("Cu litere mici", mic)