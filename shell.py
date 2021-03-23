#!/usr/bin/env python
# -*- coding: utf-8 -*-
# use suma 1 4

import cmd
from functools import reduce

class Comandos(cmd.Cmd):
    """Suma y multiplica números enteros"""
    prompt = "Introduzca un comando: "
    doc_header = "Comandos disponibles"
    ruler = "-"
    
    def do_suma(self, args):
        """Suma los argumentos que sean enteros. Ej.: suma 12 13"""
        enteros = obtener_enteros(args)
        if len(enteros) > 1:
            print('Total', sum(enteros))
        else:
            print('La operación requiere al menos dos números enteros')            

    def do_mult(self, args):
        """Multiplica argumentos que sean enteros. Ej.: mult 12 13"""
        enteros = obtener_enteros(args)
        if len(enteros) > 1:
            print('Total', reduce(lambda x,y: x*y, enteros))
        else:
            print('La operación requiere al menos dos números enteros')

    def do_salir(self, args):
        """Salir"""
        print("¡Hasta pronto!")
        return(True)
    
def obtener_enteros(args):
    """Divide cadena de argumentos y devuelve números enteros"""
    argumentos = args.split()
    enteros = list(filter(lambda x: x.isnumeric(), argumentos))
    enteros = list(map(int,enteros))
    return(enteros)
    
if __name__ == '__main__':
    Comandos().cmdloop()

