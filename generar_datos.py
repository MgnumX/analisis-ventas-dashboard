import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def generar_datos_ventas(n_rows=5000):
    np.random.seed(42)
    random.seed(42)

    categorias = ['Electrónica', 'Ropa', 'Hogar', 'Deportes', 'Juguetes']
    productos_por_categoria = {
        'Electrónica': ['Laptop', 'Smartphone', 'Tablet', 'Auriculares', 'Smartwatch'],
        'Ropa': ['Camiseta', 'Pantalón', 'Chaqueta', 'Zapatos', 'Gorra'],
        'Hogar': ['Sofá', 'Mesa', 'Silla', 'Lámpara', 'Cama'],
        'Deportes': ['Bicicleta', 'Balón', 'Raqueta', 'Pesas', 'Cinta de correr'],
        'Juguetes': ['Muñeca', 'Coche RC', 'Puzzle', 'Lego', 'Peluche']
    }
    
    regiones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
    metodos_pago = ['Tarjeta de Crédito', 'PayPal', 'Transferencia', 'Efectivo']

    fechas = [datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(n_rows)]
    
    datos = []
    for fecha in fechas:
        categoria = random.choice(categorias)
        producto = random.choice(productos_por_categoria[categoria])
        region = random.choice(regiones)
        metodo = random.choice(metodos_pago)
        
        # Precios base aproximados
        precio_base = random.uniform(20, 1500) if categoria == 'Electrónica' else random.uniform(10, 300)
        
        cantidad = random.randint(1, 10)
        costo_unitario = precio_base * random.uniform(0.4, 0.7)
        precio_venta = precio_base * random.uniform(0.9, 1.2)
        
        descuento = random.choice([0, 0, 0, 0.05, 0.1, 0.15, 0.2])
        
        venta_total = (precio_venta * cantidad) * (1 - descuento)
        costo_total = costo_unitario * cantidad
        beneficio = venta_total - costo_total

        datos.append({
            'Fecha': fecha.strftime('%Y-%m-%d'),
            'Categoria': categoria,
            'Producto': producto,
            'Region': region,
            'Metodo_Pago': metodo,
            'Cantidad': cantidad,
            'Precio_Unitario': round(precio_venta, 2),
            'Costo_Unitario': round(costo_unitario, 2),
            'Descuento': descuento,
            'Venta_Total': round(venta_total, 2),
            'Costo_Total': round(costo_total, 2),
            'Beneficio': round(beneficio, 2)
        })

    df = pd.DataFrame(datos)
    df = df.sort_values(by='Fecha').reset_index(drop=True)
    df.to_csv('ventas.csv', index=False)
    print(f"Archivo 'ventas.csv' generado exitosamente con {n_rows} registros.")

if __name__ == "__main__":
    generar_datos_ventas()
