
import os
import pandas as pd
from pathlib import Path


df_vendas = pd.read_csv(r"data\raw\supermarket_raw_00.csv")
                    

# Define o caminho do diretório e do arquivo
diretorio = r"data\raw"
caminho_arquivo = os.path.join(diretorio, "supermarket_raw_01.csv")

# Cria a pasta caso ela não exista
os.makedirs(diretorio, exist_ok=True)

# Salva os dados em formato CSV
df_vendas.to_csv(caminho_arquivo, index=False, sep=",", encoding="utf-8")

# Exibindo os dados extraídos e a confirmação
print(df_vendas)
print(f"\nDados salvos com sucesso em: {caminho_arquivo}")
print(f'Registros gerados: {len(df_vendas)}')



