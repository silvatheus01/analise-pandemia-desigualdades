import basedosdados as bd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PROJECT_ID = "base-dos-dados-395523"

# Para carregar o dado direto no pandas
# df = bd.read_table(dataset_id='br_inep_ideb',
# table_id='brasil',
# billing_project_id=PROJECT_ID)

# df.to_excel('br_inep_ideb.xlsx', index=False)

# pd.set_option('display.max_rows', None)
# print(df)


## Brasil
##########################
# df = pd.read_excel('br_inep_ideb.xlsx')

# # Podemos ver que a média é maior do que o ano de 2021, então houve uma desigualdade menor entre rede publica e privada 
# # no ensino médio 
# anos = [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021]
# resultados = []
# resultado_2021 = None

# for ano in anos:
#     filtro = (df['ano'] == ano) & (df['ensino'] == 'medio')
#     dados_filtrados = df[filtro]
    
#     # Filtrar os dados para as redes "publica" e "privada"
#     dados_publica = dados_filtrados[(dados_filtrados['rede'] == 'publica') | (dados_filtrados['rede'] == 'pública')]
#     dados_privada = dados_filtrados[dados_filtrados['rede'] == 'privada']
    
#     taxa_aprovacao_publica = dados_publica['taxa_aprovacao'].iloc[0]
#     taxa_aprovacao_privada = dados_privada['taxa_aprovacao'].iloc[0]
    
#     diferenca_taxas = abs(taxa_aprovacao_publica - taxa_aprovacao_privada)
    
#     if ano != 2021:
#         resultados.append(diferenca_taxas)
#     else:
#         resultado_2021 = diferenca_taxas

# print('Diferença 2021: ', resultado_2021)
# print('Média dos outros anos: ', np.mean(resultados))

# ########################
# #A pandemia não impediu o crescimento durante os anos
# print()
# anos_escolares = "iniciais (1-5)"
# ensino = "fundamental"

# # Filtrar os dados para o ensino "fundamental" e anos escolares "iniciais (1-5)"
# filtro = (df['ensino'] == ensino) & (df['anos_escolares'] == anos_escolares)
# dados_filtrados = df[filtro]

# resultados = []

# # Iterar pelos anos únicos
# for ano in dados_filtrados['ano'].unique():
#     dados_ano = dados_filtrados[dados_filtrados['ano'] == ano]
#     dados_publica = dados_ano[(dados_ano['rede'] == 'publica') | (dados_ano['rede'] == 'pública')]
#     dados_privada = dados_ano[dados_ano['rede'] == 'privada']

#     taxas_aprovacao = [dados_publica['taxa_aprovacao'].iloc[0], dados_privada['taxa_aprovacao'].iloc[0]]
#     media = np.mean(taxas_aprovacao)
    
#     resultados.append((ano, media))

# for ano, media in resultados:
#     print(f'Media no ano {ano}: {media}')

##############
df = bd.read_table(dataset_id='br_inep_indicadores_educacionais',
table_id='brasil',
billing_project_id=PROJECT_ID)

df.to_excel('br_inep_indicadores_educacionais__brasil.xlsx', index=False)
