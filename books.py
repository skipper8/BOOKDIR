import psycopg2
import pandas as pd
from param_dic import params

#CONNECT
param = params("lib", "5432")
con = psycopg2.connect(host= param.host, database=param.db, user=param.user, password=param.password, port=param.port)

df = pd.read_sql("SELECT * FROM books", con)
print(df)
