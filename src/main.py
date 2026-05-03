# AQUÍ VA LO NUEVO (Entrega 2)
# Solo el MENÚ y llamadas a funciones
from logica import cargar_dataset # Importas tu función

# 1. Cargar los datos al inicio (Dataset completo de 200+)
mis_datos = cargar_dataset("Data/diabetes_COMPLETO.csv")

# 2. Ahora 'mis_datos' es una lista de diccionarios que puedes usar en el menú
while True:
    print("1. Buscar")
    print("2. Estadísticas")
    print("3. Guardar resultados (F1)")
