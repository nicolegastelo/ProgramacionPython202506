# Genere una estructura de datos que permita contener un listado de notas por alumno

# codigo: codigo_alumno
# nombres: nombres
# apellidos:apellidos


# curso: nombre_curso
# credito: num_creditos
# nota: 

diccionario_notas_alumno = {
    "codigo": "20141201G",
    "nombres": "Gonzalo",
    "apellidos": "Delgado",
    "cursos": [
        {"curso": "Matematica Aplicada", "num_creditos": 6, "nota":11},
        {"curso": "Econometria", "num_creditos": 4, "nota": 15}
    ]
    # "curso1"
    # "curso2"

}

# quiero agregar un curso más en el listado
diccionario_notas_alumno['cursos'].append(
    {"curso": "Control de Procesos", "num_creditos": 2, "nota":15}
)

# Eliminando un curso del listado cursos por posicion
diccionario_notas_alumno['cursos'].remove(0) 


# Quiero saber cuantos cursos esta llevando este alumno
len( diccionario_notas_alumno['cursos']  )

# Cual es el codigo de este alumno?
diccionario_notas_alumno['codigo']








# SUpongamos que queremos tener la nota de 3 alumnos

diccionario_notas_alumno2 = {
    "codigo": "20141201G",
    "nombres": "Gonzalo",
    "apellidos": "Delgado",
    "cursos": [
        {"curso": "Matematica Aplicada", "num_creditos": 6, "nota":11},
        {"curso": "Econometria", "num_creditos": 4, "nota": 15}
    ]
    # "curso1"
    # "curso2"

}

diccionario_notas_alumno3 = {
    "codigo": "20141201G",
    "nombres": "Gonzalo",
    "apellidos": "Delgado",
    "cursos": [
        {"curso": "Matematica Aplicada", "num_creditos": 6, "nota":11},
        {"curso": "Econometria", "num_creditos": 4, "nota": 15}
    ]
    # "curso1"
    # "curso2"

}



listado_alumnos =[
    diccionario_notas_alumno,
    diccionario_notas_alumno2,
    diccionario_notas_alumno3

] 
























