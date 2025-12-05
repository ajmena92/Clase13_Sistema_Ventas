import os

# Importar todas las funcion necesarias de los otros modulos
from datos import guardar_csv, ingresar_ventas, cargar_ventas
from analisis import analiza_ventas


# La lista que funciona como base de datos
VENTAS_DATA = []


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    global VENTAS_DATA
    while True:
        # Cada vez que se muestra el menu, limpiar la pantalla
        limpiar_pantalla()
        print("\n--- 🛒 Menú de Gestión de Ventas ---")
        print("1. Ingresar nueva venta")
        print("2. Analisis de ventas todas las ventas")
        print("3. Cargar ventas desde archivo")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            ingresar_ventas(VENTAS_DATA)
        elif opcion == "2":
            analiza_ventas(VENTAS_DATA)
        elif opcion == "3":
            VENTAS_DATA = cargar_ventas()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        input("Presione Enter para continuar...")


if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión de Ventas!")
    VENTAS_DATA = cargar_ventas()  # Cargar datos existentes si los hay
    menu()
