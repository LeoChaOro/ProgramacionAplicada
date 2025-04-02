print("numeros pares e impares")

for i in range (1,50):
    residual = i%2
    if residual == 0:
        print(f'{i} es par')
    else:
        print(str(i) + ' es impar')
        
print("numeros elevados a la potenia ^4")

for i in range (0,9):
    result = i**4
    print(str(i)+' ^4=',result)
    



    while True:
        times = input("introduzca numero de veces: ")
        times = float(times)
        times = int(times)
        print(type(times))
        print(times)
        if times == 0:
            print("No hacer nada")
        else:
            for i in range(1,times+1):
                print("i = ", i)
    