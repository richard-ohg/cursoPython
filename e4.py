#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice
from poo import Becario

calificacion_alumno = []
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Juan Manual',
            'Ignacio',
            'Valeria',
            'Luis Antonio',
            'Pedro Alejandro',
            'Diana Guadalupe',
            'Jorge Luis',
            'Jesika',
            'Jesús Enrique',
            'Rafael Alejandro',
            'Servando Miguel',
            'Ricardo Omar',
            'Laura Patricia',
            'Isaías Abraham',
            'Oscar']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno.append(Becario(b,choice(calificaciones))) 

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print alumno.__str__()


asigna_calificaciones()
imprime_calificaciones()
