# #
# # # # 🎓 Python - Modul Interactiv pentru Începători (Fără bucle sau condiții)
# # #
# # # # =========================
# # # # 1. Data Types
# # # # =========================
# # # print("📘 1. TIPURI DE DATE")
# # # a = 5
# # # b = 3.14
# # # c = "Hello"
# # # d = True
# # # e = None
# # # print("✅ Exemple: ", a, b, c, d, e)
# # # input("\n🔹 Apasă Enter pentru a continua...")
# # #
# # # a = 5              # int
# # # b = 3.14           # float
# # # c = "Hello"        # str
# # # d = True           # bool
# # # e = None           # NoneType
# # #
# # # # =========================
# # # # 2. Operators Game
# # # # =========================
# # # print("\n🎮 2. JOCUL OPERATORILOR")
# # # x = float(input("📥 Introdu primul număr: "))
# # # y = float(input("📥 Introdu al doilea număr: "))
# # # op = input("⚙️ Introdu operatorul (+, -, *, /, %, **): ")
# # #
# # # operatii = {
# # #     "+": x + y,
# # #     "-": x - y,
# # #     "*": x * y,
# # #     "/": x / y,
# # #     "%": x % y,
# # #     "**": x ** y
# # # }
# # # rezultat = operatii.get(op, "Operator necunoscut")
# # # print(f"✅ Rezultatul este: {rezultat}")
# # # input("\n🔹 Apasă Enter pentru a continua...")
# # #
# # # # =========================
# # # # 3. Assertion Game
# # # # =========================
# # # print("\n🕵️‍♂️ 3. TESTĂM ASSERT")
# # # a = int(input("📥 Introdu valoarea lui a: "))
# # # b = int(input("📥 Introdu valoarea lui b: "))
# # # print("Facem assert că a == b...")
# # # assert a == b, "❌ Eroare: a NU este egal cu b!"
# # # print("✅ Bravo! a == b este adevărat!")
# # # print("Facem acum un assert că a > 20...")
# # # assert a > 20, "❌ Eroare: a NU este mai mare decât 20!"
# # # print("✅ Wow! a este mai mare decât 20!")
# # # input("\n🔹 Apasă Enter pentru a continua...")
# # #
# # # # =========================
# # # # 4. String Game
# # # # =========================
# # # print("\n🎉 4. STRINGURI INTERACTIVE")
# # # nume = input("📥 Introdu-ți numele: ")
# # # salut = "Salut, " + nume
# # # litere = len(nume)
# # # mare = nume.upper()
# # # mic = nume.lower()
# # # print("👋 " + salut)
# # # print("🔢 Numele tău are", litere, "litere.")
# # # print("🔠 Cu MAJUSCULE:", mare)
# # # print("🔡 Cu litere mici:", mic)
# # # input("\n🔹 Apasă Enter pentru a continua...")
# # #
# #
# #
# #
# # # # # cos de cumparaturi
# # #
# # # cos= ["banane", "mere"]
# # # cos.append("zmeura")
# # # print("Am adaugat in cos zmeura. Cosul este: ", cos)
# # # cos.remove("banane")
# # # print("Am scos in cos banane. Cosul este: ", cos)
# # # print(cos[1])
# # #
# # # #avioane avioane = ["F16", "Boeing737", "AirbusA380"]
# # #
# # # avioane = ["F16", "Boeing737", "AirbusA380"]
# # # print("Avioane", avioane)
# # # print(avioane[1])
# # # #del avioane[1]
# # # print(avioane)
# # #
# # # decolat = avioane.pop(1)
# # # print(decolat)
# # #
# # # print(avioane)
# # # #avioane.append(decolat)
# # # avioane.insert(1,decolat)
# # # print(avioane)
# #
# # #####
# # # tuples
# # ####
# #
# # # #Radare de coordinare
# # # pozitie_avioane=(45,88)
# # #
# # # print("radar la coord:", pozitie_avioane)
# # # print("latitudine x=", pozitie_avioane[0], "longitudine y:", pozitie_avioane[1])
# # #
# # # #modificare in lista din tuple si invers ca sa putem adauga sau modifica elemente din tupples
# # # pozitie_lista_tupples= list(pozitie_avioane)
# # # pozitie_lista_tupples[0] = 99
# # # pozitie_avioane = tuple(pozitie_lista_tupples)
# # #
# # # print(pozitie_avioane)
# #
# # ####
# # #sets- colectii fara ordine si fara duplicate
# # ###
# # #
# # # culori_unice = {"rosu", "albastru" , "galben" ,"verde","gri"}
# # # culori_unice.add("verde") #cannot add duplicate
# # # print(culori_unice)
# # #
# # # culori_unice.add("negru")
# # # print(culori_unice)
# # #
# # # culori_unice.remove("albastru")
# # # print(culori_unice)
# # #
# # # print("vreau pozitia culorii", "galben" in culori_unice)
# # # culori_extra = {"violet", "roz"}
# # # toate_culorile= culori_unice.union(culori_extra)
# # # print("all colors:", toate_culorile)
# # #
# # # culori_sortate = sorted(toate_culorile)
# # # print("culori sortate:", toate_culorile)
# # #
# # # culori_descrescator = sorted(toate_culorile, reverse=True)
# # # print("culori sortate desc:", toate_culorile)
# #
# #
# # ###################
# # #Dictionare
# # ####################
# #
# # elev= {"nume": "Andrei", "punctaj":67, "varsta":12}
# #
# #
# # print("fisa elev", elev)
# # print("punctaj:", elev["punctaj"])
# #
# # elev["clasa"] = "a IV-a"
# # print("profil nou", elev)
# #
# # print(elev.keys())
# # print(elev.values())
# # print(elev.items())
# #
# # print(elev.get("nume"))
# #
# # elev = {
# #     "varsta": elev["varsta"],
# #     "nume": elev["nume"],
# #     "punctaj": elev["punctaj"]
# #
# # }
# # print(elev)
#
#
# ###Modul3#########
# inventory = ["sabie", "scut", "potiune"]
#
# if "armura" in inventory:
#     print("Ai dobandit o potiune")
# else:
#     print("Nu ai oibectul in inventory")
#
# player_class = "mage"
#
# clase_disponibile = ("mage", "rouge", "archer", "warrior")
#
# if player_class == "warrior":
#     print("Yor choose warrior")
# elif player_class == "rouge":
#     print("Yor choose Rouge")
# elif player_class == "archer":
#     print("Yor choose Archer")
# elif player_class == "mage":
#     print("Yor choose Mage")
# else:
#     print("Unknown Class")
#
#     inventory = ["sabie", "scut", "potiune"]
#
#     if "armura" in inventory:
#         print("Ai dobandit o potiune")
#     else:
#         print("Nu ai oibectul in inventory")
#
#     player_class = "mage"
#
#     clase_disponibile = ("mage", "rouge", "archer", "warrior")
#
#     # if "mage" in "eu sunt mage"
#
#     if player_class in clase_disponibile:
#         print(f"'{player_class}' este disponibil")
#     else:
#         print("Unknown Class")
#
#     if player_class in clase_disponibile:
#         print("Yor choose warrior")
#     elif player_class in clase_disponibile:
#         print("Yor choose Rouge")
#     elif player_class in clase_disponibile:
#         print("Yor choose Archer")
#     elif player_class in clase_disponibile:
#         print("Yor choose Mage")
#     else:
#         print("Unknown Class")
#
# players = {
#     "Gogo": "Welcome Back",
#     "Radu": "Grate to see you",
#     "Simona": "How are you"
# }
#
# username = "Test"
#
# print(players.get(username), f"{username}, you are a new player")
#
# if username in players:
#     print(players[username])
# else:
#     print(f"{username}, you are new to this game")
#
# weapon_ready = True
# armor_ready = False
#
# if not armor_ready and weapon_ready:
#     print("Go to War")
# else:
#     print("Stay at Home !")
#
# has_key = False
# knows_password = True
#
# if has_key or knows_password:
#     print("The dor opens!")
# else:
#     print("You are locked in")
#
#
#
#
#
#
# #----------------- modul 3 part 2
#
# # fruits = ["1", "2", "3"]
# # for x in fruits:
# #     print(x);
# # if x == "1":
# #     print("test")
# #
# #
#
# avioane = ["F16", "Boeing737", "Airbus360"]
#
# for avion in avioane:
#     print("Decoleaza:", avion)
#
# mesaj = "EsteUnJoc"
# for litera in mesaj:
#     print("litera gasita", litera)
#
# joc = ["camp", "camp", "bomba", "camp"]
#
# for zona in joc:
#     print("estri pe: ", zona)
#     if zona == "bomba":
#         print("Boom ai pierdut")
#         break
#
#
# for numar in range(1,9):
#     print("nr: ", numar)
#
# jucator= {"nume": "Andrei", "scor": 35, "nivel": 3}
# for keys, values in jucator.items():
#     print("k=", keys, "v=", values)
#

# cutii = ["cadou", "cadou", "cadou", "cadou"]
#
# for cutie in cutii:
#     print("am deschis o cutie:", cutie)
#     break
# else:
#     print("toate")

# print ("Lansare racheta!")
# n = 5
# while n > 0:
#     print ("loading", n)
#     n -= 1
# print ("lansare!!!")

# cadouri = ["minge", "carte", "niumic"]
# while cadouri:
#     print("ai desfacut un cadou", cadouri.pop())
# print ("gata cadouri")

# obiecte = ["nisipo", "piatr", "cheie", "comora", "lemn"]
# i=0
# while i < len(obiecte):
#     if obiecte[i] == "comora":
#         print("ai gasit comora la pasul", i)
#         break
#     print("Cauti,,, Ai gasit: ", obiecte[i])
#     i += 1

# obstacole = ["drum", "noroi", "piatra", "drum"]
# i = 0
# while i < len(obstacole):
#     if obstacole[i] == "piatra":
#         i +=1
#         continue
#     print ("mergi pe:", obstacole[i])
#     i +=1


# numere = [3, 7 ,2 ,5]
# caut = 9
# i = 0
# while i < len(numere):
#     if numere[i] == caut:
#         print ("gasit", caut)
#         break
#     i += 1
# else:
#     print("numarul ", caut, "nu a fost gasit.")

# cos = []
# while True:
#     comanda = input("ce vrei sa cumperi? scrie stop pentru stop: ")
#     if comanda == "stop":
#         print("pa")
#         break
#     cos.append(comanda)
#     print("ai adaugat in cos", comanda)
#
# ###print ("\n In cos ai urmatoarele cumparaturi: ", cos)
# print ("\n In cos ai urmatoarele cumparaturi: ")
# for produse in cos:
#     print(produse)

#
# energie = 3
# while energie > 0:
#     print ("energie", energie)
#     energie -=1
# print("bateria este goala.")

#
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
#
# #🔁 1. For Loop – Joc „Aviatorul”
#
# avioane = ["F16", "Boeing737", "AirbusA380"]
# for avion in avioane:
#     print("🛫 Decolează:", avion)
# #🎲 2. For Loop – Joc „Parcurge textul”
#
# mesaj = "JOC"
# for litera in mesaj:
#     print("🔠 Litera găsită:", litera)
# #🔄 3. Break – Joc „Oprește la bomba”
#
# joc = ["câmp", "câmp", "bombă", "câmp"]
# for zona in joc:
#     print("🚶 Ești pe:", zona)
#     if zona == "bombă":
#         print("💥 BOOM! Ai pierdut.")
#         break
# #🧮 4. Range() – Joc „Numărătorul”
#
# for numar in range(1, 6):
#     print("🎯 Ținta numărul:", numar)
# #🧮 5. Range() cu step – Joc „Numere impare”
#
# for n in range(1, 10, 2):
#     print("🔢 Număr impar:", n)
# #📦 6. Iterating through dictionary – Joc „Statistici jucător”
#
# jucator = {"nume": "Tudor", "scor": 90, "nivel": 3}
# for k, v in jucator.items():
#     print("📊", k, "=>", v)
# #✅ 7. For + Else – Joc „Scanează tot și anunță”
#
# cutii = ["cadou", "cadou", "cadou"]
# for cutie in cutii:
#     print("📦 Deschizi o cutie:", cutie)
# else:
#     print("🎉 Toate cutiile au fost deschise!")

#
# # 🔁 1. while simplu – Numărătoare inversă
#
# print("🎯 Lansare rachetă!")
# n = 5
# while n > 0:
#     print("⏳", n)
#     n -= 1
# print("🚀 Lansare!")
#
#
#
# # 💡 2. while cu listă și pop()
#
# cadouri = ["minge", "carte", "robot"]
# while cadouri:
#     print("🎁 Ai desfăcut un cadou:", cadouri.pop())
# print("🎉 Nu mai sunt cadouri.")
#
# # 🔚 3. break – Găsește comoara
#
# obiecte = ["piatra", "nisip", "cheie", "comora", "lemn"]
# i = 0
# while i < len(obiecte):
#     if obiecte[i] == "comora":
#         print("🏆 Ai găsit comoara la pasul", i)
#         break
#     print("🔎 Cauti... Ai gasit:", obiecte[i])
#     i += 1
#
# #
# # ⏭ 4. continue – Sari peste obstacol
# obstacole = ["drum", "noroi", "piatra", "drum"]
# i = 0
# while i < len(obstacole):
#     if obstacole[i] == "piatra":
#         i += 1
#         continue
#     print("🚶 Mergi pe:", obstacole[i])
#     i += 1
#
#
# # 🧩 5. while + else – Găsește un număr
#
# numere = [3, 7, 2, 5]
# caut = 9
# i = 0
#
# while i < len(numere):
#     if numere[i] == caut:
#         print("✅ Găsit:", caut)
#         break
#     i += 1
# else:
#     print("❌ Numărul", caut, "nu a fost găsit.")
#
#
# # 🔁 6. Loop infinit cu break
#
#
# cos2 = []
# cos1 = ""
# while True:
#     comanda = input("🛒 Ce vrei să cumperi? (scrie 'stop' pentru a ieși): ")
#     if comanda == "stop":
#         print("👋 Pa, spor la cumpărături!")
#         break
#     #cos2.append(comanda)
#     if cos1 == "":
#         cos1 = comanda
#     else:
#         cos1 = cos1 + "," + comanda
#     print("✅ Ai adăugat la coș:", comanda)
# #
# # print("\n In cos ai urmatoarelel cumparaturi:")
# # #for produse in cos2:
# #     #print("ai urmatoarele produse in cos",produse)
# # if cos1:
# #     print(cos1)
# # else:
# #     print("Cosul este gol")
#
#
# # 🧠 7. Loop while pe o variabilă
#
# energie = 3
# while energie > 0:
#     print("⚡ Energie:", energie)
#     energie -= 1
# print("🔋 Bateria este goală.")
#
# # 🎲 Dice game
# import random
#
# while True:
#     input("🎲 Apasă Enter pentru a arunca zarul...")
#     zar = random.randint(1, 6)
#     print("Ai dat:", zar)
#
#     again = input("Vrei să mai joci? (da/nu): ")
#     if again.lower() != "da":
#         print("🎮 Joc încheiat.")
#         break