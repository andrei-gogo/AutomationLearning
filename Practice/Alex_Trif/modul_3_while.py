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

cuvant_secret = "python"
lista_cuvant = ["_", "_", "_", "_", "_", "_"]

while True:
    cuvant_introdus = input("Introdu o litera: ")
    if cuvant_introdus in cuvant_secret:
        if cuvant_introdus == "p":
            lista_cuvant[0] = cuvant_introdus
        elif cuvant_introdus == "y":
            lista_cuvant[1] = cuvant_introdus
        elif cuvant_introdus == "t":
            lista_cuvant[2] = cuvant_introdus
        elif cuvant_introdus == "h":
            lista_cuvant[3] = cuvant_introdus
        elif cuvant_introdus == "o":
            lista_cuvant[4] = cuvant_introdus
        elif cuvant_introdus == "n":
            lista_cuvant[5] = cuvant_introdus
        print(f"Ai introdus corect litera {cuvant_introdus}, cuvantul este: {lista_cuvant}")
    else:
        print("Litera nu exista")

    if lista_cuvant == ["p", "y", "t", "h", "o", "n"]:
        print("🎉 Ai câștigat!")
        break