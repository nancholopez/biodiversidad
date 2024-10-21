import pandas as pd

def cargar_datos(csv_file):
    df = pd.read_csv(csv_file)
    return df

archivo_csv = './static/especies.csv'  # Reemplaza con la ruta a tu archivo CSV
datos = cargar_datos(archivo_csv)

print(datos.head())


def filtrar_por_Departamento(df, departamento):
    return df[df['Departamento'] == departamento]

cundinamarca_data = filtrar_por_Departamento(datos, 'Cundinamarca')
print(cundinamarca_data)

conteo_especies = datos.groupby('Departamento')['Especie'].count()
print(conteo_especies)

conteo_especies.to_csv('conteo_especies.csv')
