# %%
# Célula 1: Importar as bibliotecas necessárias
import pandas as pd
import numpy as np
import os
import openpyxl
import xlsxwriter
import glob


# %%
# Função: Carregamento de dados CSV/XLSX
caminho_pasta = '../../dados_brutos/PNAD_2009'

agressao = glob.glob(os.path.join(
    caminho_pasta, 'agressao/*.xls'), recursive=True)
furto = glob.glob(os.path.join(caminho_pasta, 'furto/*.xls'), recursive=True)
roubo = glob.glob(os.path.join(caminho_pasta, 'roubo/*.xls'), recursive=True)
roubofurto = glob.glob(os.path.join(
    caminho_pasta, 'roubofurto/*.xls'), recursive=True)
seguranca = glob.glob(os.path.join(
    caminho_pasta, 'seguranca/*.xls'), recursive=True)
tentativa = glob.glob(os.path.join(
    caminho_pasta, 'tentativa/*.xls'), recursive=True)


def processar_arquivo(tipo):
    dados = {}

    for arquivo in tipo:
        try:
            nome = os.path.basename(arquivo).replace(
                '.xlsx', '').replace('.xls', '')
            xls = pd.ExcelFile(arquivo)
            for sheet_name in xls.sheet_names:
                df_nome = f"{nome}_{sheet_name}" if len(
                    xls.sheet_names) > 1 else nome
                dados[df_nome] = pd.read_excel(arquivo, sheet_name=sheet_name, header=[
                                               0, 1], skiprows=7, index_col=0, skipfooter=3)

                # tratamento dos dados

                dados[df_nome].rename(columns={
                    'unnamed: 1_level_1': '',
                    'Preta ou parda ': 'preta/parda',
                    'Preta ou parda .1': 'preta',
                    'Preta ou parda .2': 'parda',
                    'Sem rendimento a menos de 1/4 (2)': 'sem rendimento a menos de 1/4',
                    'sem rendimento a menos de 1/4 (2)'
                    'Unnamed: 5_level_1': 'total'
                }, inplace=True)

                if isinstance(dados[df_nome].columns, pd.MultiIndex):
                    dados[df_nome].columns = pd.MultiIndex.from_tuples([
                        tuple(str(c).replace('\n', '').strip() for c in col)
                        for col in dados[df_nome].columns
                    ])
                else:
                    dados[df_nome].columns = dados[df_nome].columns.str.replace('\n', '', regex=True).str.strip()


                dados[df_nome] = dados[df_nome][dados[df_nome].index.notna()]
                
                dados[df_nome].index = dados[df_nome].index.astype(str).str.lower()
                dados[df_nome].columns = pd.MultiIndex.from_tuples([tuple(str(item).lower() for item in col) for col in dados[df_nome].columns])

                for col in dados[df_nome].select_dtypes(include='object').columns:
                    dados[df_nome][col] = dados[df_nome][col].str.lower()

                dados[df_nome] = dados[df_nome].apply(pd.to_numeric, errors='coerce')
                dados[df_nome] = dados[df_nome].round(2)

                print(f"[OK] Excel {df_nome}")
        except Exception as e:
            print(f"[ERRO] Excel {arquivo}: {e}")

    return dados


dados_agressao = processar_arquivo(agressao)
dados_furto = processar_arquivo(furto)
dados_roubo = processar_arquivo(roubo)
dados_roubofurto = processar_arquivo(roubofurto)
dados_seguranca = processar_arquivo(seguranca)
dados_tentativa = processar_arquivo(tentativa)


# %%
print(dados_roubofurto['cv123011a'].info())
print(dados_roubofurto['cv123011a'].head())

# %%
print(dados_agressao['cv126011a'].info())
print(dados_agressao['cv126011a'].head())


# %%
todos_dados = {
    'agressao': dados_agressao,
    'furto': dados_furto,
    'roubo': dados_roubo,
    'roubofurto': dados_roubofurto,
    'seguranca': dados_seguranca,
    'tentativa': dados_tentativa
}

print(todos_dados['agressao']['cv126011a'].info())
print(todos_dados['agressao']['cv126011a'].head())

# %%


def exportar_dados_organizados(dicionario_principal, pasta_base='../../dados_tratados/PNAD_2009'):
    """
    Exporta um dicionário aninhado de DataFrames para arquivos CSV e XLSX,
    organizando os arquivos em pastas por categoria e por formato.
    """
    print(f"Iniciando a exportação para a pasta base: '{pasta_base}'")

    # Verifica se o dicionário principal não está vazio
    if not dicionario_principal:
        print("[AVISO] O dicionário de dados está vazio. Nenhuma exportação será feita.")
        return

    # Loop pelas categorias (ex: 'agressao', 'furto')
    for categoria, dicionario_dataframes in dicionario_principal.items():
        print(f"\n--- Exportando categoria: {categoria.upper()} ---")

        # Define e cria os diretórios de saída para esta categoria
        path_saida_csv = os.path.join(pasta_base, 'csv', categoria)
        path_saida_xlsx = os.path.join(pasta_base, 'xlsx', categoria)
        os.makedirs(path_saida_csv, exist_ok=True)
        os.makedirs(path_saida_xlsx, exist_ok=True)

        # Loop pelos DataFrames dentro da categoria
        for nome_df, df in dicionario_dataframes.items():

            # --- Exportação para CSV ---
            # Define o caminho completo do arquivo
            caminho_csv = os.path.join(path_saida_csv, f"{nome_df}.csv")
            try:
                # sep=';' e encoding='utf-8-sig' são ideais para abrir no Excel em português
                df.to_csv(caminho_csv, sep=';',
                          encoding='utf-8-sig', index=True)
                print(f"  [OK] CSV salvo: {caminho_csv}")
            except Exception as e:
                print(f"  [ERRO] Falha ao salvar CSV {caminho_csv}: {e}")

            # --- Exportação para XLSX ---
            # Define o caminho completo do arquivo
            caminho_xlsx = os.path.join(path_saida_xlsx, f"{nome_df}.xlsx")
            try:
                # index=True garante que o índice do DataFrame seja salvo
                df.to_excel(caminho_xlsx, index=True, sheet_name='dados')
                print(f"  [OK] XLSX salvo: {caminho_xlsx}")
            except Exception as e:
                print(f"  [ERRO] Falha ao salvar XLSX {caminho_xlsx}: {e}")

    print(f"\n[SUCESSO] Exportação de todos os dados concluída!")
    print(f"Verifique a pasta '{pasta_base}' no seu diretório.")


# %%
def exportar_categorias_em_abas(dados_aninhados, pasta_saida='../../dados_tratados/PNAD_2009'):
    """
    Exporta cada categoria para um único arquivo Excel, onde cada DataFrame
    da categoria se torna uma aba (planilha) dentro do arquivo.
    """
    print(
        f"Iniciando a exportação por categoria para a pasta: '{pasta_saida}'")

    # Cria a pasta de saída se ela não existir
    os.makedirs(pasta_saida, exist_ok=True)

    # Loop pelas categorias (ex: 'agressao', 'furto')
    for categoria, dicionario_dataframes in dados_aninhados.items():
        # Define o caminho do arquivo Excel para a categoria atual
        caminho_arquivo_xlsx = os.path.join(pasta_saida, f"{categoria}.xlsx")

        print(
            f"\n--- Criando arquivo para a categoria: {categoria.upper()} ---")
        print(f"Arquivo: {caminho_arquivo_xlsx}")

        try:
            # Usa o ExcelWriter para escrever várias abas no mesmo arquivo
            with pd.ExcelWriter(caminho_arquivo_xlsx, engine='xlsxwriter') as writer:
                # Loop pelos DataFrames dentro da categoria
                for nome_aba, df in dicionario_dataframes.items():
                    # Escreve cada DataFrame em uma aba com seu respectivo nome
                    # 'index=True' garante que a coluna de índice seja salva
                    df.to_excel(writer, sheet_name=nome_aba, index=True)
                    print(f"  -> Aba '{nome_aba}' salva.")

        except Exception as e:
            print(
                f"[ERRO] Falha ao criar o arquivo para a categoria '{categoria}': {e}")

    print(f"\n[SUCESSO] Exportação por categoria concluída!")
    print(f"Verifique a pasta '{pasta_saida}'.")


# %%
exportar_dados_organizados(todos_dados)

# %%
exportar_categorias_em_abas(todos_dados)
