#📘 1. Data Types
#Creează o variabilă numar_intreg și dă-i o valoare întreagă.
numar_intreg = 5
#Creează o variabilă numar_zecimal cu un număr float.
numar_zecimal = 10.0
#Stochează în mesaj orice text (de ex: "Hello, Python!").
mesaj = "Salutari din Piton"
#Creează o variabilă activ cu valoarea True și afișeaz-o.
activ = True
print("Valoarea variabilei activ este:", activ)
#Creează o variabilă necunoscut cu valoarea None și printeaz-o.
necunoscut = None
print(necunoscut)

# 🎮 2. Operators

# Folosește +, -, *, /, %, ** și //

a = 5
b = 15

add = a + b
substract = a - b
multiply = a * b
divide = a /b
exponential = a ** b
floor_div = a // b
print("Rezultat adunare:", add)
print("Rezultat scader:", substract)
print("Rezultat inmultire:", multiply)
print("Rezultat impartire:", divide)
print("Rezultat putere:", exponential)
print("Rezultat cat:", floor_div)

# Adună două numere la alegere și afișează rezultatul.
print(2+10)
# Calculează câtul și restul împărțirii dintre 17 și 4.
cat = 17 //4
rest = 17 % 4
print("Catul dintre 17 si 4 este:", cat)
print("Restul dintre 17 si 4 este:", rest)
#Calculează 3 la puterea 4.
exp_4 = 3**4
print(exp_4)
#Afișează dacă 5 este mai mare decât 3.
print("Este 5 mai mare decat 3?:", 5>3)
#Creează două variabile a și b, apoi calculează:
#(a + b) * 2 - a // b
a = 10
b = 10
formula = (a + b) * 2 - a // b
print(formula)


#🕵️‍♂️ 3. Assertions – Exerciții
#Folosește assert pentru a verifica valori.
z = 18
assert z == 18, "z nu este 18"
print("z este 18!")
zz = -5
assert zz < 0, "zz nu este numar negativ"
print("zz este numar negativ")
#Creează două variabile x = 10, y = 5 + 5, și fă assert că sunt egale.
x = 10
y = 5 + 5
assert x == y, "x și y nu sunt egale"

assert 10 > 2, "10 nu este mai mare decât 2"

nume = "Ana"
assert len(nume) == 3, "Lungimea numelui nu este 3"
print("Lungimea numelui este 3")

text = "PYTHON"
assert text.isupper(), "text nu are toate literele mari"
print("text are toate literele mari")

assert float(10) == 10.0, "float(10) nu este egal cu 10.0"
print("Float(10) este egal cu 10.0")

# 🎉 4. Strings – Exerciții

prenume = "Raul"
salut = "Buna, " + prenume
print(salut)
print("Cate litere are prenumele?\nRaspuns:",len(prenume))
print("Prenume cu majuscule:", prenume.upper())
mesaj_complet = "Salut, " + prenume + "!"
print(mesaj_complet)

#🧠 5. Recapitulare – Exerciții Combinate

a = 7
b = 3
sum = a + b
assert sum == 10, "Suma a + b nu este 10!"
print("Suma a + b este 10!")

text = "python"
assert text.lower() == "python" and text != "PYTHON", "Hmm, una din conditii nu este adevarata"
print("Pentru text, ambele asserturi sunt adevarate")

mesaj = "Pasi facuti azi: " + str(2000)
print(mesaj)

salut = "Salut"
nume = "Ioana"
print(salut + " " + nume)

x = 2
y = 3
operatori ={
    "+": x+y,
    "-": x-y,
    "*": x*y
            }

print("Rezultatul x*y folosint un operator din dictionar este:", operatori.get("*"))


