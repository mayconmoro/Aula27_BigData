# Atividade >> Correlação de Pearson
# verificar se existe alguma relação entre as ocorrências de lesão corporal dolosa e as lesões corporais seguidas de morte, por delegacias (CISPs).
# lesao_corp_morte, lesao_corp_dolosa

# Importando bibliotecas numpy, pandas, matplotlib
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

os.system("cls")  # Limpar a tela do terminal

# Importando os dados do site de registros de ocorrências ISP RJ: https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv
ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

try:
    print('Obtendo os dados...')

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # print(df_ocorrencias.head(10))
    
    df_lesoes = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']] # Delimitando as variaveis
    # print(df_lesoes.head(10))
    
    df_lesoes = df_lesoes.groupby('cisp', as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum() # Agrupar por cisp e somar quantidade de lesoes dolosas e lesoes seguidas de morte
    # print(df_lesoes.head(10))
    
    df_lesoes = df_lesoes.sort_values(by='lesao_corp_morte', ascending=False) # Ordenando os dados por lesão corporal seguida por morte
    print(df_lesoes.head(10))

    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter os dados: {e}')    

    # Calculando a Correlação entre roubo de veiculos e as recuperações de veiculos
try:
    print('\nCalculando a correlação entre lesões corporais dolosas e lesões corporais seguidas de morte...\n')
    
    correlacao = np.corrcoef(df_lesoes['lesao_corp_dolosa'], df_lesoes['lesao_corp_morte'])[0, 1] # Calcular a correlação

    print(200 * '=')
    print(f'Os dados estatísticos apontam uma forte relação entre as ocorrências de lesão corporal dolosa e as lesões corporais seguidas de morte, por delegacias (CISPs). A correlação é de {correlacao:.4f}.')
    print(f'A recomendação é que a segurança pública faça uma análise mais aprofundada sobre a proporção de lesões corporais dolosas e lesões corporais seguidas de morte, validando se a relação é de fato causal ou apenas uma correlação estatística.')
    print(200 * '=')

    # import matplotlib.pyplot as plt
    # criar um gráfico de dispersão
    plt.scatter(df_lesoes['lesao_corp_dolosa'], df_lesoes['lesao_corp_morte'])
    plt.title('Correlação entre lesão corporal dolosa e lesão corporal seguida de morte')
    plt.xlabel('lesao_corp_dolosa')
    plt.ylabel('lesao_corp_morte')

    # adicionar linha de grade
    plt.grid()
    plt.show()

except Exception as e:
    print(f'Erro ao calcular a correlação: {e}')
