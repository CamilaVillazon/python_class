'''
NAME
    T5_at_gc_content  

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa pregunta al usuario la ruta y el nombre del archivo de DNA, y 
        regrese el porcentaje de AT y GC
    

'''

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse 

# ===========================================================================
# =                            Command Line Options
# ===========================================================================


# Establecer parser
parser= argparse.ArgumentParser(description=" Este programa calcula los porcentajes de GC y de AT en una secuencia de DNA")

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

def at_gc_content(dna):
    # Contar ocurrencia de cada nucleótido
    a=dna.count('A')
    t=dna.count('T')
    g=dna.count('G')
    c=dna.count('C')

    # Contar el total de nucleótidos
    nt_totales= a + t + g + c

    # Calcular porcentaje de AT y GC
    porcentaje_at= ((a+t)/nt_totales)*100
    porcentaje_gc= ((g+c)/nt_totales)*100

    print("\n El porcentaje de AT es : ", porcentaje_at, " % \n", 
          "El porcentaje de GC es: ", porcentaje_gc, " %")


# ===========================================================================
# =                            main
# ===========================================================================


#Abrir y leer archivo. 
# Eliminar ultimo caracter. 
# Corregir a mayúsculas
# Si vienen varial lineas, separa por saltos de línea en una lista
# Eliminar espacios vacíos
try:
    archivo=open(args.Path)
    dna=archivo.read().rstrip("\n").upper().split("\n")
    dna=' '.join(dna)
    archivo.close()
    if dna.count("N")>0:
        raise ValueError(f'Su archivo contiene {dna.count("N")} N\'s')
    if len(dna)==0:
        raise ValueError(f'Archivo vacío')
except IOError:
    print ("No se encontró el archivo. ")
else:
    at_gc_content(dna)
