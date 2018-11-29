#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import xml.etree.ElementTree as ET
import csv

nombre_archivo="nmap.xml"


def host_prendidos_apagados():
	'''
		Función para hacer una lista de ip's de los host prendidos y los host apagados
	'''
	lista_prendidos=['ips de host prendidos']
	lista_apagados=['ips de host apagados']
	with open(nombre_archivo,'r') as file:
		root = ET.fromstring(file.read())
		for a in root.findall('host'):
			if a.find('status').get('state') == "up":
				lista_prendidos.append(a.find('address').get('addr'))
			else:
				lista_apagados.append(a.find('address').get('addr'))
	return lista_prendidos,lista_apagados


def crear_csv():
	'''
		Función para crear el archivo csv con las ip's que se piden
	'''
	l_p,l_a = host_prendidos_apagados()
	with open('reporte.csv','w') as file:
		employee_writer = csv.writer(file)
		employee_writer.writerow(l_p)
		employee_writer.writerow(l_a)

# print host_prendidos_apagados()
crear_csv()