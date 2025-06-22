import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from fpdf import FPDF
import shutil

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# --- Carregar o arquivo de dados original (Belo Horizonte 2002) ---
caminho_dados_bh = '../../dados_tratados/excel/belo_horrizonte_2002.xlsx'
df_original = pd.read_excel(caminho_dados_bh)
print(f"Dados de Belo Horizonte (2002) carregados. Total de {len(df_original)} registros.")

# --- Carregar o novo arquivo de dados (Minas Gerais) ---
caminho_dados_mg = '../../dados_tratados/excel/percepcao_medoMG.xlsx'
df_mg = pd.read_excel(caminho_dados_mg)
print(f"Dados de Minas Gerais carregados. Total de {len(df_mg)} registros.")


colunas_renomeadas = {
    'Sexo': 'sexo',
    'faixas de idade': 'faixa_idade',
    'Estado civil': 'estado_civil',
    'cor ou raça': 'cor_raca',
    'curso mais elevado frequentado': 'escolaridade',
    'ESTRATO': 'estrato_bairro',
    'Risco de roubo (grande, médio e pequeno)': 'risco_roubo',
    'Risco de agressão': 'risco_agressao',
    'Risco de sequestro': 'risco_sequestro'
}
df_original.rename(columns=colunas_renomeadas, inplace=True)

# --- Combinar os dois DataFrames ---
df_combinado = pd.concat([df_original, df_mg], ignore_index=True)

# --- Limpeza e Preparação (Aplicado ao DataFrame combinado) ---
colunas_essenciais = ['sexo', 'faixa_idade', 'estrato_bairro']
df_combinado.dropna(subset=colunas_essenciais, inplace=True)

print("\nDataFrames combinados com sucesso!")
print(f"Total de registros para análise: {len(df_combinado)}")
print("\nPrimeiras 5 linhas do dataset combinado:")
print(df_combinado.head())


# ===================================================================
# CÉLULA 1: ANÁLISE DE DADOS E GERAÇÃO DOS GRÁFICOS
# ===================================================================

print("Iniciando a geração das análises...")

# --- SETUP INICIAL ---
pasta_temp = 'temp_graficos'
if not os.path.exists(pasta_temp):
    os.makedirs(pasta_temp)

df_analise = df_combinado
colunas_risco = ['risco_roubo', 'risco_agressao', 'risco_sequestro']
nomes_graficos = [] 

# --- Análise 1: Percepção de Risco por Sexo ---
print("--> Gerando Análise de Risco por Sexo...")
df_risco_sexo = df_analise.groupby('sexo')[colunas_risco].mean().reset_index()
df_risco_sexo_melted = df_risco_sexo.melt(id_vars='sexo', var_name='tipo_risco', value_name='percepcao_media_risco')
plt.figure(figsize=(12, 7))
sns.barplot(data=df_risco_sexo_melted, x='tipo_risco', y='percepcao_media_risco', hue='sexo', palette='magma')
plt.title('Percepção Média de Risco por Sexo', fontsize=16, fontweight='bold')
plt.xlabel('Tipo de Crime', fontsize=12)
plt.ylabel('Percepção Média de Risco (escala)', fontsize=12)
plt.xticks(ticks=[0, 1, 2], labels=['Roubo', 'Agressão', 'Sequestro'])
plt.legend(title='Sexo')
plt.tight_layout()
caminho_grafico_sexo = os.path.join(pasta_temp, 'grafico_risco_sexo.png')
plt.savefig(caminho_grafico_sexo)
nomes_graficos.append(caminho_grafico_sexo)
plt.close()
print("--> Tabela e Gráfico de Risco por Sexo prontos.")


# --- Análise 2: Percepção de Risco por Bairro ---
print("\n--> Gerando Análise de Risco por Bairro...")
df_risco_bairro = df_analise.groupby('estrato_bairro')[colunas_risco].mean().reset_index()
df_risco_bairro_melted = df_risco_bairro.melt(id_vars='estrato_bairro', var_name='tipo_risco', value_name='percepcao_media_risco')
plt.figure(figsize=(12, 7))
sns.barplot(data=df_risco_bairro_melted, x='tipo_risco', y='percepcao_media_risco', hue='estrato_bairro', palette='crest')
plt.title('Percepção Média de Risco por Tipo de Bairro', fontsize=16, fontweight='bold')
plt.xlabel('Tipo de Crime', fontsize=12)
plt.ylabel('Percepção Média de Risco (escala)', fontsize=12)
plt.xticks(ticks=[0, 1, 2], labels=['Roubo', 'Agressão', 'Sequestro'])
plt.legend(title='Estrato do Bairro')
plt.tight_layout()
caminho_grafico_bairro = os.path.join(pasta_temp, 'grafico_risco_bairro.png')
plt.savefig(caminho_grafico_bairro)
nomes_graficos.append(caminho_grafico_bairro)
plt.close()
print("--> Tabela e Gráfico de Risco por Bairro prontos.")


# --- Análise 3: Percepção de Risco por Faixa de Idade ---
print("\n--> Gerando Análise de Risco por Faixa de Idade...")
df_risco_idade = df_analise.groupby('faixa_idade')[colunas_risco].mean().reset_index()
df_risco_idade_melted = df_risco_idade.melt(id_vars='faixa_idade', var_name='tipo_risco', value_name='percepcao_media_risco')
plt.figure(figsize=(12, 7))
sns.barplot(data=df_risco_idade_melted, x='tipo_risco', y='percepcao_media_risco', hue='faixa_idade', palette='rocket')
plt.title('Percepção Média de Risco por Faixa de Idade', fontsize=16, fontweight='bold')
plt.xlabel('Tipo de Crime', fontsize=12)
plt.ylabel('Percepção Média de Risco (escala)', fontsize=12)
plt.xticks(ticks=[0, 1, 2], labels=['Roubo', 'Agressão', 'Sequestro'])
plt.legend(title='Faixa de Idade', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
caminho_grafico_idade = os.path.join(pasta_temp, 'grafico_risco_idade.png')
plt.savefig(caminho_grafico_idade, bbox_inches='tight')
nomes_graficos.append(caminho_grafico_idade)
plt.close()
print("--> Tabela e Gráfico de Risco por Faixa de Idade prontos.")


# --- Análise 4: Matriz de Correlação Numérica entre Riscos ---
print("\n--> Gerando Matriz de Correlação...")
df_correlacao = df_analise[colunas_risco].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(df_correlacao, annot=True, cmap='viridis', fmt=".2f", linewidths=.5)
plt.title('Matriz de Correlação entre Percepções de Risco', fontsize=16, fontweight='bold')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
caminho_grafico_correlacao = os.path.join(pasta_temp, 'grafico_matriz_correlacao.png')
plt.savefig(caminho_grafico_correlacao)
nomes_graficos.append(caminho_grafico_correlacao)
plt.close()
print("--> Matriz Numérica (Heatmap) de Correlação pronta.")
print("\n--- Matriz de Correlação ---")
print(df_correlacao.round(2))

print("\n\nAnálises concluídas! Todos os gráficos foram salvos temporariamente.")


# ===================================================================
# CÉLULA 2: GERAÇÃO DO RELATÓRIO PDF FINAL
# ===================================================================

print("Iniciando a montagem do relatório em PDF...")

# Classe PDF personalizada com funções de ajuda
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        data_hoje = pd.to_datetime('today').strftime('%d de %B de %Y')
        self.cell(0, 10, f'Relatório de Percepção Social - {data_hoje}', 0, 1, 'C')
        self.ln(5)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 7, body.encode('latin-1', 'replace').decode('latin-1'))
        self.ln(5)
    def output_df_to_pdf(self, df):
        # Header
        self.set_font('Arial', 'B', 10)
        # Calcula a largura da célula baseada no número de colunas para garantir que a tabela caiba
        col_width = self.w / (len(df.columns) + 2) # Ajuste o divisor conforme necessário
        for col in df.columns:
            self.cell(col_width, 10, str(col).replace('_', ' ').title(), 1, 0, 'C')
        self.ln()
        # Body
        self.set_font('Arial', '', 10)
        for index, row in df.iterrows():
            for col in df.columns:
                value = row[col]
                if isinstance(value, float):
                    value = f'{value:.2f}'
                self.cell(col_width, 10, str(value), 1, 0, 'C')
            self.ln()
        self.ln(5)

# Iniciar PDF
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Análise Combinada de Percepção de Segurança', 0, 1, 'C')
pdf.ln(10)

# Descrição Geral da Análise
pdf.chapter_title('Introdução e Objetivo da Análise')
intro_text = (
    "Este relatório apresenta uma análise detalhada da percepção de segurança e risco de "
    "criminalidade em Minas Gerais, combinando dados de Belo Horizonte (2002) e outros "
    "dados de Minas Gerais. O objetivo é compreender como diferentes grupos demográficos "
    "(sexo, idade e localização do bairro) percebem o risco de crimes como roubo, agressão e sequestro, "
    "e identificar padrões e correlações que possam informar políticas públicas de segurança."
)
pdf.chapter_body(intro_text)

# Página 1: Risco por Sexo
pdf.chapter_title('1. Percepção Média de Risco por Sexo')
pdf.chapter_body(
    "Esta seção analisa como homens e mulheres percebem o risco de diferentes tipos de crime: "
    "roubo, agressão e sequestro. A tabela abaixo mostra os valores médios de percepção de risco "
    "para cada sexo e tipo de crime, enquanto o gráfico visualiza essas diferenças, tornando-as "
    "mais fáceis de comparar. Geralmente, as mulheres tendem a ter uma percepção de risco mais elevada em todas as categorias de crime."
)
pdf.output_df_to_pdf(df_risco_sexo.set_index('sexo').round(2))
pdf.image(caminho_grafico_sexo, w=170)
pdf.ln(5)


# Página 2: Risco por Bairro
pdf.add_page()
pdf.chapter_title('2. Percepção Média de Risco por Tipo de Bairro')
pdf.chapter_body(
    "Aqui, examinamos como a percepção de risco varia entre diferentes tipos de bairros "
    "(por exemplo, bairros violentos, não violentos, etc.). A tabela apresenta os valores "
    "médios de percepção de risco para roubo, agressão e sequestro em cada estrato de bairro. "
    "O gráfico complementar ilustra visualmente essas variações, ajudando a identificar "
    "se a percepção de insegurança é maior em áreas consideradas mais problemáticas."
)
pdf.output_df_to_pdf(df_risco_bairro.set_index('estrato_bairro').round(2))
pdf.image(caminho_grafico_bairro, w=170)
pdf.ln(5)

# Página 3: Risco por Faixa de Idade
pdf.add_page()
pdf.chapter_title('3. Percepção Média de Risco por Faixa de Idade')
pdf.chapter_body(
    "Esta seção detalha como diferentes faixas etárias percebem o risco de ser vítima de crimes. "
    "A tabela mostra a percepção média de risco para roubo, agressão e sequestro em cada faixa de idade. "
    "O gráfico correspondente permite visualizar rapidamente quais grupos etários se sentem "
    "mais ou menos seguros em relação a cada tipo de crime, o que pode influenciar a "
    "criação de programas de segurança direcionados."
)
pdf.output_df_to_pdf(df_risco_idade.set_index('faixa_idade').round(2))
pdf.image(caminho_grafico_idade, w=170)
pdf.ln(5)

# Página 4: Matriz de Correlação
pdf.add_page()
pdf.chapter_title('4. Matriz de Correlação entre Percepções de Risco')
pdf.chapter_body(
    "Esta matriz e o mapa de calor (heatmap) mostram a relação entre as percepções dos "
    "diferentes tipos de risco (roubo, agressão e sequestro). Os números variam de -1 a 1: "
    "valores próximos de 1 indicam que, se uma pessoa teme um tipo de crime, ela provavelmente "
    "também temerá o outro (correlação positiva forte). Valores próximos de -1 indicam o oposto "
    "(correlação negativa forte), e valores próximos de 0 indicam pouca ou nenhuma relação. "
    "Essa análise ajuda a entender se a sensação de insegurança é específica ou generalizada."
)
# Centralizar a imagem da matriz de correlação
pdf.image(caminho_grafico_correlacao, w=120, x=pdf.w / 2 - 60)
pdf.ln(5)


# Página 5: Conclusões
pdf.add_page()
pdf.chapter_title('5. Resultados e Conclusões')
texto_conclusao = (
    "A análise dos dados de percepção de segurança revela insights importantes sobre como diferentes "
    "grupos demográficos e sociais experienciam o medo em relação à criminalidade. A correlação positiva "
    "entre os tipos de risco sugere que a sensação de insegurança é um sentimento generalizado, não focado em um único tipo de crime.\\n\\n"
    "Observou-se que a percepção de risco não é homogênea, apresentando variações significativas "
    "quando segmentada por sexo, faixa etária e estrato do bairro de residência. "
    f"Por exemplo, a análise por sexo indicou que o público feminino percebe maior risco de sequestro (média de {df_risco_sexo[df_risco_sexo['sexo'] == 'Feminino']['risco_sequestro'].iloc[0]:.2f}) "
    f"em comparação ao público masculino (média de {df_risco_sexo[df_risco_sexo['sexo'] == 'Masculino']['risco_sequestro'].iloc[0]:.2f}). "
    f"Em relação aos bairros, os 'Bairros violentos' consistentemente mostram percepções de risco mais altas para todos os crimes. "
    f"Quanto à idade, as faixas etárias mais jovens, como 'de 10 a 20 anos', frequentemente exibem uma percepção de risco menor em comparação com grupos mais velhos.\\n\\n"
    "Estes resultados sugerem a necessidade de políticas de segurança pública que sejam sensíveis a "
    "essas diferentes percepções, focando esforços em localidades e grupos que demonstram maior "
    "sensação de insegurança."
)
pdf.chapter_body(texto_conclusao)


# --- Salvamento e Limpeza ---
pasta_analises = os.path.join('..', '..', 'analises')
if not os.path.exists(pasta_analises):
    os.makedirs(pasta_analises)
caminho_arquivo_pdf = os.path.join(pasta_analises, "relatorio_completo_percepcao_social.pdf")

try:
    pdf.output(caminho_arquivo_pdf)
    caminho_absoluto = os.path.abspath(caminho_arquivo_pdf)
    print(f"\nPDF gerado com sucesso!")
    print(f"O arquivo foi salvo em: {caminho_absoluto}")
except Exception as e:
    print(f"\nOcorreu um erro ao gerar o PDF: {e}")
finally:
    if os.path.exists(pasta_temp):
        shutil.rmtree(pasta_temp)
        print("\nArquivos temporários removidos.")