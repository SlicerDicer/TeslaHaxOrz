import socket
import requests
import json
import time
url = "http://192.168.90.100:4035/Debug/get_data_value?valueName="

def db_send(name='', value=''):
        try:
            db_ip = '192.168.90.125'
            db_port = int('8888')
            db_message = name + " value=" + value
            db_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            db_sock.sendto(db_message.encode('utf-8'), (db_ip, db_port))
            print(db_message)
        except socket.error:
            pass
while True:
	with open('tesla.list') as file_list:
		tesla_list = file_list.read().splitlines()
		for data_point in tesla_list:
			current_place = data_point[:-1]
			response = requests.get(url + data_point)
			send_json = response.json()
			t_value = send_json["value"]
			db_send(data_point, t_value)
	time.sleep(5)
