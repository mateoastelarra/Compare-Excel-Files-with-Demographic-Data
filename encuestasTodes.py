import csv
from helpers import info_global, proporciones, prop_totales, mostrar_proporciones, imprimir_distintos

pep = []
mat = []
esp = []
geo = []
todes = []


with open("Relevamiento Socioambiental Estudiantes _ 2022 _ PEP .csv", 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        pep.append(row)
        todes.append(row)


with open("Relevamiento Socioambiental Estudiantes _ 2022 _ MAT.csv", 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        mat.append(row)
        todes.append(row)


with open("Relevamiento Socioambiental Estudiantes _ 2022 _ GEO.csv", 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        geo.append(row)
        todes.append(row)


with open("Relevamiento Socioambiental Estudiantes _ 2022 _ Especial.csv", 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        esp.append(row)
        todes.append(row)


keys = list(todes[0].keys())

totales = [len(todes), len(pep), len(mat), len(esp),len(geo)]
datos = [todes, pep, mat, esp, geo]
nombres = ["todes", "pep", "mat", "esp", "geo"]

mostrar_proporciones(totales, datos, nombres, keys[19])
imprimir_distintos(totales, datos, nombres, keys[19], 0.15)
    
