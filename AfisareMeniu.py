from IntroducereAngajatNou import introducere_angajat
from StergereAngajat import stergere_angajat
from AfisareAngajatii import afisare_angajati


def meniu():

    print("\n----- Meniu -----")
    print("1. Adaugă angajat")
    print("2. Stergere Angajat")
    print("3. Afisare Angajati")
    print("0. Ieșire")
    
    while True:

        optiune = input('Introduceti optiunea: ')

        if optiune == '1':
            introducere_angajat()
        elif optiune == '2':
            stergere_angajat()
        elif optiune == '3':
            afisare_angajati()
        elif optiune == '0':
            print("Aplicatia se va inchide! Multumesc")



meniu()
