import pandas as pd
import basedosdados as bd
import pandas as pd

from src.constantes import *

def baixar_dados_ideb():
    df = bd.read_table(
        dataset_id=DATASET_ID_IDEB,
        table_id='brasil',
        billing_project_id=PROJECT_ID
    )
    df.to_csv(PATH_IDEB, index=False)

def baixar_dados_indicadores_brasil():
    df = bd.read_table(
        dataset_id=DATASET_ID_INDICADORES,
        table_id='brasil',
        billing_project_id=PROJECT_ID
    )
    df.to_csv(PATH_INDICADORES_BRASIL_ORIGINAL, index=False)

    df = pd.read_csv(PATH_INDICADORES_BRASIL_ORIGINAL)
    df = df[(df['localizacao'] == 'total') & ((df['rede'] == 'publica') | (df['rede'] == 'privada'))]
    df.sort_values('ano', inplace=True)
    df.to_csv(PATH_INDICADORES_BRASIL_TRATADO)

def baixar_dados_indicadores_uf():
    df = bd.read_table(
        dataset_id=DATASET_ID_INDICADORES,
        table_id='uf',
        billing_project_id=PROJECT_ID
    )
    df.to_csv(PATH_INDICADORES_UF_ORIGINAL, index=False)

    df = pd.read_csv(PATH_INDICADORES_UF_ORIGINAL)
    filtro = (df['localizacao'] == 'total') & (df['rede'] == 'total')
    df_filtrado = df[filtro]
    df_filtrado_outros = df_filtrado.filter(items=['ano','sigla_uf','localizacao','rede']).sort_values('ano')
    df_filtrado = pd.concat(
        [
            df_filtrado_outros,
            df_filtrado['taxa_reprovacao_em'], 
            df_filtrado['taxa_reprovacao_ef'], 
            df_filtrado['had_ef'],
            df_filtrado['had_em']
        ],
        axis=1
    )
    df_filtrado.to_csv(PATH_INDICADORES_UF_TRATADO, index=False)