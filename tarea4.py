#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

from datetime import datetime
import xml.etree.ElementTree as ET

hostDominio=0

def obtener_puertoX_abierto(puerto):
  cantPuerto=0
  with open("nmap.xml",'r') as passwd:
      root = ET.fromstring(passwd.read())
      for a in root.findall('host'):
        for x in a.findall('ports'):
          for y in x.iter('port'):
            if int(y.get('portid')) == puerto and y.find('state').get('state') == "open":
              cantPuerto += 1
  return cantPuerto

def obtener_apagados_prendidos():
  hostPrendidos=0
  hostApagados=0
  with open("nmap.xml",'r') as passwd:
      root = ET.fromstring(passwd.read())
      for a in root.findall('host'):
        if a.find('status').get('state') == "up":
          hostPrendidos += 1
        else:
          hostApagados += 1
  return hostPrendidos,hostApagados



print obtener_puertoX_abierto(22)
print obtener_apagados_prendidos()


# def escribirReporte():
# 	with open("reporte.txt", "w") as file:
# 		file.write(str(datetime.now()) + '\n')
# 		file.write("text")