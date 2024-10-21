from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

def extraer_datos_boy():
    url = 'https://cifras.biodiversidad.co/boyaca'    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Busca los datos necesarios
        cifra_especies_est_boy = soup.find('span', class_='font-inter font-black lg:text-xl')
        cifra_especies_obs_boy = soup.find('span', class_='text-lg lg:text-4xl font-black font-inter')
        parrafo_info_boy = soup.find('p', string=lambda text: text and 'A través del SiB Colombia se han publicado' in text)
        parrafo_boy = soup.find('p', class_='text-lg 3xl:text-2xl mt-10')
        div_especies_boy = soup.find('div', class_='lg:col-start-1 lg:col-end-6')

        # Nuevo div para plantas
        div_plantas_boy = soup.find('div', class_='lg:col-start-8 lg:col-end-13')

        #Búsqueda de listas dentro de DIV's y extrae datos
        especies_totales_boy = []
        if div_especies_boy:
            listas_especies_boy = div_especies_boy.find_all('ul', class_='pl-8')
            for lista in listas_especies_boy:
                especies_boy = [li.text.strip() for li in lista.find_all('li')]
                especies_totales_boy.extend(especies_boy)
        else:
            especies_totales_boy = ['No se encontró el div principal']

        # Datos del nuevo div 'div_plantas_boy'
        plantas_totales_boy = []
        if div_plantas_boy:
            listas_plantas_boy = div_plantas_boy.find_all('ul', class_='pl-8')
            for lista in listas_plantas_boy:
                plantas_boy = [li.text.strip() for li in lista.find_all('li')]
                plantas_totales_boy.extend(plantas_boy)
        else:
            plantas_totales_boy = ['No se encontró el div de plantas']

        # Extrae los textos
        cifra_esp_est_boy = cifra_especies_est_boy.text.strip() if cifra_especies_est_boy else 'No se encontró la cifra'
        cifra_esp_obs_boy = cifra_especies_obs_boy.text.strip() if cifra_especies_obs_boy else 'No se encontró la cifra'
        parrafo_inf_boy = parrafo_info_boy.text.strip() if parrafo_info_boy else 'No se encontró el párrafo'
        parrafo_texto_boy = parrafo_boy.text.strip() if parrafo_boy else 'No se encontró el párrafo'

        # Reemplaza los saltos de línea
        parrafo_inf_boy = ' '.join(parrafo_inf_boy.splitlines())
        parrafo_texto_boy = ' '.join(parrafo_texto_boy.splitlines())

        return parrafo_inf_boy, cifra_esp_est_boy, cifra_esp_obs_boy, parrafo_texto_boy, especies_totales_boy, plantas_totales_boy
    else:
        print('Error en la solicitud:', response.status_code)
        return 'Error en la solicitud', 'N/A', 'N/A', 'N/A', ['N/A']

# Llama a la función de extracción de datos
parrafo_inf_boy, cifra_esp_est_boy, cifra_esp_obs_boy, parrafo_texto_boy, especies_totales_boy, plantas_totales_boy = extraer_datos_boy()



def extraer_datos_cund():
    url = 'https://cifras.biodiversidad.co/cundinamarca'    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Busca los datos necesarios
        cifra_especies_est_cund = soup.find('span', class_='font-inter font-black lg:text-xl')
        cifra_especies_obs_cund = soup.find('span', class_='text-lg lg:text-4xl font-black font-inter')
        parrafo_info_cund = soup.find('p', string=lambda text: text and 'A través del SiB Colombia se han publicado' in text)
        parrafo_cund = soup.find('p', class_='text-lg 3xl:text-2xl mt-10')
        div_especies_cund = soup.find('div', class_='lg:col-start-1 lg:col-end-6')
        
        # Nuevo div agregado aquí
        div_plantas_cund = soup.find('div', class_='lg:col-start-8 lg:col-end-13')
        
        # Búsqueda de listas dentro de DIV's y extrae datos
        especies_totales_cund = []
        if div_especies_cund:
            listas_especies_cund = div_especies_cund.find_all('ul', class_='pl-8')
            for lista in listas_especies_cund:
                especies_cund = [li.text.strip() for li in lista.find_all('li')]
                especies_totales_cund.extend(especies_cund)
        else:
            especies_totales_cund = ['No se encontró el div principal']
        
        # Datos del nuevo div 'div_plantas_cund'
        plantas_totales_cund = []
        if div_plantas_cund:
            listas_plantas_cund = div_plantas_cund.find_all('ul', class_='pl-8')
            for lista in listas_plantas_cund:
                plantas_cund = [li.text.strip() for li in lista.find_all('li')]
                plantas_totales_cund.extend(plantas_cund)
        else:
            plantas_totales_cund = ['No se encontró el div de plantas']

        # Extrae los textos
        cifra_esp_est_cund = cifra_especies_est_cund.text.strip() if cifra_especies_est_cund else 'No se encontró la cifra'
        cifra_esp_obs_cund = cifra_especies_obs_cund.text.strip() if cifra_especies_obs_cund else 'No se encontró la cifra'
        parrafo_inf_cund = parrafo_info_cund.text.strip() if parrafo_info_cund else 'No se encontró el párrafo'
        parrafo_texto_cund = parrafo_cund.text.strip() if parrafo_cund else 'No se encontró el párrafo'

        # Reemplaza los saltos de línea
        parrafo_inf_cund = ' '.join(parrafo_inf_cund.splitlines())
        parrafo_texto_cund = ' '.join(parrafo_texto_cund.splitlines())

        # Añadir 'plantas_totales_cund' en el retorno
        return parrafo_inf_cund, cifra_esp_est_cund, cifra_esp_obs_cund, parrafo_texto_cund, especies_totales_cund, plantas_totales_cund
    else:
        print('Error en la solicitud:', response.status_code)
        return 'Error en la solicitud', 'N/A', 'N/A', 'N/A', ['N/A'], ['N/A']

# Llama a la función de extracción de datos
parrafo_inf_cund, cifra_esp_est_cund, cifra_esp_obs_cund, parrafo_texto_cund, especies_totales_cund, plantas_totales_cund = extraer_datos_cund()

# Función para extraer números de una cadena (si están entre paréntesis)
def extraer_numeros(valores):
    numeros = []
    for valor in valores:
        match = re.search(r'\(([\d.,]+)\)', valor)
        if match:
            # Convertir a float y agregar a la lista
            numeros.append(float(match.group(1).replace('.', '').replace(',', '.')))
    return numeros

# Función para crear gráficos
def crear_graficos(especies_boy, especies_cund, plantas_boy, plantas_cund):
    # Asegurar que los valores sean numéricos
    lista_especies_totales_cund = extraer_numeros(especies_cund)
    lista_especies_totales_boy = extraer_numeros(especies_boy)
    lista_plantas_totales_cund = extraer_numeros(plantas_cund)
    lista_plantas_totales_boy = extraer_numeros(plantas_boy)

    # Crear DataFrame para especies
    df_especies = pd.DataFrame({
            'Departamento': ['Boyacá', 'Cundinamarca'],
            'Especies': [sum(lista_especies_totales_boy), sum(lista_especies_totales_cund)]
        })
    
    # Crear gráfico de barras para especies
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df_especies, x='Departamento', y='Especies', hue='Departamento', palette='viridis', dodge=False)
    plt.title('Distribución de Especies en Boyacá y Cundinamarca')
    plt.xlabel('Departamento')
    plt.ylabel('Cantidad de Especies')
    plt.yticks(range(0, 130000, 10000))  # Ajusta los ticks del eje Y
    plt.tight_layout()

    # Guardar el gráfico de especies
    plt.savefig('static/graficos/distribucion_especies.png')
    plt.close()

    # Crear DataFrame para plantas
    df_plantas = pd.DataFrame({
        'Departamento': ['Boyacá', 'Cundinamarca'],
        'Plantas': [sum(lista_plantas_totales_boy), sum(lista_plantas_totales_cund)]
    })

    # Crear gráfico de barras para plantas
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df_plantas, x='Departamento', y='Plantas', hue='Departamento', palette='viridis', dodge=False)
    plt.title('Distribución de Plantas en Boyacá y Cundinamarca')
    plt.xlabel('Departamento')
    plt.ylabel('Cantidad de Plantas')
    plt.yticks(range(0, 50000, 5000))  # Ajusta los ticks del eje Y
    plt.tight_layout()

    # Guardar el gráfico de plantas
    plt.savefig('static/graficos/distribucion_plantas.png')
    plt.close()

# Llama a la función de crear gráficos
crear_graficos(especies_totales_boy, especies_totales_cund, plantas_totales_boy, plantas_totales_cund)

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza los datos extraídos dinámicamente sin CSV
    return render_template('index.html', 
                           info_boy=parrafo_inf_boy, 
                           especies_estimadas_boy=cifra_esp_est_boy, 
                           especies_observadas_boy=cifra_esp_obs_boy, 
                           descripcion_boy=parrafo_texto_boy,
                           especies_boy=especies_totales_boy,
                           plantas_boy=plantas_totales_boy,
                           info_cund=parrafo_inf_cund, 
                           especies_estimadas_cund=cifra_esp_est_cund, 
                           especies_observadas_cund=cifra_esp_obs_cund, 
                           descripcion_cund=parrafo_texto_cund,
                           especies_cund=especies_totales_cund,
                           plantas_cund=plantas_totales_cund  # Añadir nueva variable aquí
                           )

if __name__ == '__main__':
    app.run(debug=True)




