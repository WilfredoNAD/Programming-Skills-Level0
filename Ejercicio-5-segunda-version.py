"""
Crear un sistema de inscripción universitaria con las siguientes características:

LISTO - El sistema tiene un inicio de sesión con un nombre de usuario y una contraseña.

LISTO - Al iniciar sesión, se muestra un menú con los programas disponibles: Informática, Medicina, Marketing y Artes.

LISTO - El usuario debe ingresar su nombre, apellido y el programa elegido.

LISTO - Cada programa tiene solo 5 plazas disponibles. El sistema almacenará los datos de cada usuario registrado y, si se supera el límite, debe mostrar un mensaje indicando que el programa no está disponible.

LISTO - Si la información de inicio de sesión es incorrecta tres veces, el sistema debe bloquearse.

LISTO - El usuario debe elegir un campus entre tres ciudades: Londres, Manchester, Oxford.

-----En Londres, hay 1 plaza por programa; en Manchester, hay 3 plazas por programa, y en Liverpool, hay 1 plaza por programa.

-----Si el usuario selecciona un programa en un campus que no tiene plazas disponibles, el sistema debe mostrar la opción de inscribirse en el programa en otro campus."""

class SistemaInscripcion:
    def __init__(self):
        self.user = []
        self.Intentos_loggin = 0
        self.Intentos_maximos = 3
        self.Cursos = {
            "Python": 5,
            "Java": 5,
            "C++": 5,
            "Ruby":5   
        }

        self.campus = {
            "Londres":{"Python": 1, "Java": 1, "C++":1, "Ruby": 1},
            "Manchester":{"Python":3, "Java":3, "C++":3, "Ruby":3},
            "Oxford":{"Python": 1, "Java":1, "C++":1, "Ruby":1}
        }

    def login():
        while self.intentos_loggin < self.Intentos_maximos:
            Usuario = input("ingrese su Usuario: ")
            Contraseña = input("Ingrese su contraseña: ")
            if self.autentificacion(Usuario, Contraseña):
                print("Credenciales Validadas")
                print("Bienvenido al Sistema de inscripcion universitario")
                return True
            else:
                print("Usuario o Contraseña Invalido")
                self.Intentos_loggin += 1
        print("Usuario Bloqueado por limite de intentos.")
        return False
        
    def autentificacion(self, Usuario, Contraseña):
        return Usuario == "WilfredoNAD" and Contraseña == "1234"
    
    def inscripcion(self):
        if not self.login():
            return
        
        print("Cursos disponibles: Python, Java, C++, Ruby ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("ingrese su apellido: ")
        curso_elegido = input("Ingrese el curso escogido: ")
        campus = input("Elija entre los campus: Manchester, Londres, Oxford:  ")
            

        if curso_elegido not in self.cursos:
            print("Elija un curso valido")

        if campus not in self.campus:
            print("elija un campus valido")

        if self.campus[campus][curso_elegido] > 0:
            self.campus[campus][curso_elegido] -= 1
            self.user.append({"Nombre": nombre, "Apellido":apellido, "Curso":curso_elegido, "Campus":campus})
            print("Inscripcion Exitosa")
        else:
            print("No hay cupos disponibles en este curso")
            self.sugerir_campus_disponible(curso_elegido)

    def sugerir_campus_disponibles(self, curso_elegido):
        campus_disponibles = [campus for campus in self.campus if self.campus[campus][curso_elegido] > 0]
        if campus_disponibles:
            print(f"El curso {curso_elegido} esta disponible en los siguientes campus: {" ".join(campus_disponibles)}")
        else:
            print(f"No hay cupos disponibles en el curso {curso_elegido} en ningun campus")


