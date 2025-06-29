
"""
Se tiene el siguiente listado de numeros 
[100, 12, 21, 7 , 8]

Para cada uno de ellos calcule los divisores del respectivo numero

Salida esperada
8 -> [1,2,4,8]
"""


def calcular_divisores(numero_evaluar):
    """Se encarga de retornar una lista con todos los divisores de un numero dado"""
    divisores = []
    for i in range(1, numero_evaluar+1):
        if numero_evaluar%i==0:
            divisores.append(i)
    return divisores



listado_numero = [100, 12, 21, 7 , 8]

# 1. recorro el listado de numeros a evaluar
for numero in listado_numero:
    # 2. encuentro sus divisores
    divisores = calcular_divisores(numero)
    print(f'{numero} -> {divisores}')




# for numero in listado_numero:
#     # 2. encuentro sus divisores
#     divisores = []
#     for i in range(1, numero+1):
#         if numero%i==0:
#             divisores.append(i)
#     print(f'{numero} -> {divisores}')


print('Fin del programa!')


