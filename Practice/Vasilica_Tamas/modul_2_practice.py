#------------------📘 1.Data Types – Exerciții------------------

#Creează o variabilă numar_intreg și dă-i o valoare întreagă.
numar_intreg = 2

#Creează o variabilă numar_zecimal cu un număr float.
numar_zecimal = 2.2

#Stochează în mesaj orice text (de ex: "Hello, Python!").
mesaj = "Hello, Python!"

#Creează o variabilă activ cu valoarea True și afișeaz-o.
activ = True
print(activ)

#Creează o variabilă necunoscut cu valoarea None și printeaz-o.
necunoscut = None
print(necunoscut)


#----------------🎮 2. Operators – Exerciții-------------------

#Folosește +, -, *, /, %, ** și // dacă ai introdus deja.
#Adună două numere la alegere și afișează rezultatul.
print("Suma numerelor 47 si 68 este: ", 44+77)

#Calculează câtul și restul împărțirii dintre 17 și 4.
print("In urma impartirii numarului 17 la 4 rezulta catul:", 17//4, " si restul:", 17%4)

#Calculează 3 la puterea 4.
print("3 la puterea 4 este:", 3**4)

#Afișează dacă 5 este mai mare decât 3.
#assert 5>3
#print("5>3")
a = 5>3

#Creează două variabile a și b, apoi calculează:
#(a + b) * 2 - a // b
a= 5
b= 7
print("Rezultatul exercitiiului (a + b) * 2 - a // b este: ",(a + b) * 2 - a // b)


#------------🕵️‍♂️ 3. Assertions – Exerciții------------------

#Folosește assert pentru a verifica valori.
# Creează două variabile x = 10, y = 5 + 5, și fă assert că sunt egale.
x= 10
y= 5+5
assert x==y, "Eroare: x si y nu sunt egale!"

# Fă assert că 10 > 2.
assert 10>2, "Eroare: 10 nu este mai mare decat 2!"

# Creează un nume = "Ana" și folosește assert len(nume) == 3.
nume = "Ana"
assert len(nume) == 3, "Numele nu are lungimea de 3"

# Creează un text = "PYTHON" și verifică text.isupper() cu assert.
text = "PYTHON"
assert text.isupper(), "Textul nu este scris cu majuscule"

# Verifică că float(10) == 10.0 cu assert.
assert float(10) == 10.0, "Egalitatea nu este adevarata"

#----------------🎉 4. Strings – Exerciții-------------------

# Creează o variabilă prenume cu numele tău.
prenume = "Vasilica"

# Creează salut concatenând "Bună, " + prenume.
print("Bună, ", prenume)

# Afișează câte litere are prenume cu len().
print(len(prenume))

# Transformă prenume în majuscule și afișează.
prenume1 = prenume.upper()
print(prenume1)

# Creează un mesaj complet: "Salut, " + prenume + "!", apoi afișează-l
print("Salut, ", prenume, "!")


#-----------------🧠 5. Recapitulare – Exerciții Combinate------------------

# Creează două variabile a = 7, b = 3, calculează suma și folosește assert că rezultatul este 10.
a = 7
b =3
c= a+b
assert c==10, "Suma numerelor a si b este diferita de 10"

# Creează un text = "python" și folosește assert text.lower() == "python" și assert text != "PYTHON".
text = "python"
assert text.lower() == "python", "Cuvantul nu este scris cu majuscule"
assert text != "PYTHON", "Cuvantul este scris cu majuscule"

# Afișează un mesaj compus din text și un număr, de exemplu: "Nivel: " + str(5).
print("Nivel: ", str(5))

# Creează un salut = "Salut" și un nume = "Ioana", apoi unește-le cu spațiu între ele.
salut = "Salut"
nume = "Ioana"
rez = salut + " " + nume
print(rez)

# Fă x = 2, y = 3, și folosește un dicționar de operatori pentru a calcula x * y și afișa rezultatul.
x = 2
y = 3
operatie = {
    "*": x * y
}
print(operatie["*"])

# Viitoarea tema