from src.analises import *

geradores = [
    gerar_tabela_diferencas_taxas_aprovacao, 
    gerar_tabela_media_taxas_aprovacao,
    gerar_graficos_taxa_abandono,
    gerar_graficos_reprovacao_horas
]

print('Geração de análises iniciada.')
for i, gerador in enumerate(geradores):
    gerador()
    print(f'Gráfico(s) da {i+1}° análise gerado(s)')
