#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Source : https://gist.github.com/keithweaver/3d5dbf38074cee4250c7d9807510c7c3
# Flask explain : https://flask-ask.readthedocs.io/en/latest/requests.html !!!!!!! USEFUL


from flask import Flask, render_template
from flask_ask import Ask, statement, question, request, session, convert_errors
import os, time ,sys

#Creation de l'app
app = Flask(__name__)
ask = Ask(app, "/PiControle")

@app.route('/')
def homepage():
    return "Page de la raspberry"

@ask.launch
def start_skill():
    welcome_message = "Bonjour, que voulez vous faire ?"  #Message que vas dire Alexa
    return question(welcome_message)


#================================ Bluetooths Intents ====================================

@ask.intent('BlScanIntent')
def scan_bluetooth():
    
    os.popen("python3 Bl_Scripts/ScanBL.py")
    reponse = "Scann en cour. Demandez lé resultats un peu plu tard"
    return statement(reponse)

@ask.intent('BlListeIntent')
def list_bluetooth():
    
    if os.path.isfile("Bl_Scripts/BlSave.txt"):
        ListeFile = open("Bl_Scripts/BlSave.txt", "r")
        DeviceListe = ListeFile.read()
        ListeFile.close()
        reponse = "Les appareils disponibles sont : " + str(DeviceListe)
        if len(DeviceListe) == 0:
            reponse = "Aucun appareil trouvé"
   
    else : 
        reponse = "Aucun appareil trouvé"
    
    
    
    
    print(reponse)
    return statement(reponse)




@ask.session_ended
def session_ended():
    return "{}", 200




#On Off command

if __name__ == '__main__':
    app.run(debug=True)