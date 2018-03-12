import numpy as np

def divisionArbol(datosEntrenamientoPorNodo):
    return {c: (datosEntrenamientoPorNodo==c).nonzero()[0] for c in np.unique(datosEntrenamientoPorNodo)}

def calcularEntropia(elementos_meta):
    res = 0
    val, counts = np.unique(elementos_meta, return_counts=True)
    frecuencia = counts.astype('float')/len(elementos_meta)
    for p in frecuencia:
        if p != 0.0:
            res -= p * np.log2(p)
    return res

def informacionComun(elementos_meta, atributo_entrenamiento):
    res = calcularEntropia(elementos_meta)

    val, counts = np.unique(atributo_entrenamiento, return_counts=True)
    frecuencia = counts.astype('float')/len(atributo_entrenamiento)

    for p, v in zip(frecuencia, val):
        res -= p * calcularEntropia(elementos_meta[atributo_entrenamiento == v])

    return res

def tieneValoresUnicos(s):
    return len(set(s)) == 1

'''
* Construye recursivamente el arbol de decision
'''
def construirArbol(datos_entrenamiento,elementos_meta,atributos):
    if tieneValoresUnicos(elementos_meta) or len(elementos_meta) == 0:
        if elementos_meta[0] == 1:
            return '+'
        else:
            return '-'

    ganancia = np.array([informacionComun(elementos_meta, atributo_entrenamiento) for atributo_entrenamiento in datos_entrenamiento.T])
    indice_atributo_nodo = np.argmax(ganancia)
    atributo_nodo = atributos[indice_atributo_nodo]

    if np.all(ganancia < 1e-6):
        return '???'

    conjuntos_arbol_divididos = divisionArbol(datos_entrenamiento[:, indice_atributo_nodo])

    res = {}
    for k, v in conjuntos_arbol_divididos.items():
        elementos_meta_divididos = elementos_meta.take(v, axis=0)
        datos_entrenamiento_divididos = datos_entrenamiento.take(v, axis=0)
        res["%s = %s" % (atributo_nodo, k)] = construirArbol(datos_entrenamiento_divididos, elementos_meta_divididos,atributos)
    return res