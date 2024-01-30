import psycopg2
from sqlalchemy import create_engine

def dw_postgres_engine(database_name):
    
    # Koneksi ke database
    user = "root"
    password = "qwerty123"
    host = "localhost"
    port = "3000"
    
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database_name}")

    return engine