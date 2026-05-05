import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

def crear_dashboard():
    try:
        df = pd.read_csv('ventas.csv')
    except FileNotFoundError:
        print("Error: 'ventas.csv' no encontrado. Ejecuta generar_datos.py primero.")
        return

    # Procesamiento
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Mes'] = df['Fecha'].dt.to_period('M').astype(str)
    
    # KPIs
    total_ventas = df['Venta_Total'].sum()
    total_beneficio = df['Beneficio'].sum()
    margen_promedio = (total_beneficio / total_ventas) * 100
    total_ordenes = len(df)
    
    kpis_html = f"""
    <div style="display: flex; justify-content: space-around; padding: 20px; background-color: #f8f9fa; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <div style="text-align: center;">
            <h3 style="color: #6c757d; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Ventas Totales</h3>
            <h2 style="color: #2b2d42; font-size: 28px; margin: 10px 0;">${total_ventas:,.2f}</h2>
        </div>
        <div style="text-align: center;">
            <h3 style="color: #6c757d; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Beneficio Total</h3>
            <h2 style="color: #27ae60; font-size: 28px; margin: 10px 0;">${total_beneficio:,.2f}</h2>
        </div>
        <div style="text-align: center;">
            <h3 style="color: #6c757d; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Margen Promedio</h3>
            <h2 style="color: #2980b9; font-size: 28px; margin: 10px 0;">{margen_promedio:.2f}%</h2>
        </div>
        <div style="text-align: center;">
            <h3 style="color: #6c757d; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Total Órdenes</h3>
            <h2 style="color: #8e44ad; font-size: 28px; margin: 10px 0;">{total_ordenes:,}</h2>
        </div>
    </div>
    """

    # Gráficos
    ventas_mensuales = df.groupby('Mes')['Venta_Total'].sum().reset_index()
    fig1 = px.line(ventas_mensuales, x='Mes', y='Venta_Total', title='Tendencia de Ventas Mensuales', markers=True, color_discrete_sequence=['#2980b9'])
    fig1.update_layout(plot_bgcolor='white', paper_bgcolor='white')

    ventas_categoria = df.groupby('Categoria')['Venta_Total'].sum().reset_index().sort_values('Venta_Total', ascending=False)
    fig2 = px.bar(ventas_categoria, x='Categoria', y='Venta_Total', title='Ventas por Categoría', color='Categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
    fig2.update_layout(plot_bgcolor='white', paper_bgcolor='white')

    beneficio_region = df.groupby('Region')['Beneficio'].sum().reset_index()
    fig3 = px.pie(beneficio_region, names='Region', values='Beneficio', title='Beneficios por Región', hole=0.4, color_discrete_sequence=px.colors.qualitative.Set3)

    top_productos = df.groupby('Producto')['Venta_Total'].sum().reset_index().sort_values('Venta_Total', ascending=False).head(10)
    fig4 = px.bar(top_productos, x='Venta_Total', y='Producto', orientation='h', title='Top 10 Productos por Ventas', color='Venta_Total', color_continuous_scale='Viridis')
    fig4.update_layout(yaxis={'categoryorder':'total ascending'}, plot_bgcolor='white', paper_bgcolor='white')

    # HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard de KPIs - Análisis de Ventas</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
            body {{ font-family: 'Inter', sans-serif; margin: 0; padding: 40px 20px; background-color: #f4f6f9; color: #333; }}
            .container {{ max-width: 1200px; margin: auto; background: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
            h1 {{ color: #2b2d42; text-align: center; font-weight: 800; margin-bottom: 40px; }}
            .charts-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }}
            .chart-card {{ border: 1px solid #eee; border-radius: 12px; padding: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.02); }}
            .header-signature {{ text-align: center; color: #888; font-style: italic; margin-bottom: 30px; font-weight: 600; }}
            .footer {{ text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; color: #7f8c8d; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Dashboard de Rendimiento Comercial</h1>
            <div class="header-signature">Data & Insights por Emilio Morillo</div>
            
            {kpis_html}
            
            <div class="charts-grid">
                <div class="chart-card">{fig1.to_html(full_html=False, include_plotlyjs='cdn')}</div>
                <div class="chart-card">{fig2.to_html(full_html=False, include_plotlyjs=False)}</div>
                <div class="chart-card">{fig3.to_html(full_html=False, include_plotlyjs=False)}</div>
                <div class="chart-card">{fig4.to_html(full_html=False, include_plotlyjs=False)}</div>
            </div>
            
            <div class="footer">
                Generado automáticamente usando Python y Plotly. © 2026 Emilio Morillo.
            </div>
        </div>
    </body>
    </html>
    """

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Dashboard generado exitosamente en 'dashboard.html'.")

if __name__ == "__main__":
    crear_dashboard()
