# -*- coding: utf-8 -*-

import OSC
from range_sensor import get_distance

r_ip = raw_input('Entrer le IP du recepteur: ')
r_port_s = raw_input('Entrer le port du recepteur: ')
r_port = int(r_port_s)

c = OSC.OSCClient()
c.connect((r_ip, r_port))
oscmsg = OSC.OSCMessage()


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
  
  





