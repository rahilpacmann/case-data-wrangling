import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def database_conn():
    dbname = "dvdrental"
    user = "postgres"
    password = "qwerty123"
    host = "localhost"
    port = "5433"

    engine_str = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(engine_str)
    return engine

def data_3(table_name):
    try:
        engine = database_conn()
        
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, engine)
        
        return df

    except Exception as e:
        print(f"Error: {e}")
        
        return pd.DataFrame()