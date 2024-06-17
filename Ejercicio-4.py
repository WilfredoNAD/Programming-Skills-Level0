"""El usuario registra sus ingresos totales.
Hay categorías: Gastos médicos, gastos del hogar, ocio, ahorros y educación.
El usuario puede listar sus gastos dentro de las categorías y obtener el total para cada categoría.
El usuario puede obtener el total de sus gastos.
Si el usuario gasta la misma cantidad de dinero que gana, el sistema debe mostrar un mensaje aconsejando al usuario que reduzca los gastos en la categoría donde ha gastado más dinero.
Si el usuario gasta menos de lo que gana, el sistema muestra un mensaje de felicitación en la pantalla.
Si el usuario gasta más de lo que gana, el sistema mostrará consejos para mejorar la salud financiera del usuario."""

class Finanzas:

    def __init__(self):
        self.ingresos_totales = 0
        self.gastos = {
            'Gastos médicos': 0,
            'Gastos del hogar': 0,
            'Ocio': 0,
            'Ahorros': 0,
            'Educación': 0
        }

#se utiliza categoria y cantidad para interactuar con el (self) que en este caso es "gastos" para
    def registrar_ingreso(self, cantidad):
        self.ingresos_totales += cantidad
        print(f"ingresos totales actualizados: {self.ingresos_totales}")

    def registrar_gasto(self, categoria, cantidad):
        if categoria in self.gastos:
            self.gastos[categoria] += cantidad
            print(f"Gasto registrado en {categoria}: {cantidad}")
        else:
                   print("Categoría no válida")

    def obtener_total_categoria(self, categoria):
         if categoria in self.gastos:
              total = self.gastos[categoria]
              print(f"Total de gastos en {categoria}: {total}")
              return total
         else:
              print("categoria no valida")
              return 0

    def obtener_gastos_total(self):
         total = sum(self.gastos.values())
         print(f"Total de gastos: {total}")
         return total

    def revisar_finanza(self):
        total_gastos = self.obtener_gastos_total()
        if total_gastos < self.ingresos_totales:
            print("Felicidades! Estás gestionando bien tus finanzas")
        elif total_gastos == self.ingresos_totales:
            max_categoria = max(self.gastos, key=self.gastos.get)
            print(f"Advertencia: Estás gastando tanto como ganas. Considera reducir tus gastos en la categoría {max_categoria}.")
        else:
            print("Has gastado más de lo que ganas. Aquí hay algunos consejos para mejorar tu salud financiera:")
            print("- Elabora un presupuesto y síguelo.")
            print("- Reduce gastos innecesarios.")
            print("- Aumenta tus ingresos buscando fuentes adicionales.")
            print("- Ahorra una parte de tus ingresos regularmente.")

# Ejemplo de uso
# Ejemplo de uso
usuario = Finanzas()
usuario.registrar_ingreso(2000)
usuario.registrar_gasto("Gastos médicos", 200)
usuario.registrar_gasto("Gastos del hogar", 600)
usuario.registrar_gasto("Ocio", 300)
usuario.registrar_gasto("Ahorros", 400)
usuario.registrar_gasto("Educación", 500)

usuario.obtener_total_categoria("Gastos del hogar")
usuario.revisar_finanza()
