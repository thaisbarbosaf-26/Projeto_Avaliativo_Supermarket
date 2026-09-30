# Importando bibliotecas

import os
from dotenv import load_dotenv # carrega a variável informada em .env
from sqlalchemy import create_engine

import pandas as pd
from pathlib import Path


# Gerando csv após remover index, incluir separador e definir encoding (como boa prática), a partir do arquivo baixado no kaggle

df_vendas = pd.read_csv(r"data\raw\vendas_raw_00.csv") # Este é o csv original, baixado do kaggle
                    

# Definindo o caminho do arquivo original com primeiras formatações
diretorio = r"data\raw"
caminho_arquivo = os.path.join(diretorio, "vendas_raw_01.csv")

# Cria a pasta caso ela não exista
os.makedirs(diretorio, exist_ok=True)

# Salvando os dados em formato CSV
df_vendas.to_csv(caminho_arquivo, index=False, sep=",", encoding="utf-8")

# Exibindo os dados extraídos e a confirmação 
print(df_vendas)
print(f"\nDados salvos com sucesso em: {caminho_arquivo}")
print(f'Registros gerados: {len(df_vendas)}')


# Criando conexão com o banco de dados supermarket
load_dotenv()
 
CONN_URL = os.getenv("CONN_URL")
engine = create_engine(CONN_URL)



# Enviando os dados do csv_raw p/ armazenar os dados no banco de dados Supermarket

df_vendas = pd.read_csv(r"data\raw\vendas_raw_01.csv") 

df_vendas.to_sql('vendas_raw', engine, if_exists='replace', index=False) 
print(f"Dados gerados com sucesso no banco de dados: {len(df_vendas)}")

#fechar a conexão com o banco de dados
engine.dispose()


                   



