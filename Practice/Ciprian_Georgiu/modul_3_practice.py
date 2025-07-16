# Homework Tasks – Module 3: Gaming with Conditionals
# ============================
#from operator import truediv
#from os import times_result

# 🎯 Task 1: Weapon Checker
# Create a list named 'weapons' with at least 4 different weapons (e.g., "sword", "bow", "dagger", "staff").
weapons = ["sword", "bow", "dagger", "staff"]
# Use an if-else statement to check if "bow" is in the list.
if "bow" in weapons:
# ➤ If yes: print "🏹 Archer ready!"
    print( "🏹 Archer ready!")
# ➤ If no: print "❌ No archers today."
else:
    print("❌ No archers today.")
# 🎯 Task 2: Level Difficulty
# Create a tuple called 'levels' containing: ("easy", "medium", "hard").
levels = ("easy, medium", "hard")
# Create a variable 'selected_level' with a value.
selected_level = "medium"
# Use if-elif-else to print a message:
# ➤ "🟢 Easy mode: Good for beginners."
if selected_level == "easy":
    print("🟢 Easy mode: Good for beginners.")
# ➤ "🟠 Medium mode: Ready for a challenge."
elif selected_level == "medium":
    print("🟠 Medium mode: Ready for a challenge.")
# ➤ "🔴 Hard mode: Only pros allowed!"
elif selected_level == "hard":
    print("🔴 Hard mode: Only pros allowed!")
# ➤ If not in levels: print "❓ Unknown level."
else:
    print("❓ Unknown level.")
# 🎯 Task 3: Monster Power Lookup
# Create a dictionary 'monsters' with 3 monsters as keys and their attack power as values (e.g., "goblin": 25).
monsters = {
    "goblin": 25,
    "ella": 23,
    "vic": 10
}
# Ask the user to input a monster name (use input()).
monster_name = input("Choose a monster name from goblin, ella and vic: ")
# ➤ If it exists: print the attack power.
if monster_name in monsters:
    print(f"The attack power of {monster_name} is {monsters[monster_name]}.")
# # ➤ If not: print "👻 This monster is not registered."
else:
    print ("👻 This monster is not registered.")
# 🎯 Task 4: Key and Door Puzzle
# Create two boolean variables: 'has_key' and 'door_locked'.
has_key = True
door_locked = True
#  Use if-elif-else to print:
# ➤ If has_key and door is locked: "🔓 You unlock the door."
if has_key and door_locked:
    print("🔓 You unlock the door.")
# ➤ If has_key and door is not locked: "🚪 You walk through."
elif has_key and door_locked:
    print("🚪 You walk through.")
# ➤ If no key and door is locked: "🚫 You are stuck. Find a key!"
elif not has_key and door_locked:
    print("🚫 You are stuck. Find a key!")
# ➤ If no key and door is not locked: "🤔 Suspicious… but you get in."
else:
    print("🤔 Suspicious… but you get in.")

# 🎯 Task 5: Scoreboard Level-Up
# Create a dictionary with 3 players and their scores (e.g., "Lidia": 120).
scoreboard = {
    "Lidia": 120,
    "Adi": 130,
    "Andrei": 50
}
# Loop through each player:
for player, score in scoreboard.items():
# ➤ If score >= 100: print "🌟 {player} levels up!"
    if score >= 100:
        print(f"🌟 {player} levels up!")
# ➤ Else: print "🎮 {player} needs more XP."
else:
        print(f"🎮 {player} needs more XP.")
