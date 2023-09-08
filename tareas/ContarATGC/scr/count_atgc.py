'''
NAME
    T5_count_atgc  

VERSION
    2.0 11/05/2023

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa cuenta el total de A, C, G y T que hay en una secuencia de DNA ingresada por el
        usuario.

USAGE

    % python T5_count_atgc
    

'''
# ===========================================================================
# =                            imports
# ===========================================================================

import os
import argparse


# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Establecer parser
parser= argparse.ArgumentParser(description=" Este programa cuenta la ocurrencia de cada nucleotido A, T, G y C.")

# Argumentos
parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='La ruta al archivo')

# Ejecutar método parse_args()
args = parser.parse_args()


# ===========================================================================
# =                            functions
# ===========================================================================

def atgc_contenido (dna_contenido):
    # contar el total de A, T, G y C
    a=dna_contenido.count('A')
    t=dna_contenido.count('T')
    g=dna_contenido.count('G')
    c=dna_contenido.count('C')

    # imprimir el total de A, T, G y C
    print("\n El total de cada nucleotido es: \n A: ",a,"\n T: ",t,"\n G: ",g,"\n C: ",c)


# ===========================================================================
# =                            main
# ===========================================================================


# Abrir y leer archivo. 
# Eliminar ultimo caracter. 
# Corregir a mayúsculas
# Si vienen varial lineas, separa por saltos de línea en una lista
# Eliminar espacios vacíos
try: 
    archivo_abierto= open(args.Path)
    dna_contenido= archivo_abierto.read()
    dna_contenido=dna_contenido.rstrip("\n").upper().split("\n")
    dna_contenido=' '.join(dna_contenido)
    archivo_abierto.close()
    if dna_contenido.count("N")>0:
        raise ValueError(f'Su archivo contiene {dna_contenido.count("N")} N\'s')
    if len(dna_contenido)==0:
        raise ValueError(f'Archivo vacío')
except IOError:
    print ("No se encontró el archivo. ")
else:
    atgc_contenido(dna_contenido)
