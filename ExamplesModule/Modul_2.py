
# 🎓 Python - Modul Interactiv pentru Începători (Fără bucle sau condiții)

# =========================
# 1. Data Types
# =========================
print("📘 1. TIPURI DE DATE")
a = 5
b = 3.14
c = "Hello"
d = True
e = None
print("✅ Exemple: ", a, b, c, d, e)
input("\n🔹 Apasă Enter pentru a continua...")

a = 5              # int
b = 3.14           # float
c = "Hello"        # str
d = True           # bool
e = None           # NoneType

# =========================
# 2. Operators Game
# =========================
print("\n🎮 2. JOCUL OPERATORILOR")
x = float(input("📥 Introdu primul număr: "))
y = float(input("📥 Introdu al doilea număr: "))
op = input("⚙️ Introdu operatorul (+, -, *, /, %, **): ")

operatii = {
    "+": x + y,
    "-": x - y,
    "*": x * y,
    "/": x / y,
    "%": x % y,
    "**": x ** y
}
rezultat = operatii.get(op, "Operator necunoscut")
print(f"✅ Rezultatul este: {rezultat}")
input("\n🔹 Apasă Enter pentru a continua...")

# =========================
# 3. Assertion Game
# =========================
print("\n🕵️‍♂️ 3. TESTĂM ASSERT")
a = int(input("📥 Introdu valoarea lui a: "))
b = int(input("📥 Introdu valoarea lui b: "))
print("Facem assert că a == b...")
assert a == b, "❌ Eroare: a NU este egal cu b!"
print("✅ Bravo! a == b este adevărat!")
print("Facem acum un assert că a > 20...")
assert a > 20, "❌ Eroare: a NU este mai mare decât 20!"
print("✅ Wow! a este mai mare decât 20!")
input("\n🔹 Apasă Enter pentru a continua...")

# =========================
# 4. String Game
# =========================
print("\n🎉 4. STRINGURI INTERACTIVE")
nume = input("📥 Introdu-ți numele: ")
salut = "Salut, " + nume
litere = len(nume)
mare = nume.upper()
mic = nume.lower()
print("👋 " + salut)
print("🔢 Numele tău are", litere, "litere.")
print("🔠 Cu MAJUSCULE:", mare)
print("🔡 Cu litere mici:", mic)
input("\n🔹 Apasă Enter pentru a continua...")

