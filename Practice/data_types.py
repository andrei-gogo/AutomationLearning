# Naming convention for variables
'''Use lowercase letters with underscores (snake_case)'''

#Types of data types

#Each type has specific operations and methods

'''Built-in Functions -Functions provided by Python itself 
that you can call directly by their name, without needing an object, they do not have methods'''
'''Methods functions that belong to objects (data types). They are called on an object and often operate on or return information about that object, 
so you need to call them using the dot notation'''

#numeric

a = 1 # int
print(bin(a))

b =  0b10 #binary
print(int(b))

c = 1.22121 #double
print(round(c, 2))

d = 2j # complex # j or J for imaginary numbers.
print(type(d))




#text type - built in functions and methods

e = "This is a string"
print(e.upper()) # a method
print(len(e)) #  built in function


#boolean type - built in functions

is_logged = True
has_accessed =  False

print(int(is_logged)) # built in function

#sequence

f = [1, 2 ,3] # list, allows duplicates

f.append(10) #method
print(f)
print(len(f)) # built in function

g = (4, 5 ,6) # tuple, allows duplicates

print(g.count(6)) # method - how many times 6 appears
print(len(g)) #

#mapping

h = {'unu':1, 'doi':2, "trei": 3} # dictionary - key-value pair, key is unique

print(h.items())    #  method - returns as tuplets
print(h.keys())
print(h.values())
print(len(h))      # built in function len() gives number of items

#set

i = {8, 9, 10} #set, no duplicates

i.add(11) #method

print(i)
print(len(i)) #built in function




