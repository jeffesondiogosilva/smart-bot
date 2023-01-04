import pywhatkit 
import keyboard
import time
from datetime import datetime


contatos = ['+5583999970040', '+5583981606774']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0],'Olá, tudo bem? Eu sou um robô!', datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    time.sleep(20)
    keyboard.press_and_release('ctrl + w')