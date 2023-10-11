'''
NAME
    ManejoGenbank    

AUTHOR
      Camila Villazon Soto Innes  
    

'''

# ===========================================================================
# =                            imports
# ===========================================================================
from Bio import SeqIO
import argparse

# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Establecer parser
parser= argparse.ArgumentParser(description=" \n    Extraer metadatos y features de formato genbank\n")

# Argumentos
parser.add_argument('file', 
                    type=str,
                    help='ruta al archivo genebank')

# Ejecutar método parse_args()
args = parser.parse_args()


# ===========================================================================
# =                            main
# ===========================================================================


gb_file= args.file

for gb_record in SeqIO.parse(gb_file,"genbank"):
    print('date:',gb_record.annotations['date'])
    print('organism:',gb_record.annotations['organism'])
    print('country:',gb_record.features[0].qualifiers['country'])
    print('isolation:',gb_record.features[0].qualifiers['isolation_source'])

