'''
NAME
    SecuenciaRNA    

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa regresa la posición del codón inicial y donde termina el codón de término de una secuencia
        de DNA.     

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
parser= argparse.ArgumentParser(description=" Este programa indica la posicion del codón de inicio,"+
      "\n asi como la secuencia entre el codon de inicio y el de paro\n")

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

def codon_inicio_paro(dna):
    # codon de inicio complementario a ATG
    inicio_codon= 'TAC'

    # almacenar posicion del codon de inicio
    pos_inicio_codon= dna.find(inicio_codon)
    if (pos_inicio_codon > 0):
          
          # imprimir posicion del codon de inicio
          print('\n El codon de inicio esta en la posicion: ', pos_inicio_codon)
          
          # codon de paro
          paro_codon= 'ATT'
          
          # almacenar posicion del codon de paro
          pos_paro_codon= dna.find(paro_codon)

          if (pos_paro_codon > 0):
              # imprimir del codon de inicio hasta donde termina el codon de paro
              print('\n El fragmento que sera RNA es: ', dna [pos_inicio_codon:pos_paro_codon])
    
    else:
        print("\n No se encontró una secuencia codificante.\n")
        


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
    dna= archivo_abierto.read()
    dna=dna.rstrip("\n").upper().split("\n")
    dna=' '.join(dna)
    archivo_abierto.close()
    if len(dna)==0:
        raise ValueError(f'Archivo vacío')
except IOError:
    print ("No se encontró el archivo. ")
else:
    codon_inicio_paro(dna)



