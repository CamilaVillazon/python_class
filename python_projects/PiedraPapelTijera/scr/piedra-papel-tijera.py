'''
NAME
    piedra-papel-tijera   

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este script permire al usuario jugar piedra, papel o tijera con la computadora.
        El programa pide al usuario su opción y la computadora aleatoriamente eligirá su opción.
    
        
USAGE
    % py piedra-papel-tijera.py
    
'''

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse
import random

# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Establecer parser
parser= argparse.ArgumentParser(description=" Juego de piedra papel o tijera. "+
      "\n Indique el numero de partidas que quiere jugar.\n")

# Argumentos
parser.add_argument('partidas',
                    metavar='p',
                    type=int,
                    help='numero de partidas')

# Ejecutar método parse_args()
args = parser.parse_args()

# ===========================================================================
# =                            functions
# ===========================================================================

def game(name, match):
    for i in range(match): 
        print ("Partida #", (i+1))
        
        options= ["piedra", "papel", "tijera"]
        
        #opcion del usuario
        print ("Ingresa tu opción: ")
        users_choice= options[int(input())-1]
        print ("\n", name, ": ", users_choice)

        #generar la poción de la computadora
        computers_choice= options[random.randint(0,2)]
        print("\n Computadora: "+ computers_choice)

        #Ver quien gana
        if users_choice == "papel" and computers_choice== "piedra":
            print("\n Ganaste!")
        elif users_choice == "piedra" and computers_choice== "tijera":
            print("\n Ganaste!")
        elif users_choice == "tijera" and computers_choice== "papel":
            print("\n Ganaste!")
        elif users_choice == "papel" and computers_choice== "tijera":
            print("\n Perdeiste, suerte a la proxima...")
        elif users_choice == "piedra" and computers_choice== "papel":
            print("\n Perdeiste, suerte a la proxima...")
        elif users_choice == "tijera" and computers_choice== "piedra":
            print("\n Perdeiste, suerte a la proxima...")
        else: print("\n Empate, ésto no se puede quedar así!")

        print("\n============================================")


    print("\n Hasta la próxima, "+ name+ "\n")

# ===========================================================================
# =                            main
# ===========================================================================

#pedir el nombre del usuario y explicar reglas del juego
print ("================================== \n",
       "Bienvenido al juego de Piedra, Papel o Tijera \n \n",
            "¿Cómo te llamas?: ")
name= input()
print ("\n\n Hola "+ name + "!","\n   Para jugar debes  ingresar el numero correspondiente a tu opcion: \n", 
       "    1 = piedra \n    2 = papel \n    3 = tijera \n\n",
       "   La computadora elige una opción al azar.\n", 
       "   Suerte! \n")

# almacenar número de partídas en una variable
match = args.partidas

game(name, match)


    