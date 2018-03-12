def evaluar(arbol_decision,elemento_evaluacion,indice_evaluacion):
    for k,v in elemento_evaluacion.items():
        for ke,va in arbol_decision.items():
            llave = ke.split(" = ")
            nodo_arbol_decision = llave[0]
            rama = llave[1]
            if (nodo_arbol_decision == k and rama == v):
                if(va == '+' or va == '-' or va == '???'):
                    print("Elemento: "+str(indice_evaluacion) +" -> " +va)
                else:                      
                    el_ev = elemento_evaluacion.copy()
                    el_ev.pop(nodo_arbol_decision, None)                        
                    evaluar(va,el_ev,indice_evaluacion)