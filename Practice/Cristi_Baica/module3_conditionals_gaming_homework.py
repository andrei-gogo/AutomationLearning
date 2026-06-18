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

# ============================
# Homework Tasks – Module 3: Gaming with Conditionals
# ============================

# 🎯 Task 1: Weapon Checker
# Create a list named 'weapons' with at least 4 different weapons (e.g., "sword", "bow", "dagger", "staff").
weapons = ["sword", "bow", "dagger", "staff"]
# Use an if-else statement to check if "bow" is in the list.
if "bow" in weapons:
# ➤ If yes: print "🏹 Archer ready!"
    print("🏹 Archer ready!")
# ➤ If no: print "❌ No archers today."
else:
    print("❌ No archers today.");

# 🎯 Task 2: Level Difficulty
# Create a tuple called 'levels' containing: ("easy", "medium", "hard").
levels = ("easy", "medium", "hard")
# Create a variable 'selected_level' with a value.
selected_level = "easy"
# Use if-elif-else to print a message:
if selected_level == "easy":
# ➤ "🟢 Easy mode: Good for beginners."
    print("Good for beginners.")
# ➤ "🟠 Medium mode: Ready for a challenge."
elif selected_level == "medium":
    print("Ready for a challenge.")
# ➤ "🔴 Hard mode: Only pros allowed!"
elif selected_level == "hard":
    print("Only pros allowed!")
# ➤ If not in levels: print "❓ Unknown level."
else:
    print("❓ Unknown level selection.")

# 🎯 Task 3: Monster Power Lookup
# Create a dictionary 'monsters' with 3 monsters as keys and their attack power as values (e.g., "goblin": 25).
monsters = {
    "goblin": 25,
    "goblin shaman": 55,
    "owlbear": 100
}
# Ask the user to input a monster name (use input()).
user_monster = input("Choose a monster: ")
# ➤ If it exists: print the attack power.
if user_monster in monsters:
    print(f"The power for ", user_monster," is ", monsters[user_monster],".")
# ➤ If not: print "👻 This monster is not registered."
else:
    print("👻 This monster is not registered.")

# 🎯 Task 4: Key and Door Puzzle
# Create two boolean variables: 'has_key' and 'door_locked'.
has_key = input("Do you have the key? (True/False): ").lower() == "true"
door_locked = input("Is the door locked? (True/False): ").lower() == "true"
# Use if-elif-else to print:
if has_key and door_locked:
# ➤ If has_key and door is locked: "🔓 You unlock the door."
    print("🔓 You unlock the door.")
# ➤ If has_key and door is not locked: "🚪 You walk through."
elif has_key and not door_locked :
    print("🚪 You walk through.")
# ➤ If no key and door is locked: "🚫 You are stuck. Find a key!"
elif has_key == False and door_locked:
    print("🚫 You are stuck. Find a key!")
# ➤ If no key and door is not locked: "🤔 Suspicious… but you get in."
else:
#     print("🤔 Suspicious… but you get in.")

# 🎯 Task 5: Scoreboard Level-Up
# Create a dictionary with 3 players and their scores (e.g., "Lidia": 120).
players ={
    "Cristi": 99,
    "Lore": 9999,
    "Marius": 55
}

# Loop through each player:
# ➤ If score >= 100: print "🌟 {player} levels up!"
for player, score in players.items():
    if score >= 100:
        print(f"{player} levels up!")
# ➤ Else: print "🎮 {player} needs more XP."
    else:
        print(f"{player} needs more XP.")
