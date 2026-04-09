import pandas as pd

df = pd.read_csv("data/output_carrefour.csv")

## Normalizacion


    ##Mayusculas
df.columns = df.columns.str.upper()

text_cols = df.select_dtypes(include=["object","string"]).columns
df[text_cols] = df[text_cols].apply(lambda x: x.str.upper())


    ##Columna volumen a valor entero 

df['OUTPUT_VOLUME_ML'] = df['OUTPUT_VOLUME_ML'].astype("Int64")

    ##Limpiar la columna variedad

df['OUTPUT_VARIETY'] = (
    df['OUTPUT_VARIETY']
    .fillna("")
    .astype(str)
    .str.upper()
    .str.replace(r"\b(VINO|TINTO)\b", "", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)


try:
    df.to_csv("CleanCarrefour.csv",index= False,encoding= "utf-8")

    print("Archivo creado")
    
except Exception as e:
    print ("Hubo un errror al guardar",e)

