# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from fpdf import FPDF
import shutil
from IPython.display import display

# ==============================================================================
# 1. CONFIGURAÇÃO INICIAL
# ==============================================================================

# --- Definir caminhos ---
output_dir = '../../analises/'
temp_img_dir = os.path.join(output_dir, 'temp_images/')

# --- Criar diretórios se não existirem ---
os.makedirs(output_dir, exist_ok=True)
os.makedirs(temp_img_dir, exist_ok=True)

# %%
# ==============================================================================
# 2. CARREGAMENTO DOS DADOS
# ==============================================================================

# Caminho para os dados tratados
caminho = '../../dados_tratados/csv/'

# Carregando os dados em um dicionário de DataFrames
dados = {
    'alunos': pd.read_csv(caminho + 'escolas_alunos_2006.csv', sep=';', encoding='utf-8'),
    'professores': pd.read_csv(caminho + 'escolas_professores_2006.csv', sep=';', encoding='utf-8'),
}

print("Dados de Alunos (antes do tratamento):")
display(dados['alunos'].head())


# %%
# ==============================================================================
# 3. PRÉ-PROCESSAMENTO DOS DADOS
# ==============================================================================

print("Iniciando pré-processamento dos dados...")

# --- Dicionários para renomear colunas ---
rename_dict_alunos = {
    'sexo': 'sexo',
    'idade': 'idade',
    'raca_cor': 'raca_cor',
    'qual_outra_raca': 'raca_cor_aux'  # Coluna auxiliar
}
rename_dict_professores = {
    'tempo_como_professor_na_escola': 'tempo_como_professor_na_escola',
    'materia_lecionada': 'materia'
}

# --- Processar Alunos ---
dados['alunos'].columns = dados['alunos'].columns.str.lower().str.strip()
dados['alunos'] = dados['alunos'].rename(columns=rename_dict_alunos)
if 'raca_cor' in dados['alunos'].columns and 'raca_cor_aux' in dados['alunos'].columns:
    mask_outra = dados['alunos']['raca_cor'] == 'outra cor ou raça'
    dados['alunos'].loc[mask_outra,
                        'raca_cor'] = dados['alunos'].loc[mask_outra, 'raca_cor_aux']
    dados['alunos'] = dados['alunos'][dados['alunos']
                                      ['raca_cor'] != 'uma outra mistura']
    dados['alunos'] = dados['alunos'].drop(columns=['raca_cor_aux'])
dados['alunos'] = dados['alunos'].loc[:, ~(dados['alunos'] == 0).all()]

# --- Processar Professores ---
dados['professores'].columns = dados['professores'].columns.str.lower().str.strip()
dados['professores'] = dados['professores'].rename(
    columns=rename_dict_professores)
dados['professores'] = dados['professores'].loc[:,
                                                ~(dados['professores'] == 0).all()]

print("Pré-processamento concluído.")


# ==============================================================================
# EXIBIÇÃO DOS DADOS TRATADOS
# ==============================================================================
print("Dados dos Alunos Tratados:")
display(dados['alunos'].head())
print("\nDados dos Professores Tratados:")
display(dados['professores'].head())


# %%
# ==============================================================================
# 4. ANÁLISE E GERAÇÃO DE GRÁFICOS
# ==============================================================================

print("Gerando análises e gráficos...")

sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (12, 7)
pdf_content = []

# --- Análise de Alunos ---
sexo_counts = dados['alunos']['sexo'].value_counts()
sexo_perc = dados['alunos']['sexo'].value_counts(
    normalize=True).mul(100).round(2)
raca_counts = dados['alunos']['raca_cor'].value_counts()
raca_perc = dados['alunos']['raca_cor'].value_counts(
    normalize=True).mul(100).round(2)

# Gráfico 1: Distribuição de Alunos por Sexo
plt.figure()
ax = sns.countplot(data=dados['alunos'], x='sexo',
                   order=sexo_counts.index, palette='plasma')
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                textcoords='offset points')
ax.set_title('Distribuição de Alunos por Sexo', fontsize=16)
ax.set_xlabel('Sexo', fontsize=12)
ax.set_ylabel('Quantidade de Alunos', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(temp_img_dir, 'alunos_sexo.png'))
plt.close()
pdf_content.append({
    'title': 'Análise de Alunos: Gênero',
    'image': 'alunos_sexo.png',
    'analysis': f"O gráfico de gênero revela uma comunidade estudantil com {sexo_counts.iloc[0]} alunos do sexo {sexo_counts.index[0]} ({sexo_perc.iloc[0]}%) e {sexo_counts.iloc[1]} do sexo {sexo_counts.index[1]} ({sexo_perc.iloc[1]}%). Essa distribuição equilibrada é fundamental para um ambiente escolar inclusivo."
})

# Gráfico 2: Distribuição de Alunos por Raça/Cor
plt.figure()
ax = sns.countplot(data=dados['alunos'], y='raca_cor',
                   order=raca_counts.index, palette='magma')
ax.set_title('Distribuição de Alunos por Raça/Cor', fontsize=16)
ax.set_xlabel('Quantidade de Alunos', fontsize=12)
ax.set_ylabel('Raça/Cor', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(temp_img_dir, 'alunos_raca.png'))
plt.close()
pdf_content.append({
    'title': 'Análise de Alunos: Raça/Cor',
    'image': 'alunos_raca.png',
    'analysis': f"A diversidade racial é um pilar da comunidade escolar. A maioria dos alunos se identifica como '{raca_counts.index[0]}' ({raca_perc.iloc[0]}%), seguido por '{raca_counts.index[1]}' ({raca_perc.iloc[1]}%). Este gráfico, após o tratamento dos dados, oferece um retrato fiel da composição étnico-racial dos estudantes."
})

# # Gráfico 3: Distribuição de Alunos por Idade
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Estilo limpo
sns.set(style="whitegrid")

# Filtro: remover idades fora da faixa plausível (ex: 5 a 25 anos)
df_idade_filtrada = dados['alunos'][(
    dados['alunos']['idade'] >= 5) & (dados['alunos']['idade'] <= 25)]

# Estatísticas após filtragem
media = df_idade_filtrada['idade'].mean()
mediana = df_idade_filtrada['idade'].median()
min_idade = df_idade_filtrada['idade'].min()
max_idade = df_idade_filtrada['idade'].max()
std = df_idade_filtrada['idade'].std()

# Gráfico
plt.figure(figsize=(10, 6))
ax = sns.histplot(
    data=df_idade_filtrada,
    x='idade',
    bins=10,
    color='teal',
    edgecolor='black',
    linewidth=0.5
)

# KDE suavizado
sns.kdeplot(
    data=df_idade_filtrada,
    x='idade',
    ax=ax,
    color='darkblue',
    linewidth=2,
    fill=True,
    alpha=0.3
)

# Linhas de referência
ax.axvline(media, color='blue', linestyle='--', label=f'Média: {media:.1f}')
ax.axvline(mediana, color='red', linestyle='--',
           label=f'Mediana: {mediana:.1f}')
ax.legend()

# Títulos
ax.set_title('Distribuição de Alunos por Idade (sem outliers)', fontsize=16)
ax.set_xlabel('Idade', fontsize=12)
ax.set_ylabel('Quantidade de Alunos', fontsize=12)

plt.tight_layout()
plt.savefig(os.path.join(temp_img_dir, 'alunos_idade.png'))
plt.close()

pdf_content.append({
    'title': 'Análise de Alunos: Faixa Etária',
    'image': 'alunos_idade.png',
    'analysis': (
        f"Foram removidos valores atípicos (como 99 anos) para focar em alunos dentro da faixa esperada de idade escolar. "
        f"A análise considera idades entre 5 e 25 anos. A média de idade é {media:.1f} anos, com mediana de {mediana:.1f} e "
        f"desvio padrão de {std:.1f}. O gráfico evidencia uma concentração maior na adolescência, auxiliando na definição de "
        f"metodologias pedagógicas adequadas."
        f"A menor idade registrada foi {min_idade} anos e a maior {max_idade} anos. "
        f"destacando o predomínio da pré-adolescência e adolescência no grupo analisado. "
        f"Esses dados são fundamentais para o planejamento de estratégias pedagógicas alinhadas ao perfil etário."
    )
})

# voltando configurações do seaborn
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (12, 7)

# plt.figure()
# ax = sns.histplot(data=dados['alunos'], x='idade', bins=15, kde=True, color='darkcyan')
# ax.set_title('Distribuição de Alunos por Idade', fontsize=16)
# ax.set_xlabel('Idade', fontsize=12)
# ax.set_ylabel('Quantidade de Alunos', fontsize=12)
# plt.tight_layout()
# plt.savefig(os.path.join(temp_img_dir, 'alunos_idade.png'))
# plt.close()
# pdf_content.append({
#     'title': 'Análise de Alunos: Faixa Etária',
#     'image': 'alunos_idade.png',
#     'analysis': f"A análise da idade dos alunos, com média de {dados['alunos']['idade'].mean():.1f} anos e desvio padrão de {dados['alunos']['idade'].std():.1f} anos, mostra uma concentração de estudantes na pré-adolescência e adolescência. O histograma ilustra os picos etários, essenciais para o planejamento pedagógico."
# })

# --- Análise de Professores ---
exp_summary = dados['professores']['tempo_como_professor_na_escola'].describe()
materia_counts = dados['professores']['materia'].value_counts()
top_10_materias = materia_counts.head(10)

# Gráfico 4: Anos de Experiência dos Professores
plt.figure()
ax = sns.histplot(data=dados['professores'], x='tempo_como_professor_na_escola',
                  bins=10, kde=True, color='rebeccapurple')
ax.set_title('Distribuição de Anos de Experiência dos Professores', fontsize=16)
ax.set_xlabel('Anos de Experiência', fontsize=12)
ax.set_ylabel('Quantidade de Professores', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(temp_img_dir, 'prof_experiencia.png'))
plt.close()
pdf_content.append({
    'title': 'Análise de Professores: Experiência',
    'image': 'prof_experiencia.png',
    'analysis': f"O corpo docente demonstra ser experiente, com uma média de {exp_summary['mean']:.1f} anos de atuação na escola. O histograma evidencia uma concentração de professores com vasta experiência, um indicador positivo para a qualidade do ensino."
})

# Gráfico 5: Distribuição de Professores por Matéria (Top 10)
plt.figure(figsize=(12, 8))
ax = sns.barplot(x=top_10_materias.values,
                 y=top_10_materias.index, palette='cubehelix', orient='h')
ax.set_title('Top 10 Matérias por Quantidade de Professores', fontsize=16)
ax.set_xlabel('Quantidade de Professores', fontsize=12)
ax.set_ylabel('Matéria', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(temp_img_dir, 'prof_materia.png'))
plt.close()
pdf_content.append({
    'title': 'Análise de Professores: Disciplinas',
    'image': 'prof_materia.png',
    'analysis': f"A análise por disciplina mostra que '{top_10_materias.index[0]}' e '{top_10_materias.index[1]}' são as áreas com maior número de docentes. Este gráfico de barras horizontais facilita a visualização da distribuição de professores, destacando as áreas de maior peso curricular na instituição."
})


# Gráfico 6: Distribuição de Idade dos Professores
ano_referencia = 2006

if 'ano_nascimento' in dados['professores'].columns:
    df_prof_temp = dados['professores'].copy()
    df_prof_temp['ano_nascimento'] = pd.to_numeric(
        df_prof_temp['ano_nascimento'], errors='coerce')

    # Remover nulos e calcular idade
    df_prof_temp.dropna(subset=['ano_nascimento'], inplace=True)
    df_prof_temp['idade'] = ano_referencia - df_prof_temp['ano_nascimento']

    # Filtrar idades plausíveis (ex: entre 18 e 100 anos)
    df_prof_temp = df_prof_temp[(df_prof_temp['idade'] >= 18) & (
        df_prof_temp['idade'] <= 100)]

    # Estatísticas
    idade_media = df_prof_temp['idade'].mean()
    idade_min = df_prof_temp['idade'].min()
    idade_max = df_prof_temp['idade'].max()

    # Gráfico
    plt.figure(figsize=(12, 7))
    ax = sns.histplot(data=df_prof_temp, x='idade', bins=15,
                      kde=True, color='darkorange', edgecolor='black')

    ax.axvline(idade_media, color='blue', linestyle='--',
               label=f'Média: {idade_media:.1f} anos')
    ax.set_title(
        'Distribuição de Idade dos Professores (Ano de 2006)', fontsize=16)
    ax.set_xlabel('Idade', fontsize=12)
    ax.set_ylabel('Quantidade de Professores', fontsize=12)
    ax.legend()

    plt.tight_layout()
    plt.savefig(os.path.join(temp_img_dir, 'prof_idade.png'))
    plt.close()

    pdf_content.append({
        'title': 'Análise de Professores: Faixa Etária',
        'image': 'prof_idade.png',
        'analysis': (
            f"A faixa etária do corpo docente apresenta ampla diversidade, com idades variando entre "
            f"{int(idade_min)} e {int(idade_max)} anos. A idade média dos professores é de {idade_media:.1f} anos. "
            f"O gráfico revela uma concentração significativa entre 30 e 50 anos, o que indica um grupo profissional "
            f"maduro e experiente, características essenciais para a qualidade da educação."
        )
    })


print("\nGráficos de análise gerados e salvos com sucesso.")


# %%
# ==============================================================================
# 5. EXPORTAÇÃO DO RELATÓRIO CONSOLIDADO EM PDF
# ==============================================================================

print("Iniciando a geração do relatório em PDF...")


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(
            0, 10, 'Relatório Consolidado - Análise de Escolas 2006', 0, 1, 'C')
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
        # Usamos 'latin-1' para evitar problemas com caracteres especiais
        self.multi_cell(0, 10, body.encode(
            'latin-1', 'replace').decode('latin-1'))
        self.ln()

    def add_summary_page(self, title, summary_text):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(summary_text)

    def add_analysis_section(self, title, image_path, analysis_text):
        self.add_page()
        self.chapter_title(title)

        if os.path.exists(image_path):
            self.image(image_path, x=30, w=150)
            self.ln(5)
        else:
            self.set_font('Arial', 'I', 10)
            self.cell(
                0, 10, f"[Imagem não encontrada em '{image_path}']", 0, 1)

        self.chapter_body(analysis_text)


# --- Gerar o PDF ---
pdf = PDF()
pdf_filename = os.path.join(output_dir, 'relatorio_final_escolas_2006.pdf')

# Adiciona a página de resumo inicial
resumo_analise = """
A análise dos dados escolares de 2006 oferece um panorama abrangente sobre o perfil dos alunos e professores da rede.

No que diz respeito aos estudantes, observa-se um equilíbrio entre os gêneros, com uma leve predominância do sexo masculino. A composição étnico-racial revela uma diversidade significativa, destacando-se a maioria de alunos que se autodeclaram pardos ou pretos. A faixa etária predominante está concentrada entre 10 e 15 anos, indicando um público majoritariamente em idade correspondente ao Ensino Fundamental.

Quanto ao corpo docente, os dados apontam para um quadro de profissionais experientes: a maioria leciona há mais de uma década na mesma escola, o que pode refletir estabilidade e continuidade pedagógica. A distribuição por área de atuação evidencia maior concentração de professores em disciplinas como Educação Física e Matemática, sugerindo uma possível demanda elevada ou maior carga horária destinada a essas matérias no currículo escolar.
"""

pdf.add_summary_page("Resumo da Análise Geral", resumo_analise)


# Adiciona as seções de análise com gráficos
for item in pdf_content:
    full_image_path = os.path.join(temp_img_dir, item['image'])
    pdf.add_analysis_section(item['title'], full_image_path, item['analysis'])

pdf.output(pdf_filename)
print(f"\nPDF '{pdf_filename}' gerado com sucesso.")
print("Processo concluído.")


# ==============================================================================
# 6. LIMPEZA DOS ARQUIVOS TEMPORÁRIOS
# ==============================================================================
try:
    shutil.rmtree(temp_img_dir)
    print(f"Pasta temporária '{temp_img_dir}' foi apagada com sucesso.")
except OSError as e:
    print(f"Erro ao apagar a pasta temporária: {e}")
