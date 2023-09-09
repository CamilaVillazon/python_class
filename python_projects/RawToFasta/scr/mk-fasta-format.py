'''
NAME
    T5_mk-fasta-format   

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa crea un archivo fasta a partir de la secuencia de DNA en formato .txt
    

'''

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse 


# ===========================================================================
# =                            Command Line Options
# ===========================================================================


# Establecer parser
descripcion=(" Este programa toma un archivo de texto plano y un nombre \n", 
             "para una secuencia de DNA para crear un archivo fasta.")
parser= argparse.ArgumentParser(description=descripcion)

# Argumentos
parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='El path del archivo')

parser.add_argument('nombre_secuencia',
                    type=str,
                    help='Identificador o nombre de la secuencia')

parser.add_argument('path_salida',
                    type=str,
                    help='El path del archivo de salida con terminacion .fasta')

# Ejecutar método parse_args()
args = parser.parse_args()


# ===========================================================================
# =                            main
# ===========================================================================

#  Abrir y leer archivo. 
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
    #recibir argumento en una variable:
    nombre_secuencia= args.nombre_secuencia
    path_salida=args.path_salida
   
    #crear archivo fasta
    try:
        archivo_fasta=open(path_salida , "w")
        
        #escribir el archivo fasta
        archivo_fasta.write(">"+ nombre_secuencia + "\n" + dna)
        print("\n\n Se creo el archivo fasta dna.fasta. ")

        #cerrar archivo
        archivo_fasta.close()
    except IOError:
        print ("No se encontró el archivo. ")

