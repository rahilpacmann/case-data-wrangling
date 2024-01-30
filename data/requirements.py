import urllib.request, json 

def requirements_data():
    requirements_table_url = 'https://rahilpacmann.github.io/case-data-wrangling-api/requirements_table.json'
    with urllib.request.urlopen(requirements_table_url) as url:
        requirements_table = json.load(url)
    
    return requirements_table