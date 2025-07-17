
# 🎓 Python - Modul Interactiv pentru Începători (Fără bucle sau condiții)

# =========================
# 1. Data Types
# =========================
#print("📘 1. TIPURI DE DATE")
#a = 5
#b = 3.14
#c = "Hello"
#d = True
#e = None
#print("✅ Exemple: ", a, b, c, d, e)
#input("\n🔹 Apasă Enter pentru a continua...")

#a = 5              # int
#b = 3.14           # float
#c = "Hello"        # str
#d = True           # bool
#e = None           # NoneType

# =========================
# 2. Operators Game
# =========================
#print("\n🎮 2. JOCUL OPERATORILOR")
#x = float(input("📥 Introdu primul număr: "))
#y = float(input("📥 Introdu al doilea număr: "))
#op = input("⚙️ Introdu operatorul (+, -, *, /, %, **): ")

#operatii = {
#    "+": x + y,
#    "-": x - y,
#    "*": x * y,
#    "/": x / y,
#    "%": x % y,
#    "**": x ** y
#}
#rezultat = operatii.get(op, "Operator necunoscut")
#print(f"✅ Rezultatul este: {rezultat}")
#input("\n🔹 Apasă Enter pentru a continua...")

# =========================
# 3. Assertion Game
# =========================
#print("\n🕵️‍♂️ 3. TESTĂM ASSERT")
#a = int(input("📥 Introdu valoarea lui a: "))
#b = int(input("📥 Introdu valoarea lui b: "))
#print("Facem assert că a == b...")
#assert a == b, "❌ Eroare: a NU este egal cu b!"
#print("✅ Bravo! a == b este adevărat!")
#print("Facem acum un assert că a > 20...")
#assert a > 20, "❌ Eroare: a NU este mai mare decât 20!"
#print("✅ Wow! a este mai mare decât 20!")
#input("\n🔹 Apasă Enter pentru a continua...")

# =========================
# 4. String Game
# =========================
#print("\n🎉 4. STRINGURI INTERACTIVE")
#nume = input("📥 Introdu-ți numele: ")
#salut = "Salut, " + nume
#litere = len(nume)
#mare = nume.upper()
#mic = nume.lower()
#print("👋 " + salut)
#print("🔢 Numele tău are", litere, "litere.")
#print("🔠 Cu MAJUSCULE:", mare)
#print("🔡 Cu litere mici:", mic)
#input("\n🔹 Apasă Enter pentru a continua...")

# ========================
# 5. List Games
# ========================

# Cos de cumparaturi

#cos = ["banane", "mere"]

#cos.append ("cirese")

#print("Am adaugat in cos cirese, cosul actualizat este:", cos)

#cos.remove("cirese")

#print("Am scos un produs din cos:", cos)

#print(cos[1])

# Avioane

#avioane = ["F16", "Boeing737", "AirbusA380"]

#print("Avioanele din hangar sunt:", avioane)

#print(avioane[1])
#del avioane[1]

#print(avioane)

#decolat = avioane.pop(1)

#print(decolat)

#print(avioane)

#avioane.append(decolat)
#print(avioane)

# ========================
# 6. Tuples / Sets - jocuri
# ========================

# Radare de coordonare
#pozitie_avioane = (45,88)

#print("Radarul a detectat avioanele la urmatoarele coordonate:", pozitie_avioane)

#print("latitude x=", pozitie_avioane[0], " ~ long Y =", pozitie_avioane[1])

#pozitie_lista_tupples = list(pozitie_avioane)
#pozitie_lista_tupples[0] = 99
#pozitie_avioane = tuple(pozitie_lista_tupples)

#print("modificare tupple si pozitie avioane", pozitie_avioane)

#culori_unice = {"rosu", "albastru", "galben", "verde", "gri"}
#print("This is my set of colors:", culori_unice)

#culori_unice.add("verde")
#print("Culori unice modificate", culori_unice)

#culori_unice.add("negru")
#print("ai descoperit o noua culoare", culori_unice)

#culori_unice.remove("albastru")
#print("ai sters o culoare:", culori_unice)

#print("vreau pozitia culori","alt" in culori_unice)
#print("vreau pozitia culori","negru" in culori_unice)

#culori_extra = {"violet", "roz"}

#toate_culorile = culori_unice.union(culori_extra)
#print("am adaugat inca 2 culori", toate_culorile)

#culori_sortate = sorted(toate_culorile)
#print("culori sortate", culori_sortate)

#culori_descrescator = sorted(toate_culorile, reverse=True)
#print("culori sortate", culori_descrescator)



#elev = {"nume": "Andrei","punctaj_test":67, "varsta":12}

#elev = {
#    "varsta": elev["varsta"],
#     "nume": elev["nume"],
#      "punctaj_test": elev["punctaj_test"],
#}

#print(elev)



#inventory = ["sabie", "scut", "potiune"]

#if "potiune" in inventory:
#    print("Ai dobandit o potiune")
#else:
#    print("Nu ai obiectul")

#player_class = "mage"

#clase_disponibile = ("mage", "rogue", "archer", "warrior")

#if player_class == "warrior":
#        print("You choose Warrior")

#elif player_class == "rogue":
#        print("You choose Rogue")

#elif player_class == "archer":
#        print("You choose Archer")

#elif player_class == "mage":
#        print("You choose Mage")

#else:
#    print("Unknown class")


#players = {
#    "Gogo":"Welcome back",
#    "Radu":"Great to see you",
#    "Simona":"How are you"
#}

#username = "Gogo"

#print(players.get(username), f"{username}, you are a new player")

#if username in players:
#    print(players.get(username))
#else:
#    print(f"{username} you are new to this game")


#weapon_ready = True
#armor_ready = True

#if armor_ready and weapon_ready:
#    print("Go to war")
#else:
#    print("Stay at home !")

has_key = True
knows_password = False

if has_key or knows_password:
    print("The door opens!")
else:
    print("You are locked in")
