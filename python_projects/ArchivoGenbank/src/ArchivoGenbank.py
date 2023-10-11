'''
NAME
    ArchivoGenbank    

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

parser.add_argument('genes',
                    nargs='+',
                    help='lista de genes que desea buscar')

# Ejecutar método parse_args()
args = parser.parse_args()


# ===========================================================================
# =                            functions
# ===========================================================================

def gb_data(gb_file, gene_list):
    
    for gb_record in SeqIO.parse(gb_file,"genbank"):
        print('Organismo: ',gb_record.annotations['organism'])
        print('Fecha: ',gb_record.annotations['date'])
        for feature in gb_record.features:
            if feature.type == 'source':
                print ('País:',feature.qualifiers['country'])
                print('Fuente de aislado: ',feature.qualifiers['isolation_source'])
            if feature.type == 'CDS':
                for gene in gene_list:
                    if feature.qualifiers['gene'][0] == gene:
                        print('Gene:',feature.qualifiers['gene'])
                        print('ADN: ', gb_record.seq[feature.location.start : feature.location.end], '\n')
                        print('ARN: ', gb_record.seq[feature.location.start : feature.location.end].transcribe(),'\n')
                        print('Proteina: ', feature.qualifiers['translation'],'\n')



# ===========================================================================
# =                            main
# ===========================================================================

gb_file = args.file
gene_list=[]
for gene in args.genes:
    gene_list.append(gene)

gb_data(gb_file, gene_list)