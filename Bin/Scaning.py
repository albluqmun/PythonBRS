import subprocess
import time

# Lista de direcciones IP a escanear
ips = ['172.29.16.10','172.29.16.11','172.29.16.12','172.29.16.13','172.29.16.14']

# Envio de alerta
def send_warning(ip):
	print(f"El Brightsign con la ip:{ip} no responde")
	time.sleep(2)

# Recorre todas las ips
for ip in ips:
	output = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True)
	if "Tiempo de espera agotado para esta solicitud." in output.stdout or "Host de destino inaccesible" in output.stdout:
		send_warning(ip)
	else:
		print(f"El Brightsign con la ip:{ip} se encuentra conectado a la red")
		time.sleep(2)
