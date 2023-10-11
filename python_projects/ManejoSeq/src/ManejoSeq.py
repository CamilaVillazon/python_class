'''
NAME
    ManejoSeq    

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa permite calcular el promedio de calidad de cada una de las lecturas
        de un archivo fastq. 
    
        
USAGE
    % py ManejoSeq.py [-h] 

EXAMPLE

    
'''

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse
from Bio import SeqIO 


# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Establecer parser
parser= argparse.ArgumentParser(description=" \n    ManejoSeq devuelve el score de cada lectura en un archivo fastq\n")

# Argumentos
parser.add_argument('file', 
                    type=str,
                    help='ruta al archivo fastq')

parser.add_argument('score_range', 
                    type=int,
                    help="score promedio para las lecturas")

parser.add_argument('--bottom', 
                    action='store_true',
                    required=False,
                    default=False,
                    help="mostrar los scores igual o menores al score_range")


# Ejecutar método parse_args()
args = parser.parse_args()


# ===========================================================================
# =                            functions
# ===========================================================================

def fastq_scores(fq_file, score_range, bottom_score):
    n=0
    for record in SeqIO.parse(fq_file, "fastq"):
        n+=1
        score_sum=0
        for i in (record.letter_annotations['phred_quality']):
            score_sum+=i
    
        score_average=score_sum/len(record.letter_annotations['phred_quality'])
        if bottom_score:
            if score_average <= score_range: 
                print(" lectura ",n)
                print("     ID: ",record.id,"\n     score promedio:",round(score_average,0))
        elif score_average >= score_range:
            print(" lectura ",n)
            print("     ID:",record.id,"\n     score promedio: ",round(score_average,0))
    

# ===========================================================================
# =                            main
# ===========================================================================

fq_file=args.file
score_range=args.score_range
bottom_score=args.bottom

fastq_scores(fq_file, score_range, bottom_score)

