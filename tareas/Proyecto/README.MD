# Proyecto

### Autor: Camila Villazon Soto Innes

### Version: 24/05/2023


## Introducción
Python puede manipular cadenas de texto o strings, que se almacenan en variables por practicidad. En esta tarea se ejercita el nombrado consistente de variables y la manipulación de string, que incluyen: concatenación (por medio de sumas), multiplicación y manipulación por métodos de la clase cadena.

## Problema
Para poner a prueba estos elementos se resuelve el problema: Pedir una secuencia de DNA al usuario y contar el total de cada nucleótido (A, T, G, C).

## Resultados y Pruebas

#### Caso 1. El archivo de secuencia existe 
1. archivo de entrada: data/dna.txt 
2. El programa se ejecuta % py scr/Proyecto.py <data/dna.txt> 
3. El programa debe pedir el path de entrada

El resultado se vería en pantalla:  
El total de cada nucleotido es:
 
 A:  214
 
 T:  214
 
 G:  218
 
 C:  192 

#### Caso 2. El archivo de secuencia viene vacio

1. archivo de entrada: data/dna_vacio.txt 
2. descripción: el programa arroja la leyenda "Archivo vacío"

#### Caso 3. El archivo de secuencia no existe
1. archivo de entrada: data/dna_con_N.txt 
2. descripción: el programa arroja "ValueError: Su archivo contiene 6 N's"