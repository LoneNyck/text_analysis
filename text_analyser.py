import re
import csv

with open('file_to_read.txt', 'r') as file:
    content = file.read()

    testo = str(content.replace("\n", " ")).replace("'", " ")

    lista_parole_miste = testo.split(" ")

    lista_parole = [re.sub(r'[^a-zA-Z0-9àèéìòù]', '', parola).lower() for parola in lista_parole_miste]
    lista_parole = [parola for parola in lista_parole if parola]
    lista_parole.sort()

    parole_uniche = []
    length = []
    frequenze = []

    for parola in lista_parole:
        freq = lista_parole.count(parola)

        if parola in parole_uniche:
            continue
        else:
            parole_uniche.append(parola)
            length.append(len(parola))
            frequenze.append(freq)

    lista = [(parole_uniche[i], length[i], frequenze[i]) for i in range(min(len(parole_uniche), len(length), len(frequenze)))]

    with open('words.csv', 'w', newline='') as df:
        title_row = ['word', 'length', 'freq']
        writer = csv.writer(df)
        writer.writerow(title_row)
        writer.writerows(lista)