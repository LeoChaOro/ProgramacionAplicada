


#version9
rango=30
n = 0
primo = True
while (n < rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
    

