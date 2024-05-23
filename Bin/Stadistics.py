import datetime
import json
import requests
from copy import deepcopy
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

def cook_send_stadistics(video_dict):
    # Se va a hacer un envio por cada sala
    translate_languages = {'ES': 'es',
                           'ENG': 'en',
                           'POR': 'pt',
                           'FRA': 'fr',
                           'GAL': 'ga'
                           }
    template = {'id': 'stadistics',
                'type': 'sala 270', # identificador del tipo de dispositivo
                'deviceId': '', # identificador de la sala
                'languages': [],
                'total_play': 0,
                'time': datetime.datetime.now().timestamp()
                }

    moda = deepcopy(template)
    moda['deviceId'] = 'La Moda'
    guerra = deepcopy(template)
    guerra['deviceId'] = 'Europa en guerra'
    social = deepcopy(template)
    social['deviceId'] = 'La vida social I'
    social2 = deepcopy(template)
    social2['deviceId'] = 'La vida social II'
    descul = deepcopy(template)
    descul['deviceId'] = 'El despertar cultural de Pontevedra'

    for name in video_dict:
        name_separated = name.split("_")
        dict_room = locals()[name_separated[0].lower()]
        languages = dict_room["languages"]
        dict_lang = {translate_languages[name_separated[1]]: video_dict[name]}
        languages.append(dict_lang)
        dict_room["languages"] = languages

    for ele in [moda, guerra, social, social2, descul]:
        ele["total_play"] = sum(value for d in ele["languages"] for value in d.values())
        url = "https://panel-node-red.touristinsideriasbaixas.com/rooms/data"
        json_send = data=json.dumps(ele)
        requests.post(auth=('component', 't035geRtW5mKOapytbPix1Kf'), url=url, data=json_send)


# Función para resetear los valores
def reset_video_variables(video_dict):
    reset_data = {name: 0 for name in video_dict}
    requests.post(url_set, data=reset_data)


# MAIN
# Obtener las variables
video_variables = get_video_variables()

cook_send_stadistics(video_variables)

# Resetear los valores a 0
reset_video_variables(video_variables)
