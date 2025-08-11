import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        connect_timeout=10
    )
    print("Conexão com o banco de dados (psycopg2) estabelecida com sucesso!")
    conn.close()
except psycopg2.OperationalError as e:
    print(f"Erro ao conectar ao banco de dados (psycopg2): {e}")
    # Check if the exception has pgcode and pgerror attributes before printing
    if hasattr(e, 'pgcode') and e.pgcode:
        print(f"Detalhes do erro: {e.pgcode} {e.pgerror}")
    print(repr(e))
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")
    print(repr(e))