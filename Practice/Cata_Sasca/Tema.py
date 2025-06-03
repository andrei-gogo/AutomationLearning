# 📘 1. Data Types – Exerciții
#from xml.etree.ElementTree import ProcessingInstruction

#    Creează o variabilă numar_intreg și dă-i o valoare întreagă.
numar_intreg = 20
#   Creează o variabilă numar_zecimal cu un număr float.
numar_zecimal = 1.5
#    Stochează în mesaj orice text (de ex: "Hello, Python!").
mesaj = "Hello, Python!"

#   Creează o variabilă activ cu valoarea True și afișeaz-o.
activ = True
print(activ)

    #Creează o variabilă necunoscut cu valoarea None și printeaz-o.
unknown = None
print(unknown)

# 🎮 2. Operators – Exerciții

#   Folosește +, -, *, /, %, ** și // dacă ai introdus deja.
#   Adună două numere la alegere și afișează rezultatul.
plus = 2 + 3
print(plus)

#  Calculează câtul și restul împărțirii dintre 17 și 4.

Cat = 17 / 4
Restul = 17 % 4

#    Calculează 3 la puterea 4.

Putere = 3 ** 4

#    Afișează dacă 5 este mai mare decât 3.

Diferenta_numere = 5 > 3
print(Diferenta_numere)

#    Creează două variabile a și b, apoi calculează: (a + b) * 2 - a // b

a = 2
b = 3
c = (a+b) * 2 - a // b

#🕵️‍♂️ 3. Assertions – Exerciții

#    Folosește assert pentru a verifica valori.
#   Creează două variabile x = 10, y = 5 + 5, și fă assert că sunt egale.

x = 10
y = 5 + 5
assert x == y

#   Fă assert că 10 > 2.

assert (10 > 2)

#    Creează un nume = "Ana" și folosește assert len(nume) == 3.

nume = "Ana"
assert len(nume) == 3

#    Creează un text = "PYTHON" și verifică text.isupper() cu assert.

text = "PYTHON"
assert text.isupper()

#    Verifică că float(10) == 10.0 cu assert.

assert float(10) == 10.0

# 🎉 4. Strings – Exerciții

#    Creează o variabilă prenume cu numele tău.

prenume = "Cata"

#    Creează salut concatenând "Bună, " + prenume.

Salut = ("Buna," + prenume)

#    Afișează câte litere are prenume cu len().

print(len(prenume))

#    Transformă prenume în majuscule și afișează.

majuscule= prenume.upper()
print(majuscule)

#    Creează un mesaj complet: "Salut, " + prenume + "!", apoi afișează-l.
mesaj_complet = ("Salut," + prenume + "!")
print (mesaj_complet)

#🧠 5. Recapitulare – Exerciții Combinate

#    Creează două variabile a = 7, b = 3, calculează suma și folosește assert că rezultatul este 10.

a=7
b=3
sum = a + b
assert sum == 10

#    Creează un text = "python" și folosește assert text.lower() == "python" și assert text != "PYTHON".

text = "python"
assert text.lower() == "python"
assert text != "PYTHON"

#    Afișează un mesaj compus din text și un număr, de exemplu: "Nivel: " + str(5).

text_si_numar = "Nivel:" + str(5)
print(text_si_numar)

#    Creează un salut = "Salut" și un nume = "Ioana", apoi unește-le cu spațiu între ele.

Salut = "Salut"
Numele = "Ioana"
print(Salut + "_" + Numele)

#    Fă x = 2, y = 3, și folosește un dicționar de operatori pentru a calcula x * y și afișa rezultatul.

multiplicare = "*"
x=2
y=3
print(x * y)