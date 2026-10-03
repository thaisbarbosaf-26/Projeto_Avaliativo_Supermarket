# Importando bibliotecas

import os
from dotenv import load_dotenv # carrega a variável informada em .env
from sqlalchemy import create_engine

import pandas as pd




# Criando conexão com o banco de dados supermarket
load_dotenv()
 
CONN_URL = os.getenv("CONN_URL")
engine = create_engine(CONN_URL)

print("Conexão realizada com sucesso!!")

      


# Recebendo os dados da tabela vendas com as contraints


df_tab_vendas_withconstraints = pd.read_sql_table('vendas_with_constraints', engine)


df_tab_vendas_withconstraints.to_csv(r'data\processed\vendas_with_constraints.csv', index=False, sep=",", encoding="utf-8")

                            

print(f"Dados gerados com sucesso! Total de registros: {len(df_tab_vendas_withconstraints)}")

#fechar a conexão com o banco de dados
engine.dispose()



