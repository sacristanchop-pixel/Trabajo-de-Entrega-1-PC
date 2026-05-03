# AQUÍ VA LO NUEVO (Entrega 2)
# Solo el MENÚ y llamadas a funciones
from logica import cargar_dataset_completo

# Definimos la ruta al archivo de 200+ registros
RUTA_DATASET = "Data/diabetes_COMPLETO.csv"

# Llamamos a tu función y guardamos el resultado
dataset = cargar_dataset_completo(RUTA_DATASET)

if dataset:
    print(f"Carga exitosa. Registros totales: {len(dataset)}")
else:
    print("Error al cargar el archivo.")
