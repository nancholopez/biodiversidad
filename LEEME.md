# Proyecto Flask: Visualización de Biodiversidad en Boyacá, Colombia

Este proyecto es una aplicación web desarrollada con **Flask** que realiza **web scraping** sobre el sitio oficial de cifras de biodiversidad en el departamento de Boyacá ([https://cifras.biodiversidad.co/boyaca](https://cifras.biodiversidad.co/boyaca)). Su objetivo es extraer, procesar y presentar datos clave sobre las especies y plantas observadas en este departamento colombiano.

---

## Características principales

- Extracción de datos desde una fuente externa (web scraping con `BeautifulSoup`).
- Visualización de:
  - Cantidad estimada y observada de especies.
  - Listas clasificadas de especies y plantas.
  - Párrafos informativos.
- Preparado para expandirse con análisis gráfico usando `matplotlib` y `seaborn`.

---

## Tecnologías utilizadas

- **Python 3**
- **Flask**
- **Requests**
- **BeautifulSoup4**
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## Instalación y ejecución

1. Clona este repositorio o descarga el archivo `.zip`:
   ```bash
   git clone https://github.com/nancholopez/biodiversidad.git
   cd nombre-del-repo
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

5. Abre tu navegador en:
   ```
   http://127.0.0.1:5000
   ```

---

## 📁 Estructura del proyecto

```
biodiversidad/
│
├── app.py               # Código principal de la aplicación Flask
├── requirements.txt     # Dependencias necesarias
├── LEEME.md            # Este archivo
├── templates/           # Plantilla HTML
└── static/              # Archivos estáticos como CSS o imágenes
```

---

## Notas

- La extracción de datos depende de la estructura del sitio web. Si este cambia, es posible que la aplicación necesite ser actualizada.
- El proyecto puede expandirse para incluir visualizaciones gráficas y comparaciones entre departamentos.

---

## Licencia

Este proyecto es de código abierto. Puedes modificarlo y reutilizarlo según tus necesidades educativas o de desarrollo.
