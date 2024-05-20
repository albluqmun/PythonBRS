import requests
import random

# Dirección y puerto del brightsign
url = 'http://172.29.16.11:8008/SetValues'

# Lista de nombres de archivos
mp4_filenames = [
    "MODA_ES_CENTRAL.mp4", "MODA_FRA_CENTRAL.mp4", "MODA_POR_CENTRAL.mp4",
    "MODA_GAL_CENTRAL.mp4", "MODA_ENG_CENTRAL.mp4", "GUERRA_ES_CENTRAL.mp4",
    "GUERRA_POR_CENTRAL.mp4", "GUERRA_GAL_CENTRAL.mp4", "GUERRA_FRA_CENTRAL.mp4",
    "SOCIAL_ES_CENTRAL.mp4", "SOCIAL_POR_CENTRAL.mp4", "SOCIAL_GAL_CENTRAL.mp4",
    "SOCIAL_FRA_CENTRAL.mp4", "SOCIAL2_ES_CENTRAL.mp4", "SOCIAL2_GAL_CENTRAL.mp4",
    "SOCIAL2_FRA_CENTRAL.mp4", "SOCIAL2_POR_CENTRAL.mp4", "GUERRA_ENG_CENTRAL.mp4",
    "SOCIAL_ENG_CENTRAL.mp4", "SOCIAL2_ENG_CENTRAL.mp4", "DESCUL_ES_CENTRAL.mp4",
    "DESCUL_FRA_CENTRAL.mp4", "DESCUL_POR_CENTRAL.mp4", "DESCUL_GAL_CENTRAL.mp4",
    "DESCUL_ENG_CENTRAL.mp4"
]

# Crear un diccionario con valores aleatorios
mp4_dict = {name: random.randint(1, 100) for name in mp4_filenames}

# Enviar los datos como POST
response = requests.post(url, data=mp4_dict)

# Imprimir el estado de la respuesta
print("Valores aleatorios enviados:")