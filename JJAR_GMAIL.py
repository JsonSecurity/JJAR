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


cuerpo = "" #cuerpo del mensaje
comp = "" #comprueva si hay nuevos mensajes
esk = 0 #para la comprobación 
wh = True
#login
username = getpass("Correo: ")
password = getpass("Contraseña: ")

try:
	N = int(input("Número de mensajes a leer ('Enter' = defauld [1]): "))
except ValueError:
	N = 1
	print("[1]")
	pass

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)
try:
	while wh:
		time.sleep(2)
		status, mensaje = imap.select("INBOX")
		mensaje = int(mensaje[0])
		#time sleep
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
									pass #---------------------------------------------------------------
								else:
									esk = 0
									comp = cuerpo
									print("--------------------------------------------------------------------\n", cuerpo) #----------
									file = open("correos.txt", "w")
									file.write(cuerpo)
									file.close()
									time.sleep(.5)
									print("Tema: ", subject)        #----------
									#print("De: ", from_)           #----------
									print("De: stalker122@crp.xxx") #----------
		if esk == 0:
			with open("correos.txt", "r") as r:
				for linea in r:
					print(linea)

			patron = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+" #expreción regular
			print("Buscando URLS.....")
			time.sleep(.5)
			try:
				urls = re.findall(patron, cuerpo)
				print("URL DETECTADO")
				#chrome_opcions = Options()
				#chrome_opcions.add_argument("--headless")
				#driver = webdriver.Chrome(executable_path='./driver/chromedriver', options = chrome_opcions)
				driver = webdriver.Chrome(executable_path='./driver/chromedriver')

				print("ABRIENDO...\n--------------------------------------------------------------------------------------")
				driver.get("https://www.shouldiclick.org/")

				abrir = driver.find_element_by_xpath('//*[@id="url_answer"]')
				abrir.send_keys(urls[0])
				entrar = driver.find_element_by_xpath('//*[@id="main_button"]')
				entrar.click()

				print("-------------------------------------------------------------------------------------")
				print("Analizando......\n______________________________________________________________________________________")
				time.sleep(5)
				gem = driver.find_elements_by_class_name('myCounter')
				enunciado = ["Gemelo Malvado", "Estafa", "Comportamiento peligroso", "Envio de datos sin cifrar"]
				num = -1
				for gems in gem:
					num+=1
					print(enunciado[num], gems.text, "\n")
				driver.close()
			except:
				print("url no DETECTADO")
				pass
		else:
			print("seguimos buscando")
			continue
except KeyboardInterrupt:
	pass
