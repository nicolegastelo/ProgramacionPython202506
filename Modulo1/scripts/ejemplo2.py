"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total.

"""


PRECIO_PAN = 3.49
DESCUENTO = 0.6

cantidad_barras = int(input('Ingrese el numero de barras de pan vendidas que no son del día: '))

descuento_aplicado = DESCUENTO * cantidad_barras * PRECIO_PAN
precio_pagado = cantidad_barras * PRECIO_PAN *(1-DESCUENTO)


print(f'Precio barra pan {PRECIO_PAN}')
print(f'Descuento aplicado {descuento_aplicado} ')
print(f'Precio pagado por el cliente: {precio_pagado:.2f}')





