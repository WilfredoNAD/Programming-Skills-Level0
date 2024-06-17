"""
Crear un sistema de inscripción universitaria con las siguientes características:

LISTO - El sistema tiene un inicio de sesión con un nombre de usuario y una contraseña.

LISTO - Al iniciar sesión, se muestra un menú con los programas disponibles: Informática, Medicina, Marketing y Artes.

LISTO - El usuario debe ingresar su nombre, apellido y el programa elegido.

Cada programa tiene solo 5 plazas disponibles. El sistema almacenará los datos de cada usuario registrado y, si se supera el límite, debe mostrar un mensaje indicando que el programa no está disponible.

LISTO - Si la información de inicio de sesión es incorrecta tres veces, el sistema debe bloquearse.

 - El usuario debe elegir un campus entre tres ciudades: Londres, Manchester, Liverpool.

-----En Londres, hay 1 plaza por programa; en Manchester, hay 3 plazas por programa, y en Liverpool, hay 1 plaza por programa.

-----Si el usuario selecciona un programa en un campus que no tiene plazas disponibles, el sistema debe mostrar la opción de inscribirse en el programa en otro campus."""


#----------------------

Datos = {"Usuario":"WilfredoNAD", "Contraseña":"1234"}

carreras = [
    {
        "campus":"Liverpool",
        "cursos":[
            {"Nombre":"Python", "cupos":1},
            {"Nombre":"Java", "cupos":1},
            {"Nombre":"C++", "cupos":1},
            {"Nombre":"Ruby", "cupos":1}
        ]
    },
    {
        "campus":"Manchester",
        "cursos":[
            {"Nombre":"Python", "cupos":3},
            {"Nombre":"Java", "cupos":3},
            {"Nombre":"C++", "cupos":3},
            {"Nombre":"Ruby", "cupos":3}
        ]
    },
    {
        "campus":"Londres",
        "cursos":[
            {"Nombre":"Python", "cupos":1},
            {"Nombre":"Java", "cupos":1},
            {"Nombre":"C++", "cupos":1},
            {"Nombre":"Ruby", "cupos":1}
        ]
    }
]

datos_registrados = []

def login():
    intentos = 0
    Limite_Intentos = 3
    while intentos < Limite_Intentos:
        Usuario = input("ingrese su Usuario: ")
        Contraseña = input("Ingrese su contraseña: ")
        if Usuario == Datos["Usuario"] and Contraseña == Datos["Contraseña"]:
            print("Credenciales Validadas")
            print("Bienvenido al Sistema de inscripcion universitario")
            return True
        else:
            print("Usuario o Contraseña Invalido")
            intentos += 1
    print("Usuario Bloqueado por limite de intentos.")
    return False
    
def inscripcion():
    print(f"ingrese sus datos: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    
    print("Elija un campus: ")
    for carrera in range(len(carreras)):
        print("campus {} : {}".format(carrera + 1, carreras[carrera]["campus"]))
    
    Eleccion = input("Ingrese el número de la carrera: ")

    print("Elija una carrera")
    for curso in range(len(carreras[Eleccion-1]["cursos"])):
        print("curso {} : {}".format(curso + 1, carreras[Eleccion-1]["cursos"]["Nombre"]))
   


def Elegir_Campus():
    print("Elija un campus: ")
    print("1. Londres")
    print("2. Manchester")
    print("3. Liverpool")
    campus = input("Ingrese el número del campus: ")
    if campus == "1":
        return "Londres"
    elif campus == "2":
        return "Manchester"
    elif campus == "3":
        return "Liverpool"
    else:
        print("Opcion invalida, ingresar opcion valida")

# Login = login()
# if Login:
#     carrera = inscripcion()

# for carrera in carreras:
#         print(f"{carrera["campus"]}")
for carrera in range(len(carreras)):
        print("campus {} : {}".format(carrera + 1, carreras[carrera]["campus"]))

