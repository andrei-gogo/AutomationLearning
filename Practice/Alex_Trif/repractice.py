# magazin = []
# cos2 = {
#     "pere" : 10,
#     "mere" : 5,
#     "struguri" : 15,
#     "pepene" : 2}
# while True:
#     produse = input("Introdu produse: ")
#     if produse == "stop":
#         ghici = int(input("Introdu costul: "))
#         break
#     if produse in cos2:
#         magazin.append(produse)
#     else: print("nu avem")
# pret = 0
# for f in magazin:
#     pret += cos2[f]
# if pret == ghici:
#     print("da")
# else: print("ba")

#----------------------

# cuvant_secret = "pyt"
#
# lista_secreta= ["_", "_", "_"]
# while True:
#     litera_user = input("Introdu o litera: ")
#     if litera_user in cuvant_secret:
#         if litera_user == "p":
#             lista_secreta[0] = litera_user
#         if litera_user == "y":
#             lista_secreta[1] = litera_user
#         if litera_user == "t":
#             lista_secreta[2] = litera_user
#         print(f"GJ! Noul cuvant e: {lista_secreta}")
#     else:
#         print("Nope")
#     if lista_secreta == ["p", "y", "t"]:
#         print("Ai castigat")
#         break
#

#----------------------

elevi = []

while True:
    add_elevi = input("Introdu nume elev or stop: ")
    if add_elevi == "stop":
        break
    add_nota = input(f"Introdu nota pentru elevul {add_elevi} or stop: ")
    if add_nota == "stop":
        break
    elevi.append({"nume": add_elevi, "nota": int(add_nota)})
print(elevi)

nota_max=0
elev_preminat= ""
for note in elevi:
    if note["nota"] > nota_max:
        nota_max = note["nota"]
        elev_preminat = note["nume"]
print(f"Elevul castigator este: {elev_preminat} cu nota {nota_max}")