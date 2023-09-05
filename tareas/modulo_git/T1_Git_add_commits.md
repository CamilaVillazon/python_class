# Tarea 1: Git y gitHub: add, commits

## Camila Villazón Soto Innes

# Introducción
En esta tarea se repuerzan los primeros comandos de git para el control de versiones de archivos. Entre estos comando tenemos:
- ``git status`` para ver los archivos que están commited. ver estado de preparacion
- ``git commit -m`` para agregar mensaje e identificar versiones
- ``git add`` para añadir a preparación (staging area).
- ``git log`` muestra los commits que lleva. 


# Problema

Necesitamos una secuencia de un gene para probar que nuestro programa `reverse-complement` trabaja correctamente.

- En un archivo de texto, coloca la secuencia de DNA del gene *araC* de *E.coli* en formato fastA (puedes obtenerla aqui http://regulondb.ccg.unam.mx/sequence?type=GN&term=ECK120000050&format=fasta ).

- Sigue las buenas practicas de nombrado de archivos (no espacios en blanco, no caracteres especiales).

- Este archivo guardalo en la carpeta `data` del proyecto `reverse-complement`.

- Haz que el archivo sea controlado por git.

- En un reporte en markdown indica lo que hiciste y ese documento debe estar en la carpeta `doc`.


# Metodo y Resultados

Codigo total
````
 #Estando parados en reverse-complement
 #moverse a data
 cd data/
 
 #crear el archivo con la secuencia araC
 nano araC_coli.txt
 
 #añadir al área de preparación
 git add araC_coli.txt
 
 #revisar estatus
 git status 
 
 #aparece:
 #On branch master
 #Changes to be committed:
 #  (use "git restore --staged <file>..." to unstage)
 #        new file:   araC_coli.txt
 
 #Añadir mensaje
 git commit -m "seguencia inicial descargada"
 
 #Observar el historial de commmit 
  git log
  
 #Se obtiene:
 #commit 1c4842fe0ef625a24cfc5d1c024437ef8a3807e6 (HEAD -> master)
 #Author: Camila Villazon <camilav@lcg.unam.mx>
 #Date:   Mon Feb 13 22:55:27 2023 -0600
 #
 #    seguencia inicial descargada
 
````


# Conclusión
Git es una herramienta que nos permite almacenar y controlar los cambios que se hagan en el contenido del repositorio (carpeta con los cambios) mediante el directorio .git. 

De esta manera podemos tener un "Ctrl + Z" infinito que nos permite revisitar versiones anteriores que nos ayudan a dar seguimiento a errores que se puedan dar en un proyecto. 
