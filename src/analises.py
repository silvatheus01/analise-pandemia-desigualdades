import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

from src.constantes import *
from src.dados import *

def gerar_tabela_diferencas_taxas_aprovacao():
    if not os.path.exists(PATH_IDEB):
        baixar_dados_ideb()

    df = pd.read_csv(PATH_IDEB)

    anos = [2017, 2019, 2021]
    resultados_outros_anos = []
    resultado_2021 = None

    for ano in anos:
        filtro = (df['ano'] == ano) & (df['ensino'] == 'medio')
        dados_filtrados = df[filtro]
        
        dados_publica = dados_filtrados[(dados_filtrados['rede'] == 'publica') | (dados_filtrados['rede'] == 'pública')]
        dados_privada = dados_filtrados[dados_filtrados['rede'] == 'privada']
        
        taxa_aprovacao_publica = dados_publica['taxa_aprovacao'].iloc[0]
        taxa_aprovacao_privada = dados_privada['taxa_aprovacao'].iloc[0]
        
        diferenca_taxas = abs(taxa_aprovacao_publica - taxa_aprovacao_privada)
        
        if ano != 2021:
            resultados_outros_anos.append(diferenca_taxas)
        else:
            resultado_2021 = diferenca_taxas

    plt.box(on=None)
    the_table = plt.table(
        cellText=[["{0:.2f}".format(resultado_2021), np.mean(resultados_outros_anos)]],
        colLabels=['2021', 'Média dos anos 2017 e 2019'],
        loc='center',
        colWidths=[0.1,0.4]
    )

    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    the_table.auto_set_font_size(False)
    the_table.set_fontsize(12)
    the_table.scale(1.5, 2.3)

    plt.savefig(f'{DIR_GRAFICOS_TABELA}/diferencas_taxas_aprovacao')
    plt.clf()

def gerar_tabela_media_taxas_aprovacao():
    if not os.path.exists(PATH_IDEB):
        baixar_dados_ideb()

    df = pd.read_csv(PATH_IDEB)

    anos_escolares = "iniciais (1-5)"
    ensino = "fundamental"

    filtro = (df['ensino'] == ensino) & (df['anos_escolares'] == anos_escolares)
    dados_filtrados = df[filtro]

    medias = []
    anos = dados_filtrados['ano'].unique()

    for ano in anos:
        dados_ano = dados_filtrados[dados_filtrados['ano'] == ano]
        dados_publica = dados_ano[(dados_ano['rede'] == 'publica') | (dados_ano['rede'] == 'pública')]
        dados_privada = dados_ano[dados_ano['rede'] == 'privada']

        taxas_aprovacao = [dados_publica['taxa_aprovacao'].iloc[0], dados_privada['taxa_aprovacao'].iloc[0]]
        media = np.mean(taxas_aprovacao)

        medias.append(media)


    plt.box(on=None)
    the_table = plt.table(
        cellText=[["{0:.2f}".format(media)] for media in medias],
        colLabels=['Média (%)'],
        rowLabels=anos,
        loc='center',
        colWidths=[0.2],
    )

    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    the_table.auto_set_font_size(False)
    the_table.set_fontsize(12)

    the_table.scale(1.5, 2.3)
    plt.savefig(f'{DIR_GRAFICOS_TABELA}/medias_taxas_aprovacao')

def gerar_graficos_taxa_abandono():
    if not os.path.exists(PATH_INDICADORES_BRASIL_TRATADO):
        baixar_dados_indicadores_brasil()

    df = pd.read_csv(PATH_INDICADORES_BRASIL_TRATADO)
    taxas_abandono = [
        'taxa_abandono_ef', 
        'taxa_abandono_ef_anos_iniciais', 
        'taxa_abandono_ef_anos_finais',
        'taxa_abandono_ef_1_ano', 
        'taxa_abandono_ef_2_ano', 
        'taxa_abandono_ef_3_ano',
        'taxa_abandono_ef_4_ano', 
        'taxa_abandono_ef_5_ano',
        'taxa_abandono_ef_6_ano',
        'taxa_abandono_ef_7_ano', 
        'taxa_abandono_ef_8_ano', 
        'taxa_abandono_ef_9_ano',
        'taxa_abandono_em', 
        'taxa_abandono_em_1_ano',
        'taxa_abandono_em_2_ano',
        'taxa_abandono_em_3_ano', 
        'taxa_abandono_em_4_ano', 
        'taxa_abandono_em_nao_seriado'
    ]

    anos = [2018,2019,2020,2021]
    barWidth = 0.25

    def legend_without_duplicate_labels(figure):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        figure.legend(by_label.values(), by_label.keys())

    for taxa in taxas_abandono:
        posicoes = []
        plt.figure(figsize=(9, 5))
        for i, ano in enumerate(anos):
            posicao_privada = i
            posicao_publica = i + barWidth
            posicoes.append((posicao_privada+posicao_publica)/2)
            
            filtro_publica = (df['ano'] == ano) & (df['rede'] == 'publica')
            filtro_privada = (df['ano'] == ano) & (df['rede'] == 'privada')

            df_filtrado_publica = df[filtro_publica]
            df_filtrado_privada = df[filtro_privada]

            dados_abandono_publica = df_filtrado_publica[taxa]
            dados_abandono_privada = df_filtrado_privada[taxa]            

            plt.bar(posicao_privada, dados_abandono_privada, color= '#1f6eed', width=barWidth, label='privada')
            plt.bar(posicao_publica, dados_abandono_publica, color= '#59ed1f', width=barWidth, label='pública')

            plt.xlabel('Anos')
        
        plt.xticks(posicoes, anos)
        plt.ylabel('Taxa de abandono (%)')
        plt.ylim((0,12))

        legend_without_duplicate_labels(plt)
        plt.savefig(f'{DIR_GRAFICOS_BARRA}/{taxa}')
        plt.clf()  

def gerar_graficos_reprovacao_horas():
    if not os.path.exists(PATH_INDICADORES_UF_TRATADO):
        baixar_dados_indicadores_uf()

    df = pd.read_csv(PATH_INDICADORES_UF_TRATADO)

    anos = [2018,2019,2020,2021]
    ufs = df['sigla_uf'].unique()
    series = ['ef', 'em']
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

    for ano in anos:
        for serie in series: 
            plt.figure(figsize=(30, 10))
            
            for i,uf in enumerate(ufs):
                filtro = (df['ano'] == ano) & (df['sigla_uf'] == uf)
                df_filtrado = df[filtro]
                taxa_reprovacao = df_filtrado[f'taxa_reprovacao_{serie}']
                had = df_filtrado[f'had_{serie}']

                plt.scatter(taxa_reprovacao, had, color=cores[i], s = 1000)
                plt.annotate(
                    uf, 
                    (taxa_reprovacao, had), 
                    fontsize=20, 
                    annotation_clip=False, 
                    arrowprops=dict(arrowstyle='->'), 
                    ha='center', 
                    va='center', 
                    color=inverter_cor(cores[i])
                )
            
            plt.grid()
            plt.xticks(fontsize=15)
            plt.yticks(fontsize=15)
            plt.ylim((3,8))
            plt.xlim((0,22))
            plt.xlabel('Taxa de reprovação (%)', fontsize=20) 
            plt.ylabel('Média de Horas-Aula diária', fontsize=20) 
            plt.legend(
                ufs, 
                fontsize=15, 
                ncol=3, 
                labelspacing=1.5, 
                loc='upper right', 
                bbox_to_anchor=(1.1, 1.1)
            )
            
            plt.savefig(f'{DIR_GRAFICOS_DISPERSAO}/reprovacao_x_horas_aula_{serie}_{ano}')
            plt.clf()