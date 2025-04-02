

while True:

    valor = int(input("introduzca un numero entero positivo: "))
    print("valor: ", valor)
    a = isinstance(valor, int)
    if a == True and valor > 0:
        factor = 1
        for i in range (1, valor + 1):
            factor = factor*i            
        print(f'el factorial de {valor} es: ', factor)
    else:
        print("Por favor, introduzca un valor entero positivo")