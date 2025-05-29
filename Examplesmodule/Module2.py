# print ("Tipuri de date")
#
# a= 10 #int
# b= 99.1 #float
# c= "it's me" #string
# d= True #bool
# e= None #nonetype
#
# print ("examples:", a,b,c,d,e)
#
# print (f"examples:", {a},{b},{c},{d},{e})
#
# input("\n Apasa enter pentru a continua...") #initializeaza un mesaj cu new line


#operators
# adunare +
# scădere -
# înmulțire *
# împărțire /
# restul împărțirii %
# putere **
#impartire intreaga //

# print("\n Jocul operatiilor")
#
# x=float(input("\n primul numar: "))
#
# y=float(input("\n al 2lea numar: "))
#
# op= input("\n introdu un operator ca si string: ")
#
# operatii={
#     "+": x+y,
#     "-": x-y,
#     "*": x*y,
#     "/": x/y,
#     "**": x**y,
#     "//": x//y,
#     "%": x%y,
# }
# rezultat= operatii.get(op, "operator necunoscut")
#
# print(f"\n rezultatul este: {rezultat}")
# input("\n Apasa enter pentru a continua...")

#assertions

# primul_nr = int(input("\n primul numar: "))
# nr_2 = int(input("\n al 2lea numar: "))
#
# #print("este egal")
# #assert primul_nr==nr_2, "Error - nu este egal"
# #assert primul_nr>100, "este adevarat"
# #assert nr_2<10, "nu este adevarat"
# assert primul_nr != nr_2 or primul_nr >100, "nu indeplineste nicio conditie"


#String game
print("my string")

name=input("numele meu este:")
salut = "Salut" + name
litere=len(name)
mare= name.upper()
mic=name.lower()

print(salut)
print("numele meu are",litere, "litere")
print("numele cu litere mari:",mare)
print("numele cu litere mici:",mic)

