#  1. Data Types – Exerciții
#     Creează o variabilă numar_intreg și dă-i o valoare întreagă.
numar_intreg = 10
#     Creează o variabilă numar_zecimal cu un număr float.
numar_zecimal = 10.99
#     Stochează în mesaj orice text (de ex: "Hello, Python!").
mesaj = "Hello, Python!"
#     Creează o variabilă activ cu valoarea True și afișeaz-o.
activ = True
print(activ)
#     Creează o variabilă necunoscut cu valoarea None și printeaz-o.
necunoscut = None
print(necunoscut)
#
# 🎮 2. Operators – Exerciții
x = 10
y = 15
#     Folosește +, -, *, /, %, ** și // dacă ai introdus deja.
#     Adună două numere la alegere și afișează rezultatul.
print("Suma dintre x si y este: ",x + y)
#     Calculează câtul și restul împărțirii dintre 17 și 4.
print("Catul este: ", 17//4,", iar restul este: ", 17%4)
#     Calculează 3 la puterea 4.
print("3 la puterea 4 este: ",3**4)
#     Afișează dacă 5 este mai mare decât 3.
print(5>3)
#     Creează două variabile a și b, apoi calculează:
a = 5
b = 3
rezultat = (a+b) * 2 - a//b
#     (a + b) * 2 - a // b
print("Rezultatul complet este: ",rezultat)

# 🕵️‍♂️ 3. Assertions – Exerciții
#     Folosește assert pentru a verifica valori.
#     Creează două variabile x = 10, y = 5 + 5, și fă assert că sunt egale.
x = 10
y = 5+5
assert x==y, "Valorile nu sunt egale"
#     Fă assert că 10 > 2.
assert 10 > 2, "categoric fals"
#     Creează un nume = "Ana" și folosește assert len(nume) == 3.
nume = "Ana"
assert len(nume) == 3, "Numele are mai mult de 3 litere"
#     Creează un text = "PYTHON" și verifică text.isupper() cu assert.
text = "PYTHON"
assert text.isupper() == True , "textul nu e scris tot cu majuscule"
#     Verifică că float(10) == 10.0 cu assert.
assert float(10) == 10.0, "rezultatul nu e adevarat"
#
# 🎉 4. Strings – Exerciții
#
#     Creează o variabilă prenume cu numele tău.
prenume = "Baica"
#     Creează salut concatenând "Bună, " + prenume.
print(f"\n Buna, {prenume}!")
#     Afișează câte litere are prenume cu len().
print(f"Prenumele are {len(prenume)} litere.")
#     Transformă prenume în majuscule și afișează.
print(prenume.upper())
#     Creează un mesaj complet: "Salut, " + prenume + "!", apoi afișează-l.
print(f"\n Salut, {prenume}!")
#
# 🧠 5. Recapitulare – Exerciții Combinate
#
#     Creează două variabile a = 7, b = 3, calculează suma și folosește assert că rezultatul este 10.
a = 7
b = 3
suma = a+b
assert suma == 10, "Suma nu este 10"
#     Creează un text = "python" și folosește assert text.lower() == "python" și assert text != "PYTHON".
text = 'python'
assert text.lower() == "python" and text != "PYTHON", "Testul cade pentru ca nu implineste ambele conditii."
#     Afișează un mesaj compus din text și un număr, de exemplu: "Nivel: " + str(5).
print("Te afli la etajul ",str(10),".")
#     Creează un salut = "Salut" și un nume = "Ioana", apoi unește-le cu spațiu între ele.
salut = "Salut"
nume = "Ioana"
print(f"{salut} {nume}!")


#     Fă x = 2, y = 3, și folosește un dicționar de operatori pentru a calcula x * y și afișa rezultatul.
x = 2
y = 3
op = input("\n Introdu operator: ")
operatii = {
    "+" : x+y,
    "-" : x-y,
    "*" : x*y,
    "/" : x/y,
    "%" : x%y,
    "**" : x**y,
    "//" : x//y,
}
rezultat = operatii.get(op, "Operator Necunoscut")

print(f"\n Rezultatul operatiei tale este: {rezultat}, dar oricum x ori y este ", operatii.get("*"))