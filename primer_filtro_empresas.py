import pandas as pd

# Cargar el archivo
df = pd.read_csv("registro-nacional-sociedades-20260223.csv")

# Hacer la columna actividades_codigo un INTEGER

df['actividad_codigo'] = pd.to_numeric(df['actividad_codigo'], errors='coerce').astype('Int64')

# Lista de provincias a filtrar
provincias = [
    'BUENOS AIRES',
    'CIUDAD AUTONOMA BUENOS AIRES'
]

# Filtrar por provincias en dom_fiscal o dom_legal
filtered_df = df[
    (df['dom_fiscal_provincia'].isin(provincias)) |
    (df['dom_legal_provincia'].isin(provincias))
]

# Filtrar por actividad_estado = "AC"
filtered_df = filtered_df[filtered_df['actividad_estado'] == 'AC']

# Listado de Estados de domicilio 
estados_domicilio = [
   'DECLARADO POR INTERNET',
   'DECLARADO',
   'CONFIRMADO',
   'CONSTITUIDO DE OFICIO'
]

# Filtrar por estado de domicilio
filtered_df = filtered_df[filtered_df['dom_legal_estado_domicilio'].isin(estados_domicilio) | 
                          filtered_df['dom_fiscal_estado_domicilio'].isin(estados_domicilio)]


#! Listado de tipos de sociedad que NO se quieren incluir
tipos_sociedad = [
    'SOCIEDAD DEL ESTADO',
    'ASOCIACION CIVIL',
    'FUNDACION',
    'SOCIEDAD ANONIMA CON PARTICIPACION ESTATAL MAYORITARIA',
    'SOCIEDAD EXTRANJERA',
    'ASOCIACION CIVIL EXTRANJERA'    
]

# Filtrar por tipo de sociedad
filtered_df = filtered_df[
    (~filtered_df['tipo_societario'].isin(tipos_sociedad)) 
]

# Eliminar duplicados por CUIT
filtered_df = filtered_df.drop_duplicates(subset='cuit')

# Mostrar resultados
print(filtered_df.head())

# Guardar resultado
filtered_df.to_csv("empresas_filtradas_MVP_BSAS&CABA.csv", index=False)