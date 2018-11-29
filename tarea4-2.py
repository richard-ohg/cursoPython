#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import xml.etree.ElementTree as ET

nombre_archivo="nmap.xml"


def host_prendidos_apagados():
	'''
		Función para hacer una lista de ip's de los host prendidos y los host apagados
	'''
	lista_prendidos=[]
	lista_apagados=[]
	with open(nombre_archivo,'r') as passwd:
		root = ET.fromstring(passwd.read())
		for a in root.findall('host'):
			if a.find('status').get('state') == "up":
				lista_prendidos.append(a.find('address').get('addr'))
			else:
				lista_apagados.append(a.find('address').get('addr'))
	return len(lista_prendidos),len(lista_apagados)

print host_prendidos_apagados()