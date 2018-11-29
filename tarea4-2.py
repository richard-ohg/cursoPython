#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import xml.etree.ElementTree as ET
import csv

nombre_archivo="nmap.xml"


def ips_host_prendidos_apagados():
	'''
		Función para hacer una lista de ip's de los host prendidos y los host apagados
		Retorna:
			lista con ip's de hostprendidos, lista con ip's de hostapagados
	'''
	lista_prendidos=['IPs de host prendidos']
	lista_apagados=['IPs de host apagados']
	with open(nombre_archivo,'r') as file:
		root = ET.fromstring(file.read())
		for a in root.findall('host'):
			if a.find('status').get('state') == "up":
				lista_prendidos.append(a.find('address').get('addr'))
			else:
				lista_apagados.append(a.find('address').get('addr'))
	return lista_prendidos,lista_apagados


def ips_host_puerto22_abiertos():
	'''
		Función para obtener las ip's de los host que tengan el puerto 22 abierto
		Retorna:
			lista con ip's
	'''
	p22=['IPs de host que tengan el puerto 22 abierto']
	with open(nombre_archivo,'r') as file:
		root = ET.fromstring(file.read())
		for a in root.findall('host'):
			for x in a.findall('ports'):
				for y in x.iter('port'):
					if int(y.get('portid')) == 22 and y.find('state').get('state') == "open":
						p22.append(a.find('address').get('addr'))
	return p22


def ips_honeypot():
	'''
		Función para saber las ip's de los host que tienen servidor http honeypot
		Retorna
			lista de ip's 
	'''
	honeypot=['Host que son honeypot']
	with open(nombre_archivo,'r') as file:
		root = ET.fromstring(file.read())
		for a in root.findall('host'):
			for x in a.findall('ports'):
				for y in x.iter('port'):
					if int(y.get('portid')) == 80 and y.find('service').get('product') == "Dionaea Honeypot httpd":
						honeypot.append(a.find('address').get('addr'))
	return honeypot


def nombre_dominio():
	'''
		Función para saber los dominios junto a su IP
		Retorna:
			lista de tuplas que contiene ip y nombre de dominio 
	'''
 	dominios=['IP,Nombres de dominio']
	with open(nombre_archivo,'r') as file:
		root = ET.fromstring(file.read())
		for a in root.findall('host'):
			for x in a.findall('hostnames'):
				for y in x.findall('hostname'):
					dominios.append((a.find('address').get('addr'),y.get('name')))
	return dominios


def crear_csv():
	'''
		Función para crear el archivo csv con las ip's que se piden
	'''
	l_p,l_a = ips_host_prendidos_apagados()
	p22 = ips_host_puerto22_abiertos()
	honey = ips_honeypot()
	dom = nombre_dominio()
	with open('reporte.csv','w') as file:
		employee_writer = csv.writer(file)
		employee_writer.writerow(l_p)
		employee_writer.writerow(l_a)
		employee_writer.writerow(p22)
		employee_writer.writerow(honey)
		employee_writer.writerow(dom)


if __name__ == '__main__':
	crear_csv()
	