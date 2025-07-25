# %%
from io import BytesIO
from PIL import Image
import requests
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from fpdf import FPDF
import shutil
from IPython.display import display

# ==============================================================================
# 1. CONFIGURAÇÃO INICIAL
# ==============================================================================

# --- Função de Limpeza ---


def limpar_e_converter_colunas_numericas(df):
    """
    Itera sobre as colunas de um DataFrame, substitui vírgulas por pontos
    em colunas de texto e tenta convertê-las para um formato numérico.
    """
    print("Iniciando limpeza de colunas numéricas...")
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_numeric(
                    df[col].str.replace(',', '.', regex=False))
                print(f"-> Coluna '{col}' convertida para numérico.")
            except (AttributeError, ValueError):
                # Se a conversão falhar, a coluna é mantida como texto.
                pass
    print("Limpeza concluída.")
    return df

# --- Função de Limpeza Aprimorada ---


def limpar_e_converter_colunas_numericas2(df):
    """
    Itera sobre as colunas de um DataFrame, limpa e converte colunas
    de texto (object) para formato numérico.
    1. Remove pontos (usados como separador de milhar).
    2. Substitui vírgulas por pontos (para ser o separador decimal padrão).
    """
    print("Iniciando limpeza e conversão de colunas...")
    for col in df.columns:
        # Só processa colunas que são do tipo 'object' (texto)
        if df[col].dtype == 'object':
            # Verifica se a coluna parece ter números com vírgula para evitar
            # processar colunas de texto que não são numéricas.
            # O .notna() é para ignorar valores nulos (NaN)
            if df[col].str.contains(',', na=False).any():
                try:
                    # 1. Remove os pontos (separador de milhar)
                    cleaned_col = df[col].str.replace('.', '', regex=False)
                    # 2. Substitui a vírgula (separador decimal) por ponto
                    cleaned_col = cleaned_col.str.replace(
                        ',', '.', regex=False)

                    # 3. Converte para numérico
                    df[col] = pd.to_numeric(cleaned_col, errors='coerce')
                    print(
                        f"-> Coluna '{col}' foi limpa e convertida para numérico.")
                except Exception as e:
                    print(
                        f"-> Falha ao converter a coluna '{col}'. Mantida como texto. Erro: {e}")
    print("Limpeza concluída.")
    return df


# --- Definir caminhos ---
data_dir = '../../dados_brutos/datafolha_2928278/'
output_dir = '../../analises/'
output_logo_dir = '../../logo/'
temp_img_dir = os.path.join(output_dir, 'temp_images/')

# --- Criar diretórios se não existirem ---
os.makedirs(output_dir, exist_ok=True)
os.makedirs(temp_img_dir, exist_ok=True)
os.makedirs(output_logo_dir, exist_ok=True)

try:
    # base 2

    # --- Caminho completo para o arquivo ---
    arquivo_path = os.path.join(data_dir, 'PM3283_BASE_TIPO2.xlsx')

    # --- Passo 1: Verificar as planilhas disponíveis no arquivo ---
    print(f"Analisando o arquivo: '{os.path.basename(arquivo_path)}'")
    excel_file = pd.ExcelFile(arquivo_path)
    sheet_names = excel_file.sheet_names
    print(f"Planilhas encontradas: {sheet_names}")

    # --- Passo 2: Carregar a planilha desejada ---
    sheet_para_carregar = 'PM3283_BASE_TIPO2'
    if sheet_para_carregar not in sheet_names:
        print(f"AVISO: A planilha '{sheet_para_carregar}' não foi encontrada.")
        sheet_para_carregar = sheet_names[0]
        print(
            f"Carregando a primeira planilha como alternativa: '{sheet_para_carregar}'")

    # Carregue o arquivo SEM o argumento 'decimal'. Isso força
    # as colunas com formato misto a serem lidas como texto (object),
    # o que é ideal para a nossa função de limpeza.
    df2 = pd.read_excel(excel_file, sheet_name=sheet_para_carregar)
    print(f"DataFrame 'df2' carregado da planilha '{sheet_para_carregar}'.")

    # --- Passo 3: Limpar os dados carregados ---
    df2 = limpar_e_converter_colunas_numericas2(df2)

    # --- Passo 4: Verificar o resultado ---
    print("\nVerificação do DataFrame final:")
    df2.info()
    print("\nPrimeiras 5 linhas do df2:")
    print(df2.head())

except FileNotFoundError:
    print(
        f"\nERRO: Arquivo não encontrado. Verifique se o caminho está correto: '{arquivo_path}'")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")


try:
    # base 1

    # --- Caminho completo para o arquivo ---
    arquivo_path = os.path.join(data_dir, 'PM3283_BASE_TIPO1.xlsx')

    # --- Passo 1: Verificar as planilhas disponíveis no arquivo ---
    print(f"Analisando o arquivo: '{os.path.basename(arquivo_path)}'")
    excel_file = pd.ExcelFile(arquivo_path)
    sheet_names = excel_file.sheet_names
    print(f"Planilhas encontradas: {sheet_names}")

    # --- Passo 2: Carregar a planilha desejada ---
    # O código tentará carregar a planilha que você especificou.
    # Se não encontrar, carregará a primeira da lista como alternativa.
    sheet_para_carregar = 'PM3283_BASE_TIPO1'
    if sheet_para_carregar not in sheet_names:
        print(f"AVISO: A planilha '{sheet_para_carregar}' não foi encontrada.")
        # Usa a primeira planilha disponível
        sheet_para_carregar = sheet_names[0]
        print(
            f"Carregando a primeira planilha como alternativa: '{sheet_para_carregar}'")

    df1 = pd.read_excel(excel_file, sheet_name=sheet_para_carregar)
    print(f"DataFrame 'df1' carregado da planilha '{sheet_para_carregar}'.")

    # --- Passo 3: Limpar os dados carregados ---
    # Aplica a função para corrigir os erros de formato de número (com vírgula)
    df1 = limpar_e_converter_colunas_numericas(df1)

    # --- Passo 4: Verificar o resultado ---
    print("\nVerificação do DataFrame final:")
    df1.info()
    print("\nPrimeiras 5 linhas do df1:")
    print(df1.head())

except FileNotFoundError:
    print(
        f"\nERRO: Arquivo não encontrado. Verifique se o caminho está correto: '{arquivo_path}'")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")

# %%
# --- Renomear colunas do DataFrame df1 ---
# Dicionário unificado com o mapeamento completo de colunas para perguntas
mapa_de_colunas_unificado = {
    # Bloco de Identificação e Dados Sociodemográficos
    'p1': 'quantas pessoas com 16 anos ou mais moram na sua casa?',
    'p1a': 'e quantas são mulheres com 16 anos ou mais?',
    'p2': 'o(a) sr(a) poderia me dizer o primeiro nome e a idade de cada pessoa com 16 anos ou mais, incluindo o(a) sr(a), e começando do mais velho para o mais novo?',
    'p2a': 'quantas pessoas com menos de 16 anos moram em sua casa?',
    'p2b': 'por favor, me diga o nome e a idade das pessoas da sua casa com menos de 16 anos',
    'p3': 'o(a) sr(a) sempre morou nesta cidade?',
    'p4ano': 'há quanto tempo aproximadamente o(a) sr(a) mora nessa cidade?',
    'p4mes': 'há quanto tempo aproximadamente o(a) sr(a) mora nessa cidade? (em meses)',

    'p5': 'atualmente o(a) sr(a) é: solteiro(a); casado(a); amigado, amasiado (união consensual); separado(a) judicialmente / divorciado(a); separado (a) não oficialmente ou viúvo(a)?',

    'cor': 'qual das seguintes categorias descreve melhor sua cor: branca; preta; parda; amarela, indígena ou outra?',

    'escola': 'qual é o curso mais elevado que já concluiu? até que série o(a) sr(a) estudou?',

    'p8': 'em relação à orientação sexual, o(a) sr(a) diria que é : heterossexual, homossexual, ou bissexual?',
    'p9': 'atualmente, o(a) sr(a) trabalha? qual é a sua ocupação principal?',
    'p10': 'o seu trabalho fica na região central da cidade?',
    'p11': 'qual é aproximadamente a renda total mensal de todas as pessoas que moram neste domicílio, somando todas as fontes como salário, pensão, aposentadoria, benefícios sociais, aluguéis, bicos?',

    'religiao': 'vou ler uma lista de religiões para que o(a) sr(a) me indique se alguma delas é a sua',

    'idaa': 'idade_residente',
    'idab': 'idade_residente1',
    'idac': 'idade_residente2',
    'idad': 'idade_residente3',
    'idae': 'idade_residente4',
    'idaf': 'idade_residente5',
    'idag': 'idade_residente6',
    'idah': 'idade_residente7',
    'idai': 'idade_residente8',
    'idaj': 'idade_residente9',
    'idak': 'idade_residente10',
    'idal': 'idade_residente11',

    'sexoa': 'sexo_residente',
    'sexob': 'sexo_residente1',
    'sexoc': 'sexo_residente2',
    'sexod': 'sexo_residente3',
    'sexoe': 'sexo_residente4',
    'sexof': 'sexo_residente5',
    'sexog': 'sexo_residente6',
    'sexoh': 'sexo_residente7',
    'sexoi': 'sexo_residente8',
    'sexoj': 'sexo_residente9',
    'sexok': 'sexo_residente10',
    'sexol': 'sexo_residente11',

    'p2idaa': 'idade_residente_menor_de_16',
    'p2idab': 'idade_residente_menor_de_16_1',
    'p2idac': 'idade_residente_menor_de_16_2',
    'p2idad': 'idade_residente_menor_de_16_3',
    'p2idae': 'idade_residente_menor_de_16_4',
    'p2idaf': 'idade_residente_menor_de_16_5',
    'p2idag': 'idade_residente_menor_de_16_6',
    'p2idah': 'idade_residente_menor_de_16_7',
    'p2idai': 'idade_residente_menor_de_16_8',
    'p2idaj': 'idade_residente_menor_de_16_9',
    'p2idak': 'idade_residente_menor_de_16_10',
    'p2idal': 'idade_residente_menor_de_16_11',

    'p2sexoa': 'sexo_residente_menor_de_16',
    'p2sexob': 'sexo_residente_menor_de_16_1',
    'p2sexoc': 'sexo_residente_menor_de_16_2',
    'p2sexod': 'sexo_residente_menor_de_16_3',
    'p2sexoe': 'sexo_residente_menor_de_16_4',
    'p2sexof': 'sexo_residente_menor_de_16_5',
    'p2sexog': 'sexo_residente_menor_de_16_6',
    'p2sexoh': 'sexo_residente_menor_de_16_7',
    'p2sexoi': 'sexo_residente_menor_de_16_8',
    'p2sexoj': 'sexo_residente_menor_de_16_9',
    'p2sexok': 'sexo_residente_menor_de_16_10',
    'p2sexol': 'sexo_residente_menor_de_16_11',


    # Bloco de Atividades Cotidianas
    'p13a': 'durante a semana, de segunda a sexta-feira, onde o(a) sr(a) costuma ficar a maior parte da manhã, das 06h ao meio-dia em casa ou fora de casa?',
    'p13b': 'durante a semana, de segunda a sexta-feira, onde o(a) sr(a) costuma ficar a maior parte da tarde, do meio-dia às 18h em casa ou fora de casa?',
    'p13c': 'durante a semana, de segunda a sexta-feira, onde o(a) sr(a) costuma ficar a maior parte da noite, das 18h01 à meia-noite em casa ou fora de casa?',
    'p13d': 'durante a semana, de segunda a sexta-feira, onde o(a) sr(a) costuma ficar a maior parte da madrugada, da meia-noite às 06h em casa ou fora de casa?',
    'p14a': 'nos últimos 30 dias o(a) sr(a) saiu para ir ao cinema?',
    'p14b': 'nos últimos 30 dias o(a) sr(a) saiu para ir à praia ou parque?',
    'p14c': 'nos últimos 30 dias o(a) sr(a) saiu para comer fora de casa, sem contar os dias de trabalho?',
    'p14d': 'nos últimos 30 dias o(a) sr(a) saiu para visitar amigos ou parentes?',
    'p14e': 'nos últimos 30 dias o(a) sr(a) saiu para assistir algum evento esportivo amador ou profissional ao vivo?',
    'p14f': 'nos últimos 30 dias o(a) sr(a) saiu para praticar alguma atividade esportiva ou física como futebol, basquete, tênis, boliche, natação, aula de dança, ginástica ou fazer caminhada?',
    'p14g': 'nos últimos 30 dias o(a) sr(a) saiu para ir a missa, culto, atividade religiosa ou mística?',
    'p14h': 'nos últimos 30 dias o(a) sr(a) saiu para ir ao shopping ou centro comercial?',
    'p14i': 'nos últimos 30 dias o(a) sr(a) saiu para feiras populares?',
    'p14j': 'nos últimos 30 dias o(a) sr(a) saiu para assistir a algum show ou espetáculo de música, dança?',
    'p14k': 'nos últimos 30 dias o(a) sr(a) saiu para ir a algum bar ou casa noturna?',
    'p15': 'quais os três principais meios de transporte que o(a) sr(a) mais costuma utilizar durante a semana?',
    'p16': 'quem (é) são os responsáveis por cuidar e supervisionar as crianças ou adolescentes desta residência, quando não estiverem na escola ou creche?',

    # Bloco de Mapeamento de Crimes (Perguntas Gerais)
    'p17': 'o(a) sr(a) ou alguém da sua casa possui ou possuiu algum carro, caminhão ou caminhonete para uso próprio nos últimos 12 meses?',
    'p18': 'o(a) sr(a) ou alguém da sua casa possui ou possuiu alguma moto, motocicleta ou lambreta para uso próprio nos últimos 12 meses?',
    'p19': 'alguma vez, alguém furtou o(s) seu(s) carro(s), caminhão(ões) ou caminhonete(s) ou de alguém de sua casa, isto é, levou sem utilizar força ou fazer ameaça?',
    'p19_ultimos12meses': 'se sim, isso ocorreu nos últimos doze meses?',
    'p20': 'alguma vez, alguém roubou o seu(s) carro(s), caminhão(ões) ou caminhonete(s) ou de alguém de sua casa com o uso de violência ou ameaça?',
    'p20_ultimos12meses': 'se sim, isso ocorreu nos últimos doze meses?',
    'p21': 'alguma vez, alguém furtou a(s) sua(s) moto(s), motocicleta(s) ou lambreta(s) ou de alguém de sua casa, isto é, levou sem utilizar força ou fazer ameaça?',
    'p21_ultimos12meses': 'se sim, isso ocorreu nos últimos doze meses?',
    'p22': 'alguma vez, alguém roubou a(s) sua(s) moto(s), motocicleta(s) ou lambreta(s) ou de alguém de sua casa com o uso de violência ou ameaça?',
    'p22_ultimos12meses': 'se sim, isso ocorreu nos últimos doze meses?',
    'p23': 'alguma vez, o(a) sr(a) teve qualquer evidência de que alguém furtou qualquer um outro(s) bem(ns) do(a) sr(a), isto é, levou sem utilizar força ou fazer ameaça?',
    'p23_ultimos12meses': 'se sim, isso ocorreu nos últimos doze meses?',
    'p24': 'alguma vez, alguém roubou algum objeto seu, com o uso de violência ou ameaça?',
    'p24_ultimos12meses': 'se sim, isso ocorreu nos últimos doze meses?',
    'p25': 'alguma vez o(a) sr(a) foi vítima de sequestro?',
    'p25_ultimos12meses': 'se sim, isso ocorreu nos últimos doze meses?',
    'p26': 'e alguma vez o(a) sr(a) foi vítima de sequestro relâmpago?',
    'p26_ultimos12meses': 'se sim, isso ocorreu nos últimos doze meses?',

    # Fraude e Estelionato
    'p27aa': 'nos últimos 12 meses, o(a) sr(a) sofreu alguma fraude contra o seu cartão de crédito?',
    'p27b': 'nos últimos 12 meses, o(a) sr(a) sofreu fraude com cheque?',
    'p27c': 'nos últimos 12 meses, o(a) sr(a) recebeu notas de dinheiro falso?',
    'p27d': 'nos últimos 12 meses, o(a) sr(a) pagou por algum produto que não foi entregue?',
    'p27e': 'nos últimos 12 meses, o(a) sr(a) foi vítima de fraude em algum investimento que realizou?',
    'p27f': 'nos últimos 12 meses, o(a) sr(a) teve o seu celular clonado, ou seja, o seu número foi usado indevidamente por outra pessoa?',
    'p27g': 'nos últimos 12 meses, o(a) sr(a) teve linha telefônica residencial violada ou desviada?',
    'p27h': 'nos últimos 12 meses, o(a) sr(a) sofreu fraude de documentos pessoais?',
    'p27i': 'nos últimos 12 meses, o(a) sr(a) foi vítima de algum outro tipo de fraude?',
    'p27j': 'nos últimos 12 meses, o(a) sr(a) sofreu fraudes pela internet (sites de bancos falsos, etc)?',
    'p27a_ultima': 'qual dessas foi a última?',

    # Acidente
    'p28a': 'nos últimos 12 meses, o (a) sr (a) foi vítima de afogamento?',
    'p28b': 'nos últimos 12 meses, o (a) sr (a) foi vítima de queda?',
    'p28c': 'nos últimos 12 meses, o (a) sr (a) foi vítima de asfixia?',
    'p28d': 'nos últimos 12 meses, o (a) sr (a) foi vítima de eletrocução ou seja, choque de alta voltagem?',
    'p28e': 'nos últimos 12 meses, o (a) sr (a) foi vítima de acidente de trânsito? (inclui atropelamento)',
    'p28f': 'nos últimos 12 meses, o (a) sr (a) foi vítima de outro tipo de acidente?',
    'p29a': 'nos últimos 12 meses, algum conhecido seu foi vítima de afogamento?',
    'p29b': 'nos últimos 12 meses, algum conhecido seu foi vítima de queda?',
    'p29c': 'nos últimos 12 meses, algum conhecido seu foi vítima de asfixia?',
    'p29d': 'nos últimos 12 meses, algum conhecido seu foi vítima de eletrocução, ou seja, choque de alta voltagem?',
    'p29e': 'nos últimos 12 meses, algum conhecido seu foi vítima de acidente de trânsito? (inclui atropelamento)',
    'p29f': 'nos últimos 12 meses, algum conhecido seu foi vítima de outro tipo de acidente?',

    # Agressões ou Ameaças
    'p30a': 'nos últimos 12 meses, o(a) sr(a) foi vítima de insulto, humilhação ou xingamento (ofensa verbal)?',
    'p30a_quantas': 'quantas vezes?',
    'p30b': 'nos últimos 12 meses, o(a) sr(a) foi vítima de ameaça de apanhar, empurrar ou chutar?',
    'p30b_quantas': 'quantas vezes?',
    'p30c': 'nos últimos 12 meses, o(a) sr(a) foi vítima de ameaça com faca ou arma de fogo?',
    'p30c_quantas': 'quantas vezes?',
    'p30d': 'nos últimos 12 meses, o(a) sr(a) foi vítima de amedrontamento ou perseguição?',
    'p30d_quantas': 'quantas vezes?',
    'p30e': 'nos últimos 12 meses, o(a) sr(a) foi vítima de batida, empurrão ou chute?',
    'p30e_quantas': 'quantas vezes?',
    'p30f': 'nos últimos 12 meses, o(a) sr(a) foi vítima de lesão provocada por algum objeto que lhe foi atirado?',
    'p30f_quantas': 'quantas vezes?',
    'p30g': 'nos últimos 12 meses, o(a) sr(a) foi vítima de espancamento ou tentativa de estrangulamento?',
    'p30g_quantas': 'quantas vezes?',
    'p30h': 'nos últimos 12 meses, o(a) sr(a) foi vítima de esfaqueamento ou tiro?',
    'p30h_quantas': 'quantas vezes?',
    'p30i': 'nos últimos 12 meses, o(a) sr(a) foi vítima de ameaça de ter seus bens e documentos subtraídos/tomados/retirados/ por parentes, companheiros ou conhecidos?',
    'p30i_quantas': 'quantas vezes?',
    'p30j': 'nos últimos 12 meses, o(a) sr(a) foi vítima de alguma outra ameaça ou agressão?',
    'p30j_quantas': 'quantas vezes?',
    'p30b_ultima': 'qual dessas foi a última agressão ou ameaça sofrida?',

    # Ofensa Sexual e Discriminação
    'p31': 'alguma vez, alguém fez ou tentou fazer isto com o(a) sr(a)?',
    'p31a': 'isso aconteceu nos últimos 12 meses?',
    'p32a': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação por sua cor ou raça?',
    'p32a_quantas': 'quantas vezes?',
    'p32b': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação por ser homem / mulher?',
    'p32b_quantas': 'quantas vezes?',
    'p32c': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação por sua orientação ou opção sexual?',
    'p32c_quantas': 'quantas vezes?',
    'p32d': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação por doença?',
    'p32d_quantas': 'quantas vezes?',
    'p32e': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação por deficiência física?',
    'p32e_quantas': 'quantas vezes?',
    'p32f': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação por sua religião?',
    'p32f_quantas': 'quantas vezes?',
    'p32g': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação pelo lugar onde mora?',
    'p32g_quantas': 'quantas vezes?',
    'p32h': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação por sua classe social?',
    'p32h_quantas': 'quantas vezes?',
    'p32i': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação pela sua escolaridade?',
    'p32i_quantas': 'quantas vezes?',
    'p32j': 'nestes últimos 12 meses, o(a) sr(a) sofreu algum tipo de discriminação pela sua preferência política?',
    'p32j_quantas': 'quantas vezes?',
    'p32b_ultima': 'qual dessas foi a última?',

    # Detalhamento de Crimes
    'p33': 'quantas vezes o(a) sr(a) ou alguém da sua casa teve o carro, caminhão ou caminhonete furtado nos últimos 12 meses?',
    'p38': 'quantas vezes o(a) sr(a) ou alguém da sua casa teve o carro, caminhão ou caminhonete roubado nos últimos 12 meses?',
    'p48': 'quantas vezes o(a) sr(a) ou alguém da sua casa teve a moto, motocicleta ou lambreta furtada nos últimos 12 meses?',
    'p53': 'quantas vezes o(a) sr(a) ou alguém da sua casa teve a moto, motocicleta ou lambreta roubada nos últimos 12 meses?',
    'p63': 'quantas vezes seus objetos foram furtados nos últimos 12 meses?',
    'p69': 'quantas vezes seus objetos foram roubados nos últimos 12 meses?',
    'p80': 'quantas vezes o(a) sr(a) foi vítima de (sequestro ou sequestro relâmpago) nos últimos 12 meses?',
    'p91': 'quantas vezes (leia a ocorrência da p.27a) ocorreu nos últimos 12 meses?',
    'p118': 'quantas vezes o(a) sr(a) foi vítima de ofensa sexual nos últimos 12 meses?',

    # Vizinhança e Percepção de Segurança
    'p139': 'há quanto tempo o(a) sr(a) mora na sua vizinhança?',
    'p140': 'se pudesse escolher, o(a) sr(a) gostaria de continuar morando na sua vizinhança; mudaria para outro lugar do mesmo bairro; mudaria para outro bairro da cidade; mudaria para outra cidade do estado; mudaria para outro estado do brasil ou mudaria para outro país?',
    'p141': 'em relação aos seus vizinhos, o(a) sr(a) diria que: conhece todos ou quase todos; conhece muitos; conhece alguns ou não conhece nenhum?',
    'p142': 'com relação aos seus vizinhos, o(a) sr(a) diria que: confia na maioria deles; confia em alguns deles ou não confia em nenhum deles?',
    'p143a': 'em quais das seguintes situações o(a) sr(a) acha que poderia contar ou não com seus vizinhos se precisasse: para auxiliar em caso de doença ou problema de saúde?',
    'p143b': 'em quais das seguintes situações o(a) sr(a) acha que poderia contar ou não com seus vizinhos se precisasse: para pedir dinheiro emprestado?',
    'p144a': 'algum vizinho costuma pedir ajuda ou favores ao(a) sr(a) como auxiliar em caso de doença ou problema de saúde frequentemente, raramente ou nunca?',
    'p144b': 'algum vizinho costuma pedir ajuda ou favores ao(a) sr(a) como pedir dinheiro emprestado frequentemente, raramente ou nunca?',
    'p145a': 'pensando na sua vizinhança, o(a) sr(a) diria que pode contar com seus vizinhos para tomar alguma providência se: observar jovens matando aula e ficando a toa na rua',
    'p145b': 'pensando na sua vizinhança, o(a) sr(a) diria que pode contar com seus vizinhos para tomar alguma providência se: observar jovens depredando prédios',
    'p146a': 'vou ler algumas frases e gostaria que o(a) sr(a) dissesse se concorda ou se discorda com cada uma delas, pensando na sua vizinhança: as pessoas daqui são dispostas ajudar seus vizinhos',
    'p146b': 'vou ler algumas frases e gostaria que o(a) sr(a) dissesse se concorda ou se discorda com cada uma delas, pensando na sua vizinhança: as pessoas nesta vizinhança são muito unidas',
    'p147a': 'na sua vizinhança existem ou não prédios, casas ou galpões abandonados?',
    'p147b': 'na sua vizinhança existem ou não carros abandonados, arrebentados ou desmontados nas ruas?',
    'p152': 'como o(a) sr(a) se sente ao andar nas ruas do bairro onde reside durante o dia',
    'p153': 'como o(a) sr(a) se sente ao andar nas ruas do bairro onde reside durante a noite',
    'p162a': 'por causa da violência, o(a) sr(a): evita sair à noite ou chegar muito tarde em casa?',
    'p162b': 'por causa da violência, o(a) sr(a): muda de caminho entre a casa e o trabalho ou a escola ou lazer?',
    'p163a': 'pensando na sua vizinhança, o(a) sr.(a) teme ser assaltado(a)?',
    'p163b': 'pensando na sua vizinhança, o(a) sr.(a) teme ter o carro ou moto roubado num assalto?',
    'p164': 'o(a) sr(a) diria que, nos últimos 12 meses, a criminalidade na sua cidade aumentou, diminuiu ou ficou igual?',
    'p165': 'o(a) sr(a) diria que, nos últimos 12 meses, a criminalidade na sua vizinhança aumentou, diminuiu ou ficou igual?',
    'p166a': 'o(a) sr(a) tem medo de: ter sua residência invadida ou arrombada?',
    'p167a': 'o(a) sr(a) acredita que pode se tornar vítima de algum desses crimes no próximo ano? acredita que pode: ter sua residência invadida ou arrombada?',

    # Polícia e Finalização
    'p170': 'de uma maneira geral, em se tratando da polícia militar o(a) sr(a): confia muito; confia um pouco ou não confia?',
    'p171a': 'agora vou citar algumas frases e para cada frase eu gostaria que o(a) sr(a) me dissesse se concorda ou discorda?: os policiais militares sabem como agir em situações de risco e perigo',
    'p172a': 'como o(a) sr(a) avalia o atendimento da polícia militar em relação a(ao): punição dos policiais com mau comportamento?',
    'p176': 'de uma maneira geral, em se tratando da polícia civil o(a) sr(a): confia muito; confia um pouco ou não confia?',
    'p177a': 'como o(a) sr(a) avalia o atendimento da polícia civil em relação a(ao): investigação de crimes?',
    'p180': 'para finalizar, o(a) sr(a). ou alguém da sua casa possui uma arma de fogo?',
    'p181a': 'apenas para classificação, o(a) sr(a) poderia me dizer se tem televisão colorida em sua casa? (se sim) quantos?',
    'p181b': 'apenas para classificação, o(a) sr(a) poderia me dizer se tem automóvel de passeio em sua casa? (se sim) quantos?',
    'p181c': 'apenas para classificação, o(a) sr(a) poderia me dizer se tem rádio sem contar o do carro em sua casa? (se sim) quantos?',
    'p181d': 'apenas para classificação, o(a) sr(a) poderia me dizer se tem empregada doméstica mensalista em sua casa? (se sim) quantos?',
    'p181e': 'apenas para classificação, o(a) sr(a) poderia me dizer se tem máquina de lavar roupas em sua casa? (se sim) quantos?',
    'p181f': 'apenas para classificação, o(a) sr(a) poderia me dizer se tem videocassete ou dvd em sua casa? (se sim) quantos?',
    'p181g': 'apenas para classificação, o(a) sr(a) poderia me dizer se tem banheiro em sua casa? (se sim) quantos?',
    'p181h': 'apenas para classificação, o(a) sr(a) poderia me dizer se tem geladeira em sua casa? (se sim) quantos?',
    'p181i': 'apenas para classificação, o(a) sr(a) poderia me dizer se tem freezer (aparelho independente ou parte da geladeira duplex) em sua casa? (se sim) quantos?',
    'p182': 'até que ano da escola o chefe da família estudou?',
    'p183': 'tipo de moradia',


    # etc
    'rendaf': 'renda_familiar',




}

df1 = df1.rename(columns=mapa_de_colunas_unificado)
# df2 = df2.rename(columns= mapa_de_colunas_unificado)


relacionamentos = {
    1: 'Solteiro(a)',
    2: 'Casado(a)',
    3: 'Amigado(a)/(união consensual)',
    4: 'Separado(a) judicialmente / Divorciado(a)',
    5: 'Separado(a) não oficialmente ou Viúvo(a)'
}
coluna = 'atualmente o(a) sr(a) é: solteiro(a); casado(a); amigado, amasiado (união consensual); separado(a) judicialmente / divorciado(a); separado (a) não oficialmente ou viúvo(a)?'

df1['estado_civil'] = df1[coluna].map(relacionamentos)

raca_cor = {
    1: 'Branca',
    2: 'Preta',
    3: 'Parda',
    4: 'Amarela',
    5: 'Indígena',
    6: 'Outra'
}
coluna = 'qual das seguintes categorias descreve melhor sua cor: branca; preta; parda; amarela, indígena ou outra?'

df1['raca_cor'] = df1[coluna].map(raca_cor)

escolaridade = {
    1: 'Sem instrução',
    2: 'Ensino fundamental incompleto (1º Grau incomp.)',
    3: 'Ensino fundamental completo (1º Grau completo)',
    4: 'Ensino médio incompleto (2º Grau incomp.)',
    5: 'Ensino médio completo (2º Grau completo)',
    6: 'Superior incompleto (Universidade / Faculdade incompleto)',
    7: 'Superior completo (Universidade / Faculdade completo)',
    8: 'Pós-graduação',
    9: 'Não sabe/Não lembra'
}
coluna = 'qual é o curso mais elevado que já concluiu? até que série o(a) sr(a) estudou?'
df1['escolaridade'] = df1[coluna].map(escolaridade)

religioes = {
    1: "Evangélica Pentecostal",
    2: "Evangélica não Pentecostal",
    3: "Umbanda",
    4: "Candomblé ou outras religiões afro-brasileiras (Xangô, Batuque de Mina, Omoloco, Catimbó)",
    5: "Espírita Kardecista, espiritualista",
    6: "Católica",
    7: "Judaica",
    8: "Outra religião (Mórmon, Testemunha de Jeová, Seisho-No-Iê, Messiânica, Perfeita Liberdade, Budista, Santo daime, Esotérica)",
    9: "Não tem religião/nenhuma",
    10: "É ateu/não acredita em Deus"
}

coluna = 'vou ler uma lista de religiões para que o(a) sr(a) me indique se alguma delas é a sua'
df1['religiao'] = df1[coluna].map(religioes)


pd.set_option('display.max_rows', 30)  # Exibe todas as linhas
pd.set_option('display.max_columns', None)  # Exibe todas as colunas
display(df1)
# display(df2)


# %%
df_short = df1

# --- Lógica Principal ---

# 1. Definir a lista de prefixos
prefixos = ['p', 'r', 'n', 'm', 'x']

# 2. Criar a lista de colunas a serem excluídas usando a lógica (prefixo E comprimento)
colunas_para_excluir = [
    col for col in df_short.columns
    if col.lower().startswith(tuple(prefixos)) and len(col) <= 7
]

# 3. (Passo de Segurança) Imprimir a lista de colunas que serão removidas para verificação
print("\n--- Colunas selecionadas para exclusão (seguindo as regras) ---")
print(colunas_para_excluir)

# 4. Excluir as colunas identificadas
df_short = df_short.drop(columns=colunas_para_excluir)

colunas_restantes_para_excluir = [
    'errob',	'presente', 't139', 'erro1',	'errol',	'errop',	'comp0',	'erroa',	'erroc',	'errod',	'erroe',	'errof', 't4', 'quadro', 'tabela',	'sexotab', 'idatab', 'D_R', 'dig', 'cpd', 'telefone', 'inloco', 'cidade', 'uf', 'setor', 'sorteio', 'checagem', 'data', 'hini', 'hfim', 'consu', 'tipo', 'tvcor', 'carro', 'empreg', 'videodvd', 'banhe', 'gelad', 'freezer', 'escolac', 'tipo de moradia', 'cbrasil08', 'T1', 'TC', 'estado', 'FF1', 'FF2', 'FF3', 'FF4', 'FF5', 'CBRASIL08X', 'NCBRASIL08X', 'BCBRA081', 'CBRA08X', 'BCBRA08', 'CBRAESP', 'BCBRA08_E', 'BCBRA08_D', 'CBRAAC', 'CBRACDE', 'NCBRA08X', 'BSEXTAB', 'BIDA', 'BESTCIVI', 'BPEA', 'BCOR', 'ESCOLA1', 'BESC', 'B8', 'BRELIG', 'BCID'
]

# 5. Excluir colunas adicionais que não são prefixadas

print("\n--- Colunas adicionais a serem removidas (não prefixadas) ---")
print(colunas_restantes_para_excluir)

df_short = df_short.drop(
    columns=colunas_restantes_para_excluir, errors='ignore')


# --- Outra Limpeza ---

# 1. Uma lista com todos os valores que você quer substituir.
#    Incluímos strings e números para garantir que todos os casos sejam cobertos.
valores_errados = ['96', '97', '99', 96, 97, 99]

# 2. Defina o novo valor. Usar o número 0 é geralmente melhor que a string '0'.
valor_correto = 0

# 3. Use .replace() para fazer a substituição em todo o DataFrame
df_short = df_short.replace(valores_errados, valor_correto)

# --- Resultado Final ---
print("\n--- DataFrame Final (Após a Limpeza) ---")
print(df_short.head(5))
print("\nColunas restantes:", df_short.columns.tolist())

# %%
df_short.head(10)

# %%
# 1. Renomear colunas para nomes mais curtos e práticos
# (Você pode adicionar todas as outras que for usar)
mapeamento_nomes = {
    'quantas pessoas com 16 anos ou mais moram na sua casa?': 'adultos_no_domicilio',
    'e quantas são mulheres com 16 anos ou mais?': 'mulheres_adultas',
    'quantas pessoas com menos de 16 anos moram em sua casa?': 'menores_no_domicilio',
    'o(a) sr(a) diria que, nos últimos 12 meses, a criminalidade na sua cidade aumentou, diminuiu ou ficou igual?': 'percepcao_criminalidade'
}
df_short.rename(columns=mapeamento_nomes, inplace=True)


# 2. Unificar as colunas de idade dos residentes
colunas_idade = [
    'idade_residente', 'idade_residente1', 'idade_residente2', 'idade_residente3',
    'idade_residente4', 'idade_residente5', 'idade_residente6', 'idade_residente7',
    'idade_residente8', 'idade_residente9', 'idade_residente10', 'idade_residente11'
]

# Usamos melt para transformar as colunas de idade de formato largo para longo
# E removemos valores nulos que representam casas com menos residentes
idades_residentes = df_short[colunas_idade].melt(
    var_name='residente_num', value_name='idade').dropna()

# Agora temos uma Series chamada 'idades_residentes.idade' pronta para ser plotada!
print("Processamento de idades concluído. Total de residentes analisados:",
      len(idades_residentes))

# %%
# Configurações visuais
sns.set_theme(style="whitegrid", context="talk", palette="viridis")
plt.rcParams['figure.figsize'] = (14, 8)

print("Ambiente visual configurado com sucesso.")

Descricoes = []

# Funções atualizadas para salvar e descrever os gráficos


def salvar_grafico(titulo, descricao):
    nome_arquivo = f"{titulo.lower().replace(' ', '_').replace('/', '-')}.png"
    caminho = os.path.join(temp_img_dir, nome_arquivo)
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    Descricoes.append({
        'titulo': titulo,
        'descricao': descricao,
        'caminho': caminho
    })
    print(f"Gráfico salvo: {caminho}\nDescrição: {descricao}\n")


def plotar_barras(dataframe, coluna, titulo, descricao):
    if coluna not in dataframe.columns:
        print(f"ERRO: A coluna '{coluna}' não foi encontrada no DataFrame.")
        return

    plt.figure()
    ordem = dataframe[coluna].value_counts().index
    ax = sns.countplot(y=dataframe[coluna], order=ordem, palette='viridis_r')

    total = len(dataframe[coluna])
    for p in ax.patches:
        contagem = int(p.get_width())
        percentual = f'({100 * contagem / total:.1f}%)'
        rotulo = f'{contagem} {percentual}'
        ax.annotate(rotulo, (p.get_width() + (total * 0.001), p.get_y() + p.get_height()/2),
                    ha='left', va='center', fontsize=12)

    ax.set_title(titulo, fontsize=20, pad=20)
    ax.set_xlabel('Contagem e Percentual (%)', fontsize=14)
    ax.set_ylabel('')
    ax.set_xlim(0, dataframe[coluna].value_counts().max() * 1.18)
    plt.tight_layout()
    salvar_grafico(titulo, descricao)


def plotar_pizza(dataframe, coluna, titulo, descricao, limite_percentual=3.0):
    if coluna not in dataframe.columns:
        print(f"ERRO: A coluna '{coluna}' não foi encontrada no DataFrame.")
        return

    contagem = dataframe[coluna].value_counts(normalize=True) * 100
    categorias_pequenas = contagem[contagem < limite_percentual]

    if not categorias_pequenas.empty:
        dados_plot = contagem[contagem >= limite_percentual]
        dados_plot['Outras'] = categorias_pequenas.sum()
    else:
        dados_plot = contagem

    labels = dados_plot.index
    valores = dados_plot.values
    explode = [0.1 if label == 'Outras' else 0 for label in labels]

    plt.figure(figsize=(12, 10))
    cores = sns.color_palette('viridis', len(labels))

    plt.pie(
        valores,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=cores,
        explode=explode,
        textprops={'fontsize': 14}
    )

    plt.title(titulo, fontsize=20, pad=20)
    plt.axis('equal')
    salvar_grafico(titulo, descricao)


def plotar_histograma(series_de_dados, titulo, descricao, bins=40):
    media = series_de_dados.mean()
    mediana = series_de_dados.median()

    plt.figure(figsize=(10, 6))
    sns.histplot(series_de_dados, kde=True, bins=bins, color='darkblue')
    plt.axvline(media, color='red', linestyle='--',
                linewidth=2, label=f'Média: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='-',
                linewidth=2, label=f'Mediana: {mediana:.2f}')
    plt.title(titulo, fontsize=16)
    plt.xlabel('Valor')
    plt.ylabel('Frequência')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    salvar_grafico(titulo, descricao)


def plotar_boxplot(series_de_dados, titulo, descricao):
    plt.figure(figsize=(10, 4))
    sns.boxplot(x=series_de_dados, palette='coolwarm')
    plt.title(titulo, fontsize=16)
    plt.xlabel('Valor')
    plt.tight_layout()
    salvar_grafico(titulo, descricao)


def plotar_histograma_melhorado(series_de_dados, titulo, descricao, faixa_idade=(1, 100)):
    idade_min, idade_max = faixa_idade
    dados_filtrados = series_de_dados[(
        series_de_dados >= idade_min) & (series_de_dados <= idade_max)]

    if dados_filtrados.empty:
        print(f"Aviso: Nenhum dado entre {idade_min} e {idade_max} anos.")
        return

    media = dados_filtrados.mean()
    mediana = dados_filtrados.median()
    bins = int(np.sqrt(len(dados_filtrados)))

    plt.figure(figsize=(12, 7))
    sns.histplot(dados_filtrados, kde=True, bins=bins,
                 color="royalblue", alpha=0.7)
    plt.axvline(media, color='crimson', linestyle='--',
                linewidth=2.5, label=f'Média: {media:.2f}')
    plt.axvline(mediana, color='darkgreen', linestyle='-',
                linewidth=2.5, label=f'Mediana: {mediana:.2f}')
    plt.title(
        f'{titulo} (Idades de {idade_min} a {idade_max} anos)', fontsize=18)
    plt.xlabel('Idade')
    plt.ylabel('Frequência')
    plt.grid(axis='y', linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    salvar_grafico(titulo, descricao)

# --- GERAR E SALVAR GRÁFICOS COM DESCRIÇÕES DETALHADAS ---


# Gráficos de perfil demográfico
plotar_barras(df_short, 'escolaridade', 'Distribuição por Escolaridade',
              'Este gráfico de barras horizontais detalha o perfil educacional dos entrevistados, ordenando os níveis de escolaridade por frequência. Permite identificar rapidamente os graus de instrução mais comuns e mais raros na amostra.')

plotar_barras(df_short, 'estado_civil', 'Distribuição por Estado Civil',
              'O gráfico de barras exibe a distribuição do estado civil dos participantes da pesquisa, mostrando a contagem e o percentual de cada categoria, como "Casado(a)", "Solteiro(a)", entre outras.')

plotar_barras(df_short, 'raca_cor', 'Distribuição por Raça/Cor',
              'Esta visualização apresenta o perfil de raça/cor autodeclarada pelos entrevistados. O gráfico ordena as categorias da mais para a menos frequente, oferecendo um panorama da composição racial da amostra.')

# Encurtar o nome da categoria de religião antes de plotar
label_longo = 'Outra religião (Mórmon, Testemunha de Jeová, Seisho-No-Iê, Messiânica, Perfeita Liberdade, Budista, Santo daime, Esotérica)'
label_curto = 'Outra religião'
df_short['religiao'] = df_short['religiao'].replace(label_longo, label_curto)

plotar_pizza(df_short, 'religiao', 'Distribuição por Religião',
             'Este gráfico de pizza ilustra a distribuição percentual das afiliações religiosas. A fatia "Outras" agrupa as religiões com menor representatividade para uma visualização mais limpa das categorias principais.')

# Distribuição de idade dos residentes
plotar_histograma_melhorado(idades_residentes['idade'], 'Distribuição de Idade de Todos os Residentes',
                            'Este histograma apresenta a distribuição demográfica de todos os residentes mencionados na pesquisa (entre 1 e 100 anos). Linhas verticais indicam a idade média e a mediana, oferecendo um resumo central da distribuição etária.')

# Renda
plotar_histograma(df_short['renda_familiar'], 'Distribuição de Renda Familiar',
                  'O histograma mostra a frequência de cada categoria de renda familiar na amostra. A visualização permite identificar os níveis de renda mais comuns e a dispersão geral dos dados. A média e a mediana são destacadas.')

plotar_boxplot(df_short['renda_familiar'], 'Boxplot da Renda Familiar',
               'Este boxplot ilustra a distribuição da renda familiar dos entrevistados. Ele destaca a mediana, a concentração de 50% dos dados (o comprimento da caixa) e a dispersão geral dos valores, sendo útil para identificar a simetria da distribuição e possíveis outliers.')

# Renda por escolaridade
plt.figure(figsize=(12, 7))
sns.boxplot(data=df_short, x='renda_familiar', y='escolaridade', order=[
    'Sem instrução',
    'Ensino fundamental incompleto (1º Grau incomp.)',
    'Ensino fundamental completo (1º Grau completo)',
    'Ensino médio incompleto (2º Grau incomp.)',
    'Ensino médio completo (2º Grau completo)',
    'Superior incompleto (Universidade / Faculdade incompleto)',
    'Superior completo (Universidade / Faculdade completo)',
    'Pós-graduação',
    'Não sabe/Não lembra'
], palette='magma')
plt.title('Renda Familiar por Nível de Escolaridade', fontsize=16)
plt.xlabel('Renda Familiar (Categorias)')
plt.ylabel('Escolaridade')
plt.tight_layout()
salvar_grafico('Renda Familiar por Nível de Escolaridade',
               'O conjunto de boxplots explora a relação entre o nível de escolaridade e a distribuição da renda familiar. Cada boxplot representa um nível educacional, ilustrando como a faixa de renda tende a variar conforme avança o grau de instrução.')

# Percepção da criminalidade por raça/cor
plt.figure(figsize=(12, 7))
sns.countplot(data=df_short, x='percepcao_criminalidade',
              hue='raca_cor', palette='rocket')
plt.title('Percepção da Criminalidade por Raça/Cor', fontsize=16)
plt.xlabel('Nos últimos 12 meses, a criminalidade...')
plt.ylabel('Contagem')
plt.legend(title='Raça/Cor')
plt.tight_layout()
salvar_grafico('Percepção da Criminalidade por Raça-Cor',
               'O gráfico de barras agrupadas analisa como a percepção sobre a criminalidade varia entre os diferentes grupos de raça/cor, permitindo a comparação direta de suas percepções para cada categoria de resposta.')

# Correlação entre variáveis numéricas
colunas_numericas = ['adultos_no_domicilio',
                     'mulheres_adultas', 'menores_no_domicilio', 'renda_familiar']
matriz_corr = df_short[colunas_numericas].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Mapa de Calor de Correlação', fontsize=16)
plt.tight_layout()
salvar_grafico('Mapa de Calor de Correlação',
               'O mapa de calor visualiza a correlação linear entre variáveis numéricas do domicílio. Valores próximos de 1 ou -1 indicam uma forte correlação, enquanto valores próximos de 0 indicam uma fraca correlação.')

# %%
# Dicionário para renomear as colunas de criminalidade e demografia
mapa_nomes_crime = {
    'o(a) sr(a) diria que, nos últimos 12 meses, a criminalidade na sua cidade aumentou, diminuiu ou ficou igual?': 'percepcao_crime_cidade',
    'pensando na sua vizinhança, o(a) sr.(a) teme ser assaltado(a)?': 'medo_assalto_vizinhanca',
    'de uma maneira geral, em se tratando da polícia militar o(a) sr(a): confia muito; confia um pouco ou não confia?': 'confianca_pm',
    'alguma vez, alguém roubou algum objeto seu, com o uso de violência ou ameaça?': 'vitima_roubo_objeto',
    'alguma vez, o(a) sr(a) teve qualquer evidência de que alguém furtou qualquer um outro(s) bem(ns) do(a) sr(a), isto é, levou sem utilizar força ou fazer ameaça?': 'vitima_furto_objeto',
    'nos últimos 12 meses, o(a) sr(a) foi vítima de insulto, humilhação ou xingamento (ofensa verbal)?': 'vitima_insulto_12m',
    'nos últimos 12 meses, o(a) sr(a) foi vítima de amedrontamento ou perseguição?': 'vitima_perseguicao_12m',
    'alguma vez, alguém furtou o(s) seu(s) carro(s), caminhão(ões) ou caminhonete(s) ou de alguém de sua casa, isto é, levou sem utilizar força ou fazer ameaça?': 'vitima_furto_veiculo',
}

# Verifica quais colunas do dicionário existem no DataFrame
colunas_existentes = [
    col for col in mapa_nomes_crime.keys() if col in df_short.columns]
colunas_faltando = [col for col in mapa_nomes_crime.keys()
                    if col not in df_short.columns]

if colunas_faltando:
    print("AVISO: As seguintes colunas não existem em df_short e serão ignoradas:")
    for col in colunas_faltando:
        print(f" - {col}")

# Renomeia apenas as colunas existentes
df_crime = df_short.rename(columns=mapa_nomes_crime)

# Seleciona apenas as colunas renomeadas que existem
colunas_selecionadas = [mapa_nomes_crime[col] for col in colunas_existentes]
df_crime = df_crime[colunas_selecionadas]

print("DataFrame para análise de crime criado com sucesso!")


mapa_sim_nao = {1: 'Sim', 2: 'Não', 0: 'Não Respondeu'}
mapa_confianca = {1: 'Confia Muito', 2: 'Confia um Pouco',
                  3: 'Não Confia', 0: 'Não Respondeu'}

# Aplicar os mapeamentos para criar colunas textuais para os gráficos
# Usamos .get(x, x) para manter o valor original caso ele não esteja no mapa
df_crime['medo_assalto_vizinhanca_texto'] = df_crime['medo_assalto_vizinhanca'].apply(
    lambda x: mapa_sim_nao.get(x, x))
df_crime['confianca_pm_texto'] = df_crime['confianca_pm'].apply(
    lambda x: mapa_confianca.get(x, x))

print("Colunas de texto criadas para melhorar a visualização.")

df_crime.head(10)

# %%
colunas_vitimizacao = [
    'vitima_roubo_objeto',
    'vitima_furto_objeto',
    'vitima_insulto_12m',
    'vitima_perseguicao_12m',
    'vitima_furto_veiculo'
]


def plotar_respostas_unicas(dataframe, coluna, titulo, descricao):
    plt.figure(figsize=(10, 6))
    sns.countplot(y=coluna, data=dataframe,
                  order=dataframe[coluna].value_counts().index, palette='crest_r')
    plt.title(titulo, fontsize=16)
    plt.xlabel('Número de Entrevistados')
    plt.ylabel('')
    plt.tight_layout()
    salvar_grafico(titulo, descricao)


# 1. Gráficos de respostas únicas
plotar_respostas_unicas(
    df_crime,
    'medo_assalto_vizinhanca_texto',
    'Medo de ser Assaltado(a) na Vizinhança',
    'O gráfico exibe a contagem total de respostas à pergunta sobre o medo de ser assaltado na vizinhança, permitindo visualizar a proporção de entrevistados que se sentem seguros ou inseguros em seu entorno.'
)

plotar_respostas_unicas(
    df_crime,
    'confianca_pm_texto',
    'Nível de Confiança na Polícia Militar',
    'Esta visualização apresenta a distribuição das respostas sobre o nível de confiança na Polícia Militar. As categorias (Confia Muito, Confia um Pouco, Não Confia) delineiam o perfil da percepção popular sobre a instituição.'
)

# 2. Ranking de vitimização
df_vitimas_melted = df_crime.copy()
df_vitimas_melted['escolaridade'] = df_short['escolaridade']
df_vitimas_melted = df_vitimas_melted.melt(
    id_vars='escolaridade',
    value_vars=colunas_vitimizacao,
    var_name='tipo_crime',
    value_name='resposta_num'
)

df_ranking = df_vitimas_melted[df_vitimas_melted['resposta_num'] == 1]
ranking_geral = df_ranking['tipo_crime'].value_counts(
    normalize=True).mul(100).sort_values(ascending=False)

plt.figure(figsize=(12, 7))
sns.barplot(x=ranking_geral.values, y=ranking_geral.index, palette='Reds_r')
plt.title('Ranking de Vitimização (Percentual de Vítimas por Incidente)', fontsize=16)
plt.xlabel('Percentual de Entrevistados (%)')
plt.ylabel('Tipo de Incidente')
plt.tight_layout()
salvar_grafico('Ranking de Vitimização',
               'Este gráfico ranqueia os tipos de incidentes de vitimização com base no percentual de entrevistados que relataram tê-los sofrido. A visualização permite identificar rapidamente os crimes mais comuns na amostra.')

# 3. Medo por escolaridade
df_crime['escolaridade_texto'] = df_short['escolaridade']

plt.figure(figsize=(12, 7))
sns.countplot(data=df_crime, y='escolaridade_texto',
              hue='medo_assalto_vizinhanca_texto', palette='viridis')
plt.title('Medo de Ser Assaltado na Vizinhança por Escolaridade', fontsize=16)
plt.xlabel('Número de Entrevistados')
plt.ylabel('Escolaridade')
plt.legend(title='Teme ser assaltado(a)?')
plt.tight_layout()
salvar_grafico('Medo de Assalto por Escolaridade',
               'Este gráfico compara as respostas sobre o medo de ser assaltado na vizinhança entre os diferentes níveis de escolaridade, permitindo analisar se a percepção de segurança varia com o grau de instrução.')

# 4. Índice de vitimização
for col in colunas_vitimizacao:
    df_crime[f'{col}_num'] = df_crime[col].apply(lambda x: 1 if x == 1 else 0)

colunas_vitimizacao_num = [f'{col}_num' for col in colunas_vitimizacao]
df_crime['indice_vitimizacao'] = df_crime[colunas_vitimizacao_num].sum(axis=1)

# Exibe a distribuição no console (opcional)
print("Distribuição do Índice de Vitimização:")
print(df_crime['indice_vitimizacao'].value_counts())

plt.figure(figsize=(12, 7))
sns.boxplot(data=df_crime, x='indice_vitimizacao',
            y='escolaridade_texto', palette='plasma')
plt.title('Índice de Vitimização por Escolaridade', fontsize=16)
plt.xlabel('Índice de Vitimização (Nº de incidentes diferentes sofridos)')
plt.ylabel('Escolaridade')
plt.tight_layout()
salvar_grafico('Índice de Vitimização por Escolaridade',
               'Este gráfico de boxplots analisa a distribuição do "Índice de Vitimização" entre os diferentes níveis de escolaridade. O índice representa o número de tipos de incidentes diferentes sofridos por uma pessoa, permitindo investigar se existe uma correlação entre o nível educacional e a propensão a ser vítima de múltiplos crimes.')

# %% [markdown]
# ## Gerar pdf

# %%

# --- CONFIGURAÇÃO INICIAL E ESTRUTURA DE DADOS ---

output_logo_dir = '../../logo/'

os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------------
#   INFORMAÇÕES DOS GRÁFICOS EXTRAÍDAS DO PDF DE EXEMPLO
#   !! SUBSTITUA OS NOMES DOS ARQUIVOS .PNG PELOS SEUS !!
# -------------------------------------------------------------------------
graficos_info = [
    {
        "id_grafico": "Gráfico 1A: Perfil por Sexo (Barras)",
        "caminho": Descricoes[0]['caminho'],
        "objetivo": "Comparar a variabilidade (inconstância) das estimativas de vitimização entre homens e mulheres para cada tipo de crime principal.",
        "o_que_mostra": "O gráfico exibe barras agrupadas por tipo de crime. Dentro de cada grupo, compara-se o Coeficiente de Variação (CV) médio para 'homens' e 'mulheres'. Barras mais altas indicam maior instabilidade e dispersão nos dados para aquele grupo.",
        "analise": "A análise deste gráfico permite identificar se há um sexo cuja vitimização é estimada com menos consistência. Por exemplo, pode-se observar se o CV para mulheres vítimas de agressão é maior que para homens, sugerindo uma variação regional mais acentuada nos dados desse grupo, o que exige cautela ao generalizar os dados nacionais."
    },
    {
        "id_grafico": "Gráfico 1B: Perfil por Cor/Raça (Barras)",
        "caminho": Descricoes[1]['caminho'],
        "objetivo": "Comparar a variabilidade das estimativas de vitimização entre os perfis de cor/raça ('branca' e 'preta/parda') para cada tipo de crime.",
        "o_que_mostra": "Similar ao gráfico anterior, este agrupa por crime e compara o CV médio para os grupos 'branca' e 'preta/parda'. A altura da barra representa a instabilidade da estimativa.",
        "analise": "Este gráfico é crucial para analisar disparidades raciais na consistência dos dados. É comum observar um CV sistematicamente mais elevado para a população 'preta/parda', indicando que as estimativas de vitimização para este grupo são mais heterogêneas entre as localidades, o que pode mascarar realidades locais distintas."
    },
    {
        "id_grafico": "Gráfico 2: Perfil por Faixa Etária (Linhas)",
        "caminho": Descricoes[2]['caminho'],
        "objetivo": "Analisar como a variabilidade das estimativas de vitimização se comporta através das diferentes faixas etárias para cada tipo de crime.",
        "o_que_mostra": "O gráfico apresenta a tendência da variabilidade (CV médio) ao longo de várias faixas etárias. Cada linha representa um tipo de crime. Picos na linha indicam maior instabilidade para aquela faixa etária.",
        "analise": "As linhas revelam picos de instabilidade em idades específicas. Frequentemente, a faixa de '16 a 24 anos' exibe o maior CV, especialmente para roubos, refletindo maior variação geográfica na vitimização desse grupo. A tendência pode mostrar se a confiabilidade dos dados aumenta ou diminui com a idade."
    },
    {
        "id_grafico": "Gráfico 3: Motivos para Não Registrar Ocorrência (Barras Empilhadas)",
        "caminho": Descricoes[3]['caminho'],
        "objetivo": "Revelar e comparar a distribuição percentual dos motivos que levaram as vítimas a não procurarem a polícia, distinguindo por tipo de crime.",
        "o_que_mostra": "Cada barra horizontal (100%) representa um tipo de crime. Os segmentos coloridos mostram a proporção de cada motivo. O tamanho do segmento indica sua importância relativa.",
        "analise": "A análise aponta para diferentes barreiras de acesso à justiça. Para furtos, o motivo 'não era importante' tende a dominar, sugerindo baixa percepção de dano. Para agressões, 'medo de represálias' ou 'não acreditavam na polícia' podem ter maior peso, indicando uma falha de confiança ou segurança no sistema."
    },
    {
        "id_grafico": "Gráfico 4A: Heatmap Comparativo por Sexo",
        "caminho": Descricoes[4]['caminho'],
        "objetivo": "Fornecer uma visualização rápida da intensidade da variabilidade dos dados para cada combinação de tipo de crime e sexo.",
        "o_que_mostra": "Uma matriz onde linhas são os crimes e colunas são os sexos. A cor de cada célula indica a magnitude do CV, com cores mais intensas significando maior variabilidade. O valor numérico exato está anotado na célula.",
        "analise": "O heatmap permite identificar rapidamente os 'pontos quentes'. Por exemplo, a célula 'Agressão-Mulheres' pode ter a cor mais intensa, indicando que esta é a combinação com a estimativa mais instável em todo o conjunto de dados, sendo um ponto crítico para análise."
    },
    {
        "id_grafico": "Gráfico 4B: Heatmap Comparativo por Cor/Raça",
        "caminho": Descricoes[5]['caminho'],
        "objetivo": "Fornecer uma visualização rápida da intensidade da variabilidade dos dados para cada combinação de tipo de crime e cor/raça.",
        "o_que_mostra": "Uma matriz onde linhas são os crimes e colunas são os grupos de cor/raça. A cor de cada célula indica a magnitude do CV, com cores mais intensas significando maior variabilidade.",
        "analise": "Este heatmap expõe qual crime apresenta maior instabilidade de dados para qual grupo racial. Uma célula como 'Roubo Preta/Parda' com valor elevado sugere que as médias nacionais para este cruzamento devem ser interpretadas com extrema cautela, pois não representam bem as diversas realidades regionais."
    },
    {
        "id_grafico": "Gráfico 5: Heatmap de Correlação (Crime de Agressão)",
        "caminho": Descricoes[6]['caminho'],
        "objetivo": "Investigar se a variabilidade nas estimativas de vitimização por agressão dos diferentes perfis demográficos se movem em conjunto.",
        "o_que_mostra": "A matriz exibe o coeficiente de correlação (de 1 a 1) entre os CVs de todos os pares de perfis. Cores quentes (próximas de 1) indicam correlação positiva; cores frias (próximas de 1) indicam correlação negativa.",
        "analise": "Uma correlação positiva forte (ex: > 0.7) entre 'homens' e 'mulheres' significa que, nas regiões onde a estimativa para homens é instável, a para mulheres também tende a ser. Isso pode sugerir que fatores geográficos, e não apenas o perfil, causam a instabilidade dos dados de agressão."
    },
    {
        "id_grafico": "Gráfico 6: Distribuição com Boxplot",
        "caminho": Descricoes[7]['caminho'],
        "objetivo": "Comparar a distribuição completa (mediana, quartis, outliers) do CV 'Total' entre os tipos de crime.",
        "o_que_mostra": "Cada 'caixa' representa um tipo de crime. A linha na caixa é a mediana; a altura da caixa é a dispersão dos 50% centrais dos dados; as hastes indicam o alcance geral e pontos isolados são outliers.",
        "analise": "O boxplot vai além da média. Pode revelar que, embora 'Roubo' tenha uma média de CV similar a 'Furto', sua 'caixa' é muito mais alta, indicando maior inconsistência e dispersão nos dados. Outliers apontam para UFs com variabilidade excepcionalmente alta."
    },
    {
        "id_grafico": "Gráfico 7C: Radar Comparativo por Sexo + Cor/Raça",
        "caminho": Descricoes[8]['caminho'],
        "objetivo": "Unificar a análise visual da variabilidade das estimativas de vitimização combinando os fatores de sexo e cor/raça, permitindo observar perfis interseccionais.",
        "o_que_mostra": "O gráfico exibe um radar com quatro perfis combinados: 'Homem Branco', 'Homem Preto/Pardo', 'Mulher Branca' e 'Mulher Preta/Parda'. Para cada tipo de crime, é desenhado um polígono cuja forma reflete a distribuição da variabilidade das estimativas entre esses perfis. Perfis com maior distância do centro apresentam maior instabilidade.",
        "analise": "Esse radar interseccional permite identificar, de forma integrada, quais perfis demográficos estão mais sujeitos à instabilidade nas estatísticas de vitimização. Por exemplo, se o polígono de 'Agressão' se estende mais no eixo 'Mulher Preta/Parda', isso indica que as estimativas para esse perfil são mais variáveis, destacando a necessidade de abordagens políticas e analíticas interseccionais."
    },
    {
        "id_grafico": "Gráfico 8A: Ranking de Perfis por Sexo",
        "caminho": Descricoes[9]['caminho'],
        "objetivo": "Classificar os perfis de sexo com base na sua variabilidade de dados média, agregando os resultados de todos os crimes.",
        "o_que_mostra": "Um gráfico de barras horizontais simples onde a barra mais longa pertence ao perfil de sexo cuja estimativa de vitimização é, na média geral, a mais instável.",
        "analise": "Este gráfico fornece uma conclusão direta sobre qual sexo tem os dados mais heterogêneos no geral. A diferença no comprimento das barras quantifica essa disparidade na confiabilidade média das estimativas."
    },
    {
        "id_grafico": "Gráfico 8B: Ranking de Perfis por Cor/Raça",
        "caminho": Descricoes[10]['caminho'],
        "objetivo": "Classificar os perfis de cor/raça com base na sua variabilidade de dados média, agregando os resultados de todos os crimes.",
        "o_que_mostra": "Um gráfico de barras horizontais simples onde a barra mais longa pertence ao perfil de cor/raça cuja estimativa de vitimização é, na média geral, a mais instável.",
        "analise": "O ranking agregado por raça geralmente evidencia a maior vulnerabilidade estatística da população 'preta/parda'. A barra significativamente maior para este grupo indica que as políticas públicas baseadas em dados agregados podem não atender adequadamente às suas necessidades específicas."
    },
    {
        "id_grafico": "Gráfico 9A: Comparativo Homens vs. Mulheres (Dumbbell)",
        "caminho": Descricoes[11]['caminho'],
        "objetivo": "Isolar e comparar diretamente a diferença na variabilidade das estimativas entre homens e mulheres para cada tipo de crime.",
        "o_que_mostra": "Para cada crime, dois pontos são plotados (um para homens, outro para mulheres). Uma linha conecta os pontos, destacando a magnitude da diferença ('gap') entre os sexos.",
        "analise": "O dumbbell plot é excelente para visualizar o 'gap' de instabilidade. O crime com a linha de conexão mais longa indica uma diferença muito acentuada na confiabilidade dos dados entre homens e mulheres, sinalizando a necessidade de análises aprofundadas."
    },
    {
        "id_grafico": "Gráfico 9B: Comparativo Branca vs. Preta/Parda (Dumbbell)",
        "caminho": Descricoes[12]['caminho'],
        "objetivo": "Isolar e comparar diretamente a diferença na variabilidade das estimativas entre os grupos de cor/raça para cada tipo de crime.",
        "o_que_mostra": "Para cada crime, dois pontos são plotados (um para 'branca', outro para 'preta/parda'). Uma linha conecta os pontos, evidenciando a disparidade racial na consistência dos dados.",
        "analise": "Este gráfico expõe a desigualdade na precisão dos dados. Se o ponto 'preta/parda' estiver consistentemente à direita do ponto 'branca', isso indica uma fragilidade estrutural na coleta ou na homogeneidade dos dados para esse grupo."
    },
    {
        "id_grafico": "Gráfico 10: Variação Geográfica (Facet Grid)",
        "caminho": Descricoes[13]['caminho'],
        "objetivo": "Desagregar a análise nacional para investigar como o perfil de variabilidade das vítimas de agressão se comporta em cada Unidade da Federação (UF).",
        "o_que_mostra": "Uma grade de múltiplos mini-gráficos de barras. Cada mini-gráfico representa uma UF, mostrando os CVs para cada perfil. Permite comparar os padrões locais com a média nacional.",
        "analise": "A análise por UF é fundamental para a ação local. Pode-se identificar que, embora a média nacional do CV para 'homens' seja baixa, em uma UF específica ela seja a mais alta, indicando que as estratégias de segurança e de coleta de dados devem ser regionalizadas."
    }
]


class PDF(FPDF):
    def header(self):
        if self.page_no() > 2:
            self.set_font('Helvetica', 'B', 15)
            self.set_text_color(40, 40, 40)
            self.cell(
                0, 8, 'Relatório de Análise de Criminalidade no Brasil - 2010', 0, 1, 'C')
            self.set_font('Helvetica', '', 11)
            self.set_text_color(100, 100, 100)
            self.cell(
                0, 6, 'Estudo da variabilidade nas estimativas de vitimização', 0, 1, 'C')
            self.ln(5)
            self.set_draw_color(180, 180, 180)
            self.set_line_width(0.3)
            self.line(self.l_margin, self.get_y(),
                      self.w - self.r_margin, self.get_y())
            self.ln(7)

    def footer(self):
        if self.page_no() > 2:
            self.set_y(-15)
            self.set_font('Helvetica', 'I', 8)
            self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'R')

# --- FUNÇÃO AUXILIAR PARA ESCREVER SEÇÕES ---


def write_section(pdf, title, content):
    if title:
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 7, title, ln=True)
    pdf.set_font('Helvetica', '', 11)
    pdf.multi_cell(0, 5, content)
    pdf.ln(4)

# --- FUNÇÃO: ADICIONAR CAPA ---


def add_capa(pdf):
    pdf.add_page()
    logo_url = "https://cesecseguranca.com.br/wp-content/uploads/2016/04/LOGO-CRISP.png"
    response = requests.get(logo_url)
    logo_img = Image.open(BytesIO(response.content))
    logo_path = os.path.join(output_logo_dir, "crisp_logo.png")
    logo_img.save(logo_path)
    pdf.image(logo_path, x=65, y=20, w=80)

    pdf.set_font("Helvetica", 'B', 18)
    pdf.ln(85)
    pdf.cell(0, 10, "Relatório de Análise -", ln=True, align='C')
    pdf.cell(0, 10, "Pesquisa Nacional de Vitimização", ln=True, align='C')
    pdf.set_font("Helvetica", '', 13)
    pdf.cell(0, 10, "(PM 643283 A - Tipo I)", ln=True, align='C')
    pdf.ln(5)
    pdf.set_font("Helvetica", '', 11)
    pdf.cell(0, 10, "Projeto PM3283 - Dados coletados em Abril/2010",
             ln=True, align='C')
    pdf.ln(15)
    pdf.set_font("Helvetica", 'I', 10)
    pdf.cell(0, 10, f"{datetime.today().strftime('%d/%m/%Y')}",
             ln=True, align='C')

# --- FUNÇÃO: ADICIONAR SUMÁRIO ---


def add_sumario(pdf, graficos_info):
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, "Sumário", ln=True, align='C')
    pdf.ln(10)
    for idx, item in enumerate(graficos_info, start=1):
        pdf.set_font("Helvetica", '', 12)
        pdf.cell(0, 8, f"{idx}. {item['id_grafico']}", ln=True)

# --- FUNÇÃO: ADICIONAR PÁGINA DE GRÁFICO ---


def add_grafico(pdf, item):
    pdf.add_page()

    # Título da seção
    write_section(pdf, item['id_grafico'], "")

    # Descrição textual
    write_section(pdf, "Objetivo:", item['objetivo'])
    write_section(pdf, "O que o Gráfico Mostra:", item['o_que_mostra'])
    write_section(pdf, "Análise do Gráfico:", item['analise'])

    # Imagem
    if os.path.exists(item['caminho']):
        pdf.image(item['caminho'], x=30, y=135, w=150)
    else:
        pdf.set_y(135)
        pdf.set_font('Helvetica', 'B', 12)
        pdf.multi_cell(
            0, 10, f"ERRO: Imagem não encontrada:\n{item['caminho']}", border=1, align='C')

# --- FUNÇÃO: ADICIONAR ANÁLISE FINAL ---


def add_analise_consolidada(pdf):
    pdf.add_page()
    pdf.set_y(25)
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, "Análise Geral Consolidada", ln=True, align='C')
    pdf.ln(10)
    texto_final = (
        "A análise consolidada dos gráficos revela uma narrativa complexa sobre a estabilidade das estimativas de vitimização no Brasil. "
        "O Coeficiente de Variação (CV) indica o grau de imprecisão dos dados, servindo como um importante indicador para a confiabilidade das estatísticas de criminalidade.\n\n"
        "A separação da análise por sexo e cor/raça deixa claro que a variabilidade não é uniforme. Perfis demográficos específicos apresentam consistentemente CVs mais elevados, o que pode mascarar realidades locais diversas.\n\n"
        "Destaca-se o gráfico interseccional (7C), que evidencia que perfis como 'Mulher Preta/Parda' podem apresentar maior instabilidade nas estatísticas em vários tipos de crime. Isso reforça a necessidade de abordagens que considerem as intersecções sociais.\n\n"
        "Em suma, os dados demonstram heterogeneidade significativa, e políticas públicas devem ser sensíveis a essas múltiplas dimensões para promover justiça e segurança mais eficazes."
    )
    write_section(pdf, "", texto_final)


# --- INICIALIZAÇÃO DO PDF ---
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# --- EXECUÇÃO DAS ETAPAS ---
add_capa(pdf)
add_sumario(pdf, graficos_info)

for item in graficos_info:
    add_grafico(pdf, item)

add_analise_consolidada(pdf)


# --- SALVAR PDF ---
try:
    # 'Relatorio_Analise_Vitimizacao_CRISP'
    caminho_final_pdf = os.path.join(
        output_dir, 'Relatorio_Analise_Vitimizacao_CRISP.pdf')
    pdf.output(caminho_final_pdf)
    print(f"Relatório PDF gerado com sucesso em: {caminho_final_pdf}")

    try:
        shutil.rmtree(output_logo_dir)
    except Exception as e:
        print(f"Erro ao remover a pasta {output_logo_dir}: {e}")
    try:
        shutil.rmtree(temp_img_dir)
    except Exception as e:
        print(f"Erro ao remover a pasta {temp_img_dir}: {e}")
except Exception as e:
    print(f"Erro ao salvar o PDF: {e}")
