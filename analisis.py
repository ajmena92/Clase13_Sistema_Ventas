import pandas as pd


def analiza_ventas(ventas):
    """Lee el CSV de venta y realiza un análisi usando pandas."""
    try:
        df = pd.DataFrame(ventas)
        if df.empty:
            print("⚠️ No hay datos de ventas para analizar.")
            return

        print("\n--- 📈 Análisis de Ventas ---")
        # Crear columna Total
        total = total_ventas(df)
        print(f"Total de ventas: ${total:.2f}")

        # producto mas vendido
        producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum().idxmax()
        print(f"Producto más vendido: {producto_mas_vendido}")

        # print(df)
        # producto con mayor ingreso en ventas
        producto_top = df["Subtotal"].max()
        fila_venta_max = df.loc[df["Subtotal"].idxmax()]
        # producto_mayor_ingreso = df.groupby("Producto")["Subtotal"].sum().idxmax()
        # producto_mayor_ingreso = producto_top
        producto_mayor_ingreso = fila_venta_max["Producto"]
        monto_mayor_ingreso = fila_venta_max["Subtotal"]
        print(
            f"Producto con mayor ingreso en ventas: {producto_mayor_ingreso} (${monto_mayor_ingreso:.2f}) "
        )

        # Mejor Cliente
        cliente_top = df.groupby("Cliente")["Subtotal"].sum().idxmax()
        print(f"Mejor cliente: {cliente_top}")

        # Resumen por fecha
        print("\n--- Resumen de Ventas por Fecha ---")
        resumen_fecha = df.groupby("Fecha")["Subtotal"].sum().to_string()
        print(resumen_fecha)

    except Exception as e:
        print(f"❌ Error al analizar los datos: {e}")


def total_ventas(ventas):
    """Calcula el total de ventas."""
    try:
        df = ventas
        df["Subtotal"] = df["Cantidad"] * df["Precio"]
        total = df["Subtotal"].sum()
        return total
    except Exception as e:
        print(f"❌ Error al calcular el total de ventas: {e}")
        return 0
