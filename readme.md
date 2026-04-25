# 📊 Análisis de Facturación con Python

Proyecto de análisis de datos enfocado en la exploración, visualización y generación de reportes a partir de información de ventas y facturación.

---

## 🚀 Objetivo del proyecto

Analizar datos de facturación para obtener insights clave sobre el comportamiento de ventas, utilizando herramientas de análisis de datos y visualización en Python.

---

## 🧠 Tecnologías utilizadas

- 🐍 Python
- 📊 Pandas
- 📈 Plotly
- 📓 Jupyter Notebook
- 📄 FPDF

---

## 📁 Estructura del proyecto

```bash
proyecto-analisis-datos/
│
├── data/              # Archivos de datos (Excel)
├── notebooks/         # Análisis exploratorio
├── src/               # Scripts en Python
├── reports/           # Visualizaciones en HTML
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Análisis realizados

El proyecto incluye diferentes análisis de facturación:

- 📍 Facturación por país
- 🏙️ Facturación por ciudad
- 🏪 Facturación por tienda
- 📦 Facturación por tamaño
- 🍽️ Consumo por local

Cada análisis incluye visualizaciones interactivas generadas con Plotly.

---

## 📈 Visualizaciones

Las gráficas generadas se encuentran en la carpeta `reports/` y pueden abrirse directamente en el navegador.

Ejemplos:

- `Facturacion por pais.html`
- `Facturacion por ciudad.html`
- `grafico_animado.html`

---

## 📄 Generación de reportes

El proyecto incluye un script para generar presupuestos en PDF:

📌 Archivo: `src/generadorPDF.py`

Permite ingresar datos como:

- descripción del proyecto
- horas estimadas
- costo por hora

Y genera automáticamente un PDF con el total calculado.

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Sbas17God/analisis-facturacion-python.git
cd analisis-facturacion-python
```

---

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 3. Ejecutar notebooks

Abre los notebooks con Jupyter:

```bash
jupyter notebook
```

---

### 4. Ejecutar script de PDF

```bash
python src/generadorPDF.py
```

---

## 💡 Posibles mejoras

- Integrar dashboard interactivo (Streamlit o Dash)
- Automatizar carga de datos
- Conectar con base de datos
- Deploy en la nube

---

## 👨‍💻 Autor

**Sebastián Moreno**
Estudiante de Ingeniería en Sistemas Computacionales

---

## ⭐ Si te gustó el proyecto

¡Dale una estrella al repositorio!
