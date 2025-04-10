import csv
with open('SeleColombia.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Vamos Seleccion Colombia'] * 5 + ['GOOOL'])
    spamwriter.writerow(['Luis Diaz','Jhon Duran','Jhon Arias','Richard Rios', 'James Rodriguez ', 'Davison Sanchez',])