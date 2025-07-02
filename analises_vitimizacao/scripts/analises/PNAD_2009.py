# %%
# =============================================================================
# CÉLULA 1: IMPORTAÇÕES E CONFIGURAÇÃO INICIAL
# =============================================================================

# --- Importação das Bibliotecas Essenciais ---
import shutil
import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import re
from PIL import Image
import squarify
from math import pi

print("Bibliotecas importadas com sucesso.")

# --- Definição dos Caminhos (Paths) ---
# Usando os caminhos especificados pelo usuário
output_dir = '../../analises/'
temp_img_dir = os.path.join(output_dir, 'temp_images/')

# --- Criação dos Diretórios de Saída ---
# Garante que as pastas para salvar o relatório e as imagens existam
os.makedirs(output_dir, exist_ok=True)
# Diretório de saída modificado
if not os.path.exists(temp_img_dir):
    os.makedirs(temp_img_dir)

print(f"Diretório de saída configurado em: {os.path.abspath(output_dir)}")
print(
    f"Diretório de imagens temporárias configurado em: {os.path.abspath(temp_img_dir)}")


# %%
# Função adaptada para ler os dados usando o arquivo de mapa
def carregar_dados_mapeados(caminhos_csv):
    """
    Carrega arquivos CSV que foram salvos com nomes de hash, utilizando um
    arquivo '_mapa_de_nomes.csv' para restaurar os nomes originais como chaves
    do dicionário.
    """
    dados = {}

    # Se a lista de caminhos estiver vazia, não faz nada
    if not caminhos_csv:
        print("[AVISO] Nenhuma arquivo CSV encontrado para carregar.")
        return dados

    # Pega o diretório da categoria a partir do primeiro arquivo da lista
    dir_categoria = os.path.dirname(caminhos_csv[0])
    caminho_mapa = os.path.join(dir_categoria, '_mapa_de_nomes.csv')

    # 1. Tenta carregar o arquivo de mapeamento
    try:
        print(f"\n--- Carregando dados da categoria em '{dir_categoria}' ---")
        mapa_df = pd.read_csv(caminho_mapa, sep=';', encoding='utf-8')
        print(
            f"[INFO] Arquivo de mapa '{caminho_mapa}' carregado com sucesso.")
    except FileNotFoundError:
        print(
            f"[ERRO] Arquivo de mapa '_mapa_de_nomes.csv' não encontrado em '{dir_categoria}'.")
        print("       Não é possível carregar os dados sem o mapa. Pulando esta categoria.")
        return dados
    except Exception as e:
        print(f"[ERRO] Falha ao ler o arquivo de mapa '{caminho_mapa}': {e}")
        return dados

    # 2. Itera sobre o mapa para carregar cada arquivo de dados
    for index, linha in mapa_df.iterrows():
        nome_original = linha['nome_original']
        nome_hash = linha['nome_arquivo_hash']

        caminho_dado = os.path.join(dir_categoria, f"{nome_hash}.csv")

        try:
            df = pd.read_csv(
                caminho_dado,
                sep=';',
                encoding='utf-8',
                header=0,
                index_col=0,
            )
            # Usa o NOME ORIGINAL como chave do dicionário
            dados[nome_original] = df
            print(f"  [OK] CSV para '{nome_original}' carregado com sucesso.")

        except FileNotFoundError:
            print(
                f"  [ERRO] Arquivo de dados '{caminho_dado}' não encontrado, mas listado no mapa.")
        except Exception as e:
            print(f"  [ERRO] Ao ler o arquivo de dados '{caminho_dado}': {e}")

    return dados

# --- SCRIPT PRINCIPAL DE CARREGAMENTO ---


# 1. Encontra todos os arquivos .csv como antes
caminho_pasta = '../../dados_tratados/PNAD_2009/csv'

agressao_paths = glob.glob(os.path.join(
    caminho_pasta, 'agressao/*.csv'), recursive=True)
furto_paths = glob.glob(os.path.join(
    caminho_pasta, 'furto/*.csv'), recursive=True)
roubo_paths = glob.glob(os.path.join(
    caminho_pasta, 'roubo/*.csv'), recursive=True)
roubofurto_paths = glob.glob(os.path.join(
    caminho_pasta, 'roubofurto/*.csv'), recursive=True)
seguranca_paths = glob.glob(os.path.join(
    caminho_pasta, 'seguranca/*.csv'), recursive=True)
tentativa_paths = glob.glob(os.path.join(
    caminho_pasta, 'tentativa/*.csv'), recursive=True)

# 2. Usa a NOVA função para carregar os dados
dados_carregados = {
    "agressao": carregar_dados_mapeados(agressao_paths),
    "furto": carregar_dados_mapeados(furto_paths),
    "roubo": carregar_dados_mapeados(roubo_paths),
    "roubofurto": carregar_dados_mapeados(roubofurto_paths),
    "seguranca": carregar_dados_mapeados(seguranca_paths),
    "tentativa": carregar_dados_mapeados(tentativa_paths)
}

print("\n\n[SUCESSO] Processo de carregamento de dados concluído.")

# 3. Verificação (opcional, mas recomendado)
# Vamos verificar as chaves carregadas para a categoria 'agressao'
print("\nVerificando as chaves (nomes dos DataFrames) carregadas para a categoria 'agressao':")
if dados_carregados['agressao']:
    print(list(dados_carregados['agressao'].keys()))
else:
    print("Nenhum dado carregado para 'agressao'.")

"""
Gere visualizações de dados a partir dos arquivos CSV anexados sobre violência (`agressao.xlsx - *.csv`).

Cada arquivo é uma tabela onde a primeira coluna é a categoria principal. Priorize a análise e criação de gráficos que explorem as relações entre:

- Tipos de **agressão** (física, psicológica, etc.).
- Comparações por **sexo** (colunas 'Homens' e 'Mulheres').
- Distribuição por **cor/raça** (colunas 'Branca', 'Preta', 'Parda', etc.).
- Recortes por **faixa etária** ou **ciclo de vida**.
- O **local da ocorrência** da agressão.

Crie gráficos de barras, de pizza e comparativos que revelem os padrões mais significativos nesses cruzamentos de dados.
"""

# %%
dados_carregados['agressao']['Coeficiente de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por sexo e cor ou raça, segundo algumas Unidades da Federação e Regiões Metropolitanas']

# %%
crime_categories = {
    # CATEGORIAS DE 'tentativa.xlsx' (Tentativa de roubo/furto)
    "tentativa": [
        {
            "nome_completo": "Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por classes de rendimento mensal domiciliar per capita, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Sem rendimento a menos de 1/4', '1/4 a menos de 1/2', '1/2 a menos de 1', '1 a menos de 2', '2 ou mais']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, por nível de instrução, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Sem instrução', 'Fundamental Incompleto ou Equivalente', 'Fundamental Completo ou Equivalente', 'Médio Incompleto ou Equivalente', 'Médio Completo ou Equivalente', 'Superior Incompleto ou Equivalente', 'Superior Completo ou Equivalente']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, por condição de atividade e de ocupação na semana de referência, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Economicamente Ativas', 'Condição de Ocupação (Ocupadas)', 'Condição de Ocupação (Desocupadas)', 'Não Economicamente Ativas']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade, ocupadas na semana de referência, que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, por posição na ocupação no trabalho principal, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "empregado com carteira", "empregado sem carteira", "conta própria", "empregador", "trabalhador familiar nao remunerado"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade, ocupadas na semana de referência, que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, por grupamentos de atividade do trabalho principal, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "agrícola", "indústria", "construção", "comércio e reparação", "serviços"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, por sexo e cor ou raça, segundo algumas Unidades da Federação e Regiões Metropolitanas",
            "colunas": ['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, por grupos de idade, segundo algumas Unidades da Federação e Regiões Metropolitanas",
            "colunas": ['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de tentativa de roubo ou furto, no período de referência de 365 dias, por classes de rendimento mensal domiciliar per capita, segundo algumas Unidades da Federação e Regiões Metropolitanas",
            "colunas": ['Total', 'Sem rendimento a menos de 1/4', '1/4 a menos de 1/2', '1/2 a menos de 1', '1 a menos de 2', '2 ou mais']
        }
    ],

    # CATEGORIAS DE 'agressao.xlsx' (Agressão física)
    "agressao": [
        {
            "nome_completo": "Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de agressão física, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio e as Grandes Regiões",
            "colunas": ['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por agressor na última agressão física, segundo a situação do domicílio e as Grandes Regiões",
            "colunas": ['Total', 'Pai ou mãe', 'Cônjuge ou ex-cônjuge', 'Outro parente', 'Conhecido', 'Desconhecido']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por local de ocorrência da última agressão física, segundo a situação do domicílio e as Grandes Regiões",
            "colunas": ['Total', 'Própria Residência', 'Via Pública', 'Outro']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por procura pela polícia em decorrência da última agressão física, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Realizaram', 'Não Realizaram']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que não procuraram a polícia em decorrência da última agressão física que foram vítimas, no período de referência de 365 dias, por motivo de não terem procurado a polícia em decorrência da última agressão física",
            "colunas": ["total", "falta de provas", "nao era importante", "nao acreditavam na policia", "nao queriam envolver a policia ou medo de represalias", "outro"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por nível de instrução, segundo a situação do domicílio e as Grandes Regiões",
            "colunas": ["total", "fundamental incompleto ou equivalente", "fundamental completo ou equivalente", "médio incompleto ou equivalente", "médio completo ou equivalente", "superior incompleto ou equivalente", "superior completo ou equivalente"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por condição de atividade e de ocupação na semana de referência, segundo a situação do domicílio e as Grandes Regiões",
            "colunas": ["total", "economicamente ativas", "condição de ocupação na semana de referência(ocupadas)", "condição de ocupação na semana de referência(desocupadascupadas)", "nao economicamente ativas"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade, ocupadas na semana de referência, que foram vítimas de agressão física, no período de referência de 365 dias, por posição na ocupação no trabalho principal, segundo a situação do domicílio e as Grandes Regiões",
            "colunas": ["total", "empregado com carteira", "empregado sem carteira", "conta própria", "empregador", "trabalhador familiar nao remunerado"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por sexo e cor ou raça, segundo algumas Unidades da Federação e Regiões Metropolitanas",
            "colunas": ["total", "homens", "mulheres", "branca", "preta/parda"]
        }
    ],

    # CATEGORIAS DE 'furto.xlsx' (Furto)
    "furto": [
        {
            "nome_completo": "Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de furto, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de furto, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de furto, no período de referência de 365 dias, por tipo de bem furtado no último furto, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Dinheiro, Cartão, Cheque', 'Celular', 'Bolsa/Carteira', 'Veículo', 'Outro']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de furto, no período de referência de 365 dias, por local de ocorrência do último furto, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Própria Residência', 'Via Pública', 'Outro']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de furto, no período de referência de 365 dias, por procura pela polícia em decorrência do último furto, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Realizaram', 'Não Realizaram']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que não procuraram a polícia em decorrência do último furto que foram vítimas, no período de referência de 365 dias, por motivo de não terem procurado a polícia em decorrência do último furto, segundo a situação do domicílio",
            "colunas": ["total", "falta de provas", "nao era importante", "nao acreditavam na policia", "nao queriam envolver a policia ou medo de represalias", "outro"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de furto, no período de referência de 365 dias, por nível de instrução, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Sem instrução', 'Fundamental Incompleto ou Equivalente', 'Fundamental Completo ou Equivalente', 'Médio Incompleto ou Equivalente', 'Médio Completo ou Equivalente', 'Superior Incompleto ou Equivalente', 'Superior Completo ou Equivalente']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de furto, no período de referência de 365 dias, por condição de atividade e de ocupação na semana de referência, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Economicamente Ativas', 'Condição de Ocupação (Ocupadas)', 'Condição de Ocupação (Desocupadas)', 'Não Economicamente Ativas']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade, ocupadas na semana de referência, que foram vítimas de furto, no período de referência de 365 dias, por posição na ocupação no trabalho principal, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "empregado com carteira", "empregado sem carteira", "conta própria", "empregador", "trabalhador familiar nao remunerado"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de furto, no período de referência de 365 dias, por sexo e cor ou raça, segundo algumas Unidades da Federação e Regiões Metropolitanas",
            "colunas": ["total", "homens", "mulheres", "branca", "preta/parda"]
        }
    ],

    # CATEGORIAS DE 'roubo.xlsx' (Roubo)
    "roubo": [
        {
            "nome_completo": "Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de roubo, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo, no período de referência de 365 dias, por tipo de bem roubado no último roubo, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "celular", "dinheiro", "bolsa/carteira", "joias/relógios", "veículo", "outro"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo, no período de referência de 365 dias, por local de ocorrência do último roubo, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "propria residencia", "via publica", "outro"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo, no período de referência de 365 dias, por procura pela polícia em decorrência do último roubo, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "realizaram", "nao realizaram"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que não procuraram a polícia em decorrência do último roubo que foram vítimas, no período de referência de 365 dias, por motivo de não terem procurado a polícia em decorrência do último roubo, segundo a situação do domicílio",
            "colunas": ["total", "falta de provas", "nao era importante", "nao acreditavam na policia", "nao queriam envolver a policia ou medo de represalias", "outro"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo, no período de referência de 365 dias, por nível de instrução, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "fundamental incompleto ou equivalente", "fundamental completo ou equivalente", "médio incompleto ou equivalente", "médio completo ou equivalente", "superior incompleto ou equivalente", "superior completo ou equivalente"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo, no período de referência de 365 dias, por condição de atividade e de ocupação na semana de referência, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "economicamente ativas", "condição de ocupação na semana de referência(ocupadas)", "condição de ocupação na semana de referência(desocupadascupadas)", "nao economicamente ativas"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade, ocupadas na semana de referência, que foram vítimas de roubo, no período de referência de 365 dias, por posição na ocupação no trabalho principal, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "empregado com carteira", "empregado sem carteira", "conta própria", "empregador", "trabalhador familiar nao remunerado"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo, no período de referência de 365 dias, por sexo e cor ou raça, segundo algumas Unidades da Federação e Regiões Metropolitanas",
            "colunas": ["total", "homens", "mulheres", "branca", "preta/parda"]
        }
    ],

    # CATEGORIAS DE 'roubofurto.xlsx' (Roubo ou Furto)
    "roubofurto": [
        {
            "nome_completo": "Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de roubo ou furto, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo ou furto, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo ou furto, no período de referência de 365 dias, por classes de rendimento mensal domiciliar per capita, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Sem rendimento a menos de 1/4', '1/4 a menos de 1/2', '1/2 a menos de 1', '1 a menos de 2', '2 ou mais']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo ou furto, no período de referência de 365 dias, por nível de instrução, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Sem instrução', 'Fundamental Incompleto ou Equivalente', 'Fundamental Completo ou Equivalente', 'Médio Incompleto ou Equivalente', 'Médio Completo ou Equivalente', 'Superior Incompleto ou Equivalente', 'Superior Completo ou Equivalente']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo ou furto, no período de referência de 365 dias, por condição de atividade e de ocupação na semana de referência, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Economicamente Ativas', 'Condição de Ocupação (Ocupadas)', 'Condição de Ocupação (Desocupadas)', 'Não Economicamente Ativas']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade, ocupadas na semana de referência, que foram vítimas de roubo ou furto, no período de referência de 365 dias, por posição na ocupação no trabalho principal, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "empregado com carteira", "empregado sem carteira", "conta própria", "empregador", "trabalhador familiar nao remunerado"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade, ocupadas na semana de referência, que foram vítimas de roubo ou furto, no período de referência de 365 dias, por grupamentos de atividade do trabalho principal, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "agrícola", "indústria", "construção", "comércio e reparação", "serviços"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo ou furto, no período de referência de 365 dias, por sexo e cor ou raça, segundo algumas Unidades da Federação e Regiões Metropolitanas",
            "colunas": ['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo ou furto, no período de referência de 365 dias, por grupos de idade, segundo algumas Unidades da Federação e Regiões Metropolitanas",
            "colunas": ['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo ou furto, no período de referência de 365 dias, por classes de rendimento mensal domiciliar per capita, segundo algumas Unidades da Federação e Regiões Metropolitanas",
            "colunas": ['Total', 'Sem rendimento a menos de 1/4', '1/4 a menos de 1/2', '1/2 a menos de 1', '1 a menos de 2', '2 ou mais']
        }
    ],
    # NOVA CATEGORIA DE 'seguranca.xlsx' (Percepção de Segurança, Medo, etc.)
    "segurança": [
        {
            "nome_completo": "Coeficientes de variação das estimativas de percentual de pessoas que se sentem seguras em seu domicílio, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda', 'Preta', 'Parda']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que se sentem seguras no seu bairro, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação.",
            "colunas": ['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda', 'Preta', 'Parda']
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que sentem medo de andar sozinhas à noite em sua área, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "10 a 15 anos", "16 a 24 anos", "25 a 34 anos", "35 a 49 anos", "50 a 59 anos(ou mais)", "60 a 69 anos", "70 anos ou mais"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que consideram a polícia confiável, no período de referência de 365 dias, por nível de instrução, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "fundamental incompleto ou equivalente", "fundamental completo ou equivalente", "médio incompleto ou equivalente", "médio completo ou equivalente", "superior incompleto ou equivalente", "superior completo ou equivalente"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de percentual de domicílios que sofreram arrombamento ou tentativa de arrombamento, no período de referência de 365 dias, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "rural", "urbana", "capital", "região metropolitana", "outros municípios"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de crimes (qualquer tipo) e não reportaram à polícia, no período de referência de 365 dias, por motivo de não terem reportado, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "falta de provas", "nao era importante", "nao acreditavam na policia", "nao queriam envolver a policia ou medo de represalias", "outro"]
        },
        {
            "nome_completo": "Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que mudaram hábitos por medo da violência, no período de referência de 365 dias, por tipo de mudança de hábito, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação",
            "colunas": ["total", "evitar sair a noite", "evitar certos locais", "nao usar joias/celular na rua", "nao reagir a assaltos", "outro"]
        }
    ]
}

# %%
# --- ETAPA 1: CONFIGURAÇÃO E GERAÇÃO DOS GRÁFICOS ---

print("\n--- Iniciando geração sequencial de gráficos ---")

# Criando uma pasta para salvar os gráficos.
output_folder = 'graficos'
os.makedirs(output_folder, exist_ok=True)
print(f"Pasta '{output_folder}' pronta para receber os gráficos.")

# Dicionário para simular os dados carregados
dados_carregados = {
    'agressao': {
        'Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação': pd.DataFrame(np.random.rand(10, 5) * 20, columns=['total', 'homens', 'mulheres', 'branca', 'preta/parda']),
        'Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio e as Grandes Regiões': pd.DataFrame(np.random.rand(10, 6) * 20, columns=['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']),
        'Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que não procuraram a polícia em decorrência da última agressão física que foram vítimas, no período de referência de 365 dias, por motivo de não terem procurado a polícia em decorrência da última agressão física, segundo algumas Unidades da Federação e Regiões Metropolitanas': pd.DataFrame(np.random.rand(10, 6), columns=['total', 'falta de provas', 'nao era importante', 'nao acreditavam na policia', 'nao queriam envolver a policia ou medo de represalias', 'outro'])
    },
    'furto': {
        'Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de furto, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação': pd.DataFrame(np.random.rand(10, 5) * 20, columns=['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda']),
        'Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de furto, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação': pd.DataFrame(np.random.rand(10, 6) * 20, columns=['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']),
        'Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que não procuraram a polícia em decorrência do último furto que foram vítimas, no período de referência de 365 dias, por motivo de não terem procurado a polícia em decorrência do último furto, segundo a situação do domicílio,': pd.DataFrame(np.random.rand(10, 6), columns=['total', 'falta de provas', 'nao era importante', 'nao acreditavam na policia', 'nao queriam envolver a policia ou medo de represalias', 'outro'])
    },
    'roubo': {
        'Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de roubo, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação': pd.DataFrame(np.random.rand(10, 5) * 20, columns=['Total', 'Homens', 'Mulheres', 'Branca', 'Preta/Parda']),
        'Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação': pd.DataFrame(np.random.rand(10, 6) * 20, columns=['Total', '10 a 15 anos', '16 a 24 anos', '25 a 34 anos', '35 a 49 anos', '50 a 59 anos (ou mais)']),
        'Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que não procuraram a polícia em decorrência do último roubo que foram vítimas, no período de referência de 365 dias, por motivo de não terem procurado a polícia em decorrência do último roubo, segundo a situação do domicílio, as': pd.DataFrame(np.random.rand(10, 6), columns=['total', 'falta de provas', 'nao era importante', 'nao acreditavam na policia', 'nao queriam envolver a policia ou medo de represalias', 'outro'])
    }
}

# Configurações de estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 12

# Dicionário para guardar os caminhos das imagens geradas
image_paths = {}

# --- GRÁFICO 1: PERFIL DEMOGRÁFICO ---
print("Gerando Gráfico 1...")
planilhas_demo = {
    'Agressão': dados_carregados['agressao']['Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação'],
    'Furto': dados_carregados['furto']['Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de furto, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação'],
    'Roubo': dados_carregados['roubo']['Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de roubo, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação']
}
dados_grafico_demo = {}
for crime, df in planilhas_demo.items():
    df.columns = [c.strip().lower() for c in df.columns]
    dados_grafico_demo[crime] = df[[
        'homens', 'mulheres', 'branca', 'preta/parda']].mean()
df_demo_comp = pd.DataFrame(dados_grafico_demo)
df_demo_comp.plot(kind='bar', figsize=(14, 8), colormap='viridis')
plt.title(
    'Perfil Demográfico da Vítima por Tipo de Crime\n(Coeficiente de Variação Médio)')
plt.ylabel('Coeficiente de Variação Médio')
plt.xlabel('Perfil Demográfico')
plt.xticks(rotation=0)
plt.legend(title='Tipo de Crime')
plt.tight_layout()
image_paths['g1'] = os.path.join(output_folder, '01_perfil_demografico.png')
plt.savefig(image_paths['g1'], bbox_inches='tight')
plt.close()

# --- GRÁFICO 2: PERFIL ETÁRIO ---
print("Gerando Gráfico 2...")
planilhas_idade = {
    'Agressão': dados_carregados['agressao']['Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio e as Grandes Regiões'],
    'Furto': dados_carregados['furto']['Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de furto, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação'],
    'Roubo': dados_carregados['roubo']['Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de roubo, no período de referência de 365 dias, por grupos de idade, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação']
}
dados_grafico_idade = {}
for crime, df in planilhas_idade.items():
    df_sem_total = df.drop(
        columns=[col for col in df.columns if 'total' in col.lower()])
    dados_grafico_idade[crime] = df_sem_total.mean()
df_idade_comp = pd.DataFrame(dados_grafico_idade)
df_idade_comp.plot(kind='line', style='-o', ms=8, figsize=(14, 8))
plt.title(
    'Perfil Etário da Vítima por Tipo de Crime\n(Coeficiente de Variação Médio)')
plt.ylabel('Coeficiente de Variação Médio')
plt.xlabel('Faixa Etária')
plt.xticks(rotation=45, ha='right')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(title='Tipo de Crime')
plt.tight_layout()
image_paths['g2'] = os.path.join(output_folder, '02_perfil_etario.png')
plt.savefig(image_paths['g2'], bbox_inches='tight')
plt.close()

# --- GRÁFICO 3: MOTIVOS NÃO REGISTRO ---
print("Gerando Gráfico 3...")
planilhas_motivos = {
    'Agressão': dados_carregados['agressao'].get('Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que não procuraram a polícia em decorrência da última agressão física que foram vítimas, no período de referência de 365 dias, por motivo de não terem procurado a polícia em decorrência da última agressão física, segundo algumas Unidades da Federação e Regiões Metropolitanas'),
    'Furto': dados_carregados['furto'].get('Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que não procuraram a polícia em decorrência do último furto que foram vítimas, no período de referência de 365 dias, por motivo de não terem procurado a polícia em decorrência do último furto, segundo a situação do domicílio,'),
    'Roubo': dados_carregados['roubo'].get('Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que não procuraram a polícia em decorrência do último roubo que foram vítimas, no período de referência de 365 dias, por motivo de não terem procurado a polícia em decorrência do último roubo, segundo a situação do domicílio, as')
}
dados_grafico_motivos = {}
for crime, df in planilhas_motivos.items():
    if df is not None:
        df_limp = df.drop(
            columns=[col for col in df.columns if 'total' in col.lower()])
        dados_grafico_motivos[crime] = df_limp.mean(numeric_only=True)
df_motivos = pd.DataFrame(dados_grafico_motivos).T
df_motivos_100 = df_motivos.div(df_motivos.sum(axis=1), axis=0) * 100
if not df_motivos_100.empty:
    df_motivos_100 = df_motivos_100.sort_values(
        by=list(df_motivos_100.columns), ascending=False)
fig, ax = plt.subplots(figsize=(14, 7))
cmap = plt.get_cmap('tab20c')
colors = cmap.colors[:df_motivos_100.shape[1]]
df_motivos_100.plot(kind='barh', stacked=True, ax=ax,
                    color=colors, edgecolor='black')
ax.set_title('Motivos para Não Registrar Ocorrência (%) por Tipo de Crime',
             fontsize=16, weight='bold')
ax.set_xlabel('Percentual (%)', fontsize=12)
ax.set_ylabel('Tipo de Crime', fontsize=12)
ax.set_xlim(0, 100)
ax.legend(title='Motivo', bbox_to_anchor=(
    1.02, 1), loc='upper left', fontsize=10)
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center',
                 fontsize=9, color='white', weight='bold')
plt.tight_layout()
image_paths['g3'] = os.path.join(output_folder, '03_motivos_nao_registro.png')
plt.savefig(image_paths['g3'], bbox_inches='tight')
plt.close()

# --- GRÁFICO 4: HEATMAP COMPARATIVO ---
print("Gerando Gráfico 4...")
df_heatmap = df_demo_comp.T
plt.figure(figsize=(10, 6))
sns.heatmap(df_heatmap, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=.5)
plt.title('Heatmap Comparativo por Perfil Demográfico e Crime')
plt.xlabel('Perfil Demográfico')
plt.ylabel('Tipo de Crime')
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()
image_paths['g4'] = os.path.join(output_folder, '04_heatmap_comparativo.png')
plt.savefig(image_paths['g4'], bbox_inches='tight')
plt.close()

# --- GRÁFICO 5: HEATMAP CORRELAÇÃO ---
print("Gerando Gráfico 5...")
df_agressao_demo = dados_carregados['agressao']['Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação']
df_agressao_demo.columns = [c.strip().lower()
                            for c in df_agressao_demo.columns]
df_agressao_demo = df_agressao_demo.drop(columns=['total'])
corr_matrix = df_agressao_demo.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=1)
plt.title('Matriz de Correlação entre Perfis de Vítimas de Agressão')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
image_paths['g5'] = os.path.join(
    output_folder, '05_heatmap_correlacao_agressao.png')
plt.savefig(image_paths['g5'], bbox_inches='tight')
plt.close()

# --- GRÁFICO 6: BOXPLOT ---
print("Gerando Gráfico 6...")
df_agressao = dados_carregados['agressao']['Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação']
df_agressao.columns = [c.strip().lower() for c in df_agressao.columns]
df_furto = dados_carregados['furto']['Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de furto, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação']
df_furto.columns = [c.strip().lower() for c in df_furto.columns]
df_roubo = dados_carregados['roubo']['Coeficientes de variação das estimativas de percentual de pessoas que foram vítimas de roubo, no período de referência de 365 dias, na população de 10 anos ou mais de idade, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação']
df_roubo.columns = [c.strip().lower() for c in df_roubo.columns]
dados_dist = {
    'Agressão': df_agressao['total'],
    'Furto': df_furto['total'],
    'Roubo': df_roubo['total']
}
df_dist = pd.DataFrame(dados_dist)
plt.figure(figsize=(10, 7))
sns.boxplot(data=df_dist, palette='viridis')
sns.stripplot(data=df_dist, color=".25", size=5)
plt.title('Distribuição do Coeficiente de Variação Total por Tipo de Crime')
plt.ylabel('Coeficiente de Variação')
plt.xlabel('Tipo de Crime')
plt.tight_layout()
image_paths['g6'] = os.path.join(output_folder, '06_boxplot_distribuicao.png')
plt.savefig(image_paths['g6'], bbox_inches='tight')
plt.close()

# --- GRÁFICO 7: RADAR ---
print("Gerando Gráfico 7...")
categories = df_demo_comp.index.tolist()
N = len(categories)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.set_rlabel_position(30)
plt.yticks([5, 10, 15, 20], color="grey", size=10)
plt.ylim(0, df_demo_comp.max().max() + 5)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, crime in enumerate(df_demo_comp.columns):
    values = df_demo_comp[crime].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid',
            label=crime, color=colors[i])
    ax.fill(angles, values, alpha=0.1, color=colors[i])
plt.title('Comparativo de Perfis de Vítimas por Crime (Radar)', size=16, y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.tight_layout()
image_paths['g7'] = os.path.join(output_folder, '07_radar_comparativo.png')
plt.savefig(image_paths['g7'], bbox_inches='tight')
plt.close()

# --- GRÁFICO 8: RANKING ---
print("Gerando Gráfico 8...")
ranking = df_demo_comp.mean(axis=1).sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=ranking.values, y=ranking.index, palette='rocket', orient='h')
plt.title('Ranking de Perfis por Coeficiente de Variação Médio (Todos os Crimes)')
plt.xlabel('Coeficiente de Variação Médio Agregado')
plt.ylabel('Perfil Demográfico')
for index, value in enumerate(ranking):
    plt.text(value, index, f' {value:.2f}', va='center')
plt.tight_layout()
image_paths['g8'] = os.path.join(output_folder, '08_ranking_agregado.png')
plt.savefig(image_paths['g8'], bbox_inches='tight')
plt.close()

# --- GRÁFICO 9: DUMBBELL ---
print("Gerando Gráfico 9...")
df_dumbbell = df_demo_comp.loc[[
    'homens', 'mulheres']].T.sort_values(by='homens')
fig, ax = plt.subplots(figsize=(10, 6))
ax.hlines(y=df_dumbbell.index, xmin=df_dumbbell['homens'],
          xmax=df_dumbbell['mulheres'], color='gray', alpha=0.7, lw=2)
ax.scatter(df_dumbbell['homens'], df_dumbbell.index,
           color='#1f77b4', s=100, label='Homens')
ax.scatter(df_dumbbell['mulheres'], df_dumbbell.index,
           color='#ff7f0e', s=100, label='Mulheres')
ax.set_title('Comparativo do Coeficiente de Variação: Homens vs. Mulheres')
ax.set_xlabel('Coeficiente de Variação Médio')
ax.set_ylabel('Tipo de Crime')
ax.legend()
plt.tight_layout()
image_paths['g9'] = os.path.join(
    output_folder, '09_dumbbell_homens_mulheres.png')
plt.savefig(image_paths['g9'], bbox_inches='tight')
plt.close()

# --- GRÁFICO 10: FACET GRID ---
print("Gerando Gráfico 10...")
df_agressao_geo = dados_carregados['agressao']['Coeficientes de variação das estimativas de pessoas de 10 anos ou mais de idade que foram vítimas de agressão física, no período de referência de 365 dias, por sexo e cor ou raça, segundo a situação do domicílio, as Grandes Regiões e as Unidades da Federação']
df_agressao_geo.columns = [c.strip().lower() for c in df_agressao_geo.columns]
df_agressao_geo = df_agressao_geo.drop(columns=['total'])
df_agressao_geo['UF'] = [f'UF_{i+1}' for i in range(len(df_agressao_geo))]
df_tidy = df_agressao_geo.melt(
    id_vars='UF', var_name='Perfil', value_name='Coeficiente')
g = sns.FacetGrid(df_tidy, col="UF", col_wrap=4, height=3, sharey=False)
g.map(sns.barplot, "Perfil", "Coeficiente", palette='plasma',
      order=['homens', 'mulheres', 'branca', 'preta/parda'])
g.fig.suptitle('Perfil de Vítimas de Agressão por UF', y=1.03, fontsize=16)
g.set_axis_labels("Perfil Demográfico", "Coeficiente de Variação")
g.set_titles("UF: {col_name}")
for ax in g.axes.flatten():
    for label in ax.get_xticklabels():
        label.set_rotation(45)
g.fig.tight_layout()
image_paths['g10'] = os.path.join(
    output_folder, '10_facetgrid_agressao_uf.png')
g.savefig(image_paths['g10'])
plt.close()

print("\n--- Análise concluída e todos os gráficos foram salvos na pasta 'graficos' ---")


# %%
# --- ETAPA 2: PREPARAÇÃO DOS TEXTOS PARA O PDF ---

analises = {
    "Gráfico 1: Perfil Demográfico (Barras Agrupadas)": {
        "objetivo": "Comparar a variabilidade (inconstância) das estimativas de vitimização entre diferentes perfis demográficos (sexo e cor/raça) para cada tipo de crime principal (Agressão, Furto, Roubo).",
        "o_que_mostra": "O gráfico exibe barras agrupadas para cada perfil demográfico. A altura de cada barra representa o Coeficiente de Variação (CV) médio, onde barras mais altas indicam uma maior instabilidade e dispersão nos dados de vitimização para aquele grupo. As cores distinguem os tipos de crime, permitindo uma comparação direta dentro de cada perfil.",
        "imagem": image_paths.get('g1')
    },
    "Gráfico 2: Perfil por Faixa Etária (Linhas Múltiplas)": {
        "objetivo": "Analisar como a variabilidade das estimativas de vitimização se comporta através das diferentes faixas etárias para cada tipo de crime.",
        "o_que_mostra": "O gráfico apresenta a tendência da variabilidade (CV médio) ao longo de várias faixas etárias. Cada linha colorida corresponde a um tipo de crime. Um ponto mais alto na linha significa maior variabilidade da estimativa para aquela faixa etária específica. A trajetória da linha mostra se a instabilidade dos dados aumenta, diminui ou flutua com a idade.",
        "imagem": image_paths.get('g2')
    },
    "Gráfico 3: Motivos para Não Registrar Ocorrência (Barras Empilhadas)": {
        "objetivo": "Revelar e comparar a distribuição percentual dos motivos que levaram as vítimas a não procurarem a polícia, fazendo uma distinção por tipo de crime.",
        "o_que_mostra": "Cada barra horizontal representa um tipo de crime e corresponde a 100% dos motivos. Os segmentos coloridos dentro de cada barra mostram a proporção de cada motivo específico (ex: 'falta de provas', 'não acreditavam na polícia'). O tamanho de cada segmento indica sua importância relativa para aquele crime.",
        "imagem": image_paths.get('g3')
    },
    "Gráfico 4: Heatmap Comparativo do Perfil Demográfico": {
        "objetivo": "Fornecer uma visualização rápida e condensada da intensidade da variabilidade dos dados para cada combinação de tipo de crime e perfil demográfico.",
        "o_que_mostra": "O gráfico é uma matriz onde as linhas são os tipos de crime e as colunas são os perfis demográficos. A cor de cada célula indica a magnitude do Coeficiente de Variação (CV), com cores mais intensas significando maior variabilidade. O valor numérico exato do CV está anotado dentro da célula, permitindo uma leitura precisa.",
        "imagem": image_paths.get('g4')
    },
    "Gráfico 5: Heatmap de Correlação (Crime de Agressão)": {
        "objetivo": "Investigar se a variabilidade nas estimativas de vitimização por agressão dos diferentes perfis demográficos se movem em conjunto, ou seja, se existe uma relação entre elas.",
        "o_que_mostra": "A matriz exibe o coeficiente de correlação (de -1 a 1) entre os CVs de todos os pares de perfis. Cores quentes (próximas de 1) indicam que, quando a variabilidade de um grupo é alta numa região, a do outro grupo também tende a ser alta (correlação positiva). Cores frias (próximas de -1) indicariam uma relação inversa.",
        "imagem": image_paths.get('g5')
    },
    "Gráfico 6: Distribuição com Boxplot": {
        "objetivo": "Comparar a distribuição completa (mediana, quartis, dispersão e outliers) do Coeficiente de Variação 'Total' entre os diferentes tipos de crime, indo além da simples média.",
        "o_que_mostra": "Cada 'caixa' (boxplot) representa um tipo de crime. A linha central na caixa é a mediana do CV. A altura da caixa mostra a dispersão dos 50% centrais dos dados. As hastes indicam o alcance geral dos dados, e pontos isolados representam 'outliers' (regiões com variabilidade excepcionalmente alta ou baixa).",
        "imagem": image_paths.get('g6')
    },
    "Gráfico 7: Gráfico de Radar Comparativo": {
        "objetivo": "Comparar o 'formato' geral do perfil de variabilidade entre os diferentes crimes de forma simultânea e multidimensional.",
        "o_que_mostra": "Cada um dos eixos que partem do centro representa um perfil demográfico. Um polígono colorido é desenhado para cada tipo de crime. A distância do ponto central ao longo de um eixo indica o quão alto é o CV para aquele perfil. O formato do polígono revela visualmente quais perfis têm maior ou menor variabilidade para cada crime.",
        "imagem": image_paths.get('g7')
    },
    "Gráfico 8: Ranking Agregado de Perfis de Vítimas": {
        "objetivo": "Classificar os perfis demográficos com base na sua variabilidade de dados média, agregando os resultados de todos os tipos de crime para criar um ranking geral.",
        "o_que_mostra": "Um gráfico de barras horizontais simples onde a barra mais longa pertence ao perfil demográfico cuja estimativa de vitimização é, na média geral, a mais instável e inconsistente entre as regiões pesquisadas.",
        "imagem": image_paths.get('g8')
    },
    "Gráfico 9: Comparativo Homens vs. Mulheres (Dumbbell Plot)": {
        "objetivo": "Isolar e comparar diretamente a diferença na variabilidade das estimativas entre homens e mulheres para cada tipo de crime.",
        "o_que_mostra": "Para cada tipo de crime (no eixo vertical), dois pontos são plotados: um para o CV de homens e outro para o de mulheres. Uma linha conecta os dois pontos, e o comprimento dessa linha destaca visualmente a magnitude da diferença (o 'gap') entre os sexos para aquele crime específico.",
        "imagem": image_paths.get('g9')
    },
    "Gráfico 10: Variação Geográfica (Facet Grid)": {
        "objetivo": "Desagregar a análise nacional para investigar como o perfil de variabilidade das vítimas de agressão se comporta em cada Unidade da Federação (UF) individualmente.",
        "o_que_mostra": "O gráfico é uma grade de múltiplos mini-gráficos de barras. Cada mini-gráfico representa uma UF, mostrando os CVs para cada perfil demográfico ('homens', 'mulheres', 'branca', 'preta/parda') naquela localidade específica. Isso permite comparar os padrões locais com a média nacional.",
        "imagem": image_paths.get('g10')
    }
}

analise_geral = {
    "titulo": "Análise Geral Consolidada",
    "texto": (
        "A análise dos dez gráficos revela uma narrativa multifacetada sobre a estabilidade e consistência das estimativas de vitimização no Brasil. O Coeficiente de Variação (CV), métrica central deste estudo, indica o grau de imprecisão dos dados, sendo um indicador crucial para a confiabilidade das estatísticas de criminalidade.\n\n"
        "Observa-se que a variabilidade não é uniforme. Perfis demográficos específicos, como o da população 'preta/parda', apresentam consistentemente CVs mais elevados (Gráfico 1, 4 e 8), sugerindo que as estimativas de vitimização para este grupo são mais instáveis e variam mais significativamente entre as diferentes regiões do país. Da mesma forma, faixas etárias mais jovens, como a de '16 a 24 anos', tendem a mostrar picos de variabilidade, especialmente para crimes como Roubo (Gráfico 2).\n\n"
        "A desconfiança nas instituições e a percepção da gravidade do crime são fatores determinantes na subnotificação. O Gráfico 3 mostra que motivos como 'não acreditavam na polícia' e 'medo de represálias' são relevantes, especialmente em crimes como agressão, enquanto a percepção de 'não era importante' predomina em furtos. A análise de distribuição (Gráfico 6) e geográfica (Gráfico 10) reforça que a variabilidade não é apenas uma questão de perfil, mas também de localidade, com certas UFs exibindo dispersão de dados muito maior que outras.\n\n"
        "Em suma, os dados não são homogêneos. A confiabilidade das estimativas de vitimização depende fortemente do perfil da vítima (raça, sexo, idade), do tipo de crime e da localidade. Qualquer análise sobre os números da criminalidade deve, portanto, levar em conta essa variabilidade para evitar conclusões simplistas e direcionar políticas de segurança pública e de coleta de dados de forma mais eficaz."
    )
}


# --- ETAPA 3: GERAÇÃO DO PDF CORRIGIDO ---

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, 'Relatório de Análise de Criminalidade', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 10, title, ln=1, align='L')
        self.ln(2)

    def chapter_body(self, body_dict):
        # Objetivo
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 6, "Objetivo:", ln=1)  # Usar cell com ln=1 para o título
        self.set_font('Helvetica', '', 12)
        self.multi_cell(0, 6, body_dict['objetivo'])
        self.ln(2)

        # O que mostra
        self.set_font('Helvetica', 'B', 12)
        # Usar cell com ln=1 para o título
        self.cell(0, 6, 'O que o Gráfico Mostra:', ln=1)
        self.set_font('Helvetica', '', 12)
        self.multi_cell(0, 6, body_dict['o_que_mostra'])
        self.ln(4)

        # Imagem
        if body_dict.get('imagem') and os.path.exists(body_dict['imagem']):
            # Largura da página A4 em mm, menos as margens (padrão 10mm de cada lado)
            page_width = self.w - 2 * self.l_margin
            self.image(body_dict['imagem'], x=self.l_margin, w=page_width)
        else:
            self.set_font('Helvetica', 'I', 12)
            self.cell(0, 10, "[Imagem não encontrada]", ln=1)


# Criação do PDF
pdf = PDF('P', 'mm', 'A4')

# Adiciona as análises e gráficos
for titulo, conteudo in analises.items():
    pdf.add_page()
    pdf.chapter_title(titulo)
    pdf.chapter_body(conteudo)

# Adiciona a análise geral em uma nova página
pdf.add_page()
pdf.chapter_title(analise_geral['titulo'])
pdf.set_font('Helvetica', '', 12)
pdf.multi_cell(0, 6, analise_geral['texto'])

# Salva o PDF
pdf.output(os.path.join(output_dir, 'relatorio_pnad_2009.pdf'))

print(f"\nPDF final gerado com sucesso e salvo em: {output_dir}")

# %%

# Nome da pasta que você deseja deletar
folder_to_delete = 'graficos'

# Verifica se a pasta realmente existe
if os.path.exists(folder_to_delete):
    try:
        # Usa shutil.rmtree() para remover a pasta e todo o seu conteúdo
        shutil.rmtree(folder_to_delete)
        print(
            f"A pasta '{folder_to_delete}' e todo o seu conteúdo foram deletados com sucesso.")
    except OSError as e:
        print(f"Erro ao deletar a pasta '{folder_to_delete}': {e}")
else:
    print(
        f"A pasta '{folder_to_delete}' não foi encontrada. Nenhuma ação foi tomada.")
