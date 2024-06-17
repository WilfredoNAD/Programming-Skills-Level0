class SistemaInscripcion:
    def __init__(self):
        self.usuarios = []
        self.intentos_login = 0
        self.intentos_maximos = 3
        self.cursos = {
            "Python": 5,
            "Java": 5,
            "C++": 5,
            "Ruby": 5
        }

        self.campus = {
            "Londres": {"Python": 1, "Java": 1, "C++": 1, "Ruby": 1},
            "Manchester": {"Python": 3, "Java": 3, "C++": 3, "Ruby": 3},
            "Oxford": {"Python": 1, "Java": 1, "C++": 1, "Ruby": 1}
        }

    def login(self):
        while self.intentos_login < self.intentos_maximos:
            usuario = input("Ingrese su usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            if self.autenticacion(usuario, contraseña):
                print("Credenciales Validadas")
                print("Bienvenido al Sistema de Inscripción Universitario")
                return True
            else:
                print("Usuario o Contraseña Inválido")
                self.intentos_login += 1
        print("Usuario Bloqueado por límite de intentos.")
        return False

    def autenticacion(self, usuario, contraseña):
        return usuario == "WilfredoNAD" and contraseña == "1234"

    def inscripcion(self):
        if not self.login():
            return

        print("Cursos disponibles: Python, Java, C++, Ruby")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        curso_elegido = input("Ingrese el curso escogido: ")
        campus = input("Elija entre los campus: Manchester, Londres, Oxford: ")

        if curso_elegido not in self.cursos:
            print("Elija un curso válido.")
            return

        if campus not in self.campus:
            print("Elija un campus válido.")
            return

        if self.campus[campus][curso_elegido] > 0:
            self.campus[campus][curso_elegido] -= 1
            self.usuarios.append({"Nombre": nombre, "Apellido": apellido, "Curso": curso_elegido, "Campus": campus})
            print("Inscripción Exitosa")
        else:
            print("No hay cupos disponibles en este curso en el campus seleccionado.")
            self.sugerir_campus_disponibles(curso_elegido)

    def sugerir_campus_disponibles(self, curso_elegido):
        campus_disponibles = [campus for campus in self.campus if self.campus[campus][curso_elegido] > 0]
        if campus_disponibles:
            print(f"El curso {curso_elegido} está disponible en los siguientes campus: {', '.join(campus_disponibles)}")
        else:
            print(f"No hay cupos disponibles en el curso {curso_elegido} en ningún campus.")

# Uso del sistema
sistema = SistemaInscripcion()
sistema.inscripcion()
print(sistema.usuarios)
