import random
from matplotlib import pyplot as plt

numeros_a = range(1, 14)
numeros_b = [random.randint(1, 2000) for i in range(13)]
plt.plot(numeros_a, numeros_b)
plt.show()