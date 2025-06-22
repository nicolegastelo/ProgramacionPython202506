
Ingrese la base y la altura de un triángul, luego realice el cálculo del área. Por último muestre  el resultado en pantalla
""



# 1. Ingreso de datos
# funcion "input" -> retorna un "str", si deseo un número debo convertirlo
base_triangulo = int(input("Ingrese la base del triangulo:"))
altura_triangulo = int(input("Ingrese la altura del triangulo:"))

#2. Calcula area dle triangulo

area_triangulo = base_triangulo * altura_triangulo /2

#3. Imprimir resultado
print(area_triangulo)
#Imprimiendo con "f" fromat string delante del texto
print(f"El area del triangulo con base () y la altura () es : {}")
print(type(base_triangulo))