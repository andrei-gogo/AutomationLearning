# ============================
# Homework Tasks – Module 3: Gaming with Conditionals
# ============================

# 🎯 Task 1: Weapon Checker
# Create a list named 'weapons' with at least 4 different weapons (e.g., "sword", "bow", "dagger", "staff").
# Use an if-else statement to check if "bow" is in the list.
# ➤ If yes: print "🏹 Archer ready!"
# ➤ If no: print "❌ No archers today."

weapons = ["sword", "bow", "dagger", "staff"]
if "bow" in weapons:
    print("🏹 Archer ready!")
else:
    print("❌ No archers today.")


# 🎯 Task 2: Level Difficulty
# Create a tuple called 'levels' containing: ("easy", "medium", "hard").
# Create a variable 'selected_level' with a value.
# Use if-elif-else to print a message:
# ➤ "🟢 Easy mode: Good for beginners."
# ➤ "🟠 Medium mode: Ready for a challenge."
# ➤ "🔴 Hard mode: Only pros allowed!"
# ➤ If not in levels: print "❓ Unknown level."

levels = ("easy", "medium", "hard")
selected_level = "easy"
if selected_level == "easy":
    print("🟢 Easy mode: Good for beginners.")
elif selected_level == "medium":
    print("🟠 Medium mode: Ready for a challenge.")
elif selected_level == "hard":
    print("🔴 Hard mode: Only pros allowed!")
else:
    print("❓ Unknown level.")

# 🎯 Task 3: Monster Power Lookup
# Create a dictionary 'monsters' with 3 monsters as keys and their attack power as values (e.g., "goblin": 25).
# Ask the user to input a monster name (use input()).
# ➤ If it exists: print the attack power.
# ➤ If not: print "👻 This monster is not registered."

monsters = {
    "goblin": 25,
    "dragon": 55,
    "orc": 15
}

choosen_monster = input("Choose a monster from `goblin`, `dragon` or `orc`:")
if choosen_monster in monsters:
    print("Monster power: ", monsters[choosen_monster])
else:
    print("👻 This monster is not registered.")

# 🎯 Task 4: Key and Door Puzzle
# Create two boolean variables: 'has_key' and 'door_locked'.
# Use if-elif-else to print:
# ➤ If has_key and door is locked: "🔓 You unlock the door."
# ➤ If has_key and door is not locked: "🚪 You walk through."
# ➤ If no key and door is locked: "🚫 You are stuck. Find a key!"
# ➤ If no key and door is not locked: "🤔 Suspicious… but you get in."

has_key = False;
door_locked = False;

if has_key and door_locked:
    print("🔓 You unlock the door.")
elif has_key and not door_locked:
    print("🚪 You walk through.")
elif not has_key and door_locked:
    print("🚫 You are stuck. Find a key!")
elif not has_key and not door_locked:
    print("🤔 Suspicious… but you get in.")

# 🎯 Task 5: Scoreboard Level-Up
# Create a dictionary with 3 players and their scores (e.g., "Lidia": 120).
# Loop through each player:
# ➤ If score >= 100: print "🌟 {player} levels up!"
# ➤ Else: print "🎮 {player} needs more XP."

# scores ={
#     "Lidia": 120,
#     "Alex": 140,
#     "Tudor": 80
# }
# for player, score in scores{
#     if score >= 100
# }


# 91% of storage used …
# If you run out of space, you can't save to Drive or use Gmail. Get 100 GB of storage for $1.99 $0.49/month for 3 months (personalized price).
#
# # ============================
# # Module 3 - Python Conditionals: Gaming Examples
# # ============================
#
# # --- Example 1: List & if ---
# inventory = ["sword", "shield", "potion"]
# if "potion" in inventory:
#     print("🧪 You have a potion to heal!")
# else:
#     print("⚠️ No potions left. Be careful!")
#
# # --- Example 2: Tuple & elif ---
# player_class = "mage"
# available_classes = ("warrior", "archer", "mage", "rogue")
#
# if player_class == "warrior":
#     print("🛡️ You chose Warrior: Strong and brave!")
# elif player_class == "archer":
#     print("🏹 You chose Archer: Sharp and fast!")
# elif player_class == "mage":
#     print("✨ You chose Mage: Master of magic!")
# elif player_class == "rogue":
#     print("🗡️ You chose Rogue: Sneaky and deadly!")
# else:
#     print("❓ Unknown class. Please choose again.")
#
# # --- Example 3: Dictionary & get() ---
# players = {
#     "Andrei": "Welcome back, warrior Andrei!",
#     "Lidia": "Hello Lidia, ready for your quest?",
#     "Sergiu": "Greetings, Commander Sergiu!"
# }
#
# username = "Gogo"
# print(players.get(username, f"⚔️ {username}, you are a new adventurer!"))
#
# # --- Example 4: Dictionary & if-else ---
# username = "sss"
# if username in players:
#     print(players[username])
# else:
#     print(f"⚔️ {username}, you are a new adventurer!")
#
# # --- Example 5: Boolean & and ---
# weapon_ready = True
# armor_ready = False
#
# if weapon_ready and armor_ready:
#     print("🔥 You are fully geared for battle!")
# else:
#     print("⚠️ Prepare your equipment before fighting.")

