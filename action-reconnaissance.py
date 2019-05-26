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
	anniv = datetime.date(year+1, manniv, janniv) 
	diff = anniv - today



	if intent_message.intent.intent_name == 'xrobquin:Reconnaissance_proche':
		
		if (diff.days%365-1) == 0:
    			liste_reponses_marie = ["Je vous souhaite un très heureux anniversaire"]
		else:
    			liste_reponses_marie = ["j'adore votre haut",
                              "Comment allez vous aujourd'hui?",
                              "J moins "+str(diff.days%365-1)+" avant votre anniversaire",
                              "Je suis ravie de faire la conversation avec vous",
                              "On commande des sushis ?",
                              "J'ai hâte de voir monsieur Robquin habillé en requin",
                              "Etes-vous allée courir aujourd'hui ?",
                              "Puis-je vous demander une carte postale de Namur ?" ]
			
		sentence = 'Salut '	
		
		if len(intent_message.slots.Name)==1:
			name = intent_message.slots.Name.first().value
			if (name =='William'):
				name = 'Williame'
				result_sentence = 'Ravie de discuter avec vous'
			elif (name =='Marie'):
				index_reponse = random.randint(0,len(liste_reponses_marie)-1)
				result_sentence = liste_reponses_marie[index_reponse]
			    
			sentence += name
			sentence += ', '
			sentence += result_sentence
			
				
			
				
			
		hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
	
	
	
	
	
	
	
	
