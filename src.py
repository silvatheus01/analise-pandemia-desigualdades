import basedosdados as bd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

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
#Taxa de abandono
# df = bd.read_table(dataset_id='br_inep_censo_escolar',
# table_id='escola',
# billing_project_id=PROJECT_ID)

# df.to_excel('br_inep_censo_escolar__escola.xlsx', index=False)

# df = bd.read_table(
#     dataset_id='br_inep_indicadores_educacionais',
#     table_id='brasil',
#     billing_project_id=PROJECT_ID
# )

# df.to_excel('br_inep_indicadores_educacionais__brasil.xlsx', index=False)

# Tratamento
# df = pd.read_excel('br_inep_indicadores_educacionais__brasil.xlsx')
# df = df[(df['localizacao'] == 'total') & ((df['rede'] == 'publica') | (df['rede'] == 'privada'))]
# df.sort_values('ano', inplace=True)
# df.to_csv('br_inep_indicadores_educacionais__brasil__tratado.csv')


# taxas_abandono = {
#     'taxa_abandono_ef':'Ensino Fundamental', 
#     'taxa_abandono_ef_anos_iniciais':'Ensino Fundamental Anos Iniciais', 
#     'taxa_abandono_ef_anos_finais':'Ensino Fundamental Anos Finais',
#     'taxa_abandono_ef_1_ano':'Ensino Fundamental - 1º ano', 
#     'taxa_abandono_ef_2_ano':'Ensino Fundamental - 2º ano', 
#     'taxa_abandono_ef_3_ano':'Ensino Fundamental - 3º ano',
#     'taxa_abandono_ef_4_ano':'Ensino Fundamental - 4º ano', 
#     'taxa_abandono_ef_5_ano':'Ensino Fundamental - 5º ano' ,
#     'taxa_abandono_ef_6_ano':'Ensino Fundamental - 6º ano',
#     'taxa_abandono_ef_7_ano':'Ensino Fundamental - 7º ano', 
#     'taxa_abandono_ef_8_ano':'Ensino Fundamental - 8º ano', 
#     'taxa_abandono_ef_9_ano':'Ensino Fundamental - 9º ano',
#     'taxa_abandono_em':'Ensino Médio', 
#     'taxa_abandono_em_1_ano':'Ensino Médio - 1º ano',
#     'taxa_abandono_em_2_ano':'Ensino Médio - 2º ano',
#     'taxa_abandono_em_3_ano':'Ensino Médio - 3º ano', 
#     'taxa_abandono_em_4_ano':'Ensino Médio - 4º ano' , 
#     'taxa_abandono_em_nao_seriado':'Ensino Médio Não seriado'
# }

# anos = [2018,2019,2020,2021]
# posicao = np.arange(len(anos))
# barWidth = 0.25
# df = pd.read_csv('br_inep_indicadores_educacionais__brasil__tratado.csv')

# def legend_without_duplicate_labels(figure):
#     handles, labels = plt.gca().get_legend_handles_labels()
#     by_label = dict(zip(labels, handles))
#     figure.legend(by_label.values(), by_label.keys())

# for taxa, label in taxas_abandono.items():
#     posicoes = []
#     for i, ano in enumerate(anos):
#         posicao_privada = i
#         posicao_publica = i + barWidth
#         posicoes.append((posicao_privada+posicao_publica)/2)
        
#         filtro_publica = (df['ano'] == ano) & (df['rede'] == 'publica')
#         filtro_privada = (df['ano'] == ano) & (df['rede'] == 'privada')

#         df_filtrado_publica = df[filtro_publica]
#         df_filtrado_privada = df[filtro_privada]

#         dados_abandono_publica = df_filtrado_publica[taxa]
#         dados_abandono_privada = df_filtrado_privada[taxa]            

#         plt.bar(posicao_privada, dados_abandono_privada, color= '#1f6eed', width=barWidth, label='privada')
#         plt.bar(posicao_publica, dados_abandono_publica, color= '#59ed1f', width=barWidth, label='pública')

#         plt.xlabel(f'Abandono: {label}')

    
#     plt.xticks(posicoes, anos)
#     plt.ylabel('Taxa de abandono')
#     plt.title('Taxa de abandono por ano na rede privada e pública')

#     legend_without_duplicate_labels(plt)
#     #plt.legend()
#     plt.savefig(f'grafico_abandono_{taxa}')
#     plt.clf()  

## Gráfico de dispersão taxa de reprovação x esforço docente
# df = bd.read_table(dataset_id='br_inep_indicadores_educacionais',
# table_id='uf',
# billing_project_id=PROJECT_ID)

# df.to_csv('br_inep_indicadores_educacionais__uf.csv', index=False)

# df = pd.read_csv('br_inep_indicadores_educacionais__uf.csv')

# filtro = (df['localizacao'] == 'total') & (df['rede'] == 'total')
# df_filtrado = df[filtro]

# df_filtrado_outros = df_filtrado.filter(items=['ano','sigla_uf','localizacao','rede']).sort_values('ano')
# df_filtrado = pd.concat(
#     [
#         df_filtrado_outros,
#         df_filtrado['taxa_reprovacao_em'], 
#         df_filtrado['taxa_reprovacao_ef'], 
#         df_filtrado['had_ef'],
#         df_filtrado['had_em']
#     ],
#     axis=1
# )

# df_filtrado.to_csv('br_inep_indicadores_educacionais__uf__tratado.csv', index=False)

df = pd.read_csv('br_inep_indicadores_educacionais__uf__tratado.csv')

anos = [2018,2019,2020,2021,2022]
ufs = df['sigla_uf'].unique()
series = {
    'ef':'Ensino Fundamental', 
    'em': 'Ensino Médio'
}
cores = [
  '#FF0000',
  '#00FF00',
  '#0000FF',
  '#FFFF00',
  '#00FFFF',
  '#FF00FF',
  '#990000',
  '#009900',
  '#000099',
  '#999900',
  '#009999',
  '#990099',
  '#CC0000',
  '#00CC00',
  '#0000CC',
  '#CCCC00',
  '#00CCCC',
  '#CC00CC',
  '#660000',
  '#006600',
  '#000066',
  '#666600',
  '#006666',
  '#660066',
  '#330000',
  '#003300',
  '#000033',
  '#333300',
  '#003333',
  '#330033',
  '#110000',
  '#001100',
  '#000011',
  '#111100',
  '#001111',
  '#110011',
]

def inverter_cor(cor):
    if cor.startswith("#") and len(cor) == 7:
        r = cor[1:3]
        g = cor[3:5]
        b = cor[5:7]
        cor_invertida = f"#{255 - int(r, 16):02X}{255 - int(g, 16):02X}{255 - int(b, 16):02X}"
        return cor_invertida
    else:
        return None


cor_branca = int('FFFFFF', 16)

for ano in anos:
    for serie_key, serie in series.items(): 
        plt.figure(figsize=(30, 10))

        num_rotulos = 20
        for i,uf in enumerate(ufs):
            filtro = (df['ano'] == ano) & (df['sigla_uf'] == uf)
            df_filtrado = df[filtro]
            taxa_reprovacao = df_filtrado[f'taxa_reprovacao_{serie_key}']
            had = df_filtrado[f'had_{serie_key}']

            plt.scatter(taxa_reprovacao, had, color=cores[i], s = 1000)
            plt.annotate(uf, (taxa_reprovacao, had), fontsize=20, annotation_clip=False, arrowprops=dict(arrowstyle='->'), ha='center', va='center', color=inverter_cor(cores[i]))
        
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.title(f'Gráfico de dispersão - {serie} - {ano}', fontsize=30)
        plt.xlabel('Taxa de reprovação', fontsize=20) 
        plt.ylabel('Média de Horas-Aula diária', fontsize=20) 
        plt.legend(ufs, fontsize=15, ncol=3, labelspacing=1.5, loc='upper right', bbox_to_anchor=(1.1, 1.1))
        
        plt.savefig(f'dispersao_{serie_key}_{ano}')
        plt.clf()
            

        

df = df[filtro]

df_filtrado_taxa_reprovacao = df.filter(like='taxa_reprovacao_')

print(df[np.isnan(df['taxa_reprovacao_ef']) == False])
