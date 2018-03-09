import id3_version1

def main():
    archivo_entrenamiento = open('entrenamiento_descuentos.csv')

    objetivo = "Descuento"

    datos_entrenamiento = [[]]
    
    for linea in archivo_entrenamiento:
        linea = linea.strip("\n")
        datos_entrenamiento.append(linea.split(','))
    
    datos_entrenamiento.remove([])
    atributos = datos_entrenamiento[0]
    datos_entrenamiento.remove(atributos)

    arbol_decision = id3_version1.construirArbol(datos_entrenamiento, atributos, objetivo)

    
if __name__ == '__main__':
    main()