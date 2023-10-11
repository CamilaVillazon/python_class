# ArchivoGenbank

### Autor: Camila Villazón
### Versión: 02/10/2023

## Introducción
En el trabajo bioinformático se trabaja constantemente con diferentes archivos de secuencias. 
Dichos archivos contienen incluso cientos de secuencias, por lo que es necesario extraer información 
de forma eficiente.

## Problema
Generar una función que extraiga los metadatos, features y ciertas secuencias del
origin de un archivo de genebnk.

## Metodología
1. Usuario ingresa el path al archivo genbank, y los genes de interés.
2. El programa mostrará Organismo, Fecha, País, Fuente de aislado, Gene,
ADN, ARN y Proteina. 

## Resultados y Pruebas

El usuario puede probar con lo siguiente:

''' % py .\ArchivoGenbank\src\ArchivoGenbank.py .\ArchivoGenbank\data\virus.gb N L'''

Debiendo obtener:

Organismo:  Isfahan virus
Fecha:  13-AUG-2018
País: ['Iran:Isfahan province']
Fuente de aislado:  ['Phlebotomus papatasi']
Gene: ['N']
ADN:  ATGACTTCTGTAGT...

ARN:  AUGACUUCUGUAGU...

Proteina:  ['MTSVVKRIATGSS...']

Gene: ['L']
ADN:  ATGGATGAGTACTCTG...

ARN:  AUGGAUGAGU...

Proteina:  ['MDEYSEEKWGDSD...']