import csv 
import os 

CALE = 'temacurs16/temacurs16/'
fisier_angajati = 'angajati.csv'

def stergere_angajat():
    nume = input('Introduceti numele angajatului: ')
    prenume = input('Introduceti prenumele angajatului: ')

    with open(CALE + fisier_angajati, 'r', newline='') as file:
        reader=csv.reader(file)
        inregistrati =list(reader)

    for inregistrare in inregistrati:
        if inregistrare[0] == nume and inregistrare[1] == prenume:
            inregistrati.remove(inregistrare)
            break

    with open(CALE + fisier_angajati, 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerows(inregistrati)
        


stergere_angajat()