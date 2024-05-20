import requests
from xml.etree import ElementTree as ET

# URL para obtener las variables
url_get = "http://172.29.16.11:8008/GetUserVars"

# URL para resetear los valores de las variables
url_set = "http://172.29.16.11:8008/SetValues"

# Función para obtener datos
def get_video_variables():
    response = requests.get(url_get)
    root = ET.fromstring(response.content)
    video_dict = {}
    
    for var in root.findall('BrightSignVar'):
        name = var.get('name')
        value = var.text
        if name and name.endswith('.mp4'):
            video_dict[name] = int(value)
    
    return video_dict

# Función para calcular reproducciones diarias y ajustar el valor
def adjust_social_es_central(video_dict):
    video_name = "SOCIAL_ES_CENTRAL.mp4"
    if video_name in video_dict:
        reproductions_per_day = 16  # Reproducciones por día
        video_dict[video_name] -= int(reproductions_per_day)

# Función para resetear los valores
def reset_video_variables(video_dict):
    reset_data = {name: 0 for name in video_dict}
    requests.post(url_set, data=reset_data)

# Función para guardar el diccionario en un archivo de texto
def save_dict_to_file(video_dict, filename):
    with open(filename, 'w') as file:
        for key, value in video_dict.items():
            file.write(f"{key}: {value}\n")


# MAIN
# Obtener las variables
video_variables = get_video_variables()

# Ajustar el valor de SOCIAL_ES_CENTRAL
adjust_social_es_central(video_variables)

# Guardar el diccionario en un archivo de texto
save_dict_to_file(video_variables, 'video_variables.txt')

# Resetear los valores a 0
reset_video_variables(video_variables)
