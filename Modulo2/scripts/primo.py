

# Evaluar del siguiente listado aquellos numeros que son primos


def calcular_divisores(numero_evaluar):
    """Se encarga de retornar una lista con todos los divisores de un numero dado"""
    divisores = []
    for i in range(1, numero_evaluar+1):
        if numero_evaluar%i==0:
            divisores.append(i)
    return divisores


# mi listado de numeros
listado = [7,13,10,15]

# Por cada numero, evaluo 
for numero in listado:

    divisores = calcular_divisores(numero)
    if len(divisores)==2:
        print(f'Numero {numero} -> PRIMO')
    else:
        print(f'Numero {numero} -> NO PRIMO')


print('Fin de mi programa!!!')