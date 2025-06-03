# ========
# 1. Data Types
# ========
"""
# Creează o variabilă numar_intreg și dă-i o valoare întreagă.
număr_întreg = 10

# Creează o variabilă numar_zecimal cu un număr float
număr_zecimal = 3.14

# Stochează în mesaj orice text (de ex: "Hello, Python!").
mesaj = "Hello, Python!"

# Creează o variabilă activ cu valoarea True și afișeaz-o
activ = True
print(activ)

# Creează o variabilă necunoscut cu valoarea None și printeaz-o
necunoscut = None
print(necunoscut)
"""
"""
# ========
# 2. Operators
# ========

# Adună două numere la alegere și afișează rezultatul.
a1 = 5
b1 = 6
print("Rezultatul adunarii 5+6 este:", a1 + b1)

# Calculează câtul și restul împărțirii dintre 17 și 4.
print("Câtul împărțirii 17//4 este:", 17 // 4)
print("Restul împărțirii 17 % 4 este:", 17 % 4)

# Calculează 3 la puterea 4.
print("Puterea 3 ** 4 este:", 3 ** 4)

# Afișează dacă 5 este mai mare decât 3.
print("Este 5 mai mare decât 3?", 5 > 3)

# Creează două variabile a și b, apoi calculează expresia (a + b) * 2 - a // b.
a = 20
b = 3
rezultat = (a + b) * 2 - a // b
print("Daca a =20 si b=3, rezultatul expresiei: (a + b) * 2 - a // b este:", rezultat)
"""

# ========
# 3. Assertions
# ========

"""# Creează două variabile x = 10, y = 5 + 5, și fă assert că sunt egale.
x = 10
y = 5 + 5
assert x == y, "x și y nu sunt egale!"

# Fă assert că 10 > 2.
assert 10 > 2, "10 nu este mai mare decât 2!"

# Creează un nume = "Ana" și folosește assert len(nume) == 3.
nume = "Ana"
assert len(nume) == 3, "Lungimea numelui nu este 3!"

# Creează un text = "PYTHON" și verifică text.isupper() cu assert.
text = "PYTHON"
assert text.isupper(), "Textul nu este complet cu majuscule!"

# Verifică că float(10) == 10.0 cu assert.
assert float(10) == 10.0, "Conversia float nu este corectă!"

print("Toate verificările au fost trecute cu succes!")"""

# ========
# 4. Strings
# ========

"""# Creează o variabilă prenume cu numele tău.
prenume = "Simona"

# Creează salut concatenând "Bună, " + prenume.
salut = "Bună, " + prenume
print(salut)

# Afișează câte litere are prenume cu len().
print("Numărul de litere:", len(prenume))

# Transformă prenume în majuscule și afișează.
print("Prenume în majuscule:", prenume.upper())

# Creează un mesaj complet: "Salut, " + prenume + "!", apoi afișează-l.
mesaj = "Salut, " + prenume + "!"
print(mesaj)"""

# ========
# 5. Recapitulare
# ========

"""# Creează două variabile a = 7, b = 3, calculează suma și folosește assert că rezultatul este 10.
a = 7
b = 3
suma = a + b
assert suma == 10, "Suma nu este corectă!"
print("Suma:", suma)

# Creează un text = "python" și folosește assert text.lower() == "python" și assert text != "PYTHON".
text = "python"
assert text.lower() == "python", "Textul nu este convertit corect!"
assert text != "PYTHON", "Textul este incorect!"
print("Text:", text)

# Afișează un mesaj compus din text și un număr, de exemplu: "Nivel: " + str(5).
nivel = 5
mesaj = "Nivel: " + str(nivel)
print(mesaj)

# Creează un salut = "Salut" și un nume = "Ioana", apoi unește-le cu spațiu între ele.
salut = "Salut"
nume = "Ioana"
mesaj = salut + " " + nume
print(mesaj)

# Fă x = 2, y = 3, și folosește un dicționar de operatori pentru a calcula x * y și afișeazǎ rezultatul.
x = 2
y = 3
operatori = {
    "*": x * y
}
print("Rezultatul lui x * y:", operatori["*"]) """
