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
    <div class="kpi-container">
        <div class="kpi-card">
            <h3 class="kpi-title">Ventas Totales</h3>
            <h2 class="kpi-value value-sales">${total_ventas:,.2f}</h2>
        </div>
        <div class="kpi-card">
            <h3 class="kpi-title">Beneficio Total</h3>
            <h2 class="kpi-value value-profit">${total_beneficio:,.2f}</h2>
        </div>
        <div class="kpi-card">
            <h3 class="kpi-title">Margen Promedio</h3>
            <h2 class="kpi-value value-margin">{margen_promedio:.2f}%</h2>
        </div>
        <div class="kpi-card">
            <h3 class="kpi-title">Total Órdenes</h3>
            <h2 class="kpi-value value-orders">{total_ordenes:,}</h2>
        </div>
    </div>
    """

    # Gráficos con diseño limpio
    layout_config = dict(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20),
        font=dict(family="Inter, sans-serif", color="#333")
    )

    ventas_mensuales = df.groupby('Mes')['Venta_Total'].sum().reset_index()
    fig1 = px.area(ventas_mensuales, x='Mes', y='Venta_Total', title='Tendencia de Ventas Mensuales', markers=True, color_discrete_sequence=['#3b82f6'])
    fig1.update_layout(**layout_config)

    ventas_categoria = df.groupby('Categoria')['Venta_Total'].sum().reset_index().sort_values('Venta_Total', ascending=False)
    fig2 = px.bar(ventas_categoria, x='Categoria', y='Venta_Total', title='Ventas por Categoría', color='Categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
    fig2.update_layout(**layout_config)

    beneficio_region = df.groupby('Region')['Beneficio'].sum().reset_index()
    fig3 = px.pie(beneficio_region, names='Region', values='Beneficio', title='Beneficios por Región', hole=0.5, color_discrete_sequence=px.colors.qualitative.Set2)
    fig3.update_layout(**layout_config)

    top_productos = df.groupby('Producto')['Venta_Total'].sum().reset_index().sort_values('Venta_Total', ascending=False).head(10)
    fig4 = px.bar(top_productos, x='Venta_Total', y='Producto', orientation='h', title='Top 10 Productos', color='Venta_Total', color_continuous_scale='Blues')
    fig4.update_layout(yaxis={'categoryorder':'total ascending'}, **layout_config)

    # HTML content con diseño visualmente responsivo y premium
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard de KPIs - Análisis de Ventas</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
            
            :root {{
                --bg-color: #f3f4f6;
                --card-bg: #ffffff;
                --text-main: #1f2937;
                --text-muted: #6b7280;
                --accent-blue: #3b82f6;
                --accent-green: #10b981;
                --accent-purple: #8b5cf6;
            }}

            * {{ box-sizing: border-box; margin: 0; padding: 0; }}
            
            body {{
                font-family: 'Inter', sans-serif;
                background-color: var(--bg-color);
                color: var(--text-main);
                padding: 2rem 1rem;
                line-height: 1.5;
            }}

            .container {{
                max-width: 1400px;
                margin: 0 auto;
            }}

            .header {{
                text-align: center;
                margin-bottom: 3rem;
            }}

            .header h1 {{
                font-weight: 700;
                font-size: 2.5rem;
                color: var(--text-main);
                letter-spacing: -0.02em;
            }}

            .header-signature {{
                font-weight: 600;
                color: var(--accent-blue);
                margin-top: 0.5rem;
                font-size: 1.1rem;
            }}

            .kpi-container {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 1.5rem;
                margin-bottom: 2.5rem;
            }}

            .kpi-card {{
                background: var(--card-bg);
                padding: 1.5rem;
                border-radius: 16px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }}

            .kpi-card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            }}

            .kpi-title {{
                color: var(--text-muted);
                font-size: 0.875rem;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                font-weight: 600;
                margin-bottom: 0.5rem;
            }}

            .kpi-value {{
                font-size: 2.25rem;
                font-weight: 700;
            }}

            .value-sales {{ color: var(--text-main); }}
            .value-profit {{ color: var(--accent-green); }}
            .value-margin {{ color: var(--accent-blue); }}
            .value-orders {{ color: var(--accent-purple); }}

            .charts-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
                gap: 1.5rem;
            }}

            @media (max-width: 768px) {{
                .charts-grid {{
                    grid-template-columns: 1fr;
                }}
            }}

            .chart-card {{
                background: var(--card-bg);
                border-radius: 16px;
                padding: 1.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
                overflow: hidden;
            }}

            .footer {{
                text-align: center;
                margin-top: 4rem;
                padding-top: 2rem;
                border-top: 1px solid #e5e7eb;
                color: var(--text-muted);
                font-size: 0.875rem;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📊 Dashboard Analytics</h1>
                <div class="header-signature">Data & Insights por Emilio Morillo</div>
            </div>
            
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
