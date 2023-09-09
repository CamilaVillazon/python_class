# mk-fasta-format

## Autor: Camila Villazon Soto Innes

### Version: 07/09/2023

## Introducción

En bioinformática es común trabajar con archivos en formato fasta para manejar las secuencias. 
Programas como blast y otras herramientas requieren que las secuencias esten en ese formato.


## Problema

Algunas bases de datos dan las secuencias en formato plano, es decir sin formato alguno, 
solo la secuencia en una sola línea o en ocasiones en multiples lineas.

Este programa `mk-fasta-format` ayuda al usuario a poner convertir facilmente el formato plano a formato fasta.

## Metodología o Algoritmo

El programa `mk-fasta-sormat` hace lo siguiente:

1. Pedir al usuario el path del archivo tipo .txt con una secuencia de DNA, que se almacena en la variable archivo_original.  
    (Se recomienda que para probar el programa, se utilice el archivo dna.txt encontrado en la carpeta data)
2. Pedir el nombre de la secuencia de DNA al usuario, que será usado como identificador de la secuencia.
3. Leer la secuencia de dna del archivo de entrada
7. Formatear la secuencia de formato plano a format fasta
8. Guardar la secuencia fasta en el archivo de salida

## Resultados y pruebas

#### Caso 1. El archivo de secuencia existe y se genera un archivo en formato fastA

archivo de entrada: data/dna.txt
archivo de salida: results/ejemplo-fasta
descripción: 

1. El programa se ejecuta 
```% py scr/T5_mk-fasta-format.py  ```

2. El programa debe pedir lo siguiente:

```path nombre_secuencia path_salida ```

3. El resultado esta en el archivo ejemplo.fasta y el contenido se vería
``` ```

#### Caso 2. El archivo de secuencia viene vacio 
archivo de entrada: data/dna_vacio.txt
archivo de salida: results/dna_vacio.fasta
descripción: el programa arroja la leyenda "Archivo vacío"



#### Caso 3. El archivo de secuencia no existe
archivo de entrada: data/dna_con_N.txt
archivo de salida: reults/dna_con_N.fasta
descripción: el programa arroja "ValueError: Su archivo contiene 6 N's"

