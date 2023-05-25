'''
NAME
    Proyecto.py  

VERSION
    24/05/2023

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa cuenta el total de A, C, G y T que hay en una secuencia de DNA ingresada por el
        usuario.

USAGE

    % python Proyecto.py <path>
    

'''
# ===========================================================================
# =                            imports
# ===========================================================================

import os
import argparse
import re


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
    """Contar el total de A, T, G y C

    Parameters:
    argument1 (str): cadena con secuencia de DNA

    Returns:
    str : cadena con el total de A, T, G y C

   """
    a=dna_contenido.count('A')
    t=dna_contenido.count('T')
    g=dna_contenido.count('G')
    c=dna_contenido.count('C')

    resultado = f'El contenido de A, T, G, C es:\nA: {a}\nT: {t}\nG: {g}\nC: {c}\n'
    return(resultado)


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
    for nt in dna_contenido:
        if(nt!="A") and (nt!="T") and (nt!="G") and (nt!="C"):
            raise ValueError(f'Su archivo contiene {dna_contenido.count("N")} N\'s')
    if len(dna_contenido)==0:
        raise ValueError(f'Archivo vacío')
except IOError:
    print ("No se encontró el archivo. ")
else:
    resultado=atgc_contenido(dna_contenido)
    print(resultado)