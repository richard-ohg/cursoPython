#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

lista=[]

def esPalindromo(cadena):
	'''
		Funcion para saber si una cadena es palindromo o no
		Recibe:
			cadena a validar
		Retorna
			True si es palindromo, false si no es
	'''
	return cadena == cadena[::-1]

def palindromoMasGrande(cadena):
	'''
		Función para saber el palindromo mas grande de una cadena
		Recibe: 
			cadena a validar
		Retorna:
			palindromo más grande
	'''
	palindromos=[]
	for i in range(len(cadena)):
		for j in range(len(cadena),0,-1):
			if esPalindromo(cadena[i:j]):
				if len(cadena[i:j]) > 1:
					palindromos.append(cadena[i:j])	
	palindromos.sort(key=len)
	# print(palindromos)
	return palindromos[-1]
		

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

if __name__ == '__main__':
	
	palabras=['hfjfalas','andanitalavalatinanfjdsnf','dbadbsnosoj','kfsjdamigonogimajjsoso.']
	print("lista de numeros primos: ",agregarPrimos(2,7))
	for pal in palabras:
		print("Palindromo mas grande : ", palindromoMasGrande(pal))
	

