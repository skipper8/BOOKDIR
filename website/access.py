import psycopg2
import pandas as pd
from param_dic import params

class Accesss(self):
    def __init__(self):
        #CONNECT
        self.param = params("lib", "5432")
        self.con = psycopg2.connect(host= param.host, database=param.db, user=param.user, password=param.password, port=param.port)
    
    def search(self, tabel, searchvalue, text):
        return pd.read_sql("SELECT * WHERE %(w) = %(t) FROM %(tb)", con, params={"t":text,"tb":table, "w":searchvalue})
    
    def gather_all(self, table):
        return pd.read_sql("SELECT * FROM %(tb)", con, params={"tb":table})
