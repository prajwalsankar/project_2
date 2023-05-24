import pandas as pd
import pyodbc
import warnings
warnings.filterwarnings('ignore')

conn = pyodbc.connect('Driver={SQL Server};'
                    'Server={DESKTOP-6V3O1TC\SQLEXPRESS};'
                    'Database=task1;'
                    'Trusted_Connection=yes;')
cursor = conn.cursor()
r=pd.read_sql_query('select * from products',conn)
pd.set_option('display.max_rows', None)
print(r)
print(type(r))
