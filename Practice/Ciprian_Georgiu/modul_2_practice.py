# 📘 1. Data Types – Exerciții
#   Creează o variabilă numar_intreg și dă-i o valoare întreagă.
from http.cookiejar import uppercase_escaped_char

numar_intreg = 10
# Creează o variabilă numar_zecimal cu un număr float.
numar_zecimal = 3.14
#   Stochează în mesaj orice text (de ex: "Hello, Python!").
mesaj = "Hello, Python!"
#   Creează o variabilă activ cu valoarea True și afișeaz-o.
activ = True
#   Creează o variabilă necunoscut cu valoarea None și printeaz-o.
necunoscut = None
print(necunoscut)

# 🎮 2. Operators – Exerciții
#
#   Folosește +, -, *, /, %, ** și // dacă ai introdus deja.
a = 2
b = 4
operatii = {
    "inmultire": a * b,
    "scadere": a - b,
    "impartire reala": a / b,
    "restul": a % b,
    "ridicare la putere": a ** b,
    "impartire intreaga": a // b,
}

print(f"Rezultatul este: {operatii}")
#   Adună două numere la alegere și afișează rezultatul.
a = 2
b = 3
adunare = a + b
print(f"Rezultatul adunarii este: {adunare}")
#Calculează câtul și restul împărțirii dintre 17 și 4.
catul: int = 17 // 4
restul: int = 17 % 4
print(f"Catul este: {catul}")
print (f"Restul este: {restul}")
#Calculează 3 la puterea 4.
a = 3
b = 4
rezultat = a ** b
print (f"Rezultaul calculului 3 la puterea 4 este: {rezultat}")
#   Afișează dacă 5 este mai mare decât 3.
a = 5
b = 3
rezultat = a > b
print(rezultat)
#   Creează două variabile a și b, apoi calculează:
a = 2
b = 3
(a + b) * 2 - a // b
rezultat = (a + b) * 2 - a // b
print(f"Rezultatul calcului este: {rezultat}")
# 🕵️‍♂️ 3. Assertions – Exerciții
#   Folosește assert pentru a verifica valori.
##a = 2
##assert a == 3, "2 nu este mai mare decat 3"
#   Creează două variabile x = 10, y = 5 + 5, și fă assert că sunt egale.
x = 10
y = 5 + 5
assert x == y
#   Fă assert că 10 > 2.
assert 10>2
print("10 este mai mare decat 2, deci nu apare o eroare ""AssertionError")
#   Creează un nume = "Ana" și folosește assert len(nume) == 3.
nume = "Ana"
assert len(nume) == 3
print(f"Numele Ana contine {len(nume)} caractere.")
#   Creează un text = "PYTHON" și verifică text.isupper() cu assert.
text = "PYTHON"
assert text.isupper(), "Textul nu este scris cu majuscule."
print("Textul este scris cu majuscule.")
#   Verifică că float(10) == 10.0 cu assert.
assert float(10) == 10.0, "Nu sunt valori egale."
print("Valorile sunt egale.")
#
# 🎉 4. Strings – Exerciții
#
#   Creează o variabilă prenume cu numele tău.
prenume = "Ciprian"
#   Creează salut concatenând "Bună, " + prenume.
prenume = "Ciprian"
print(f"Buna, Georgiu {prenume}.")
#     Afișează câte litere are prenume cu len().
prenume = "Ciprian"
print(f"Prenumele meu are {len(prenume)} caractere.")
#     Transformă prenume în majuscule și afișează.
prenume = "Ciprian"
print(prenume.upper())
#   Creează un mesaj complet: "Salut, " + prenume + "!", apoi afișează-l.
prenume = "Ciprian"
mesaj = "Nu pare asa nasol Python-ul pana acum!"
print(f"Salut, Georgiu {prenume}. {mesaj}")

#
# 🧠 5. Recapitulare – Exerciții Combinate
#
#   Creează două variabile a = 7, b = 3, calculează suma și folosește assert că rezultatul este 10.
a = 7
b = 3
suma = a + b
assert suma == 10, "Rezultatul nu este egal cu 10"
print("Rezultatul este egal cu 10.")
#   Creează un text = "python" și folosește assert text.lower() == "python" și assert text != "PYTHON".
text = "python"
assert text.lower() == "python"
assert text != "PYTHON"
#   Afișează un mesaj compus din text și un număr, de exemplu: "Nivel: " + str(5).
text = "Bucovinei"
numar = 32
print(f"El sta pe strada {text} la numarul {numar}.")
#   Creează un salut = "Salut" și un nume = "Ioana", apoi unește-le cu spațiu între ele.
salut = "Salut"
nume = "Ioana"
print(salut + " " + nume)
#   Fă x = 2, y = 3, și folosește un dicționar de operatori pentru a calcula x * y și afișa rezultatul.
x = 2
y = 3

operatori = {
    "*": x * y
}
rezultat = operatori
print("Rezultatul inmultirii folosint un dictionar de operatori este:", operatori.get("*"))
