# Importando bibliotecas
import os
import pandas as pd
from sqlalchemy import create_engine # Cria a conexão com o banco de dados

# Criando conexão com o banco supermarket
engine = create_engine(
    "postgresql+psycopg2://postgres:admin123@localhost:5432/supermarket"
)

print("Conexão realizada com sucesso!")

