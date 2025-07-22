# =========================
# 5.  Lists Game
# =========================

# cos = ["banane", "mere"]
#
# cos.append("struguri")
#
# print("am adaugat in cos struguri, Cosul actualizat este: ",cos)
#
# cos.remove("mere")
#
# print("am sters din cos mere, Cosul actualizat este: ",cos)
# print(cos[0])
#
# avioane = ["F16", "F22", "Boeing737", "AirbusA380"]
#
# print("Avioanele din hangar sunt: ", avioane)
#
# print(avioane[1])
# del avioane[1]
# print(avioane)
#
# decolat = avioane.pop(1)
#
# print("A decolat: ", decolat)
# print(avioane)
#
# # avioane.append(decolat)
# # print(avioane)
# avioane.insert(0, decolat)

# =========================
# 6. Tuple & Seturi
# =========================
#Radare de coordonare

# pozitie_avioane = (45, 88)
# print("Avioanele se gasesc la urmatoarea pozitie pe radar: ", pozitie_avioane)
# print("Avioanele se gasesc la LAT: ", pozitie_avioane[0], " iar LONG: ", pozitie_avioane[1])
#
# pozitie_lista_tupplesz = list(pozitie_avioane)
# pozitie_lista_tupplesz[0] = 99
# pozitie_avioane = tuple(pozitie_lista_tupplesz)
#
# print("modificare tupple si pozitie avione", pozitie_avioane)
#
# culori_unice = {"rosu","albastru","mov","alb","negru"}
# print("Culorile unice sunt: ", culori_unice)
#
# culori_unice.add("galben")
# print("Culorile unice dupa add sunt: ", culori_unice)
# culori_unice.remove("negru")
#
# culori_extra = {"violet", "turcoaz"}
# toate_culorile = culori_unice.union(culori_extra)
#
# print("toate culorile sunt ", toate_culorile)
#
# culori_sortate = sorted(toate_culorile)
# print("culorile sortate alfabetic sunt:", culori_sortate)
#
# culori_descrescator = sorted(toate_culorile, reverse=True)
# print(culori_descrescator)

# =========================
# 7. Dictionare
# =========================
# elev = {"nume": "Andrei","punctaj_test":77,"varsta":14}
# print("Fisa elev", elev)
# print("Rezultat la test",elev["punctaj_test"])
#
# elev["clasa"] ="a IV-a"
# print("Profil nou", elev)
#
# # valorile pot fi rescrise pentru orice cheie din dictionar
# print(elev.items())
# print(elev.values())
# print(elev.keys())
# print(elev.get("nume"))
#
# elev = {
#     "varsta": elev["varsta"],
#     "nume": elev["nume"],
#     "punctaj_test": elev["punctaj_test"]
# }
# print(elev)