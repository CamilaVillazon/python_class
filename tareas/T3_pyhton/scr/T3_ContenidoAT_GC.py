'''
NAME
    T3_ContenidoAT_GC   

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa pregunta al usuario la ruta y el nombre del archivo de DNA, y 
        regrese el porcentaje de AT y GC
    

'''
# ===========================================================================
# =                            main
# ===========================================================================


# pedrir archivo con la secuendia de DNA al usuario
print("==================================== \n  Ingrese el nombre o la ruta de un archivo tipo .txt con una secuencia de DNA: ")
archivo_original= input()

#obrir y leer archivo
with open(archivo_original) as archivo_abierto:
    dna_contenido= archivo_abierto.read()

    #quitar el caracter de nueva linea
    dna_contenido=dna_contenido.rstrip("\n")

    #calcular porcentaje de AT y GC
    a=dna_contenido.count('A')
    t=dna_contenido.count('T')
    g=dna_contenido.count('G')
    c=dna_contenido.count('C')

    nt_totales= a + t + g + c

    porcentaje_at= ((a+t)/nt_totales)*100
    porcentaje_gc= ((g+c)/nt_totales)*100

    #imprimir resultados
    print("\n El porcentaje de AT es : ", porcentaje_at, " % \n El porcentaje de GC es: ", porcentaje_gc, " %")
