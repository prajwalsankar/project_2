import pandas as pd
import pyodbc
import warnings
warnings.filterwarnings('ignore')
conn=pyodbc.connect('Driver={SQL Server};'
                    'Server={DESKTOP-6V3O1TC\SQLEXPRESS};'
                    'Database=task1;'
                    'Trusted_Connection=yes;')

df=pd.read_sql_query('select * from productdata',conn)
pd.set_option('display.max_rows', None)
dis=pd.read_sql_query('select distinct Category,Product,Sales,Quarter from productdata',conn)

print(df)
print(type(df))
                    
#print(dis)
