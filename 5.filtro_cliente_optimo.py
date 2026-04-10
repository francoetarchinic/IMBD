import pandas as pd

#Cargar el archivo
df = pd.read_csv("4.empresas_filtradas_MVP_BSAS&CABA_processed.csv")

#Filtrar por ultima situacion medida
filtered_df = df[df['deuda_situacion_promedio'] == '1.0']

#Filtrar por riesgo historico
filtered_df = filtered_df[filtered_df['historico_riesgo'] == 'SIN RIESGO']

#Filtrar sin cheques rechazados
filtered_df = filtered_df[filtered_df['cheques_rechazados'] == False]

# Mostrar resultados
print(filtered_df.head())



#! Concatenar Domicilios Fiscal & Legal


## Transformar a string Numero de Domicilio Fiscal & Legal (sin decimales y sin 0)
filtered_df['dom_fiscal_numero'] = filtered_df['dom_fiscal_numero'].apply(
    lambda x: str(int(x)) if pd.notna(x) else ''
)
filtered_df['dom_legal_numero'] = filtered_df['dom_legal_numero'].apply(
    lambda x: str(int(x)) if pd.notna(x) else ''
)

# Limpiar nulos
cols = [
    'dom_fiscal_piso', 'dom_fiscal_departamento',
    'dom_legal_piso', 'dom_legal_departamento'
]
filtered_df[cols] = filtered_df[cols].fillna('')

## Función para armar domicilio
def armar_domicilio(calle, numero, piso, depto, localidad, provincia):
    piso = str(piso).strip()
    depto = str(depto).strip()

    piso_depto = ''
    if piso or depto:
        piso_depto = f", {piso}° {depto}".strip()

    return f"{calle} {numero}{piso_depto}; {localidad}; {provincia}"

## Concatenar Domicilios
filtered_df['dom_fiscal_completo'] = filtered_df.apply(
    lambda x: armar_domicilio(
        x['dom_fiscal_calle'],
        x['dom_fiscal_numero'],
        x['dom_fiscal_piso'],
        x['dom_fiscal_departamento'],
        x['dom_fiscal_localidad'],
        x['dom_fiscal_provincia']
    ),
    axis=1
)

filtered_df['dom_legal_completo'] = filtered_df.apply(
    lambda x: armar_domicilio(
        x['dom_legal_calle'],
        x['dom_legal_numero'],
        x['dom_legal_piso'],
        x['dom_legal_departamento'],
        x['dom_legal_localidad'],
        x['dom_legal_provincia']
    ),
    axis=1
)

#* Guardar resultado
filtered_df.to_csv("6.empresas_sit_financiera_optima.csv", index=False)