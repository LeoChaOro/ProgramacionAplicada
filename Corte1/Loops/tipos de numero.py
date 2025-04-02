a = input("Enter a number: ")
a = int(a)
b = input("Enter b number: ")
b = float(b)
c = a + b

if a == b:
    print("iguales")
else:
    print("Diferentes")

print("tipo de a es  ", type(a))
print("tipo de b es ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("a y b son del mismo tipo")
else:
    print("a y b  son de diferentes tipos")