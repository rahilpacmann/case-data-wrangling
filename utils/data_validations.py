import sys
sys.path.insert(0,'/home/laode/case-data-wrangling/data')

from tabulate import tabulate
from requirements import requirements_data
from data_source_full import data_full

# Check table requirments
def check_table_requirements(actual_table, requirements_table):
    
    actual_table_name = [table_name for table_name in actual_table]
    requirements_table_name = list(requirements_table.keys())
    table_checking = []

    for table_name in requirements_table_name:
        
        if table_name in actual_table_name:
            table_checking.append([table_name, "✓"])
            
        else:
            table_checking.append([table_name, "✗"])
            
    table_headers = ['Table_name', 'Is_Exist']
    table = tabulate(table_checking, headers = table_headers, tablefmt = 'grid')
    print("=> STEP 1: Check Table")
    print(table)
    

# Check table
def check_shape(actual_table):
    print("=> STEP 2: Check Data Shape")
    shape_checking = []
    
    for table_name in actual_table:
        n_row = actual_table[table_name].shape[0]
        n_col = actual_table[table_name].shape[1]
        shape_checking.append([table_name, n_row, n_col])
    
    # Print Table
    table_headers = ['Table_name', 'Number of rows', 'Number of columns']
    table = tabulate(shape_checking, headers = table_headers, tablefmt = 'grid')
    print(table)
    
# Check columns
def check_columns(actual_table, requirements_table):
    print("=> STEP 3: Check Columns")
    
    for table_name in requirements_table:
        result = []
        
        actual_columns = list(actual_table[table_name].columns)
        requirements_columns = []
        
        requirements_table_data = requirements_table[table_name]
        for column in requirements_table_data:
            requirements_columns.append(column['column_name'])

        for column_name in set(actual_columns + requirements_columns):
            in_actual_table = '✔' if column_name in actual_columns else '✘'
            in_requirements_table = '✔' if column_name in requirements_columns else '✘'
            result.append([column_name, in_actual_table, in_requirements_table])

        if set(actual_columns) == set(requirements_columns):
            pass

        else:
            headers = ["column_name", "in_actual_table", "in_requirements_table"]
            print(f"Table : {table_name}")
            print(tabulate(result, headers = headers, tablefmt = "grid"))
            print("\n")
            
# Check data types
def check_data_types(actual_table, requirements_table):
    print("=> STEP 4: Check Data Types")
    summary_data = []

    for table_name, df in actual_table.items():
        if table_name in requirements_table:
            for column_info in requirements_table[table_name]:
                column_name = column_info["column_name"]
                requirements_type = column_info["data_type"]
                
                if column_name in df.columns:
                    actual_type = str(df[column_name].dtype)
                    match = "✔" if actual_type == requirements_type else "✘"
                    summary_data.append([table_name, column_name, actual_type, requirements_type, match])
                else:
                    summary_data.append([table_name, column_name, "N/A", requirements_type, "✘ (Column not found)"])

    headers = ["Table Name", "Column Name", "Actual Type", "Requirements Type", "Match"]

    mismatch_data = [row for row in summary_data if "✘" in row[4]]
    
    if mismatch_data:
        print("\nSummary of Mismatches Data Types:")
        print(tabulate(mismatch_data, headers = headers, tablefmt = "grid"))
    
    else:
        print("All Data Types Match")
        
        
# Check missing values
def check_missing_values(actual_table):
    print("=> STEP 5: Check Missing Values")

    missing_summary = []

    for table_name, df in actual_table.items():
        missing_count = df.isnull().sum()
        missing_percentage = (df.isnull().mean() * 100).round(2)
        
        for column_name, count in missing_count.items():
            if count > 0:
                percentage = missing_percentage[column_name]
                missing_summary.append([table_name, column_name, count, percentage])

    if missing_summary:
        print("Missing Value Summary:")
        print(tabulate(missing_summary, headers=["Table Name", "Column Name", "Missing Value Count", "Missing Value Percentage"], tablefmt="grid"))
    
    else:
        print("There's no Missing Values")
        
# Check duplicates
def check_duplicates_data(actual_table):
    print("=> STEP 6: Check Duplicates Data")
    duplicate_summary = []

    for table_name, df in actual_table.items():
        try:
            duplicate_rows = df[df.duplicated(keep = False)]
            
            if not duplicate_rows.empty:
                duplicate_summary.append([table_name, len(duplicate_rows)])
        except:
            pass

    if duplicate_summary:
        print("Duplicate Data Summary:")
        print(tabulate(duplicate_summary, headers=["Table Name", "Duplicate Rows Count"], tablefmt="grid"))
    else:
        print("No Duplicate Data Found")
        

def data_validations_all(actual_data, requirements_data):
    actual_table = actual_data
    requirements_table = requirements_data
    
    check_table_requirements(actual_table = actual_table,
                             requirements_table = requirements_table)
    
    print("-"*100)
    print("\n")
    
    check_shape(actual_table = actual_table)
    
    print("-"*100)
    print("\n")
    
    check_columns(actual_table = actual_table,
                  requirements_table = requirements_table)
    
    print("-"*100)
    print("\n")
    
    check_data_types(actual_table = actual_table,
                     requirements_table = requirements_table)

    print("-"*100)
    print("\n")
    
    check_missing_values(actual_table = actual_table)

    print("-"*100)
    print("\n")
    
    check_duplicates_data(actual_table = actual_table)
    
    
if __name__ == "__main__":
    actual_table = data_full()
    requirements_table = requirements_data()
    
    check_table_requirements(actual_table = actual_table,
                             requirements_table = requirements_table)
    
    print("-"*100)
    print("\n")
    
    check_shape(actual_table = actual_table)
    
    print("-"*100)
    print("\n")
    
    check_columns(actual_table = actual_table,
                  requirements_table = requirements_table)
    
    print("-"*100)
    print("\n")
    
    check_data_types(actual_table = actual_table,
                     requirements_table = requirements_table)

    print("-"*100)
    print("\n")
    
    check_missing_values(actual_table = actual_table)

    print("-"*100)
    print("\n")
    
    check_duplicates_data(actual_table = actual_table)