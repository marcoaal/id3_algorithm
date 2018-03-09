import math

def calcularEntropia(elementos_positivos,elementos_negativos):
    num_elementos = elementos_positivos + elementos_negativos
    print(elementos_positivos)
    print(num_elementos)
    print(elementos_negativos)
    entropia = -(elementos_positivos/num_elementos) * math.log2(elementos_positivos/num_elementos)-(elementos_negativos/num_elementos) * math.log2(elementos_negativos/num_elementos)
    print(entropia)

def calcularGanancia(atributo,datos_entrenamiento):
    print(atributo)

def dividirElementos(datos_entrenamiento,atributos,objetivo):    
    indice_objetivo = atributos.index(objetivo)
    elementos_positivos = 0
    elementos_negativos = 0
    for dato_unico_entrenamiento in datos_entrenamiento:
        if dato_unico_entrenamiento[indice_objetivo] == "si":
            elementos_positivos+=1
        else:
            elementos_negativos+=1
    calcularEntropia(elementos_positivos,elementos_negativos)

def construirArbol(datos_entrenamiento, atributos, objetivo):    
    dividirElementos(datos_entrenamiento,atributos,objetivo)
    return True