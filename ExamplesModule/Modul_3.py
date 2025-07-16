# 🎮 1. Using if with a List – Game Inventory Check

inventory = ["sword", "shield", "potion"]

if "potion" in inventory:
    print("🧪 You have a potion to heal!")
else:
    print("⚠️ No potions left. Be careful!")

# 🧙‍♂️ 2. Using elif with a Tuple – Character Class Chooser

player_class = "mage"
available_classes = ("warrior", "archer", "mage", "rogue")

if player_class == "warrior":
    print("🛡️ You chose Warrior: Strong and brave!")
elif player_class == "archer":
    print("🏹 You chose Archer: Sharp and fast!")
elif player_class == "mage":
    print("✨ You chose Mage: Master of magic!")
elif player_class == "rogue":
    print("🗡️ You chose Rogue: Sneaky and deadly!")
else:
    print("❓ Unknown class. Please choose again.")

# 👾 3. Using if...else with a Dictionary – Welcome Message in a Game Lobby

players = {
    "Andrei": "Welcome back, warrior Andrei!",
    "Lidia": "Hello Lidia, ready for your quest?",
    "Sergiu": "Greetings, Commander Sergiu!"
}

username = "Gogo"
print(players.get(username, f"⚔️ {username}, you are a new adventurer!"))

# 🛡️ 4. Using and – Combat Readiness Check

weapon_ready = True
armor_ready = True

if weapon_ready and armor_ready:
    print("🔥 You are fully geared for battle!")
else:
    print("⚠️ Prepare your equipment before fighting.")

# 🧭 5. Using or – Finding a Way Out

has_key = False
knows_password = True

if has_key or knows_password:
    print("🚪 The door opens! You may proceed.")
else:
    print("🔒 You are locked in. Find another way!")

# 🕹️ 6. Combining Conditions in a Mini Game Score System

score = 120
lives = 2

if score > 100 and lives >= 1:
    print("🏆 Level Cleared! Great job!")
elif score < 100 and lives >= 1:
    print("🔁 Try again to beat the level.")
else:
    print("💀 Game Over.")