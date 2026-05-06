# Retail KPI Dashboard

> Data & Insights by Emilio Morillo

[![Live Demo](https://img.shields.io/badge/Live_Demo-View_Online-blue?style=for-the-badge)](https://MgnumX.github.io/retail-kpi-dashboard/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)

![Dashboard Preview](preview.png)

<details>
<summary>First chart — close-up</summary>

![Chart Preview](preview_chart1.png)

</details>

---

## 🇺🇸 English

Python pipeline that generates a synthetic retail dataset and renders an interactive HTML dashboard with KPIs and charts. No server needed — open `dashboard.html` directly in any browser.

### Key Insights

Three questions this dashboard answers out of the box:

1. **Which product categories drive the most revenue?** The bar chart ranks total sales per category, so you can immediately spot where to push harder.

2. **Where are profits actually coming from?** The donut chart splits net profit by region. Useful for catching underperforming territories before they become a problem.

3. **Is the business growing or just busy?** The monthly area chart shows whether revenue peaks are seasonal trends or real growth.

### Features

- Generates 5,000 synthetic sales records with realistic pricing, discounts, and margins
- Computes Total Sales, Net Profit, Average Margin, and Order Count
- Exports a self-contained `dashboard.html` — no backend, no dependencies at runtime
- `capture_preview.py` takes full-page and cropped screenshots headlessly via Playwright

### Setup

```bash
pip install pandas numpy plotly playwright
playwright install chromium
```

### Run

```bash
python generar_datos.py       # generates ventas.csv
python generar_dashboard.py   # generates dashboard.html
# open dashboard.html in your browser

python capture_preview.py     # optional: saves preview.png + preview_chart1.png
```

### Structure

```
.
├── generar_datos.py       # synthetic data generator
├── generar_dashboard.py   # data processing + chart builder
├── capture_preview.py     # headless screenshots (Playwright)
├── ventas.csv             # generated dataset
├── dashboard.html         # interactive output
├── preview.png            # full-page screenshot
├── preview_chart1.png     # first chart crop
└── README.md
```

---

## 🇪🇸 Español

Pipeline en Python que genera un dataset sintético de retail y produce un dashboard HTML interactivo con KPIs y gráficos. No necesita servidor, basta con abrir `dashboard.html` en el navegador.

### Insights Clave

Tres preguntas que este dashboard responde de inmediato:

1. **¿Qué categorías generan más ingresos?** El gráfico de barras muestra las ventas por categoría para saber dónde concentrar esfuerzos.

2. **¿De dónde viene realmente el beneficio?** La dona divide el beneficio neto por región. Sirve para detectar territorios poco rentables antes de que sean un problema.

3. **¿El negocio crece o solo está ocupado?** El gráfico de área mensual deja claro si los picos de ventas son estacionales o crecimiento real.

### Características

- Genera 5,000 registros sintéticos con precios, descuentos y márgenes realistas
- Calcula Ventas Totales, Beneficio Neto, Margen Promedio y Cantidad de Órdenes
- Exporta un `dashboard.html` autocontenido sin dependencias en tiempo de ejecución
- `capture_preview.py` toma screenshots de página completa y recortes sin abrir el navegador

### Instalación

```bash
pip install pandas numpy plotly playwright
playwright install chromium
```

### Ejecución

```bash
python generar_datos.py       # genera ventas.csv
python generar_dashboard.py   # genera dashboard.html
# abrir dashboard.html en el navegador

python capture_preview.py     # opcional: guarda preview.png + preview_chart1.png
```

### Estructura

```
.
├── generar_datos.py       # generador de datos sintéticos
├── generar_dashboard.py   # procesamiento de datos + gráficos
├── capture_preview.py     # screenshots headless (Playwright)
├── ventas.csv             # dataset generado
├── dashboard.html         # dashboard interactivo
├── preview.png            # screenshot completo
├── preview_chart1.png     # recorte del primer gráfico
└── README.md
```
