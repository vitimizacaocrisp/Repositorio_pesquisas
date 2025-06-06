# %%
# Célula 1: Importar as bibliotecas necessárias
import pandas as pd
import numpy as np
import os
import openpyxl

# %%
# Célula 3: Definir os caminhos para os arquivos

# Caminho para o arquivo original que você quer ler
caminho_arquivo_original = '../../dados_brutos/percepcao_medo_MG_2008/amostra_BH.xls'
caminho_arquivo_original_2 = '../../dados_brutos/percepcao_medo_MG_2008/amostra_MG.xls'
caminho_arquivo_original_3 = '../../dados_brutos/percepcao_medo_MG_2008/populacao_idade_sexo.csv'

# Caminho da pasta onde o novo arquivo será salvo
caminho_saida = '../../dados_tratados'

# %%
# Célula 4: Carregar os dados do arquivo CSV

print("Tentando carregar o arquivo...")
try:
    # Tenta carregar o arquivo com codificação
    df = pd.read_excel(caminho_arquivo_original, na_values=[
                       "", " ", "NA", "NaN", "nan", "null", "NULL", "None"])
    df2 = pd.read_excel(caminho_arquivo_original_2, na_values=[
                        "", " ", "NA", "NaN", "nan", "null", "NULL", "None"])
    df3 = pd.read_csv(caminho_arquivo_original_3, na_values=[
                      "", " ", "NA", "NaN", "nan", "null", "NULL", "None"], encoding='utf-8')
    print("Arquivo carregado com sucesso")
except Exception as e:
    print(f"Erro ao ler com UTF-8: {e}")
    try:
        df = pd.read_excel(caminho_arquivo_original, na_values=[
                           "", " ", "NA", "NaN", "nan", "null", "NULL", "None"])
        df2 = pd.read_excel(caminho_arquivo_original_2, na_values=[
                            "", " ", "NA", "NaN", "nan", "null", "NULL", "None"])
        df3 = pd.read_csv(caminho_arquivo_original_3, na_values=[
                          "", " ", "NA", "NaN", "nan", "null", "NULL", "None"], sep=';', skiprows=4, encoding='latin1')
        print("Arquivo carregado com sucesso usando codificação 'latin1'!")
    except Exception as e_latin1:
        print(f"ERRO: Falha ao carregar o arquivo. Verifique o caminho e o separador.")
        print(f"Erro detalhado: {e_latin1}")
        df = None
        df2 = None

# Se o DataFrame foi carregado, exibe as primeiras 5 linhas e as informações
if df is not None:
    print("\n--- AMOSTRA DOS DADOS (5 PRIMEIRAS LINHAS) ---")
    df.head()
    df.info()
    print("\n--- AMOSTRA DOS DADOS (5 PRIMEIRAS LINHAS) ---")
    df2.head()
    df2.info()
    print("\n--- AMOSTRA DOS DADOS (5 PRIMEIRAS LINHAS) ---")
    df3.head()
    df3.info()


# %%
# CÉLULA 5 - LIMPEZA INICIAL

# Remover colunas com todos os valores NaN
colunas_nulas_df3 = df3.columns[df3.isna().all()]
df3.drop(columns=colunas_nulas_df3, inplace=True)

# Exibir colunas removidas
if len(colunas_nulas_df3) > 0:
    print(
        f"✅ 'df3': {len(colunas_nulas_df3)} coluna(s) completamente nula(s) removida(s):")
    print(list(colunas_nulas_df3))
else:
    print("ℹ️ 'df3': Nenhuma coluna completamente nula foi encontrada.")


# === FUNÇÃO DE TRATAMENTO GERAL ===

def tratar_df(df, nome='df'):
    if df is not None:
        print(f"\n--- INÍCIO DO TRATAMENTO DE '{nome}' ---")

        # Remover linhas duplicadas
        duplicatas = df.duplicated().sum()
        if duplicatas > 0:
            df.drop_duplicates(inplace=True)
            print(f"✅ '{nome}': {duplicatas} linha(s) duplicada(s) removida(s).")
        else:
            print(f"ℹ️ '{nome}': Nenhuma linha duplicada encontrada.")

        # Remover colunas 100% nulas
        colunas_antes = df.shape[1]
        df.dropna(axis=1, how='all', inplace=True)
        colunas_depois = df.shape[1]
        removidas = colunas_antes - colunas_depois
        if removidas > 0:
            print(
                f"✅ '{nome}': {removidas} coluna(s) completamente nula(s) removida(s).")
        else:
            print(f"ℹ️ '{nome}': Nenhuma coluna completamente nula encontrada.")

        # Preencher nulos em colunas numéricas com 0
        colunas_num = df.select_dtypes(include=np.number).columns
        df[colunas_num] = df[colunas_num].fillna(0)
        print(f"✅ '{nome}': Valores nulos em colunas numéricas preenchidos com 0.")

        # Exibir info
        print(f"\n--- INFO DE '{nome}' ---")
        df.info()
        print(f"--- FIM DO TRATAMENTO DE '{nome}' ---\n")
    else:
        print(f"⚠️ '{nome}' não encontrado. Etapa de tratamento ignorada.\n")

# === TRATAMENTO DE df, df2 e df3 ===


tratar_df(df, 'df')
tratar_df(df2, 'df2')
tratar_df(df3, 'df3')

# %%
print(df)
print(df2)
print(df3)

# %%
# Célula 6: Unir os DataFrames
df_final = None  # Inicializa a variável

# Verifica se os três DataFrames existem
if 'df' in locals() and df is not None and 'df2' in locals() and df2 is not None and 'df3' in locals() and df3 is not None:
    print("Unindo os DataFrames 'df', 'df2' e 'df3'...")
    try:
        # Concatena os três DataFrames
        df_final = pd.concat([df, df2, df3], ignore_index=True)

        print("✅ DataFrames unidos com sucesso!")

        print("\n--- INFORMAÇÕES GERAIS DO DATAFRAME FINAL ---")
        df_final.info()

    except Exception as e:
        print(f"❌ Ocorreu um erro ao unir os DataFrames: {e}")
        print("Verifique se as colunas são compatíveis para a união.")

else:
    print("⚠️ Um ou mais DataFrames ('df', 'df2', 'df3') não foram carregados ou tratados corretamente. Etapa de união pulada.")


# %%
# Célula 7: Exportar o DataFrame Final (CSV e Excel)

# Cria o diretório de saída se ele não existir
if not os.path.exists(f"{caminho_saida}/csv"):
    os.makedirs(f"{caminho_saida}/csv")
    print(f"Pasta '{caminho_saida}' criada com sucesso!")

if not os.path.exists(f"{caminho_saida}/excel"):
    os.makedirs(f"{caminho_saida}/excel")
    print(f"Pasta '{caminho_saida}' criada com sucesso!")

print(f"Arquivo de entrada: {caminho_arquivo_original}")

# Verifica se o dataframe final foi criado com sucesso antes de salvar
if df_final is not None:

    # --- 1. EXPORTAR PARA CSV ---
    try:
        nome_arquivo_csv = 'percepcao_medoMG.csv'
        caminho_arquivo_csv_completo = os.path.join(
            f"{caminho_saida}/csv", nome_arquivo_csv)
        df_final.to_csv(caminho_arquivo_csv_completo,
                        index=False, sep=';', encoding='utf-8')
        print(f"✅ SUCESSO! Arquivo CSV salvo em:")
        print(f"'{caminho_arquivo_csv_completo}'")
    except Exception as e:
        print(f"❌ ERRO ao salvar o arquivo CSV: {e}")

    print("-" * 30)  # Linha separadora

    # --- 2. EXPORTAR PARA EXCEL ---
    try:
        nome_arquivo_excel = 'percepcao_medoMG.xlsx'
        caminho_arquivo_excel_completo = os.path.join(
            f"{caminho_saida}/excel", nome_arquivo_excel)
        # 'index=False' evita que o índice do pandas seja salvo como uma coluna no Excel
        df_final.to_excel(caminho_arquivo_excel_completo,
                          index=False, engine='openpyxl')
        print(f"✅ SUCESSO! Arquivo Excel salvo em:")
        print(f"'{caminho_arquivo_excel_completo}'")
    except Exception as e:
        print(f"❌ ERRO ao salvar o arquivo Excel: {e}")

else:
    print("⚠️ O DataFrame final ('df_final') não existe. A etapa de exportação foi pulada.")
