import pandas as pd

df = pd.read_csv('data/output_jumbo.csv')


## Normalizacion


    ##Mayusculas
df.columns = df.columns.str.upper()

text_cols = df.select_dtypes(include=["object","string"]).columns
df[text_cols] = df[text_cols].apply(lambda x: x.str.upper())

