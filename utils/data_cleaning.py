import sys
sys.path.insert(0,'/home/laode/case-data-wrangling/data')

from requirements import requirements_data
from data_source_full import data_full

# Handle missing values
def handle_mismatch_columns(actual_table):
    country_df = actual_table['country']
    country_df.insert(0, 'country_id', range(1, len(country_df) + 1))
    actual_table['country'] = country_df
    
    city_df = actual_table['city']
    city_df = city_df.merge(country_df, on = 'country', how = 'left')

    city_df = city_df[['city_id', 'country_id', 'city', 'last_update']]
    actual_table['city'] = city_df
    
    return actual_table

def remove_missing_values(actual_table):
    cleaned_actual_table = {}

    for table_name, df in actual_table.items():
        cleaned_df = df.dropna() 
        cleaned_actual_table[table_name] = cleaned_df

    return cleaned_actual_table

# Handle data types
def adjust_data_types(actual_table, requirements_table):
    adjusted_table_dict = {}

    for table_name, df in actual_table.items():
        if table_name in requirements_table:
            table_requirements = requirements_table[table_name]

            for column_info in table_requirements:
                column_name = column_info["column_name"]
                data_type = column_info["data_type"]

                if column_name in df.columns:
                    df[column_name] = df[column_name].astype(data_type)

            adjusted_table_dict[table_name] = df

    return adjusted_table_dict

# Handle duplicates data
def remove_duplicates(actual_table):
    cleaned_table_dict = {}

    for table_name, df in actual_table.items():
        if table_name == 'city':
            cleaned_df = df.drop_duplicates(keep = 'first')  # Menghapus data duplikat dengan mempertahankan record data yang pertama
            cleaned_table_dict[table_name] = cleaned_df

        else:
            cleaned_table_dict[table_name] = df

    return cleaned_table_dict

# Data cleaning all 
def cleaning_all(actual_data, requirements_data):
    actual_table = actual_data
    requirements_table = requirements_data
    
    actual_table_clean = handle_mismatch_columns(actual_table = actual_table)
    actual_table_clean = remove_missing_values(actual_table = actual_table_clean)
    actual_table_clean = adjust_data_types(actual_table = actual_table_clean, requirements_table = requirements_table)
    actual_table_clean = remove_duplicates(actual_table = actual_table_clean)
    
    return actual_table_clean