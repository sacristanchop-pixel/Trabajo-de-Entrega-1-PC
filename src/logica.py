# AQUÍ VA LO NUEVO (Entrega 2)
# Lectura con csv.reader y estructuras de datos
import csv

def cargar_dataset(ruta):
    # Estructura 1: LISTA (aquí guardaremos todo)
    lista_datos = [] 
    
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        # csv.DictReader convierte cada fila automáticamente en un DICCIONARIO
        # Estructura 2: DICCIONARIO (cada fila es uno)
        lector = csv.DictReader(archivo)
        for fila in lector:
            lista_datos.append(fila)
            
    return lista_datos # Devolvemos la lista llena de diccionarios
