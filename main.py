import id3_version1
import evaluacion_id3
import numpy as np
from pprint import pprint
from datetime import datetime

'''
Aprendizaje
FI,UNAM
12/03/18
'''

def main():
    archivo_entrenamiento = open('entrenamiento_descuentos.csv')

    elementos_entrenamiento = []
    elementos_meta = []

    lineas_entrenamiento = list(archivo_entrenamiento)

    archivo_evaluacion= open('evaluacion_descuentos.csv')
    
    lineas_evaluacion = list(archivo_evaluacion)
    atributos_evaluacion = lineas_evaluacion[0].split(',')    

    lineas_evaluacion.pop(0)

    diccionario_eval = {}
    
    for i in range(len(lineas_entrenamiento[0].split(',')) - 1):
        elementos_entrenamiento.append([])
        atributos_evaluacion[i] = atributos_evaluacion[i].strip("\n")
        diccionario_eval[atributos_evaluacion[i]] = []

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

    for linea in lineas_evaluacion:
        linea = linea.strip("\n")
        indice_atrib = 0
        for e_v in linea.split(','):
            diccionario_eval[atributos_evaluacion[indice_atrib]].append(e_v)
            indice_atrib = indice_atrib + 1

    FMT = '%H:%M:%S.%f'

    tiempo_inicio = datetime.now().strftime(FMT)

    print("\n----------- ÁRBOL DE DECISIÓN -----------\n")
    arbol_decision = id3_version1.construirArbol(datos_entrenamiento,elementos_meta,atributos)
    pprint(arbol_decision)

    tiempo_fin = datetime.now().strftime(FMT)

    diferencia_tiempo = datetime.strptime(tiempo_fin, FMT) - datetime.strptime(tiempo_inicio, FMT)

    print("\nInicio: "+tiempo_inicio)
    print("Fin: "+ tiempo_fin)
    print("Diferencia: "+ str(diferencia_tiempo))

    print("\n\n----------- EVALUACIÓN -----------\n")
    
    tiempo_inicio = datetime.now().strftime(FMT)
    
    for i in range(len(diccionario_eval[atributos_evaluacion[0]])):
        elemento_evaluacion = {}
        for k,v in diccionario_eval.items():
            elemento_evaluacion[k] = v[i]
        evaluacion_id3.evaluar(arbol_decision,elemento_evaluacion,i)

    tiempo_fin = datetime.now().strftime(FMT)
    diferencia_tiempo = datetime.strptime(tiempo_fin, FMT) - datetime.strptime(tiempo_inicio, FMT)

    print("\nInicio: "+tiempo_inicio)
    print("Fin: "+ tiempo_fin)
    print("Diferencia: "+ str(diferencia_tiempo))
    
if __name__ == '__main__':
    main()