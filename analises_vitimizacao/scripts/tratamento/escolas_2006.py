# %%
# Célula 1: Importar as bibliotecas necessárias
import pandas as pd
import numpy as np
import os
import openpyxl

# %%
dicionario_completo_de_nomes = {
    'NOME DA ESCOLA': 'nome_escola',
    'A ESCOLA': 'cidade_escola',
    'Bh ou RMBH': 'local_bh_rmbh',
    'A ESCOLA (2)': 'bairro_escola',
    'TURMA': 'turma',
    'HORA INÍCIO': 'hora_inicio',
    'HORA FIM': 'hora_fim',
    'APLICADORES': 'aplicadores',
    'RVACÕES': 'observacoes',
    'DATA DA APLICAÇÃO': 'data_aplicacao',
    'NÚMERO DO QUESTIONÁRIO': 'id_questionario',
    'Quantos anos você tem?': 'idade',
    'Em que bairro você mora?': 'bairro',
    'Em que cidade você mora?': 'cidade',
    'Sexo': 'sexo',
    'quantos desses bens há na sua casa? Rádio': 'bens_radio',
    'Tv em Cores': 'bens_tv_cores',
    'Vídeo Cassete/DVD': 'bens_dvd',
    'Freezer': 'bens_freezer',
    'Forno Microondas': 'bens_microondas',
    'Aspirador de pó': 'bens_aspirador',
    'Máquina de lavar roupa': 'bens_maquina_lavar',
    'Números de telefone fixo': 'bens_telefone_fixo',
    'Telefone celular': 'bens_celular',
    'Aparelho de ar condicionado': 'bens_ar_condicionado',
    'Computador': 'bens_computador',
    'Carro': 'bens_carro',
    'Banheiro': 'bens_banheiro',
    'Qual a sua raça, ou cor?': 'raca_cor',
    'Uma outra mistura. Qual?': 'raca_cor_mistura_outra',
    'Outra cor ou raça. Qual?': 'raca_cor_outra',
    'Qual a sua religião?': 'religiao',
    'Outra. Qual?': 'religiao_outra',
    'Quem são os responsáveis por você?': 'responsaveis',
    'Outros. Quais?': 'responsaveis_outros',
    'Até que ano seu pai (ou seu responsável do sexo masculino) estudou?': 'escolaridade_pai',
    'O que seu pai (ou seu responsável do sexo masculino) faz atualmente?': 'ocupacao_pai',
    'Outra situação. Qual?': 'ocupacao_pai_outra',
    'Até que ano sua mãe (ou sua responsável do sexo feminino) estudou?': 'escolaridade_mae',
    'O que sua mãe (ou sua responsável do sexo feminino) faz atualmente?': 'ocupacao_mae',
    'Outra situação. Qual? (2)': 'ocupacao_mae_outra',
    'Nenhuma/Nada': 'ocupacao_mae_nenhuma',
    'O que você costuma fazer quando não está na escola? Assistir à televisão, jogar vídeo game ou no computador em casa': 'hobbie_tv_jogos',
    'Praticar esportes (futebol, vôlei, natação, etc.) em clubes': 'hobbie_esporte_clube',
    'Praticar esportes na rua ou em casa': 'hobbie_esporte_rua',
    'Estudar (matérias da escola, cursos de inglês, outras línguas, etc.)': 'hobbie_estudar',
    'Participar de grupo musical, dança, teatro, capoeira': 'hobbie_grupo_artistico',
    'Participar de organizações de jovens da comunidade, incluindo grupos de jovens da igreja': 'hobbie_grupo_comunitario',
    'Ouvir música': 'hobbie_ouvir_musica',
    'Ler': 'hobbie_ler',
    'Trabalhar': 'hobbie_trabalhar',
    'Sair com amigos para festas, barzinhos, passear': 'hobbie_sair_amigos',
    'Outras.': 'hobbie_outros',
    'Quais': 'hobbie_outros_quais',
    'Você trabalha fora?': 'trabalha_fora',
    'Sim. Qual a sua função?': 'trabalha_funcao',
    'Se sim, você ajuda, com dinheiro, nas despesas de sua casa ou alguém de sua família?': 'trabalha_ajuda_despesa',
    'Você está satisfeito com seu aprendizado na escola?': 'satisfacao_aprendizado',
    'Em sua opinião, qual a sua dedicação à escola?': 'dedicacao_escola',
    'Considerando as suas condições (econômica, social, cultural) e de sua família, até que série você acha que irá estudar, durante toda sua vida?': 'expectativa_escolaridade',
    'Se pudesse escolher, você...': 'preferencia_mudar_escola',
    'Por que você gostaria de mudar de escola?': 'motivo_mudar_escola',
    'Marque de zero a dez a nota que você dá para...sua escola': 'nota_escola',
    'O diretor da sua escola': 'nota_diretor',
    'A maioria de seus professores': 'nota_professores',
    'Seus colegas de classe': 'nota_colegas_classe',
    'Seus colegas de escola': 'nota_colegas_escola',
    'Minha escola não oferece nenhuma atividade': 'escola_sem_atividade_extra',
    'Quais atividades abaixo são oferecidas pela sua escola? Eventos esportivos, capoeira': 'atividade_oferecida_esportes',
    'Cursos profissionalizantes (computação, cabeleireiro, manicure, cozinha)': 'atividade_oferecida_cursos',
    'Feiras culturais ou de ciências': 'atividade_oferecida_feiras',
    'Grupos de teatro e de dança': 'atividade_oferecida_grupos_arte',
    'Oficinas culturais (percussão, reciclagem, bordados, costura, arte, etc...)': 'atividade_oferecida_oficinas',
    'Aulas durante todo o dia para alguns alunos': 'atividade_oferecida_aula_integral',
    'Palestras (Proerd, de educação sexual, etc...)': 'atividade_oferecida_palestras',
    'Atividades nos finais de semana para toda a comunidade': 'atividade_oferecida_fim_semana',
    'Parcerias (Valores de Minas, CDL, etc...)': 'atividade_oferecida_parcerias',
    'Outras. (2)': 'atividade_oferecida_outras',
    'Quais?': 'atividade_oferecida_outras_quais',
    'Nos últimos 12 meses, com que freqüência os responsáveis por você (por exemplo: pai, mãe, tio, tia, avós, irmãos, etc.) acompanharam suas notas, seus deveres e/ou trabalhos da escola?': 'freq_acomp_notas_resp',
    'Nos últimos 12 meses, com que freqüência os responsáveis por você (por exemplo: pai, mãe, tio, tia, avós, irmãos, etc) participaram das reuniões na escola?': 'freq_reunioes_resp',
    'Nos últimos 12 meses, com que freqüência os responsáveis por você (por exemplo: pai, mãe, tio ou tia, avós, irmãos, etc.) participaram das atividades escolares abertas à comunidade?': 'freq_atividades_resp',
    'Qual a atitude mais grave que sua escola já tomou, quando algum aluno desrespeitou algum professor?': 'atitude_grave_desrespeito_prof',
    'Qual a atitude mais grave que sua escola já tomou, quando algum aluno brigou com outro aluno, dentro e nas proximidades desta escola?': 'atitude_grave_briga_aluno',
    'Qual a atitude mais grave que sua escola já tomou, quando algum aluno foi pego fumando cigarros dentro desta escola?': 'atitude_grave_fumar_cigarro',
    'Qual a atitude mais grave que sua escola já tomou, quando algum aluno foi pego consumindo bebida alcoólica dentro desta escola?': 'atitude_grave_beber_alcool',
    'Qual a atitude mais grave que sua escola já tomou, quando algum aluno foi pego com drogas (exemplo: maconha, cola, loló, tiner, cocaína, crack) dentro desta escola?': 'atitude_grave_drogas',
    'Qual a atitude mais grave que sua escola já tomou, quando algum aluno foi pego com armas (revólver, faca, canivete, navalha, pedaços de pau, porretes etc) dentro desta escola?': 'atitude_grave_armas',
    'O que você acha que deveria melhorar nesta escola?': 'melhoria_escola_opcao1',
    'Opção': 'melhoria_escola_opcao2',
    'Opção (2)': 'melhoria_escola_opcao3',
    'Opção (3)': 'melhoria_escola_opcao4',
    'Opção (4)': 'melhoria_escola_opcao5',
    'Opção (5)': 'melhoria_escola_opcao6',
    'O que você considera necessário (importante) para melhorar a segurança nesta escola?': 'melhoria_seguranca_opcao1',
    'Opção (6)': 'melhoria_seguranca_opcao2',
    'Opção (7)': 'melhoria_seguranca_opcao3',
    'Opção (8)': 'melhoria_seguranca_opcao4',
    'Opção (9)': 'melhoria_seguranca_opcao5',
    'Opção (10)': 'melhoria_seguranca_opcao6',
    'Q.': 'pergunta_generica_q1',
    'Q.45.': 'pergunta_q45',
    'Qual?': 'pergunta_q45_qual',
    'Q. (2)': 'pergunta_generica_q2',
    'Outros. Quem?': 'pergunta_generica_q2_quem',
    'Q. (3)': 'pergunta_generica_q3',
    'Outros. Quem? (2)': 'pergunta_generica_q3_quem',
    'Q. (4)': 'pergunta_generica_q4',
    'Outros. Quem? (3)': 'pergunta_generica_q4_quem',
    'Nos últimos 12 meses, quantas vezes você não foi à aula por medo de ser roubado, agredido ou por ter sido ameaçado de roubo ou agressão nesta escola?': 'faltou_aula_medo',
    'Q.53.': 'pergunta_q53',
    'Q.54.': 'pergunta_q54',
    'Não teve nenhum problema\xa0 (briga ou discussão) nessa escola': 'sem_problema_briga_discussao',
    'Você ou algum morador de sua casa tem arma de fogo?': 'possui_arma_fogo_casa',
    'Q. (5)': 'pergunta_generica_q5',
    'Q.69.': 'pergunta_q69',
    'Qual? (2)': 'pergunta_q69_qual',
    'Q. (6)': 'pergunta_generica_q6',
    'Se sim, você poderia citar alguns desses objetivos?': 'pergunta_generica_q6_objetivos',
    'Q.72.': 'pergunta_q72',
    'Quais? (2)': 'pergunta_q72_quais',
    'Q.73.': 'pergunta_q73',
    'Quais? (3)': 'pergunta_q73_quais',
    'Na sua opinião, o quanto você acha que as pessoas de fora da escola (vizinhos da escola, pais e familiares dos alunos, etc...) participam das atividades oferecidas pelo Programa Escola Viva, Comunidade Ativa nesta escola?': 'participacao_comunidade_externa',
    'Q.75.': 'pergunta_q75',
    'Q. (7)': 'pergunta_generica_q7',
    'DIGITADOR': 'digitador',
    'Outra. Qual? (2)': 'outra_qual_2',
    'roubo': 'ocorrencia_roubo',
    'furto': 'ocorrencia_furto',
    'agressao': 'ocorrencia_agressao',
    'ofensa professor': 'ocorrencia_ofensa_professor',
    'participação no programa': 'participacao_programa',
    'participação dos pais': 'participacao_pais',
    'pertence a gangue': 'pertence_gangue',
    'envolvimento com gangues': 'envolvimento_gangues',
    'furtou': 'ja_furtou',
    'uso de bebida': 'uso_bebida',
    'uso de cigarros': 'uso_cigarro',
    'usou solventes': 'uso_solventes',
    'uso maconha': 'uso_maconha',
    'uso uso de crack': 'uso_crack'
}

dicionario_completo_de_nomes = {
    k.lower(): v for k, v in dicionario_completo_de_nomes.items()}

# %%
dicionario_professores = {
    'NOME DA ESCOLA': 'nome_escola',
    'A ESCOLA': 'cidade_escola',
    'A ESCOLA (2)': 'bairro_escola',
    'TURMA': 'turma',
    'HORA INÍCIO': 'hora_inicio',
    'HORA FIM': 'hora_fim',
    'APLICADORES': 'aplicadores',
    'RVACÕES': 'observacoes',
    'DATA DA APLICAÇÃO': 'data_aplicacao',
    'NÚMERO DO QUESTIONÁRIO': 'id_questionario',
    'Ano de nascimento': 'ano_nascimento',
    'Bairro onde mora': 'bairro',
    'Cidade onde mora': 'cidade',
    'Sexo': 'sexo',
    'Raça ou cor': 'raca_cor',
    'Q.5. - Raça mistura': 'raca_cor_mistura',
    'Q.5. - Outra raça': 'raca_cor_outra',
    'Religião': 'religiao',
    'outra religião': 'religiao_outra',
    'Quantidade de cada item existente em sua casa? Rádio': 'bens_radio',
    'televisor em cores': 'bens_tv_cores',
    'videocassete/dvd': 'bens_dvd',
    'freezer': 'bens_freezer',
    'microondas': 'bens_microondas',
    'aspirador de pó': 'bens_aspirador',
    'máquina de lavar roupa': 'bens_maquina_lavar',
    'linha de telefone fixo': 'bens_telefone_fixo',
    'celular': 'bens_celular',
    'aparelho de ar condicionado': 'bens_ar_condicionado',
    'computador': 'bens_computador',
    'carro': 'bens_carro',
    'banheiro': 'bens_banheiro',
    'empregada mensalista': 'possui_empregada_mensalista',
    'Há quanto tempo é professor dessa escola (anos e meses)': 'tempo_como_professor_na_escola',
    'Qual matéria leciona nesta escola': 'materia_lecionada',
    'Se pudesse escolher... gostaria de continuar trabalhando nesta escola ou mudaria para outra escola': 'preferencia_continuar_ou_mudar',
    'Por que gostaria de mudar para outra escola': 'motivo_mudar_escola',
    'outro motivo': 'motivo_mudar_escola_outro',
    'O fator que mais compromete/dificulta o processo ensino/aprendizagem nesta escola': 'fator_dificulta_aprendizagem_1',
    'outro fator': 'fator_dificulta_aprendizagem_2',
    'outro fator (2)': 'fator_dificulta_aprendizagem_3',
    'outro fator (3)': 'fator_dificulta_aprendizagem_4',
    'outro fator (4)': 'fator_dificulta_aprendizagem_5',
    'outro fator (5)': 'fator_dificulta_aprendizagem_6',
    'O fator que mais facilita o processo ensino/aprendizagem nesta escola': 'fator_facilita_aprendizagem_1',
    'outro fator (6)': 'fator_facilita_aprendizagem_2',
    'outro fator (7)': 'fator_facilita_aprendizagem_3',
    'outro fator (8)': 'fator_facilita_aprendizagem_4',
    'outro fator (9)': 'fator_facilita_aprendizagem_5',
    'outro fator (10)': 'fator_facilita_aprendizagem_6',
    'A maior dificuldade em auxiliar os alunos nas atividades em aula deve-se...': 'dificuldade_auxiliar_alunos_1',
    'fator': 'dificuldade_auxiliar_alunos_2',
    'fator2': 'dificuldade_auxiliar_alunos_3',
    'fator (2)': 'dificuldade_auxiliar_alunos_4',
    'fator3': 'dificuldade_auxiliar_alunos_5',
    'fator (3)': 'dificuldade_auxiliar_alunos_6',
    'Q.15.': 'pergunta_q15',
    'A maioria dos alunos com os quais você convive nesta escola é...': 'perfil_maioria_alunos',
    'Q.17.': 'pergunta_q17',
    'Q.17.4': 'pergunta_q17_4',
    'Você acha que é fácil, difícil ou impossível entrar com': 'percepcao_facilidade_entrar_itens',
    'Dentre as opções assinale os três recursos que você considera mais importantes para garantir a seguranca nesta escola': 'recurso_seguranca_importante_1',
    'opção': 'recurso_seguranca_importante_2',
    'opção (2)': 'recurso_seguranca_importante_3',
    'opção (3)': 'recurso_seguranca_importante_4',
    'opção (4)': 'recurso_seguranca_importante_5',
    'opção (5)': 'recurso_seguranca_importante_6',
    'Dentre as opções assinale os três recursos que esta escola vem utilizando para solucionar os problema de seguranca': 'recurso_seguranca_utilizado_1',
    'opção (6)': 'recurso_seguranca_utilizado_2',
    'opção (7)': 'recurso_seguranca_utilizado_3',
    'opção (8)': 'recurso_seguranca_utilizado_4',
    'opção (9)': 'recurso_seguranca_utilizado_5',
    'opção (10)': 'recurso_seguranca_utilizado_6',
    'Q.': 'pergunta_generica_q1',
    'Q.24.': 'pergunta_q24',
    'Q.25.': 'pergunta_q25',
    'Quando sai desta escola de': 'transporte_saida_escola',
    'Q.28.': 'pergunta_q28',
    'Q.29.': 'pergunta_q29',
    'Q.30.': 'pergunta_q30',
    'Q.31.': 'pergunta_q31',
    'Q.32.': 'pergunta_q32',
    'Você diria que nos últimos doze meses a violência desntro desta escola': 'percepcao_violencia_12meses',
    'Q.34.': 'pergunta_q34',
    'Quando você esta dentro desta escola você se sente...': 'sentimento_seguranca_escola',
    'Q.36.': 'pergunta_q36',
    'Qual atitude': 'qual_atitude',
    'Q. (2)': 'pergunta_generica_q2',
    'Outros. Quem': 'pergunta_generica_q2_quem',
    'Q. (3)': 'pergunta_generica_q3',
    'Outros. Quem (2)': 'pergunta_generica_q3_quem',
    'Você sabe o que é o Programa Escola Viva, Comunidade Ativa?': 'conhece_programa_escola_viva',
    'Q.47.': 'pergunta_q47',
    'Quais': 'pergunta_q47_quais',
    'Q. (4)': 'pergunta_generica_q4',
    'Se sim, vocÃª poderia citar algum desses objetivos': 'programa_escola_viva_objetivos',
    'Você participa das atividades do Programa': 'participa_programa_escola_viva',
    'Se sim, por favor descreva sua participação no Programa Escola Viva': 'descricao_participacao_programa',
    'Q.51.': 'pergunta_q51',
    'quais': 'pergunta_q51_quais',
    'Na sua opinião o quanto você acha que as pessoas de fora da escola participam das atividades oferecidas pelo Programa nesta escola': 'percepcao_participacao_externa_programa',
    'Q.53.': 'pergunta_q53',
    'Na sua opinião, o Programa Escola Viva...': 'opiniao_programa_escola_viva',
    'DIGITADOR': 'digitador'
}

dicionario_professores = {
    k.lower(): v for k, v in dicionario_professores.items()}

# %%
caminho_pasta = '../../dados_brutos/violencia_escolas_2006/'


def carregar_dados(arquivo):
    try:

        dados = pd.read_csv(
            arquivo,
            na_values=["", " ", "na", "NaN", "nan", "null", "NULL", "None"],
            # sep=';',         # Separador de campos
            encoding='utf-8',  # Codificação do arquivo
            header=[0],      # A primeira linha é o cabeçalho
            # skiprows=1,  # Pular a segunda linha (se necessário)
        )

        # tratamento

        # Substituir strings vazias por NaN (em todo o DataFrame)
        dados.replace(r'^\s*$', np.nan, regex=True, inplace=True)
        # Substituir strings vazias por NaN (apenas em colunas de texto)
        for col in dados.select_dtypes(include=np.number).columns:
            # Preenche os valores nulos/vazios (NaN) com 0
            dados[col] = dados[col].fillna(0)

        # deixar as colunas em caixa baixa

        for col in dados.select_dtypes(include='object').columns:
            dados[col] = dados[col].str.lower()

        dados.columns = dados.columns.astype(str).str.lower()

        # Lista de valores que, se forem os únicos em uma coluna, causam a remoção
        valores_para_remover = ['não', 'na']

        colunas_para_apagar = []
        for coluna in dados.columns:
            # Obtém os valores únicos da coluna, ignorando os nulos (NaN/None)
            valores_unicos = dados[coluna].dropna().unique()

            # Condição para apagar:
            # 1. A coluna é totalmente vazia.
            # 2. A coluna SÓ tem valores de um tipo da lista `valores_para_remover`.
            if len(valores_unicos) == 0 or \
                    (len(valores_unicos) == 1 and valores_unicos[0] in valores_para_remover):
                colunas_para_apagar.append(coluna)

        # Apaga as colunas identificadas
        df_limpo = dados.drop(columns=colunas_para_apagar)

        print("\nDataFrame Limpo:")
        print(df_limpo)

        print(f"[OK] CSV '{arquivo}' carregado.")
    except Exception as e:
        print(f"[ERRO] Ao ler o arquivo CSV '{arquivo}': {e}")

    return dados


def tratar_raca_cor(df):
    """
    Substitui valores 'outra cor ou raça' na coluna 'raca_cor' pelos valores de
    'raca_cor_mistura_outra' ou 'raca_cor_outra', se disponíveis.
    Em seguida, remove essas colunas auxiliares.
    """
    def substituir_outra_cor(row):
        if row['raca_cor'] == 'outra cor ou raça':
            if row.get('raca_cor_mistura_outra') not in [None, 'na'] and pd.notna(row.get('raca_cor_mistura_outra')):
                return row['raca_cor_mistura_outra']
            elif row.get('raca_cor_outra') not in [None, 'na'] and pd.notna(row.get('raca_cor_outra')):
                return row['raca_cor_outra']
        return row['raca_cor']

    # Aplica substituição
    if 'raca_cor' in df.columns:
        df['raca_cor'] = df.apply(substituir_outra_cor, axis=1)

    # Remove colunas auxiliares, se existirem
    colunas_auxiliares = ['raca_cor_mistura_outra', 'raca_cor_outra']
    colunas_para_remover = [
        col for col in colunas_auxiliares if col in df.columns]
    if colunas_para_remover:
        df.drop(columns=colunas_para_remover, inplace=True)

    return df

# Aplicar a função


dados = {
    'alunos': carregar_dados(caminho_pasta + 'alunos_2006.csv'),
    'professores': carregar_dados(caminho_pasta + 'professores_2006.csv')
}

dados['alunos'].rename(columns=dicionario_completo_de_nomes, inplace=True)
dados['professores'].rename(columns=dicionario_professores, inplace=True)

# tratamento tempo como professor
# sai de 250 anos para 25 anos
dados['professores']['tempo_como_professor_na_escola'] = dados['professores']['tempo_como_professor_na_escola']/10
# tratamento data de nascimento
dados['professores'] = dados['professores'].astype({'ano_nascimento': 'int64'})


dados['alunos'] = tratar_raca_cor(dados['alunos'])
dados['professores'] = tratar_raca_cor(dados['professores'])


# %%
print(dados['alunos'].head())
print(dados['alunos'].info())
print(dados['professores'].head())
print(dados['professores'].info())

# %%
# Célula 7: Exportar o DataFrame Final (CSV e Excel)

caminho_saida = '../../dados_tratados'

# Cria o diretório de saída se ele não existir
if not os.path.exists(f"{caminho_saida}/csv"):
    os.makedirs(f"{caminho_saida}/csv")
    print(f"Pasta '{caminho_saida}' criada com sucesso!")

if not os.path.exists(f"{caminho_saida}/excel"):
    os.makedirs(f"{caminho_saida}/excel")
    print(f"Pasta '{caminho_saida}' criada com sucesso!")


# Verifica se o dataframe final foi criado com sucesso antes de salvar
if dados['alunos'] is not None and dados['professores'] is not None:

    # --- 1. EXPORTAR PARA CSV ---
    try:
        nome_arquivo_csv = 'escolas_alunos_2006.csv'
        caminho_arquivo_csv_completo = os.path.join(
            f"{caminho_saida}/csv", nome_arquivo_csv)
        dados['alunos'].to_csv(caminho_arquivo_csv_completo,
                               index=False, sep=';', encoding='utf-8')
        print(f"✅ SUCESSO! Arquivo CSV salvo em:")
        print(f"'{caminho_arquivo_csv_completo}'")
    except Exception as e:
        print(f"❌ ERRO ao salvar o arquivo CSV: {e}")

    print("-" * 30)  # Linha separadora

    # --- 2. EXPORTAR PARA EXCEL ---
    try:
        nome_arquivo_excel = 'escolas_alunos_2006.xlsx'
        caminho_arquivo_excel_completo = os.path.join(
            f"{caminho_saida}/excel", nome_arquivo_excel)
        # 'index=False' evita que o índice do pandas seja salvo como uma coluna no Excel
        dados['alunos'].to_excel(
            caminho_arquivo_excel_completo, index=False, engine='openpyxl')
        print(f"✅ SUCESSO! Arquivo Excel salvo em:")
        print(f"'{caminho_arquivo_excel_completo}'")
    except Exception as e:
        print(f"❌ ERRO ao salvar o arquivo Excel: {e}")

    # professores
    # --- 1. EXPORTAR PARA CSV ---
    try:
        nome_arquivo_csv = 'escolas_professores_2006.csv'
        caminho_arquivo_csv_completo = os.path.join(
            f"{caminho_saida}/csv", nome_arquivo_csv)
        dados['professores'].to_csv(
            caminho_arquivo_csv_completo, index=False, sep=';', encoding='utf-8')
        print(f"✅ SUCESSO! Arquivo CSV salvo em:")
        print(f"'{caminho_arquivo_csv_completo}'")
    except Exception as e:
        print(f"❌ ERRO ao salvar o arquivo CSV: {e}")

    print("-" * 30)  # Linha separadora

    # --- 2. EXPORTAR PARA EXCEL ---
    try:
        nome_arquivo_excel = 'escolas_professores_2006.xlsx'
        caminho_arquivo_excel_completo = os.path.join(
            f"{caminho_saida}/excel", nome_arquivo_excel)
        # 'index=False' evita que o índice do pandas seja salvo como uma coluna no Excel
        dados['professores'].to_excel(
            caminho_arquivo_excel_completo, index=False, engine='openpyxl')
        print(f"✅ SUCESSO! Arquivo Excel salvo em:")
        print(f"'{caminho_arquivo_excel_completo}'")
    except Exception as e:
        print(f"❌ ERRO ao salvar o arquivo Excel: {e}")

else:
    print("⚠️ O DataFrame final ('df_final') não existe. A etapa de exportação foi pulada.")
