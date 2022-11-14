def info_global(categ, lista):
    rtas = {}
    for dato in lista:
        if dato[categ] in rtas.keys():
            rtas[dato[categ]] += 1
        else:
            rtas[dato[categ]] = 1
    return rtas


def proporciones(total, dic, key):
    return f'{dic[key] / total : .2f}'


def prop_totales(total, dic):
    aux = {}
    for key in dic:
        aux[key] = proporciones(total, dic, key)
    return aux


def mostrar_proporciones(totales, datos, nombres, key):
    print(key + " :")
    for i in range(len(totales)):
        print( nombres[i] + ": " , end = '') 
        print(prop_totales(totales[i], info_global(key, datos[i])))


def detectar_distintos(a,b, umbral):
    if abs(a - b) > umbral:
        return True
    return False


def imprimir_distintos(totales, datos, nombres, key, umbral):
    print(key + " :")
    propors = [] 
    for i in range(len(totales)):
        propors.append(prop_totales(totales[i], info_global(key, datos[i])))


    for i in range(1, len(propors)):
        print( nombres[i] + ": " , end = '') 
        for key in propors[i]:
            if detectar_distintos(float(propors[i][key]), float(propors[0][key]), umbral):
                print(key + " - ", end = '')
        print('')

