import id3_version1
import numpy as np
from pprint import pprint
from datetime import datetime
import copy

def evaluar(arbol_decision,elemento_evaluacion,indice_evaluacion):
    for k,v in elemento_evaluacion.items():
        for ke,va in arbol_decision.items():
                llave = ke.split(" = ")
                nodo_arbol_decision = llave[0]
                rama = llave[1]
                if (nodo_arbol_decision == k and rama == v):
                    if(va == '+' or va == '-' or va == '???'):
                        print(str(indice_evaluacion) +" -> " +va)
                    else:                      
                        el_ev = elemento_evaluacion.copy()
                        el_ev.pop(nodo_arbol_decision, None)                        
                        evaluar(va,el_ev,indice_evaluacion)

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

    print("Tiempo de inicio: "+datetime.now().strftime('%H:%M:%S.%f'))

    print("\n------ Árbol de decisión ------\n")
    arbol_decision = id3_version1.construirArbol(datos_entrenamiento,elementos_meta,atributos)
    pprint(arbol_decision)

    print("\n------ Evaluación ------\n")    

    #pprint(diccionario_eval)
    
    #print(len(diccionario_eval[atributos_evaluacion[0]]))
    for i in range(len(diccionario_eval[atributos_evaluacion[0]])):
        elemento_evaluacion = {}
        for k,v in diccionario_eval.items():
            elemento_evaluacion[k] = v[i]
        evaluar(arbol_decision,elemento_evaluacion,i)

    print("Tiempo de finalización: "+datetime.now().strftime('%H:%M:%S.%f'))
    
if __name__ == '__main__':
    main()