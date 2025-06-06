# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from fpdf import FPDF

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# %%
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

# %%
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

# %%
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
    def output_df_to_pdf(self, df):
        # Header
        self.set_font('Arial', 'B', 10)
        col_width = self.w / (len(df.columns) + 1.5)
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

# Página 1: Risco por Sexo
pdf.chapter_title('1. Análise da Percepção de Risco por Sexo')
pdf.output_df_to_pdf(df_risco_sexo.set_index('sexo'))
pdf.image(caminho_grafico_sexo, w=170)

# Página 2: Risco por Bairro
pdf.add_page()
pdf.chapter_title('2. Análise da Percepção de Risco por Bairro')
pdf.output_df_to_pdf(df_risco_bairro.set_index('estrato_bairro'))
pdf.image(caminho_grafico_bairro, w=170)

# Página 3: Risco por Faixa de Idade
pdf.add_page()
pdf.chapter_title('3. Análise da Percepção de Risco por Faixa de Idade')
pdf.output_df_to_pdf(df_risco_idade.set_index('faixa_idade'))
pdf.image(caminho_grafico_idade, w=170)

# Página 4: Matriz de Correlação
pdf.add_page()
pdf.chapter_title('4. Matriz Numérica de Correlação entre Riscos')
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 7, "A tabela e o mapa de calor abaixo mostram a correlação entre a percepção dos diferentes tipos de risco. Valores próximos de 1 indicam uma forte correlação positiva, significando que quem teme um tipo de crime também tende a temer o outro.")
pdf.ln(5)
pdf.image(caminho_grafico_correlacao, w=120, x=pdf.w / 2 - 60)

# Página 5: Conclusões
pdf.add_page()
pdf.chapter_title('5. Resultados e Conclusões')
texto_conclusao = (
    "A análise dos dados de percepção de segurança revela insights importantes sobre como diferentes "
    "grupos demográficos e sociais experienciam o medo em relação à criminalidade. A correlação positiva "
    "entre os tipos de risco sugere que a sensação de insegurança é um sentimento generalizado, não focado em um único tipo de crime.\n\n"
    "Observou-se que a percepção de risco não é homogênea, apresentando variações significativas "
    "quando segmentada por sexo, faixa etária e estrato do bairro de residência. "
    "Por exemplo, a análise por sexo indicou [descreva aqui a principal diferença, ex: que o público feminino percebe maior risco de sequestro].\n\n"
    "Estes resultados sugerem a necessidade de políticas de segurança pública que sejam sensíveis a "
    "essas diferentes percepções, focando esforços em localidades e grupos que demonstram maior "
    "sensação de insegurança."
)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 7, texto_conclusao.encode('latin-1', 'replace').decode('latin-1'))


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
    for caminho in nomes_graficos:
        os.remove(caminho)
    os.rmdir(pasta_temp)
    print("\nArquivos temporários removidos.")


