'''
NAME
    TiendaAnimales    

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este script permire al usuario ordenar una pizza. 
        El usuario debe ingresar los ingredientes que desee por línea de comandos.
    
        
USAGE
    % py TiendaMascotas.py [-h] {perro,gato} nombre

EXAMPLE
% py TiendaMascotas.py perro Firulais


Nombre: Firulais
Edad: 4
Edad en años de tu mascota: 16
Color: negro con manchas
    
'''

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse
from random import choice

# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Establecer parser
parser= argparse.ArgumentParser(description=" \n    Bienvenido al Refugio de Animales! \n     Adopta una mascota (perro o gato).\n")

# Argumentos
parser.add_argument('mascota', 
                    type=str,
                    choices=["perro", "gato"],
                    help='Mascota a elegir')

parser.add_argument('nombre', 
                    type=str,
                    help="Dale un nombre a tu mascota")


# Ejecutar método parse_args()
args = parser.parse_args()

# ===========================================================================
# =                            classes
# ===========================================================================

# clase parental
class mascota():
    # constructor de la clase padre
    def __init__(self, nombre):
        # inicializar el atributo nombre
        self.nombre = nombre

    # método tiempo que inicializa la edad con un valor aleatorio
    def tiempo(self):
        self.edad=choice(range(1,10))
        

    # método aspecto que inicializa el atributo color
    def aspecto(self):
        self.color=choice(["negro","blanco","pardo"])



# subclase gato de clase mascota 
class gato(mascota):
    # Constructor. También llama métodos de la clase parental
    def __init__(self, nombre):
        super().__init__(nombre)
        super().tiempo()
        super().aspecto()
    
    # Overriding del método tiempo
    def tiempo(self):
        self.edad *= 7
        return (self.edad)

    #polimorfismo del color
    def pelaje(self):
        self.color +=" con rayas"
        return(self.color)

    

class perro(mascota):
    # Constructor. También llama métodos de la clase parental
    def __init__(self, nombre):
        super().__init__(nombre)
        super().tiempo()
        super().aspecto()
    
    # Overriding del método tiempo
    def tiempo(self):
        self.edad*=4
        return(self.edad)

    #polimorfismo del color
    def pelaje(self):
        self.color+=" con manchas"
        return(self.color)

        


# ===========================================================================
# =                            main
# ===========================================================================

# Parsear argumentos que vienen de línea de comandos
tipo_mascota=args.mascota
nombre=args.nombre

# Crear objeto
if tipo_mascota=="gato":
    tu_mascota=gato(nombre)

else:
    tu_mascota=perro(nombre)

# Imprimir características del objeto
print("Tu mascota tiene las siguientes caracteristicas: \n",
      f"Nombre: {tu_mascota.nombre}\n",
      f"Edad: {tu_mascota.edad}\n",
      f"Edad en años de tu mascota: {tu_mascota.tiempo()}\n",
      f"Color: {tu_mascota.pelaje()}\n")