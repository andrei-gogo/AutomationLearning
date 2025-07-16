#
# # 🎓 Python - Modul Interactiv pentru Începători (Fără bucle sau condiții)
#
# # =========================
# # 1. Data Types
# # =========================
# print("📘 1. TIPURI DE DATE")
# a = 5
# b = 3.14
# c = "Hello"
# d = True
# e = None
# print("✅ Exemple: ", a, b, c, d, e)
# input("\n🔹 Apasă Enter pentru a continua...")
#
# a = 5              # int
# b = 3.14           # float
# c = "Hello"        # str
# d = True           # bool
# e = None           # NoneType
#
# # =========================
# # 2. Operators Game
# # =========================
# print("\n🎮 2. JOCUL OPERATORILOR")
# x = float(input("📥 Introdu primul număr: "))
# y = float(input("📥 Introdu al doilea număr: "))
# op = input("⚙️ Introdu operatorul (+, -, *, /, %, **): ")
#
# operatii = {
#     "+": x + y,
#     "-": x - y,
#     "*": x * y,
#     "/": x / y,
#     "%": x % y,
#     "**": x ** y
# }
# rezultat = operatii.get(op, "Operator necunoscut")
# print(f"✅ Rezultatul este: {rezultat}")
# input("\n🔹 Apasă Enter pentru a continua...")
#
# # =========================
# # 3. Assertion Game
# # =========================
# print("\n🕵️‍♂️ 3. TESTĂM ASSERT")
# a = int(input("📥 Introdu valoarea lui a: "))
# b = int(input("📥 Introdu valoarea lui b: "))
# print("Facem assert că a == b...")
# assert a == b, "❌ Eroare: a NU este egal cu b!"
# print("✅ Bravo! a == b este adevărat!")
# print("Facem acum un assert că a > 20...")
# assert a > 20, "❌ Eroare: a NU este mai mare decât 20!"
# print("✅ Wow! a este mai mare decât 20!")
# input("\n🔹 Apasă Enter pentru a continua...")
#
# # =========================
# # 4. String Game
# # =========================
# print("\n🎉 4. STRINGURI INTERACTIVE")
# nume = input("📥 Introdu-ți numele: ")
# salut = "Salut, " + nume
# litere = len(nume)
# mare = nume.upper()
# mic = nume.lower()
# print("👋 " + salut)
# print("🔢 Numele tău are", litere, "litere.")
# print("🔠 Cu MAJUSCULE:", mare)
# print("🔡 Cu litere mici:", mic)
# input("\n🔹 Apasă Enter pentru a continua...")

#====================
#5. List Game's
#===================


# # Cos de cumparaturi
#
# cos = ["banane", "mere"]
#
# cos.append("zmeura")
#
# print("Am adaugat in cos zmeura. Cosul actualizat este", cos)
#
# cos.remove("zmeura")
#
# print("Am scos un produs din cos:", cos)
# print(cos[1])
#
# # Avioane
#
# avioane = ["F16", "Boeing737", "AirbusA380"]
#
# print("Avioanele din hangar sunt:", avioane)
#
# print(avioane[1])
# del avioane[1]
# print(avioane)
#
# decolat = avioane.pop(1)
# print(decolat)
#
# print(avioane)
# avioane.append(decolat)
# print(avioane)
#


#====================
#5. Tuples / Sets - Jocuri
#===================

#Radare de coordonare

# pozitie_avioane = (45,88)
#
# print("Radarul a detectat avioanele la urmatoarele coordonate:" , pozitie_avioane)
#
# print("latitudine x =", pozitie_avioane[0], " ~ long Y =", pozitie_avioane[1])
#
# pozitie_lista_tuppelsz = list(pozitie_avioane)
# pozitie_lista_tuppelsz[0] = 99
# pozitie_avioane = tuple(pozitie_lista_tuppelsz)
#
# print("modificare tupple si pozitioe avioane", pozitie_avioane)


# culori_unice = {"rosu", "albastru", "galben", "verde", "gri"}
#
# print("This is my set of colors:", culori_unice)
# culori_unice.add("verde")
#
# print("Culori unnice modificate", culori_unice)
#
# culori_unice.add("negru")
# print("ai descoperit o noua culoare", culori_unice)
#
# culori_unice.remove("albastru")
# print("ai stres culoare", culori_unice)
#
# print("vreau pozitia culorii", "galben" in culori_unice)
#
# culori_extra = {"violet", "roz"}
# toate_culorile = culori_unice.union(culori_extra)
#
# print("am adaugat inca 2 culori", toate_culorile)
#
# culori_sortate = sorted(toate_culorile)
# print("culori sortate", culori_sortate)
#
# culori_descrescator = sorted(toate_culorile, reverse=True)
# print("culori sortate", culori_descrescator)


# elev = {"nume": "Andrei", "punctaj_test": 67, "varsta": 12}
#
#
# print("Fisa elev", elev)
# print("Rezultat la test:",elev["punctaj_test"])
#
# elev["clasa"] = "a IV-a"
#
# print("Profil Nou", elev)
#
# elev (punctaj)


