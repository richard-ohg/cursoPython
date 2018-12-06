#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

# Para correr:
# python tarea3.py -f archivo_palabras

import itertools as it
import sys
import optparse

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-f','--file', dest='file', default=None, help='Archivo de donde se obtendran las palabras')
    opts,args = parser.parse_args()
    return opts


def permutaciones(lista,cantidad):
	palabras=[]
	perm=list(it.permutations(lista, cantidad))
	for pal in perm:
		palabras.append("".join(pal))
	return palabras

def cambiar_min_mayus(lista):
	for palabra in lista:
		lis=[palabra.replace(letra,letra.upper()) for letra in palabra]
	return lis

def cambiar():
	pass

def leer_palabras(archivo):
	lista=[]
	with open(archivo) as file:
		for line in file:
			lista.append(line[:-1])
	return lista





if __name__ == '__main__':
	opts = addOptions()
	if opts.file is None:
		print "Debe contener un archivo con palabras"
		sys.exit(1)
	palabras = leer_palabras(opts.file)
	with open('contrasenas.txt','w') as f:
		for num in range(1,len(palabras)+1):
			perm = permutaciones(palabras,num)
			for pal in perm:
				f.write(pal+'\n')