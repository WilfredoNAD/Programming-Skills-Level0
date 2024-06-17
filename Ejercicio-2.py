"""Crea un sistema de envío en línea con las siguientes características:

--El sistema tiene un inicio de sesión que se bloquea después del tercer intento fallido.
Muestra un menú que permite: Enviar un paquete, salir del sistema.
--Para enviar un paquete, se requieren detalles del remitente y del destinatario.
--El sistema asigna un número de paquete aleatorio a cada paquete enviado.
--El sistema calcula el precio del envío. $2 por kg.
--El usuario debe ingresar el peso total de su paquete, y el sistema debe mostrar la cantidad a pagar.
--El sistema debe preguntar si el usuario desea realizar otra operación.
--Si la respuesta es sí, debe regresar al menú principal. Si es no, debe cerrar el sistema."""

import random

Datos = {"Username":"WilfredoNAD", "Password":1234}

def login():
    intentos = 0
    limite_intentos = 3
    while intentos < limite_intentos:
        Usuario = input("Ingrese su Usuario: ")
        Contraseña = int(input("Ingrese su Contraseña: "))
        if Usuario == Datos["Username"] and Contraseña == Datos["Password"]:
            print("Credenciales Aceptadas")
            print("Bienvenido a Mega Entregas")
            return True
        else:
            print("Usuario o Contrasea erroneos, Intente de nuevo")
            intentos += 1
    print("Usuario Bloqueado por limite de intentos.")
    print("Comuniquese con soporte para el desbloqueo.")
    return False
    


def Envio():
    Nombre_remitente = input("Ingrese el nombre del remitente: ")
    Nombre_Lugar = input("Ingrese la ciudad a enviar")
    Peso_Paquete = float(input("Ingrese el peso del paquete: "))
    Precio_Paquete = 2 * Peso_Paquete
    Nombre_Destinatario = input("Ingrese el nombre de la persona que recibe: ")
    Nombre_Destino = input("Indique que ciudad que recibe el paquete: ")
    Numero_Track = random.randint(1000, 9999)
    print("Descripcion del Envio: ")
    print(f"Nombre del remitente: {Nombre_remitente}")
    print(f"Nombre del destino: {Nombre_Lugar}")
    print(f"Peso Total {Peso_Paquete}")
    print(f"Precio total: {Precio_Paquete}")
    print(f"Nombre de la persona que retira: {Nombre_Destinatario}")
    print(f"Lugar de retiro: {Nombre_Destino}")
    print(f"Track de rastreo: {Numero_Track}")



def main():
    if not login():
        return
    while True:
        print("\nSeleccione una opción:")
        print("1. Envio")
        print("2. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "1":
            Envio()
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()