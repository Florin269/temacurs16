import csv 
import os 

CALE = 'temacurs16/temacurs16/'
fisier_angajati = 'angajati.csv'

numeColoana = 'Nume'

def introducere_angajat():
    
    nume = input('Introduceti numele angajatului: ')
    prenume = input('Introduceti prenumele angajatului: ')
    salariul = input('Introduceti salariul angajatului: ')

    with open(CALE + fisier_angajati, 'a' , newline='') as file:
        writer=csv.writer(file)

        if file.tell() == 0:
            writer.writerow([numeColoana,'Prenume','Salariu'])

        writer.writerow([nume,prenume,salariul])

        print(f'Angajatul {nume} {prenume} a fost adaugat cu succes')

# introducere_angajat()