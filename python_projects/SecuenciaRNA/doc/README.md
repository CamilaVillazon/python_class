# T1_SecuenciaRNA

## Autor: Camila Villazon Soto Innes

### Version: 07/09/2023

# Introducción
El tipo de dato string es una clase que se puede manipular a conveniencia gracias a los multiples métodos que posee.
Algunos de estos métodos son: 
- 'find()': que permite encontrar la posicion de un caracter determinado
- '+': no es un método, pero es un operador que nos permite concatenar diferentes variables

# Problema
Para ejercitar la manipulación de cadenas se plantea el siguiente problema: 
Encontrar la posición del codón de inicio en una secuencia de ADN. De igul forma, imprimir la secuencia entre el codón de inicio y el codón de paro.

# Metodología
1. El usuario ingresa el archivo con la secuencia de ADN por paso de argumentos en línea de comandos
2. Se establece que el codón de inicio complementario es TAC. Se encuentra su posición con la función 'find'
3. Se imprime la posición 
4. Buscar la posición del codón de paro con 'find'
5. Se imprime la secuencia entre el codón de paro y de inicio, ya que se puede imprimir la cadena indicando la posicion [inicio:fin]



# Resultados
#### Caso 1. El archivo de secuencia existe 

archivo de entrada: data/dna.txt
descripción: 

1. El programa se ejecuta 
```% py scr/T1_SecuenciaRNA.py  ```

2. El programa debe pedir lo siguiente:

```path  ```

3. El resultado se vería en pantalla
```
 El codon de inicio esta en la posicion:  55

 El fragmento que sera RNA es:  TACCG
 ```

#### Caso 2. El archivo de secuencia viene vacio 
archivo de entrada: data/dna_vacio.txt
descripción: el programa arroja la leyenda "Archivo vacío"


#### Caso 3. El archivo de secuencia no existe
archivo de entrada: incorrecto
descripción: No se encontró el archivo.

### Caso 4. El archivo no contiene un codón de paro o término
archivo de entrada: data/dna_sin_codon.txt
descripción: No se encontró una secuencia codificante.