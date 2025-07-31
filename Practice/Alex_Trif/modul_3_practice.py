# ============================
# Homework Tasks – Module 3: Gaming with Conditionals
# # ============================
#
# # 🎯 Task 1: Weapon Checker
# # Create a list named 'weapons' with at least 4 different weapons (e.g., "sword", "bow", "dagger", "staff").
# # Use an if-else statement to check if "bow" is in the list.
# # ➤ If yes: print "🏹 Archer ready!"
# # ➤ If no: print "❌ No archers today."
#
# weapons = ["sword", "bow", "dagger", "staff"]
# if "bow" in weapons:
#     print("🏹 Archer ready!")
# else:
#     print("❌ No archers today.")
#
#
# # 🎯 Task 2: Level Difficulty
# # Create a tuple called 'levels' containing: ("easy", "medium", "hard").
# # Create a variable 'selected_level' with a value.
# # Use if-elif-else to print a message:
# # ➤ "🟢 Easy mode: Good for beginners."
# # ➤ "🟠 Medium mode: Ready for a challenge."
# # ➤ "🔴 Hard mode: Only pros allowed!"
# # ➤ If not in levels: print "❓ Unknown level."
#
# levels = ("easy", "medium", "hard")
# selected_level = "easy"
# if selected_level == "easy":
#     print("🟢 Easy mode: Good for beginners.")
# elif selected_level == "medium":
#     print("🟠 Medium mode: Ready for a challenge.")
# elif selected_level == "hard":
#     print("🔴 Hard mode: Only pros allowed!")
# else:
#     print("❓ Unknown level.")
#
# # 🎯 Task 3: Monster Power Lookup
# # Create a dictionary 'monsters' with 3 monsters as keys and their attack power as values (e.g., "goblin": 25).
# # Ask the user to input a monster name (use input()).
# # ➤ If it exists: print the attack power.
# # ➤ If not: print "👻 This monster is not registered."
#
# monsters = {
#     "goblin": 25,
#     "dragon": 55,
#     "orc": 15
# }
#
# choosen_monster = input("Choose a monster from `goblin`, `dragon` or `orc`:")
# if choosen_monster in monsters:
#     print("Monster power: ", monsters[choosen_monster])
# else:
#     print("👻 This monster is not registered.")
#
# # 🎯 Task 4: Key and Door Puzzle
# # Create two boolean variables: 'has_key' and 'door_locked'.
# # Use if-elif-else to print:
# # ➤ If has_key and door is locked: "🔓 You unlock the door."
# # ➤ If has_key and door is not locked: "🚪 You walk through."
# # ➤ If no key and door is locked: "🚫 You are stuck. Find a key!"
# # ➤ If no key and door is not locked: "🤔 Suspicious… but you get in."
#
# has_key = False;
# door_locked = False;
#
# if has_key and door_locked:
#     print("🔓 You unlock the door.")
# elif has_key and not door_locked:
#     print("🚪 You walk through.")
# elif not has_key and door_locked:
#     print("🚫 You are stuck. Find a key!")
# elif not has_key and not door_locked:
#     print("🤔 Suspicious… but you get in.")
#
# # 🎯 Task 5: Scoreboard Level-Up
# # Create a dictionary with 3 players and their scores (e.g., "Lidia": 120).
# # Loop through each player:
# # ➤ If score >= 100: print "🌟 {player} levels up!"
# # ➤ Else: print "🎮 {player} needs more XP."
#
# # scores ={
# #     "Lidia": 120,
# #     "Alex": 140,
# #     "Tudor": 80
# # }
# # for player, score in scores{
# #     if score >= 100
# # }
#
#
# # 91% of storage used …
# # If you run out of space, you can't save to Drive or use Gmail. Get 100 GB of storage for $1.99 $0.49/month for 3 months (personalized price).
# #
# # # ============================
# # # Module 3 - Python Conditionals: Gaming Examples
# # # ============================
# #
# # # --- Example 1: List & if ---
# # inventory = ["sword", "shield", "potion"]
# # if "potion" in inventory:
# #     print("🧪 You have a potion to heal!")
# # else:
# #     print("⚠️ No potions left. Be careful!")
# #
# # # --- Example 2: Tuple & elif ---
# # player_class = "mage"
# # available_classes = ("warrior", "archer", "mage", "rogue")
# #
# # if player_class == "warrior":
# #     print("🛡️ You chose Warrior: Strong and brave!")
# # elif player_class == "archer":
# #     print("🏹 You chose Archer: Sharp and fast!")
# # elif player_class == "mage":
# #     print("✨ You chose Mage: Master of magic!")
# # elif player_class == "rogue":
# #     print("🗡️ You chose Rogue: Sneaky and deadly!")
# # else:
# #     print("❓ Unknown class. Please choose again.")
# #
# # # --- Example 3: Dictionary & get() ---
# # players = {
# #     "Andrei": "Welcome back, warrior Andrei!",
# #     "Lidia": "Hello Lidia, ready for your quest?",
# #     "Sergiu": "Greetings, Commander Sergiu!"
# # }
# #
# # username = "Gogo"
# # print(players.get(username, f"⚔️ {username}, you are a new adventurer!"))
# #
# # # --- Example 4: Dictionary & if-else ---
# # username = "sss"
# # if username in players:
# #     print(players[username])
# # else:
# #     print(f"⚔️ {username}, you are a new adventurer!")
# #
# # # --- Example 5: Boolean & and ---
# # weapon_ready = True
# # armor_ready = False
# #
# # if weapon_ready and armor_ready:
# #     print("🔥 You are fully geared for battle!")
# # else:
# #     print("⚠️ Prepare your equipment before fighting.")
#
#
# # TEMA PENTRU ACASA
#
#
#
#
# # 1. Creeaza un dictionar cu datele tale (nume, varsta, oras)
# # 2. Foloseste un for loop pentru a parcurge si afisa cheile si valorile
# date = {"nume" : "Alex", "varsta" : 33, "oras" : "Baia Mare"}
# for n, v in date.items():
#     print (n, "-", v)
#
# # 3. Scrie un program care cere un numar si afiseaza daca e par sau impar
# number = int(input("Introdu un numar par sau impar: "))
# if number % 2 == 0:
#         print("nr par:", number)
# else:
#         print("nr impar:", number)
#
# # 4. Creeaza o lista cu elemente duplicate si elimina-le folosind set
# listaduplicate = ["mouse", "mouse", "lanterna", "camera"]
# listafaraduplicate = list(set(listaduplicate))
# print("lista fara dupes:", listafaraduplicate)
#
# # 5. Foloseste un loop for infinit cu o conditie de oprire (break)
# for numere in range(999999999):
#     numar = int(input("Introdu un nr: "))
#     if numar == 5:
#         print("Ai nimerit")
#         break
#     else:
#         print("mai incearca")
#
# # 6. Simuleaza un joc simplu unde introduci doua numere si un operator, si afisezi rezultatul (ca in clasa)
# numar_a = int(input("Introdu primul numar: "))
# numar_b = int(input("Introdu al2lea  numar: "))
# operator = input("Introdu un operator: ")
# operatii = {
#     "+" : numar_a + numar_b,
#     "-" : numar_a - numar_b,
#     "*" : numar_a * numar_b,
#     "/" : numar_a / numar_b
# }
# rezultat = operatii.get(operator, "Operator necunoscut")
# print("Rezultatul numerelor: ", numar_a, numar_b, "si operatorului", operator, "este: ", rezultat)
#
#
# # 7. Optional: Incearca sa sortezi un set folosind `sorted()` si explica de ce functioneaza
#
# numere_sortate = {"1", "2", "3", "5"}
# numere_sortate.add("4")
# numere_sortate.remove("5")
# print("numere sortate: ", sorted(numere_sortate))


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



# 📝 Temă: Jocul „Magazinul Secret”
# 🎯 Scop:
# Utilizatorul trebuie să adauge produse într-un coș și să plătească exact prețul corect, altfel pierde jocul.
#
# ✅ Cerințe:
# Creează un while loop care cere utilizatorului să adauge produse până când tastează stop.
#
# Salvează produsele într-o listă.
#
# La final, afişează produsele adăugate și cere un buget total (input()).
#
# Fiecare produs are un preț predefinit într-un dicționar.
#
# Folosește un for pentru a calcula suma totală.
#
# Cu if/else, verifică dacă utilizatorul a introdus suma corectă:
#
# dacă da: ✅ Felicitări, ai cumpărat corect!
#
# dacă nu: ❌ Ai greșit suma, încearcă din nou!

# cos = []
# cos2 = {
#     "pere" : 10,
#     "mere" : 5,
#     "struguri" : 15,
#     "pepene" : 2}
# total_cos = 0
#
# while True:
#     cumparaturi = input("Ce vrei sa cumperi? (introdu `stop` pentru a te opri): ")
#     if cumparaturi == "stop":
#         print("Ai terminat cumparaturile! ")
#         print("lista: ", cos)
#         cos_total= int(input("Introdu o valoare aproximativa pentru produse: "))
#         break
#     cos.append(cumparaturi)
# for produs in cos:
#     total_cos += cos2[produs]
#
#
# if cos_total == total_cos:
#     print("✅ Felicitări, ai cumpărat corect!")
# else:
#     print("❌ Ai greșit suma, încearcă din nou!")

# 📝 Tema 2: Jocul „Ghiceste Cuvantul”
# 🎯 Scop:
# Utilizatorul trebuie să ghicească un cuvânt secret, literă cu literă.
#
# ✅ Cerințe:
# Definește un cuvânt secret (ex: "python").
#
# Creează o listă cu _ pentru fiecare literă din cuvânt.
#
# Folosește un while pentru a cere litere de la utilizator.
#
# Dacă litera e în cuvânt, înlocuiește _ cu litera respectivă.
#
# Arată progresul după fiecare rundă.
#
# Când toate literele au fost ghicite → afișează 🎉 Ai câștigat!

# cuvant_secret = "python"
# lista_cuvant = ["_", "_", "_", "_", "_", "_"]
#
# while True:
#     cuvant_introdus = input("Introdu o litera: ")
#     if cuvant_introdus in cuvant_secret:
#         if cuvant_introdus == "p":
#             lista_cuvant[0] = cuvant_introdus
#         elif cuvant_introdus == "y":
#             lista_cuvant[1] = cuvant_introdus
#         elif cuvant_introdus == "t":
#             lista_cuvant[2] = cuvant_introdus
#         elif cuvant_introdus == "h":
#             lista_cuvant[3] = cuvant_introdus
#         elif cuvant_introdus == "o":
#             lista_cuvant[4] = cuvant_introdus
#         elif cuvant_introdus == "n":
#             lista_cuvant[5] = cuvant_introdus
#         print(f"Ai introdus corect litera {cuvant_introdus}, cuvantul este: {lista_cuvant}")
#     else:
#         print("Litera nu exista")
#
#     if lista_cuvant == ["p", "y", "t", "h", "o", "n"]:
#         print("🎉 Ai câștigat!")
#         break


# 📝 Tema 3: Jocul „Clasamentul Elevilor”
# 🎯 Scop:
# Adaugă elevi și scorurile lor într-o listă și află cine are cel mai mare scor.
#
# ✅ Cerințe:
# Creează un while care cere nume și scor pentru fiecare elev.
#
# Oprește când se tastează stop.
#
# Salvează datele în lista de dicționare:
#
# elevi = [{"nume": "Ana", "scor": 90}, ...]
# Folosește un for ca să cauți scorul cel mai mare.
#
# Cu if/else, afișează elevul câștigător.

elevi = []
score = []
elevi_score = {}

while True:
    elevi_add = input("introdu un nume elev or `stop`: ")
    elevi_score = int(input("introdu un scor or `stop`: "))
    if elevi_add or elevi_score == "stop":
        break
    elevi.append(elevi_add)
    score.append(elevi_score)
    elevi_score["name"] = elevi_add
    elevi_score["scor"] = elevi_score

print(elevi_score[elevi], elevi_score[elevi_score])



