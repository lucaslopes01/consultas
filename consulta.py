import pandas as pd
import os
from class_mysql import BDMySQL
mysql = BDMySQL('tributo')

consulta = pd.read_excel(os.getenv('ARQUIVO'))

print(consulta)

# extrair cnpj utilizando pandas  

# transformar cnpj em cnpjbase

# remover cnpj base repetidos 

# consultar tabela no banco buscando cnpj ordenado pelo ano [0]
# se não encontrar busca cnpj base ordenado pelo ano [0]
# cria uma lista com as consultas se ja cnpj base ja estiver sido consultado, não consulta e pega a forma de tributação


# gravar na tabela as informações extraidas do banco (forma tributação e ano)

