#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

# Diccionario por comprensión, llave: número odioso, valor: tupla(número en binario, número en hexa).
# Número odioso -> impar de 1's en su binario
print ({x:(bin(x),hex(x)) for x in range(50) if bin(x).count('1')%2 != 0})