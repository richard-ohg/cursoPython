#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

lista=[]

def esPrimo(numero):
	'''
		Función para saber si un número es primo o no
		Recibe:
			un número
		Retorna 
			True -> si es primo
			False -> si no lo es
	'''
	for x in range(2,numero):
		if numero%x == 0:
			return False
	return True

def agregarPrimos(num,cantidad):
	'''
		Función recursiva para agregar los primeros n números primos a una lista
		Recibe:
			cantidad de números primos
		Retorna:
			lista con números primos
	'''

	# No recursivo
	'''
	lista = []
	num=2
	while len(lista) < cantidad:
		if esPrimo(num):
			lista.append(num)
		num += 1
	return lista
	'''
	# Recursivo
	if len(lista) < cantidad:
		if esPrimo(num):
			lista.append(num)
			#print(lista)
			return agregarPrimos(num+1, cantidad)
		else:
			#print(lista)
			return agregarPrimos(num+1, cantidad)
	return lista


print("lista de numeros primos: ",agregarPrimos(2,7))






