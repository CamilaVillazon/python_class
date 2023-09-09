# count_atgc

## Autor: Camila Villazon Soto Innes

### Version: 07/09/2023

# Introducción
Python puede manipular cadenas de texto o strings, que se almacenan en variables por practicidad. 
En esta tarea se ejercita el nombrado consistente de variables y la manipulación de string, que incluyen: concatenación (por medio de sumas), multiplicación y manipulación por métodos de la clase cadena.

# Problema
Para poner a prueba estos elementos se resuelve el problema: 
Pedir una secuencia de DNA al usuario y contar el total de cada nucleótido (A, T, G, C).

# Metodología
1. La secuencia de DNA proporcionada por el usuario se almacena en la variable dna
2. Para asegurar que la secuencia esté en mayúsculas se usa la función upper
3. Se imprime la secuencia
4. Para contar la ocurrencia de cada nucleotido se usa la función count, y se almacena en una variable correspondiente a, t, g, y c
5. Se imprime el resultado con print

# Resultados y Pruebas

#### Caso 1. El archivo de secuencia existe y se genera un archivo en formato fastA

archivo de entrada: data/dna.txt
descripción: 

1. El programa se ejecuta 
```% py scr/T5_count_atgc.py  ```

2. El programa debe pedir lo siguiente:

```path  ```

3. El resultado se vería en pantalla
``` ```

#### Caso 2. El archivo de secuencia viene vacio 
archivo de entrada: data/dna_vacio.txt
descripción: el programa arroja la leyenda "Archivo vacío"


#### Caso 3. El archivo de secuencia no existe
archivo de entrada: data/dna_con_N.txt
descripción: el programa arroja "ValueError: Su archivo contiene 6 N's"