import csv
import pandas as pd


def guardar_csv(ventas, archivo="ventas.csv"):
    """Guarda la lista de ventas en un archivo CSV."""
    if not ventas:  # Lista vacía se detiene la función
        print("No hay datos para guardar.")
        return

    try:
        with open(archivo, mode="w", newline="", encoding="utf-8") as base:
            columnas = ["Producto", "Cantidad", "Precio", "Cliente", "Fecha"]
            writer = csv.DictWriter(base, fieldnames=columnas)

            writer.writeheader()
            writer.writerows(ventas)

            print(f"Datos guardados correctamente en {archivo}.")
    except Exception as e:
        print(f"Error al guardar los datos en {archivo}: {e}")


def ingresar_ventas(ventas):
    """ "Permite al usuario ingres una o varias ventas"""
    fecha = ""
    cliente = ""
    while True:
        try:
            producto = input("Ingrese el nombre del producto: ").upper()
            cantidad = int(input("Ingrese la cantidad vendida: "))
            precio = float(input("Ingrese el precio del producto: "))
            # Solicitar fecha y cliente solo si no se han proporcionado
            if cliente == "" and fecha == "":
                fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
                cliente = input("Ingrese el nombre del cliente: ").upper()

            # Validar datos
            if cantidad <= 0:
                print("⚠️ La cantidad deber ser mayor a cero.")
                continue
            if precio < 0:
                print("⚠️ El precio debe ser mayor a cero.")
                continue

            # Agregar a  la lista de ventas
            venta = {
                "Producto": producto,
                "Cantidad": cantidad,
                "Precio": precio,
                "Cliente": cliente,
                "Fecha": fecha,
            }
            # Añadir la venta a la lista principal
            ventas.append(venta)
            # Preguntrar si desea ingresar otra venta
            continuar = input("¿Desea ingresar otra venta? (s/n): ").lower()
            if continuar != "s":
                guardar_csv(ventas)  # Guardar después de cada ingreso
                break
        except ValueError:
            print(
                "❌ Error Cantidad y precio deben ser numericos. Por favor, intente de nuevo."
            )
            continue
        except Exception as e:
            print(f"❌ Error al ingresar los datos: {e}")
            continue


def cargar_ventas(archivo_csv="ventas.csv"):
    """Carga las ventas desde un archivo CSV y las devuelve como una lista de diccionarios."""
    try:
        # Leer el archivo CSV usando pandas
        df = pd.read_csv(archivo_csv)

        # Convertir el DataFrame a una lista de diccionarios
        # Se retorna una lista de diccionarios global VENTAS_DATA
        ventas_cargadas = df.to_dict(orient="records")
        print(f"✅ Datos cargados correctamente desde {archivo_csv}.")
        return ventas_cargadas

    except FileNotFoundError:
        print(f"⚠️ El archivo {archivo_csv} no existe. No existen ventas registradas.")
        return []
    except Exception as e:
        print(f"❌ Error al cargar los datos desde {archivo_csv}: {e}")
        return []


if __name__ == "__main__":
    # Prueba de la función guardar_csv
    ventas_ejemplo = [
        {
            "Producto": "Laptop",
            "Cantidad": 2,
            "Precio": 1200,
            "Cliente": "Juan Perez",
            "Fecha": "2024-06-01",
        },
        {
            "Producto": "Mouse",
            "Cantidad": 5,
            "Precio": 25,
            "Cliente": "Ana Gomez",
            "Fecha": "2024-06-02",
        },
    ]
    ingresar_ventas(ventas_ejemplo)
