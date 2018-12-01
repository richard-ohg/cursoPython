#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def esPalindromo(cadena):
	'''
		Función para saber si una cadena es palindroma o no
		Recibe:
			cadena
		Retorna:
			True -> si lo es
			False -> si no lo es
	'''
	if cadena == cadena[::-1]:
		return True
	else:
		return False

if palin("anitalavalatina"):
	print "es palindromo"
else:
	print "no es"
