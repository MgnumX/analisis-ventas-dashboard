# 📊 Análisis de Ventas & Dashboard de KPIs

> **Data & Insights por Emilio Morillo**

![Dashboard Preview](preview.png)

> *Vista completa del dashboard interactivo generado automáticamente con Python y Plotly.*

<details>
<summary>🔍 Ver primera gráfica en detalle</summary>

![Chart Preview](preview_chart1.png)

</details>

Este proyecto proporciona un flujo de trabajo completo para el análisis de datos de retail. Incluye la creación de un conjunto de datos sintético realista y su posterior procesamiento para generar un dashboard interactivo de indicadores clave de rendimiento (KPIs).

## ✨ Características Principales
- **Dataset Sintético (`generar_datos.py`)**: Construye una base de datos `ventas.csv` con datos aleatorios pero coherentes: fechas de transacción, categorías, productos específicos, regiones y costos estructurados para un modelo de negocio realista.
- **Procesamiento de Datos**: Calcula KPIs financieros cruciales (Ventas Totales, Beneficio Neto, Margen de Rentabilidad).
- **Dashboard Visual (`generar_dashboard.py`)**: Un reporte en HTML puro (`dashboard.html`) construido con la potencia de Plotly para mostrar visualizaciones dinámicas de tendencias de ventas, análisis por categorías, distribución geográfica y un top de productos.

## 🚀 Requisitos y Configuración
Asegúrate de tener instalado Python 3.8 o superior, y las siguientes bibliotecas:

```bash
pip install pandas numpy plotly playwright
playwright install chromium
```

## 🛠️ Instrucciones de Ejecución

1. **Paso 1: Generar el dataset**
   Ejecuta el script para crear el archivo `ventas.csv`.
   ```bash
   python generar_datos.py
   ```

2. **Paso 2: Compilar el Dashboard**
   Procesa el dataset generado y crea la visualización en HTML.
   ```bash
   python generar_dashboard.py
   ```

3. **Paso 3: Visualizar**
   Simplemente haz doble clic o abre `dashboard.html` en tu navegador web preferido para explorar el análisis completo interactivo.

4. **Paso 4 (opcional): Capturar screenshots**
   Genera `preview.png` (full page) y `preview_chart1.png` (primer gráfico) sin abrir ninguna ventana.
   ```bash
   python capture_preview.py
   ```

## 📂 Estructura del Repositorio
```text
.
├── generar_datos.py       # Script de creacion de datos sinteticos
├── generar_dashboard.py   # Motor de analisis y creacion de graficos
├── capture_preview.py     # Capturas headless via Playwright
├── ventas.csv             # Dataset (generado localmente)
├── dashboard.html         # Dashboard interactivo final
├── preview.png            # Screenshot full-page del dashboard
├── preview_chart1.png     # Crop del primer grafico
└── README.md              # Documentacion del proyecto
```

---
*Desarrollado para transformar datos crudos en estrategias accionables.*
