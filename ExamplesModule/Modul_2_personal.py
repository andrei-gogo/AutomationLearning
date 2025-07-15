#
# # # 🎓 Python - Modul Interactiv pentru Începători (Fără bucle sau condiții)
# #
# # # =========================
# # # 1. Data Types
# # # =========================
# # print("📘 1. TIPURI DE DATE")
# # a = 5
# # b = 3.14
# # c = "Hello"
# # d = True
# # e = None
# # print("✅ Exemple: ", a, b, c, d, e)
# # input("\n🔹 Apasă Enter pentru a continua...")
# #
# # a = 5              # int
# # b = 3.14           # float
# # c = "Hello"        # str
# # d = True           # bool
# # e = None           # NoneType
# #
# # # =========================
# # # 2. Operators Game
# # # =========================
# # print("\n🎮 2. JOCUL OPERATORILOR")
# # x = float(input("📥 Introdu primul număr: "))
# # y = float(input("📥 Introdu al doilea număr: "))
# # op = input("⚙️ Introdu operatorul (+, -, *, /, %, **): ")
# #
# # operatii = {
# #     "+": x + y,
# #     "-": x - y,
# #     "*": x * y,
# #     "/": x / y,
# #     "%": x % y,
# #     "**": x ** y
# # }
# # rezultat = operatii.get(op, "Operator necunoscut")
# # print(f"✅ Rezultatul este: {rezultat}")
# # input("\n🔹 Apasă Enter pentru a continua...")
# #
# # # =========================
# # # 3. Assertion Game
# # # =========================
# # print("\n🕵️‍♂️ 3. TESTĂM ASSERT")
# # a = int(input("📥 Introdu valoarea lui a: "))
# # b = int(input("📥 Introdu valoarea lui b: "))
# # print("Facem assert că a == b...")
# # assert a == b, "❌ Eroare: a NU este egal cu b!"
# # print("✅ Bravo! a == b este adevărat!")
# # print("Facem acum un assert că a > 20...")
# # assert a > 20, "❌ Eroare: a NU este mai mare decât 20!"
# # print("✅ Wow! a este mai mare decât 20!")
# # input("\n🔹 Apasă Enter pentru a continua...")
# #
# # # =========================
# # # 4. String Game
# # # =========================
# # print("\n🎉 4. STRINGURI INTERACTIVE")
# # nume = input("📥 Introdu-ți numele: ")
# # salut = "Salut, " + nume
# # litere = len(nume)
# # mare = nume.upper()
# # mic = nume.lower()
# # print("👋 " + salut)
# # print("🔢 Numele tău are", litere, "litere.")
# # print("🔠 Cu MAJUSCULE:", mare)
# # print("🔡 Cu litere mici:", mic)
# # input("\n🔹 Apasă Enter pentru a continua...")
# #
#
#
#
# # # # cos de cumparaturi
# #
# # cos= ["banane", "mere"]
# # cos.append("zmeura")
# # print("Am adaugat in cos zmeura. Cosul este: ", cos)
# # cos.remove("banane")
# # print("Am scos in cos banane. Cosul este: ", cos)
# # print(cos[1])
# #
# # #avioane avioane = ["F16", "Boeing737", "AirbusA380"]
# #
# # avioane = ["F16", "Boeing737", "AirbusA380"]
# # print("Avioane", avioane)
# # print(avioane[1])
# # #del avioane[1]
# # print(avioane)
# #
# # decolat = avioane.pop(1)
# # print(decolat)
# #
# # print(avioane)
# # #avioane.append(decolat)
# # avioane.insert(1,decolat)
# # print(avioane)
#
# #####
# # tuples
# ####
#
# # #Radare de coordinare
# # pozitie_avioane=(45,88)
# #
# # print("radar la coord:", pozitie_avioane)
# # print("latitudine x=", pozitie_avioane[0], "longitudine y:", pozitie_avioane[1])
# #
# # #modificare in lista din tuple si invers ca sa putem adauga sau modifica elemente din tupples
# # pozitie_lista_tupples= list(pozitie_avioane)
# # pozitie_lista_tupples[0] = 99
# # pozitie_avioane = tuple(pozitie_lista_tupples)
# #
# # print(pozitie_avioane)
#
# ####
# #sets- colectii fara ordine si fara duplicate
# ###
# #
# # culori_unice = {"rosu", "albastru" , "galben" ,"verde","gri"}
# # culori_unice.add("verde") #cannot add duplicate
# # print(culori_unice)
# #
# # culori_unice.add("negru")
# # print(culori_unice)
# #
# # culori_unice.remove("albastru")
# # print(culori_unice)
# #
# # print("vreau pozitia culorii", "galben" in culori_unice)
# # culori_extra = {"violet", "roz"}
# # toate_culorile= culori_unice.union(culori_extra)
# # print("all colors:", toate_culorile)
# #
# # culori_sortate = sorted(toate_culorile)
# # print("culori sortate:", toate_culorile)
# #
# # culori_descrescator = sorted(toate_culorile, reverse=True)
# # print("culori sortate desc:", toate_culorile)
#
#
# ###################
# #Dictionare
# ####################
#
# elev= {"nume": "Andrei", "punctaj":67, "varsta":12}
#
#
# print("fisa elev", elev)
# print("punctaj:", elev["punctaj"])
#
# elev["clasa"] = "a IV-a"
# print("profil nou", elev)
#
# print(elev.keys())
# print(elev.values())
# print(elev.items())
#
# print(elev.get("nume"))
#
# elev = {
#     "varsta": elev["varsta"],
#     "nume": elev["nume"],
#     "punctaj": elev["punctaj"]
#
# }
# print(elev)


###Modul3#########
inventory = ["sabie", "scut", "potiune"]

if "armura" in inventory:
    print("Ai dobandit o potiune")
else:
    print("Nu ai oibectul in inventory")

player_class = "mage"

clase_disponibile = ("mage", "rouge", "archer", "warrior")

if player_class == "warrior":
    print("Yor choose warrior")
elif player_class == "rouge":
    print("Yor choose Rouge")
elif player_class == "archer":
    print("Yor choose Archer")
elif player_class == "mage":
    print("Yor choose Mage")
else:
    print("Unknown Class")

    inventory = ["sabie", "scut", "potiune"]

    if "armura" in inventory:
        print("Ai dobandit o potiune")
    else:
        print("Nu ai oibectul in inventory")

    player_class = "mage"

    clase_disponibile = ("mage", "rouge", "archer", "warrior")

    # if "mage" in "eu sunt mage"

    if player_class in clase_disponibile:
        print(f"'{player_class}' este disponibil")
    else:
        print("Unknown Class")

    if player_class in clase_disponibile:
        print("Yor choose warrior")
    elif player_class in clase_disponibile:
        print("Yor choose Rouge")
    elif player_class in clase_disponibile:
        print("Yor choose Archer")
    elif player_class in clase_disponibile:
        print("Yor choose Mage")
    else:
        print("Unknown Class")

players = {
    "Gogo": "Welcome Back",
    "Radu": "Grate to see you",
    "Simona": "How are you"
}

username = "Test"

print(players.get(username), f"{username}, you are a new player")

if username in players:
    print(players[username])
else:
    print(f"{username}, you are new to this game")

weapon_ready = True
armor_ready = False

if not armor_ready and weapon_ready:
    print("Go to War")
else:
    print("Stay at Home !")

has_key = False
knows_password = True

if has_key or knows_password:
    print("The dor opens!")
else:
    print("You are locked in")






