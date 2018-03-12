import id3_version1
import numpy as np
from pprint import pprint

def main():
    archivo_entrenamiento = open('entrenamiento_descuentos.csv')

    elementos_entrenamiento = []
    elementos_meta = []

    lineas_entrenamiento = list(archivo_entrenamiento)
    
    for i in range(len(lineas_entrenamiento[0].split(',')) - 1):
        elementos_entrenamiento.append([])

    atributos = lineas_entrenamiento[0].split(',')
    atributos = atributos[:-1]

    lineas_entrenamiento.pop(0)

    for linea in lineas_entrenamiento:
        linea = linea.strip("\n")
        elementos_meta.append(int(linea.split(',')[len(linea.split(',')) - 1]))
        for i in range(len(linea.split(',')) - 1):
            elementos_entrenamiento[i].append(linea.split(',')[i])            

    datos_entrenamiento = np.array(elementos_entrenamiento).T
    elementos_meta = np.array(elementos_meta)

    pprint(id3_version1.construirArbol(datos_entrenamiento,elementos_meta,atributos))
    
if __name__ == '__main__':
    main()