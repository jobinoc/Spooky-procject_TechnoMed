# -*- coding: utf-8 -*-  permet l'utilisation des accents dans les commentaire

## Exemple simple d'envoi de messages OSC

import OSC  ## charge le module OSC (pyOSC)
from range_sensor import get_distance

c = OSC.OSCClient() ##instancie OCS.client dans c.  Le client OSC sera invoqué par c
c.connect(('192.168.0.107',1880)) ## connection au "serveur", i.e. la machine à qui on veut envoyer les messages
oscmsg = OSC.OSCMessage() ## le message OSC - OSC.OSCMessage() - est placé dans oscmsg

print(c)

## préparation du message:
def envoiOSC():

    ## spécifie l'adresse (path) dans le message OSC
    addr_OSC="/composition/layers/1/clips/2/transport/position/out"
    oscmsg.setAddress(addr_OSC)
    
    dist = get_distance()

    ## on ajoute la valeur numérique au message OSC
    oscmsg.append('Distance (cm): %s' %dist)

    ## on envoie le message OSC
    c.send(oscmsg)
    print oscmsg

    ## on réinitialise (vide) le message OSC
    oscmsg.clearData()


## répète la fonction
i = 0
while i < 25:
    envoiOSC()
    i += 1
  
  





