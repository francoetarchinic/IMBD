import pandas as pd

#Cargar el archivo
df = pd.read_csv("empresas_filtradas_MVP_BSAS&CABA_processed.csv")

#Filtrar por ultima situacion medida
filtered_df = df[df['deuda_situacion_promedio'] == '1.0']

#Filtrar por riesgo historico
filtered_df = filtered_df[filtered_df['historico_riesgo'] == 'SIN RIESGO']

#Filtrar sin cheques rechazados
filtered_df = filtered_df[filtered_df['cheques_rechazados'] == False]

# Mostrar resultados
print(filtered_df.head())

# Guardar resultado
filtered_df.to_csv("empresas_sit_financiera_optima.csv", index=False)