#!/usr/bin/env python2
from hermes_python.hermes import Hermes
import datetime
from pytz import timezone
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()
	

	now = datetime.datetime.now()
	year = now.year
	today = datetime.date.today()
	anniv = datetime.date(year+1, 6, 3) 
	diff = anniv - today



	if intent_message.intent.intent_name == 'xrobquin:Reconnaissance_proche':
		
		liste_reponses_appetit = [" J'adore ce haut", " Comment allez vous aujourd'hui?", " j'ai besoin de repos"]
		sentence = 'Salut '	
		
		if len(intent_message.slots.Name)==1:
			name = intent_message.slots.Name.first().value
			if (name =='William'):
				name = 'Williame'
			    
			sentence += name
			sentence += ', '
			sentence += liste_reponses_appetit[random.randint(0,len(liste_reponses_appetit)-1)]
			
			
			    
			
			
		if len(intent_message.slots.Name2)==1:
			sentence += ' et salut '
			name = intent_message.slots.Name2.first().value
			if (name =='William'):
				name = 'Williame'

			
			
				
			
		hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
h.subscribe_intents(intent_received).start()
