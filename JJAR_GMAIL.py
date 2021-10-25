import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from getpass import getpass
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class color:
    BB = "\033[34;1m" # Blue light
    YY = "\033[33;1m" # Yellow light
    GG = "\033[32;1m" # Green light
    WW = "\033[0;1m"  # White light
    RR = "\033[31;1m" # Red light
    CC = "\033[36;1m" # Cyan light
    B = "\033[34m"    # Blue
    Y = "\033[33m"    # Yellow
    G = "\033[32m"    # Green
    W = "\033[0m"     # White
    R = "\033[31m"    # Red
    C = "\033[36m"    # Cyan


banner = color.R + '''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒
▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒
▒░░░░░░░░████████████████████████░░░░░░░░░░▒
▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████
▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████
████████████████████████████████████████████
'''
os.system('clear')
print(banner)
zz = "{}{}{} ".format(color.W + '[',color.R + '+',color.W + ']') #xD
cuerpo = "" #cuerpo del mensaje
comp = "" #comprueva si hay nuevos mensajes
esk = 0 #para la comprobación 
log = True #para el bucle
N = 1 #numero de mensajes a leer

try:
    while log:
        try:
            username = getpass("{}{}".format(zz, color.G + "username: "))
            password = getpass("{}{}".format(zz, color.G + "passwod: "))
            imap = imaplib.IMAP4_SSL("imap.gmail.com")
            imap.login(username, password)
            log = False
        except:
            log = True
            print("{}{}".format(zz, color.RR + "falied"))
            continue
except KeyboardInterrupt:
    pass
#login
try:
    while True:
        time.sleep(2)
        status, mensaje = imap.select("INBOX")
        mensaje = int(mensaje[0])
        for i in range(mensaje, mensaje -N, -1):
            try:
                res, mensaje = imap.fetch(str(i), "RFC822")
            except:
                break
            for respuesta in mensaje:
                if isinstance(respuesta, tuple):
                    mensaje = email.message_from_bytes(respuesta[1])
                    subject = decode_header(mensaje["Subject"])[0][0]

                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    from_ = mensaje.get("From")

                    if mensaje.is_multipart():
                        for part in mensaje.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            
                            try:
                                cuerpo = part.get_payload(decode=True).decode()
                            except:
                                pass

                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                if cuerpo == comp:
                                    esk = 1
                                    pass
                                else:
                                    print("{}{}".format(zz,color.G + "De: stalker122@srp.sgd"))
                                    print("{}{}{}".format(zz,color.G + "Tema: ", subject))
                                    print("{}{}\n\n{}".format(zz,color.G + "Correo:", cuerpo))
                                    esk = 0
                                    comp = cuerpo
                                    file = open("correos.txt", "w")
                                    file.write(cuerpo)
                                    file.close()
                                    time.sleep(.5)

        if esk == 0:
            with open("correos.txt", "r") as r:
                for linea in r:
                    print(linea)

            patron = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+" #expreción regular
            print("{}{}".format(zz,color.G +"Buscando URLS..."))
            time.sleep(.5)
            try:
                urls = re.findall(patron, cuerpo)
                print("{}{}".format(zz,color.G + "URL Detectado"))
                #chrome_opcions = Options()
                #chrome_opcions.add_argument("--headless")
                #driver = webdriver.Chrome(executable_path='./driver/chromedriver', options = chrome_opcions)
                driver = webdriver.Chrome(executable_path='./driver/chromedriver')

                print("{}{}".format(zz,color.G + "ABRIENDO..."))
                driver.get("https://www.shouldiclick.org/")

                abrir = driver.find_element_by_xpath('//*[@id="url_answer"]')
                abrir.send_keys(urls[0])
                entrar = driver.find_element_by_xpath('//*[@id="main_button"]')
                entrar.click()

                print("{}{}".format(zz,color.G + "Analizando..."))
                time.sleep(5)
                gem = driver.find_elements_by_class_name('myCounter')
                enunciado = ["Gemelo Malvado","Estafa","Comportamiento peligroso","Envio de datos sin cifrar"]
                num = -1
                for gems in gem:
                    num+=1
                    print(enunciado[num], gems.text, "\n")
                    time.sleep(2)
                    driver.close()
                    print("{}{}".format(zz,color.G + "Seguimos Buscando"))
            except KeyboardInterrupt:
                print("{}{}".format(zz,color.G + "URl No Detectado"))
                print("{}{}".format(zz,color.G + "Seguimos Buscando"))
                pass
        else:
            continue
except KeyboardInterrupt:
    print("{}{}".format(zz,color.GG + "Finish"))
    pass
