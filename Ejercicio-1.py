Datos = {"BankUser":"WilfredoNAD", "BankPass":1234, "BankBalance":2000}

def login():
    intentos = 0
    Limite_Intentos = 3
    while intentos < Limite_Intentos:
        Usuario = input("ingrese su Usuario: ")
        Contraseña = int(input("Ingrese su contraseña: "))
        if Usuario == Datos["BankUser"] and Contraseña == Datos["BankPass"]:
            print("Credenciales Validadas")
            print("Bienvenido a Banca Sectaria")
            return True
        else:
            print("Usuario o Contraseña Invalido")
            intentos += 1
    print("Usuario Bloqueado por limite de intentos.")
    return False
        

def Retiro():
    print(f"Saldo Disponible: {Datos['BankBalance']}")
    monto_a_retirar = int(input("Ingrese el monto que desea retirar: "))
    if monto_a_retirar > Datos["BankBalance"]:
        print("Monto invalido por falta de saldo")
    else:
        Datos["BankBalance"] -= monto_a_retirar
    print(f"Usted ha retirado la cantidad de: {monto_a_retirar}")
    print(f"Balance actual: {Datos['BankBalance']}")

def Deposito():
    print(f"Saldo Disponible: {Datos['BankBalance']}")
    monto_a_depositar = int(input("Ingrese la monto a depositar: "))
    Datos["BankBalance"] += monto_a_depositar
    print(f"Monto depositado: {monto_a_depositar}")
    print(f"Balance actual: {Datos['BankBalance']}")

def Transferencia():
    print(f"Saldo disponible: {Datos['BankBalance']}")
    monto_a_transferir = int(input("Ingrese la cantidad a transferir"))
    if monto_a_transferir > Datos["BankBalance"]:
        print("Monto no valido por falta de saldo")
    else:
        Datos["BankBalance"] -= monto_a_transferir
        print(f"Usted a transferir la cantidad de: {monto_a_transferir}")
        print(f"Balance despues de realizacion de transferencia: {Datos['BankBalance']}")


def main():
    if not login():
        return
    while True:
        print("\nSeleccione una opción:")
        print("1. Retiro")
        print("2. Depósito")
        print("3. Transferencia")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "1":
            Retiro()
        elif opcion == "2":
            Deposito()
        elif opcion == "3":
            Transferencia()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()