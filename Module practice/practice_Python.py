print("Tipuri de date")

a= 10 #int
b= 12.2 #float
c= "doesn't metter" #string
d= True #boolean
e= None #non type

print("Examples:", a, b, c, d, e)
input("\n Apasa Enter pentru a continua....") #input pt a invita la o actiune in timp ce se ruleaza codul

# ======
#Operators
# ======


# adunare +
# scădere -
# înmulțire *
# împărțire /
# impartire intreaga //
# restul împărțirii %
# putere **
# ======

print("\n Jocul Operatiilor")

x = float(input("\n Primul numar:"))

y = float(input("\n Al doilea numar:"))

op = input("\n Introdu un operator ca si string")

operatii={
    "+": x+y,
    "-": x-y,
    "*": x*y,
    "/": x/y,
    "//": x//y,
    "%": x%y,
    "**": x**y,
}

rezultat=operatii.get(op, "Operator Necunoscut")

print(f"\n Rezultatul este: {rezultat}")
input("\n Apasa Enter pentru a continua....")

# ======
#Asserions
# ======

a1 = int(input("\n Primul numar:"))

b2 = int(input("\n Al doilea numar:"))

print("Assert a ==b ...")

assert a1==b2, "X! error a1 nu este egal cu b2"

assert a1>120, "Este adevarat!"
assert b2<10, "Nu este adevarat!"

# ======
#String Game
# ======

print("My string")

name = input("numele meu:")
salut = "Salut" + name
litere = len(name)
mare = name.upper()
mic = name.lower()

print(salut)
print("Numele meu are:", litere, "litere")
print("Cu majuscule", mare)
print("Cu minuscule", mic)

