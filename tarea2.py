import string
from random import choice, randint

total=[['$','-','_','#','&'],list(string.ascii_lowercase),list(string.ascii_uppercase),range(0,10)]
tam=8
pwd=[]

def genPassword(cont):
	'''
		Función para generar una contraseña segura
		Recibe:
			cantidad de caracteres que quieres
		Retorna:
			contraseña
	'''
	if cont == 0:
		cad="".join(pwd)
		return cad
	else:
		pwd.append(str(choice(total[randint(0,3)])))
		return genPassword(cont-1)

print(genPassword(tam))