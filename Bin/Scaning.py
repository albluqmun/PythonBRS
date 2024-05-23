import datetime
import requests
import subprocess


# Lista de direcciones IP a escanear
ips = ['172.29.16.10','172.29.16.11','172.29.16.12','172.29.16.13','172.29.16.14']

# Envio de alerta
def send_warning(ip=None, status="ok"):
	data = {'id': 'error',  # identificador de la llamada
 			'is_error': 0 if status == "ok" else 1, # 0 para todo ok; 1 para error
 			'msg_error': "" if status == "ok" else "El Brightsign con ip {ip} no esta disponible", # se muestra el mensaje de error si lo hay. Vacio en otro caso
 			'time': datetime.datetime.now().timestamp(), # fecha y hora actual
			}
	url = "https://panel-node-red.touristinsideriasbaixas.com/rooms/data"
	requests.post(auth=('component', 't035geRtW5mKOapytbPix1Kf'), url=url, data=data)


# Recorre todas las ips
errors = False
for ip in ips:
	output = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True)
	if "Tiempo de espera agotado para esta solicitud." in output.stdout or "Host de destino inaccesible" in output.stdout:
		send_warning(ip=ip, status="error")
		errors = True

if not errors:
	send_warning()
