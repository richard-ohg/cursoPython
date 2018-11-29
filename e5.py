#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

eq1 = ['Juan Manuel','Ignacio','Valeria','Luis Antonio','Pedro Alejandro']
eq2 = ['Diana Guadalupe','Jorge Luis','Jesika','Jesus Enrique','Rafael Alejandro']
eq3 = ['Servando Miguel','Ricardo Omar','Laura Patricia','Isaias Abraham','Oscar']

#expresion funcional:
# 1) funcion lambda que sume las tres listas
# 2) filtre la lista resultante para obtener a los que tienen un solo nombre (filter)
# 3) convierta a mayusculas los nombres del resultado anterior (map)
# 4) obtener una cadena con los nombres resultantes, separando los nombres con coma (reduce)
#UNA SOLA EXPRESION

print( reduce(lambda x,y: x+","+y ,map(lambda lista: lista.upper(),filter(lambda lista: " " not in lista,(lambda lista1,lista2,lista3: lista1+lista2+lista3)(eq1,eq2,eq3)))) )
