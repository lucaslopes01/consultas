import pandas as pd
import os
from class_mysql import BDMySQL
mysql = BDMySQL('b7')
consulta = pd.read_excel(os.getenv('ARQUIVO'),  dtype={'cnpj': str})  
coluna = consulta.cnpj

lista ={}
for i in coluna:
    cnpj_base = str(i).zfill(14)[:8]
    lista[cnpj_base] = ''

consulta['forma_tributacao'] = ''
for l in lista:
    
    sql = f"SELECT forma_tributacao , MAX(ano) As ano  FROM b7.regime_tributario WHERE cnpj_base = '{l}' GROUP BY forma_tributacao ORDER BY ano Desc"
    retorna = mysql.retorna_query(sql)
    if retorna:
        lista[l] = retorna[0]['forma_tributacao']

for index, row in consulta.iterrows():
    cnpj_base_n = str(row['cnpj']).zfill(14)[:8]
    if cnpj_base_n in lista:
        consulta.at[index, 'forma_tributacao'] = lista[cnpj_base_n]
print(consulta)
del mysql
consulta.to_excel(os.getenv('ARQUIVO'), index=False)

    


# Exibir o DataFrame atualizado

    









# consulta['nova'] =  ''
# consulta.loc[0,'forma_tributacao']='2'
# print (consulta)

    # novo_base = str(i)
    # cnpj_base = novo_base[:7]
    # novo_base_z = novo_base.zfill(14)


    # cnpj_base_z = cnpj_base.zfill(8)
  
    # lista_cnpj_base.append(cnpj_base_z)

    
    # sql_cnpj_base = f"SELECT forma_tributacao , MAX(ano) As ano  FROM b7.regime_tributario WHERE cnpj_base = '{cnpj_base_z}' GROUP BY forma_tributacao"
    # sql = f"SELECT forma_tributacao , MAX(ano) As ano  FROM b7.regime_tributario WHERE cnpj = '{novo_base}' GROUP BY forma_tributacao"
    # retorna = mysql.retorna_query(sql)  
    # retorna_cnpj_base = mysql.retorna_query(sql_cnpj_base)  
    
    # if retorna:
    #     print(retorna)
    # else:
    #     print(retorna_cnpj_base)
        

# print(consulta)

# extrair cnpj utilizando pandas  

# transformar cnpj em cnpjbase

# remover cnpj base repetidos 

# consultar tabela no banco buscando cnpj ordenado pelo ano [0]
# se não encontrar busca cnpj base ordenado pelo ano [0]
# cria uma lista com as consultas se ja cnpj base ja estiver sido consultado, não consulta e pega a forma de tributação


# gravar na tabela as informações extraidas do banco (forma tributação e ano)

