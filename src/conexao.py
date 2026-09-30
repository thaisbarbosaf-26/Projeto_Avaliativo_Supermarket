
import os
from dotenv import load_dotenv # carrega a variável informada em .env
from sqlalchemy import create_engine

load_dotenv()
 
CONN_URL = os.getenv("CONN_URL")
engine = create_engine(CONN_URL)

print("Conexão realizada com sucesso!")

