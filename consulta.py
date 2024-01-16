import pandas as pd
import os
from class_mysql import BDMySQL
mysql = BDMySQL('tributo')

consulta = pd.read_excel(os.getenv('ARQUIVO'))

print(consulta)