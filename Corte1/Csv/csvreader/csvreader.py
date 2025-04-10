import csv
with open('SeleBrasil.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Vamos Seleccion Brasilera'] * 5 + ['Regates'])
    spamwriter.writerow(['Vinicius Jr','Rodrygo Goes','Gabriel','Ederson Moraes', 'Alisson Beker ', 'Davison Sanchez',])

with open('SeleBrasil.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))