# Correlação de Pearson

# Utilizando os dados abertos da segurança pública https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv
# importar bibliotecas os   
import os
# importar bibliotecas pandas, numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# limpeza do terminal
os.system('cls' if os.name == 'nt' else 'clear')

# criando a constante do endereço digital
ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Obter os dados
try:
    print('Obtendo os dados...')

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # print(df_ocorrencias.head(10))

    # Delimitando as variaveis
    df_veiculos = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]
    # print(df_veiculos.head(10))

    # Agrupar por cisp e somar quantidade de roubo_veiculo e recupera_veiculos
    df_veiculos = df_veiculos.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()
    # print(df_veiculos.head(10))

    # Ordenando os dados pela recuperacao de veiculos
    # df_veiculos = df_veiculos.sort_values(by='recuperacao_veiculos', ascending=False)
    # print(df_veiculos.head(10))

    print('Dados obtidos com sucesso!')
    
except Exception as e:
    print(f'Erro ao ler o arquivo: {e}')

# Calculando a Correlação entre roubo de veiculos e as recuperações de veiculos
try:
    print('\nCalculando a correlação entre roubos e recuperações de veículos...')

    # Calcular a correlação
    correlacao = np.corrcoef(df_veiculos['roubo_veiculo'], df_veiculos['recuperacao_veiculos'])[0, 1]

    print(f'correlação entre roubo e recuperação: {correlacao}')

    # import matplotlib.pyplot as plt
    # criar um gráfico de dispersão
    plt.scatter(df_veiculos['roubo_veiculo'], df_veiculos['recuperacao_veiculos'])
    plt.title('Correlação entre roubos e recuperações de veículos')
    plt.xlabel('Roubos de veículos')
    plt.ylabel('Recuperações de veículos')
    # adicionar linha de grade
    plt.grid()
    plt.show()

except Exception as e:
    print(f'Erro ao calcular a correlação: {e}')