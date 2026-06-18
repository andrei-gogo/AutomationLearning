
#1. Data Types – Exerciții
#Creează o variabilă numar_intreg și dă-i o valoare întreagă.
numar_intreg = 2

#Creează o variabilă numar_zecimal cu un număr float.
numar_zecimal = 3.2

# #Stochează în mesaj orice text (de ex: "Hello, Python!").
mesaj = "Salut!"

#Creează o variabilă activ cu valoarea True și afișeaz-o.
activ = True
print(activ)

##Creează o variabilă necunoscut cu valoarea None și printeaz-o.
valnecunoscut = None
print (valnecunoscut)
#
# 2. Operators – Exerciții
#Folosește +, -, *, /, %, ** și // dacă ai introdus deja.

x=int(input("\n primul numar: "))
y=int(input("\n al 2lea numar: "))

operatii={
    "+": x+y,
    "-": x-y,
    "*": x*y,
    "/": x/y,
    "**": x**y,
    "//": x//y,
    "%": x%y,
}

# #Adună două numere la alegere și afișează rezultatul.
rezultat= operatii.get("+")
print(f"\n rezultatul este: {rezultat}")

#Calculează câtul și restul împărțirii dintre 17 și 4
x=17
y=4
operatii={
    "+": x+y,
    "-": x-y,
    "*": x*y,
    "/": x/y,
    "**": x**y,
    "//": x//y,
    "%": x%y,
}
catul = operatii.get("//")
rest = operatii.get("%")
print(f"\n catul impartirii este: {catul}")
print(f"\n restul impartirii este: {rest}")

#Calculează 3 la puterea 4.
a = 3
b = 4
operatie={
    "+": a+b,
    "-": a-b,
    "*": a*b,
    "/": a/b,
    "**": a**b,
    "//": a//b,
    "%": a%b,
}

rezultat= operatie.get("**")
print (rezultat)

#    Afișează dacă 5 este mai mare decât 3.

assert 5>3
print("5 este mai mare ca 3")

# #Creează două variabile a și b, apoi calculează:
#
a=5
b=7
calcul= (a + b) * 2 - a // b
print (calcul)

#3.Assertions – Exerciții
#Folosește assert pentru a verifica valori.

a=5
b=7
assert b>a
print("este corect")
#
# #Creează două variabile x = 10, y = 5 + 5, și fă assert că sunt egale.
x=10
y=5+5
assert x==y
#
# #Fă assert că 10 > 2.
#
assert 10>2
print("corect again")

#Creează un nume = "Ana" și folosește assert len(nume) == 3.

nume="Ana"
assert len(nume)==3
print("numele are", len(nume), "litere")

#Creează un text = "PYTHON" și verifică text.isupper() cu assert
text = "PYTHON"
assert text.isupper()
print ("true")

#Verifică că float(10) == 10.0 cu assert.

assert float(10) == 10.0
print ("true")

#4. Strings – Exerciții
#Creează o variabilă prenume cu numele tău.

prenume= "Alice"
#
# #Creează salut concatenând "Bună, " + prenume.
#
salut= "Buna" + prenume
#
# #Afișează câte litere are prenume cu len().
#
print("prenumele meu are", len(prenume), "litere")
#
# #Transformă prenume în majuscule și afișează.
majuscule = prenume.upper()
print(majuscule)

# #Creează un mesaj complet: "Salut, " + prenume + "!", apoi afișează-l.
mesaj = "Salut, " + prenume + "!"
print(mesaj)

#5. Recapitulare – Exerciții Combinate

#Creează două variabile a = 7, b = 3, calculează suma și folosește assert că rezultatul este 10.

a=7
b=3
sum= a+b
assert sum==10

#Creează un text = "python" și folosește assert text.lower() == "python" și assert text != "PYTHON".
#
text="python"
assert text.lower()=="python"
assert text != "PYTHON"

# #Afișează un mesaj compus din text și un număr, de exemplu: "Nivel: " + str(5).
print("Nivel: " + str(5))
#
# # Creează un salut = "Salut" și un nume = "Ioana", apoi unește-le cu spațiu între ele.
#
salut = "Salut"
nume="Ioana"

print (salut + " " + nume)

# Fă x = 2, y = 3, și folosește un dicționar de operatori pentru a calcula x * y și afișa rezultatul.

x=2
y=3
inmultire = {
    "*": x*y
}
rezultat = inmultire.get("*", "not found")
print(rezultat)


