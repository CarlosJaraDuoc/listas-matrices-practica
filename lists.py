import os
import time
# Lista
milista = [1, 2, 3, 4, 5]
# Añadir elemento al final de lista
milista.append(10)
# Insertar elemento en lista (posición, elemento)
print("Insertar elemento en lista (posición, elemento)")
milista.insert(3, "Juan")
print(milista)
time.sleep(2)
os.system("cls")
# Elimina elemento ingresado buscando coincidencia
print("Elimina elemento ingresado buscando coincidencia")
milista.remove("Juan")
print(milista)
time.sleep(2)
os.system("cls")
# Invierte los elementos de una lista
print("Invierte los elementos de una lista")
milista.reverse()
print(milista)
time.sleep(2)
os.system("cls")
# Ordena los elementos numéricos de menor a mayor
print("Ordena los elementos numéricos de menor a mayor")
milista.sort()
print(milista)
time.sleep(2)
os.system("cls")

for i in milista:
    print(i)
print(milista)
print(type(milista))