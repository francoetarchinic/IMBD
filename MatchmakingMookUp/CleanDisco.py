import pandas as pd

df = pd.read_csv('data\output_disco.csv')

## Normalizacion


    ##Mayusculas
df.columns = df.columns.str.upper()

text_cols = df.select_dtypes(include=["object","string"]).columns
df[text_cols] = df[text_cols].apply(lambda x: x.str.upper())


    ##Normalizacion de Volumen 
col = "OUTPUT_VOLUME_ML"

df[col] = (
    df[col]
    .astype(str)
    .str.upper()
    .str.strip()
)

mask_liters = df[col].str.contains(r'(?<!M)L\b', regex=True, na=False)
df[col] = df[col].str.replace(r'(?<=\d)\.(?=\d{3}\b)', '', regex=True)
df[col] = df[col].str.extract(r'(\d+(?:\.\d+)?)', expand=False)
df[col] = pd.to_numeric(df[col], errors="coerce")
df.loc[mask_liters, col] = df.loc[mask_liters, col] * 1000
df[col] = df[col].round(0).astype("Int64")
df[col].unique()

try:
    df.to_csv("CleanDisco.csv",index=False,encoding="utf-8")
    
    print("Archivo creado")

except Exception as e:
    print("Hubo un erro al guardar", e)
