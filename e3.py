#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

calificacion_alumno = {}
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
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def aprobado():
    aprobados=[]
    noAprobados=[]
    for alu,cal in calificacion_alumno.items():
        if cal >= 8:
            aprobados.append(alu)
        else:
            noAprobados.append(alu)
    return tuple(aprobados),tuple(noAprobados)

def promedio():
    prom=0
    for cal in calificacion_alumno.values():
        prom+=cal
    return float(prom)/len(calificacion_alumno)

def conjunto():
    return set([a for a in calificacion_alumno.values()])

            

asigna_calificaciones()
imprime_calificaciones()
print(aprobado())
print(promedio())
print(conjunto())

