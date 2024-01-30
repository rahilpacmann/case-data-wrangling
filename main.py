import pandas as pd
from utils.data_warehouse_connections import dw_postgres_engine
from utils.data_cleaning import cleaning_all
from utils.data_transform import generate_film_list_table
from data.requirements import requirements_data
from data.data_source_full import data_full
import warnings 
  
warnings.filterwarnings('ignore')

# LOAD TO "dvdrental_database"
def load_dvdrental_clean(data):
    engine = dw_postgres_engine(database_name = 'dvdrental_clean')
    
    for table_name, df in data.items():
        df.to_sql(table_name, engine, if_exists = 'replace', index = False)

    engine.dispose()
    
# LOAD TO "dvdrental_analysis"
def load_dvdrental_analysis(data):
    engine = dw_postgres_engine(database_name = "dvdrental_analysis")
    data.to_sql('film_list', engine, if_exists = 'replace', index = False)
    
if __name__ == '__main__':
    actual_table = data_full()
    requirements_table = requirements_data()
    data_clean = cleaning_all(actual_data = actual_table,
                              requirements_data = requirements_table)
    
    load_dvdrental_clean(data = data_clean)
    print("Load to dvdrental_clean database COMPLETED!!!")
    
    film_list = generate_film_list_table(actual_table_clean = data_clean)
    load_dvdrental_analysis(data = film_list)
    print("Load to dvdrental_analyis database COMPLETED!!!")