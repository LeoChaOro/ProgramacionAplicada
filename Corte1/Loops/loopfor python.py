import time

cadena = 'Python'

for letra in cadena:
    if letra == 'y':
        continue
    print(letra)
    time.sleep(1)
