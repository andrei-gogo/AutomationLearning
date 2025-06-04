# 📘 1. Data Types – Exerciții
#
#     Creează o variabilă numar_intreg și dă-i o valoare întreagă.
# print("Variabila numar intreg")
# x = int(input("\n Variabila numar intreg: ")) #variabila numar intreg
# print(f"\n Introdu o variabila cu numar intreg este: {x}")
# input("\n Press Enter to continue...")

#     Creează o variabilă numar_zecimal cu un număr float.
# print("Variabila numar float")
# y = float(input("\n Variabila numar float: ")) #variabila numar intreg
# print(f"\n Variabila cu numar float este: {y}")
# input("\n Press Enter to continue...")

#     Stochează în mesaj orice text (de ex: "Hello, Python!").

# print("Mesaj cu text")
# print("Hello Python! by Raluca")

#     Creează o variabilă activ cu valoarea True și afișeaz-o.
# z= True
# print("Variabila booleana:" ,z)
#     Creează o variabilă necunoscut cu valoarea None și printeaz-o.
# w= None
# print("Variabila necunoscut:" ,w)

# 🎮 2. Operators – Exerciții
#
#     Folosește +, -, *, /, %, ** și // dacă ai introdus deja.

# operatii ={
# #      "+": x+y,
# #      "-": x-y,
# #      "*": x*y,
# #      "/": x/y,
# #      "//": x//y,
# #      "**": x**y,
# #      "%": x%y,
# #
# #  }

#     Adună două numere la alegere și afișează rezultatul.
# x = int(input("\n Primul numar: "))
# y = int(input("\n  Numar doi: "))
# op = input("\n Introdu un operator: ")
#
# operatii ={
#      "+": x+y,
#      "-": x-y,
#      "*": x*y,
#      "/": x/y,
#      "//": x//y,
#      "**": x**y,
#      "%": x%y,
#
#  }
#
# rezultat = operatii.get(op, "Operator Necunoscut")
#
# print(f"\n Rezultatul este: {rezultat}")

#     Calculează câtul și restul împărțirii dintre 17 și 4.
# a= 17
# b= 4
# op = input("\n Introdu un operator: ")
#
# operatii ={
#     "/": a/b,
# }
# rezultat = operatii.get(op, "Operator Necunoscut")
# print(f"\n Rezultatul este: {rezultat}")

#     Calculează 3 la puterea 4.
# a= 3
# b= 4
# op = input("\n Introdu un operator: ")
#
# operatii ={
#     "**": a**b,
# }
# rezultat = operatii.get(op, "Operator Necunoscut")
# print(f"\n Rezultatul este: {rezultat}")

#     Afișează dacă 5 este mai mare decât 3.
# a = int(input(" Introdu valoarea lui a: "))
# b = int(input(" Introdu valoarea lui b: "))
#
# print("Facem assert că 5 > 3...")
#
# assert a>b, "X! Error: 5 nu este mai mare ca 3!"

#     Creează două variabile a și b, apoi calculează:
#     (a + b) * 2 - a // b
# a = int(input("\n Numarul A: "))
# b = int(input("\n  Numarul B: "))
#
# rezultat = (a + b) * 2 - (a // b)
# print(f"\nRezultatul (a + b) * 2 - a // b este egal cu: {rezultat}")
# input("\n Press Enter to continue...")

# 🕵️‍♂️ 3. Assertions – Exerciții
#
#     Folosește assert pentru a verifica valori.
# a = int(input(" Introdu valoarea lui a: "))
# b = int(input(" Introdu valoarea lui b: "))
#
# print("Facem assert că a == b...")
#
# assert a==b, "X! Error: a nu este egal cu b!"
# input("\n Press Enter to continue...")


#     Creează două variabile x = 10, y = 5 + 5, și fă assert că sunt egale.
# x=10
# y=5+5
# print("Facem assert că x == y...")
#
# assert x==y, "X! Error: x nu este egal cu y!"
# input("\n Press Enter to continue...")


#     Fă assert că 10 > 2.
# x=10
#
# print("Facem assert că 10 > 2 ...")
#
# assert x>2, "X! Error: x nu este mai mare decat 2!"
# input("\n Press Enter to continue...")

#     Creează un nume = "Ana" și folosește assert len(nume) == 3.

# print("Length of name")
#
# name =input("numele:")
#
# litere = len(name)
# print( "Numele are" ,litere, "litere")
# input("\n Press Enter to continue...")

#     Creează un text = "PYTHON" și verifică text.isupper() cu assert.
# print("Text cu majuscule")
#
# text ="PYTHON"
#
# assert text.isupper()==True, "X Error: Textul nu e cu cu majuscule"
# input("\n Press Enter to continue...")


#     Verifică că float(10) == 10.0 cu assert.


#
# 🎉 4. Strings – Exerciții
#
#     Creează o variabilă prenume cu numele tău.
#     Creează salut concatenând "Bună, " + prenume.
#     Afișează câte litere are prenume cu len().
#     Transformă prenume în majuscule și afișează.
#     Creează un mesaj complet: "Salut, " + prenume + "!", apoi afișează-l.
#
# 🧠 5. Recapitulare – Exerciții Combinate
#
#     Creează două variabile a = 7, b = 3, calculează suma și folosește assert că rezultatul este 10.
#     Creează un text = "python" și folosește assert text.lower() == "python" și assert text != "PYTHON".
#     Afișează un mesaj compus din text și un număr, de exemplu: "Nivel: " + str(5).
#     Creează un salut = "Salut" și un nume = "Ioana", apoi unește-le cu spațiu între ele.
#     Fă x = 2, y = 3, și folosește un dicționar de operatori pentru a calcula x * y și afișa rezultatul.