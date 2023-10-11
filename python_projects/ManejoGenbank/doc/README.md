# ManejoGenbank

### Autor: Camila Villazón
### Versión: 02/10/2023

## Introducción
En el trabajo bioinformático se trabaja constantemente con diferentes archivos de secuencias. 
Dichos archivos contienen incluso cientos de secuencias, por lo que es necesario extraer información 
de forma eficiente.

## Problema
Generar una función que extraiga los metadatos y features de un archivo de genebnk.

## Metodología
1. Usuario ingresa el path al archivo genbank.
2. El programa mostrará Organismo, Fecha, País y Fuente de aislado. 

## Resultados y Pruebas

El usuario puede probar con lo siguiente:

''' % py .\ManejoGenbank\src\ManejoGenbank.py .\ManejoGenbank\data\virus.gb'''

Debiendo obtener:

date: 13-AUG-2018
organism: Isfahan virus
country: ['Iran:Isfahan province']
isolation: ['Phlebotomus papatasi']