#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

# Para correr:
# python tarea3.py -f archivo_palabras

import itertools as it
import sys
import optparse
from random import choice

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-f','--file', dest='file', default=None, help='Archivo de donde se obtendran las palabras')
    opts,args = parser.parse_args()
    return opts


def permutaciones(lista,cantidad):
	palabras=[]
	perm=list(it.permutations(lista, cantidad))
	# print(len(perm))
	for pal in perm:
		palabras.append("".join(pal))
	return palabras

def cambiar_min_mayus(lista):
	lis=[]
	for palabra in lista:
		for letra in palabra:
			lis.append(palabra.replace(letra,letra.upper()))
	return lis

def cambiar_letras_numeros(lista):
	lis=[]
	for palabra in lista:
		if 'a' in palabra or 'e' in palabra or 'o' in palabra :
			for letra in palabra:
				if letra == 'a':
					new_string = palabra.replace(letra,'4')
					lis.append(new_string)
				if letra == 'e':
					new_string = palabra.replace(letra,'3')
					lis.append(new_string)
				if letra == 'o':
					new_string = palabra.replace(letra,'0')
					lis.append(new_string)
		else:
			lis.append(palabra)
	return lis
		

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
	# print len(palabras)
	with open('contrasenas.txt','w') as f:
		for pal in palabras:
			f.write(pal+'\n')
		new_list = set(cambiar_min_mayus(palabras))
		# print len(new_list)
		for pal in new_list:
			f.write(pal+'\n')
		new_list = set(cambiar_letras_numeros(palabras))
		# print len(new_list)
		for pal in new_list:
			f.write(pal+'\n')
		perm = permutaciones(palabras,2)
		# print len(perm)
		for pal in perm:
			f.write(pal+'\n')
		new_list = set(cambiar_min_mayus(perm))
		# print len(new_list)
		for pal in new_list:
			f.write(pal+'\n')
		new_list = set(cambiar_letras_numeros(new_list))
		# print len(new_list)
		for pal in new_list:
			f.write(pal+'\n')
		perm = permutaciones(palabras,3)
		# print len(perm)
		for pal in perm:
			f.write(pal+'\n')
		new_list = set(cambiar_min_mayus(perm))
		# print len(new_list)
		for pal in new_list:
			f.write(pal+'\n')
		new_list = set(cambiar_letras_numeros(new_list))
		# print len(new_list)
		for pal in new_list:
			f.write(pal+'\n')

