import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def calcular_deciles_deuda():

        # 1. Cargar datos
    df = pd.read_csv("6.empresas_sit_financiera_optima.csv")

    # 2. Limpiar
    df["deuda_total"] = pd.to_numeric(df["deuda_total"], errors="coerce")
    df = df.dropna(subset=["deuda_total"])
    df = df[df["deuda_total"] > 0]

    # 3. Convertir a valor real (porque está en miles)
    df["deuda_total"] = df["deuda_total"] * 1000

    # 4. Crear bins logarítmicos
    bins = 10
    edges = np.logspace(
        np.log10(df["deuda_total"].min()),
        np.log10(df["deuda_total"].max()),
        bins + 1
    )

    # 5. Clasificar en rangos
    df["rango"] = pd.cut(df["deuda_total"], bins=edges)

    # 6. Clasificar en número de bin 
    df["bin_num"] = pd.cut(df["deuda_total"], bins=edges, labels=False) + 1

    # 7. Contar empresas por rango
    conteo = df["rango"].value_counts().sort_index()

    # 8. Función para formatear (K / M)
    def formatear(valor):
        if valor >= 1e6:
            return f"{valor/1e6:.1f}M"
        elif valor >= 1e3:
            return f"{valor/1e3:.1f}K"
        else:
            return str(int(valor))

    # 9. Crear etiquetas legibles
    labels = [
        f"{formatear(r.left)} - {formatear(r.right)}"
        for r in conteo.index
    ]


    # 10. Graficar
    plt.figure()

    ax = conteo.plot(kind="bar")  

    plt.xticks(ticks=range(len(labels)), labels=labels, rotation=45)

    plt.xlabel("Rangos de deuda")
    plt.ylabel("Cantidad de empresas")
    plt.title("Distribución de empresas por nivel de endeudamiento")

    # Agregar números arriba de cada barra
    for i, valor in enumerate(conteo):
        ax.text(i, valor, str(valor), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

   

if __name__ == "__main__":
    calcular_deciles_deuda()


    