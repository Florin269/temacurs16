import csv 
import os 

CALE = 'temacurs16/temacurs16/'
fisier_angajati = 'angajati.csv'

def afisare_angajati():
    with open(CALE + fisier_angajati,'r', newline='') as file:
        for linie in file:
            print(linie)


afisare_angajati()