#pip install tabula-py PyMuPDF openpyxl seaborn

# Importações
import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns

from openpyxl import load_workbook
from IPython.display import display

# Configurações de exibição
plt.style.use('ggplot')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Função: Carregamento de dados CSV/XLSX
def carregar_dados(caminho_pasta):
    arquivos_csv = glob.glob(os.path.join(caminho_pasta, '**/csv/*.csv'), recursive=True)
    arquivos_xls = glob.glob(os.path.join(caminho_pasta, '**/tabelas/*.xls*'), recursive=True)
    dados = {}

    for arquivo in arquivos_csv:
        try:
            nome = os.path.basename(arquivo).replace('.csv', '')
            dados[nome] = pd.read_csv(arquivo, encoding='latin1', sep=';', decimal=',')
            print(f"[OK] CSV {nome}")
        except Exception as e:
            print(f"[ERRO] CSV {arquivo}: {e}")

    for arquivo in arquivos_xls:
        try:
            nome = os.path.basename(arquivo).replace('.xlsx', '').replace('.xls', '')
            xls = pd.ExcelFile(arquivo)
            for sheet_name in xls.sheet_names:
                df_nome = f"{nome}_{sheet_name}" if len(xls.sheet_names) > 1 else nome
                dados[df_nome] = pd.read_excel(arquivo, sheet_name=sheet_name)
                print(f"[OK] Excel {df_nome}")
        except Exception as e:
            print(f"[ERRO] Excel {arquivo}: {e}")

    return dados

# Função: Tratamento básico dos dados
def tratar_dados(dados_brutos):
    dados_tratados = {}

    for nome, df in dados_brutos.items():
        try:
            df = df.dropna(axis=1, how='all')

            # Padronização de nomes
            df.columns = [col.strip().upper().replace(' ', '_') for col in df.columns]

            for col in df.select_dtypes(include=['object']):
                df[col] = df[col].astype(str).str.upper().str.strip()

            date_cols = [col for col in df.columns if 'DATA' in col or 'DATE' in col]
            for col in date_cols:
                df[col] = pd.to_datetime(df[col], errors='coerce')

            dados_tratados[nome] = df
            print(f"[OK] Tratamento: {nome}")
        except Exception as e:
            print(f"[ERRO] Tratamento {nome}: {e}")

    return dados_tratados

# Etapa 3: Análise exploratória genérica
def analise_exploratoria(dados_tratados, exportar_graficos=False):
    os.makedirs('graficos', exist_ok=True)

    for nome, df in dados_tratados.items():
        print(f"\n📊 Análise: {nome}")
        print("="*60)

        print("✅ Shape:", df.shape)
        print("\n📌 Primeiras linhas:")
        display(df.head())

        print("\n📈 Estatísticas:")
        display(df.describe(include='all'))

        # Colunas categóricas com poucos valores únicos
        cat_cols = [col for col in df.select_dtypes(include='object') if df[col].nunique() < 30]

        for col in cat_cols:
            print(f"\n🔸 {col}:")
            display(df[col].value_counts(dropna=False))

            # Gráfico de barras
            plt.figure(figsize=(10, 4))
            df[col].value_counts().plot(kind='bar')
            plt.title(f'Distribuição: {col} - {nome}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            if exportar_graficos:
                plt.savefig(f'graficos/{nome}_{col}_barras.png')
            plt.show()

        # Colunas numéricas
        num_cols = df.select_dtypes(include=np.number).columns
        if len(num_cols) >= 2:
            print("\n🔢 Matriz de Correlação:")
            plt.figure(figsize=(8, 6))
            sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
            plt.title(f'Correlação Numérica - {nome}')
            plt.tight_layout()
            if exportar_graficos:
                plt.savefig(f'graficos/{nome}_correlacao.png')
            plt.show()


# Exportar dados tratados
def exportar_dados(dados_tratados, pasta_saida='dados_tratados', formato='xlsx'):
    os.makedirs(pasta_saida, exist_ok=True)

    for nome, df in dados_tratados.items():
        try:
            nome_limpo = nome.replace(' ', '_').replace('/', '_')[:50]
            caminho_saida = os.path.join(pasta_saida, f"{nome_limpo}.{formato}")
            if formato == 'csv':
                df.to_csv(caminho_saida, index=False, sep=';', encoding='utf-8-sig')
            else:
                df.to_excel(caminho_saida, index=False)
            print(f"[EXPORTADO] {nome} -> {caminho_saida}")
        except Exception as e:
            print(f"[ERRO] ao exportar {nome}: {e}")

# Exportar dados tratados e gráficos
def exportar_dados_e_graficos(dados_tratados, pasta_dados='dados_tratados', pasta_graficos='graficos', formato='xlsx'):
    os.makedirs(pasta_dados, exist_ok=True)
    os.makedirs(pasta_graficos, exist_ok=True)

    for nome, df in dados_tratados.items():
        nome_limpo = nome.replace(' ', '_').replace('/', '_')[:50]

        # 📁 Exporta os dados tratados
        try:
            caminho_saida = os.path.join(pasta_dados, f"{nome_limpo}.{formato}")
            if formato == 'csv':
                df.to_csv(caminho_saida, index=False, sep=';', encoding='utf-8-sig')
            else:
                df.to_excel(caminho_saida, index=False)
            print(f"[DADOS EXPORTADOS] {nome} -> {caminho_saida}")
        except Exception as e:
            print(f"[ERRO EXPORTAÇÃO DE DADOS] {nome}: {e}")

        # 📊 Exporta gráficos categóricos
        try:
            cat_cols = [col for col in df.select_dtypes(include='object') if df[col].nunique() < 30]
            for col in cat_cols:
                plt.figure(figsize=(10, 4))
                df[col].value_counts().plot(kind='bar')
                plt.title(f'Distribuição: {col} - {nome}')
                plt.xticks(rotation=45)
                plt.tight_layout()
                caminho_grafico = os.path.join(pasta_graficos, f"{nome_limpo}_{col}_barras.png")
                plt.savefig(caminho_grafico)
                plt.close()
                print(f"[GRÁFICO CATEGÓRICO] {col} -> {caminho_grafico}")
        except Exception as e:
            print(f"[ERRO GRÁFICO CATEGÓRICO] {nome}: {e}")

        # 📈 Exporta matriz de correlação
        try:
            num_cols = df.select_dtypes(include=np.number).columns
            if len(num_cols) >= 2:
                plt.figure(figsize=(8, 6))
                sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
                plt.title(f'Correlação Numérica - {nome}')
                plt.tight_layout()
                caminho_corr = os.path.join(pasta_graficos, f"{nome_limpo}_correlacao.png")
                plt.savefig(caminho_corr)
                plt.close()
                print(f"[GRÁFICO CORRELAÇÃO] -> {caminho_corr}")
        except Exception as e:
            print(f"[ERRO GRÁFICO DE CORRELAÇÃO] {nome}: {e}")



CAMINHO_DADOS = '../../dados_brutos/PNAD_2009/' 

print("🔄 Carregando dados...")
dados_brutos = carregar_dados(CAMINHO_DADOS)

print("\n🧹 Tratando dados...")
dados_tratados = tratar_dados(dados_brutos)

print("\n📊 Executando análise exploratória...")
analise_exploratoria(dados_tratados, exportar_graficos=True)