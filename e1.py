#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

aprobados = []

def aprueba_becario(nombre_completo):
    '''
        Función para saber si un becario aprobó o no, se introduce el nombre en mayúsculas a la lista
        Recibe:
            nombre completo
        Regresa:
            True -> si aprobó
            False -> si no aprobó

    '''
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        if n.lower() in ['manuel', 'valeria', 'alejandro', 'luis', 'enrique','omar','abraham','oscar']:
            return False
    aprobados.append(nombre_completo.upper())
    aprobados.sort()
    return True

def borrar(nombre_completo):
    '''
        Borra el becario aprobado
        Recibe:
            nombre completo
        Regresa:
            True -> si se encuentra y fue borrado
            False -> si no está en la lista de aprobados
    '''
    if nombre_completo.upper() in aprobados:
            aprobados.remove(nombre_completo.upper())
            return True
    return False
        


becarios = ['Cervantes Varela JUAN MaNuEl',
            'Leal González IgnaciO',
            'Ortiz Velarde valeria',
            'Martínez Salazar LUIS ANTONIO',
            'Rodríguez Gallardo pedro alejandro',
            'Tadeo Guillén DiAnA GuAdAlUpE',
            'Ferrusca Ortiz jorge luis',
            'Juárez Méndez JeSiKa',
            'Pacheco Franco jesus ENRIQUE',
            'Vallejo Fernández RAFAEL alejanDrO',
            'López Fernández serVANDO MIGuel',
            'Hernández González ricaRDO OMAr',
            'Acevedo Gómez LAura patrICIA',
            'Manzano Cruz isaías AbrahaM',
            'Espinosa Curiel OscaR']
for b in becarios:
    if aprueba_becario(b):
        print 'APROBADOO: ' + b.upper()
    else:
        print 'REPROBADO: ' + b.upper()


print aprobados
borrar('López Fernández serVANDO MIGuel')
print aprobados





#print becarios
