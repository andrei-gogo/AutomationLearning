
# TEMA PENTRU ACASA




# 1. Creeaza un dictionar cu datele tale (nume, varsta, oras)
# 2. Foloseste un for loop pentru a parcurge si afisa cheile si valorile
date = {"nume" : "Alex", "varsta" : 33, "oras" : "Baia Mare"}
for n, v in date.items():
    print (n, "-", v)

# 3. Scrie un program care cere un numar si afiseaza daca e par sau impar
number = int(input("Introdu un numar par sau impar: "))
if number % 2 == 0:
        print("nr par:", number)
else:
        print("nr impar:", number)

# 4. Creeaza o lista cu elemente duplicate si elimina-le folosind set
listaduplicate = ["mouse", "mouse", "lanterna", "camera"]
listafaraduplicate = list(set(listaduplicate))
print("lista fara dupes:", listafaraduplicate)

# 5. Foloseste un loop for infinit cu o conditie de oprire (break)
for numere in range(999999999):
    numar = int(input("Introdu un nr: "))
    if numar == 5:
        print("Ai nimerit")
        break
    else:
        print("mai incearca")

# 6. Simuleaza un joc simplu unde introduci doua numere si un operator, si afisezi rezultatul (ca in clasa)
numar_a = int(input("Introdu primul numar: "))
numar_b = int(input("Introdu al2lea  numar: "))
operator = input("Introdu un operator: ")
operatii = {
    "+" : numar_a + numar_b,
    "-" : numar_a - numar_b,
    "*" : numar_a * numar_b,
    "/" : numar_a / numar_b
}
rezultat = operatii.get(operator, "Operator necunoscut")
print("Rezultatul numerelor: ", numar_a, numar_b, "si operatorului", operator, "este: ", rezultat)


# 7. Optional: Incearca sa sortezi un set folosind `sorted()` si explica de ce functioneaza

numere_sortate = {"1", "2", "3", "5"}
numere_sortate.add("4")
numere_sortate.remove("5")
print("numere sortate: ", sorted(numere_sortate))


# # EXERCITII RECAPITULARE
#
# # 1. Tuples - demonstratie imutabilitate
# pozitie = (10, 20)
# print("Pozitie initiala:", pozitie)
# # pozitie[0] = 99  # va da eroare
#
# # 2. Operators Game
# x = float(input("Introdu primul numar: "))
# y = float(input("Introdu al doilea numar: "))
# op = input("Introdu operatorul (+, -, *, /, %, **): ")
# operatii = {
#     "+": x + y,
#     "-": x - y,
#     "*": x * y,
#     "/": x / y,
#     "%": x % y,
#     "**": x ** y
# }
# rezultat = operatii.get(op, "Operator necunoscut")
# print("Rezultatul este:", rezultat)
#
# # 3. Seturi - operatii
# culori = {"rosu", "verde"}
# culori.add("albastru")
# culori.remove("rosu")
# print("Culori actualizate:", sorted(culori))
#
# # 4. Eliminare duplicate din lista
# numere = [1, 2, 2, 3, 4, 4, 5]
# numere_fara_duplicate = list(set(numere))
# print("Fara duplicate:", numere_fara_duplicate)
#
# # 5. Dictionare - parcurgere
# elev = {"nume": "Tudor", "punctaj": 95}
# for k, v in elev.items():
#     print(k, "->", v)
#
# # 6. For loop + else
# cutii = ["cadou", "cadou", "cadou"]
# for cutie in cutii:
#     print("Deschizi o cutie:", cutie)
# else:
#     print("Toate cutiile au fost deschise!")
#
# # 7. Range si paritate
# for n in range(1, 10):
#     if n % 2 == 0:
#         print("Par:", n)
#     else:
#         print("Impar:", n)







