# ManejoSeq

### Autor: Camila Villazón
### Versión: 02/10/2023

## Introducción
En el trabajo bioinformático se trabaja constantemente con diferentes archivos de secuencias. 
Dichos archivos contienen incluso cientos de secuencias, por lo que es necesario extraer información 
de forma eficiente.

## Problema
Generar una función que extraiga las lecturas de un archivo fastq que en promedio cumplan 
con el score indicado por el usuario.

## Metodología
1. Usuario el path al archivo fastq, el score deseado y opcionalmente,
si se muestran las lecturas debajo del score.
2. El programa mostrará el id y el score promedio de las lecturas que cumplan la condición. 

## Resultados y Pruebas

El usuario puede probar con lo siguiente:

''' %  py .\ManejoSeq\src\ManejoSeq.py .\ManejoSeq\data\sample.fastq 20 --bottom '''

Debiendo obtener:

 lectura  11
     ID:  HWI-ST279:219:D0RJNACXX:6:2303:16177:171984
     score promedio: 17.0
 lectura  13
     ID:  HWI-ST279:219:D0RJNACXX:6:2303:16383:171755
     score promedio: 13.0