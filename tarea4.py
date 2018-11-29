#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
# para md5 https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
# para sha1 https://stackoverflow.com/questions/22058048/hashing-a-file-in-python 

from datetime import datetime
import xml.etree.ElementTree as ET
import hashlib

nombre_archivo="nmap.xml"
hostDominio=0

def md5(archivo):
  '''
		Función para calcular el hash MD5 de un archivo
		Recibe:
			nombre del archivo
		Retorna:
			hash 
	'''
  hash_md5 = hashlib.md5()
  with open(archivo, "rb") as f:
      for chunk in iter(lambda: f.read(4096), b""):
          hash_md5.update(chunk)
  return hash_md5.hexdigest()

def sha1(archivo):
  '''
		Función para calcular el hash sha1 de un archivo
		Recibe:
			nombre del archivo
		Retorna:
			hash 
	'''
  hash_md5 = hashlib.sha1()
  with open(archivo, "rb") as f:
      for chunk in iter(lambda: f.read(4096), b""):
          hash_md5.update(chunk)
  return hash_md5.hexdigest()


def obtener_apagados_prendidos():
  '''
		Función para obtener el número de host prendidos y host apagados
		Retorna:
			host prendidos, host apagados
	'''
  hostPrendidos=0
  hostApagados=0
  with open(nombre_archivo,'r') as passwd:
      root = ET.fromstring(passwd.read())
      for a in root.findall('host'):
        if a.find('status').get('state') == "up":
          hostPrendidos += 1
        else:
          hostApagados += 1
  return hostPrendidos,hostApagados

def host_puertos_abiertos():
  '''
		Función para obtener el número de host que tienen los puertos 22,53,80 y 443 abiertos
		Recibe:
			número del puerto
		Retorna:
			cantidad de host 
	'''
  p22=0
  p53=0
  p80=0
  p443=0
  with open(nombre_archivo,'r') as passwd:
      root = ET.fromstring(passwd.read())
      for a in root.findall('host'):
        for x in a.findall('ports'):
          for y in x.iter('port'):
            if int(y.get('portid')) == 22 and y.find('state').get('state') == "open":
              p22 += 1
            if int(y.get('portid')) == 53 and y.find('state').get('state') == "open":
              p53 += 1
            if int(y.get('portid')) == 80 and y.find('state').get('state') == "open":
              p80 += 1
            if int(y.get('portid')) == 443 and y.find('state').get('state') == "open":
              p443 += 1
  return p22,p53,p80,p443

def escribirReporte():
  '''
		Función para escribir en un archivo llamado "reporte.txt" y en pantalla todo lo que se pide
	'''
  hash_md5 = md5(nombre_archivo)
  hash_sha1 = sha1(nombre_archivo)
  hapagados,hprendidos=obtener_apagados_prendidos()
  p22,p53,p80,p443 = host_puertos_abiertos() 

  with open("reporte.txt", "w") as file:
  	file.write(str(datetime.now()) + '\n\n')
  	file.write("MD5: " + md5(nombre_archivo) + '\n')
  	file.write("SHA1: " + sha1(nombre_archivo) + '\n')
  	file.write("Cantidad de host prendidos: %d \n" % hprendidos)
  	file.write("Cantidad de host apagados: %d \n" % hapagados)
  	file.write("Cantidad de host con puerto 22 abierto: %d \n" % p22)
  	file.write("Cantidad de host con puerto 53 abierto: %d \n" % p53)
  	file.write("Cantidad de host con puerto 80 abierto: %d \n" % p80)
  	file.write("Cantidad de host con puerto 443 abierto: %d \n" % p443)

	print "MD5: " + md5(nombre_archivo)
	print "SHA1: " + sha1(nombre_archivo)
	print "Cantidad de host prendidos: %d" % hprendidos
	print "Cantidad de host apagados: %d" % hapagados
	print "Cantidad de host con puerto 22 abierto: %d" % p22
	print "Cantidad de host con puerto 53 abierto: %d"  % p53
	print "Cantidad de host con puerto 80 abierto: %d" % p80
	print "Cantidad de host con puerto 443 abierto: %d" % p443


if __name__ == '__main__':
	escribirReporte()