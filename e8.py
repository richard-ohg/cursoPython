#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

# Para ejecutarlo:
# python e8.py archivo_correo archivo_ips

from sys import argv
import re

correos='[a-z0-9]+[a-zA-Z0-9_]@(gmail|hotmail)\.com'
ips= "[0-2]?[0-9]{,2}\.[0-2]?[0-9]{,2}\.[0-2]?[0-9]{,2}\.[0-2]?[0-9]{,2}"

with open(argv[1]) as f1, open(argv[2]) as f2:
	for x in f1:
		if re.search(correos,x):
			print "El correo es correcto"
		else:
			print "El correo esta mal"

	for y in f2:
		if re.search(ips,y):
			print "La ip es correcta"
		else:
			print "La ip es incorrecta"
			