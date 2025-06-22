# Repositório de Análises de Vitimização e Percepção de Segurança

[Acessar Website](https://drive.google.com/drive/folders/1k4qvQ4Vq6tAyDYbkf6zF0jkFH89Tp3Hf?usp=sharing)

## Sumário
- [Introdução](#introdução)
- [Metodologia e Estrutura Técnica](#metodologia-e-estrutura-técnica)
- [Descrição dos Scripts de Processamento e Análise](#descrição-dos-scripts-de-processamento-e-análise)
- [Metadados e Documentação Técnica](#metadados-e-documentação-técnica)
- [Projetos de Análise e Resultados](#projetos-de-análise-e-resultados)
- [Fontes de Dados Utilizadas](#fontes-de-dados-utilizadas)
- [Inventário de Pesquisas Relevantes](#inventário-de-pesquisas-relevantes)

## Introdução
O presente repositório tem por finalidade centralizar, processar e analisar dados de vitimização e percepção de segurança, com foco especial em pesquisas realizadas no Brasil. O projeto foi concebido para assegurar a gestão da informação científica e a reprodutibilidade das análises, em conformidade com as melhores práticas de organização de código e dados.

Nesta plataforma, são disponibilizados desde os microdados brutos e scripts de tratamento (ETL) até as análises estatísticas e os relatórios consolidados.

## Metodologia e Estrutura Técnica

### Estrutura do Repositório
O projeto está organizado na seguinte estrutura de diretórios para segregar de forma clara os dados, códigos e resultados:
```text
/analises_vitimizacao
├── dados_brutos/
│   └── "identificação_data_dataset"/
├── dados_tratados/
│   ├── csv/
│   └── excel/
├── scripts/
│   ├── tratamento/
│   └── analise/
├── analises/
│   └── relatorios/
├── documentos/
│   └── "identificação_data_dataset"/
└── metadados/
├── por_fonte/
└── dicionario_unificado.csv
```

- **dados_brutos/**: Contém os dados originais e imutáveis, conforme foram coletados.
- **dados_tratados/**: Armazena os dados após o processo de limpeza e tratamento, prontos para a análise.
- **scripts/**: Abriga o código-fonte, dividido em tratamento (ETL) e análise (modelagem e visualização).
- **analises/**: Guarda os resultados finais, como relatórios (.pdf) e gráficos.
- **documentos/**: Inclui documentação de apoio, como os questionários originais das pesquisas.
- **metadados/**: Contém dicionários de variáveis, logs de integração e outra documentação técnica.

### Acesso e Configuração do Ambiente
Para replicar o ambiente e executar as análises, os seguintes passos são recomendados:
1.  **Clonagem do Repositório:** O repositório pode ser clonado por meio do seguinte comando Git:
    ```
    git clone [https://github.com/vitimizacaocrisp/Repositorio_pesquisas](https://github.com/vitimizacaocrisp/Repositorio_pesquisas)
    ```
2.  **Acesso aos Dados Brutos:** Os dados originais, devido ao seu volume, não são versionados diretamente no repositório. O download pode ser realizado a partir do seguinte link:
    [Acessar Dados no Google Drive](https://drive.google.com/drive/folders/1k4qvQ4Vq6tAyDYbkf6zF0jkFH89Tp3Hf?usp=sharing)
3.  **Organização dos Dados:** Os arquivos baixados devem ser descompactados e alocados na pasta `/dados_brutos/`.
4.  **Instalação de Dependências:** As bibliotecas Python necessárias para a execução dos scripts estão listadas no arquivo `pyproject.toml`. A instalação pode ser feita com o pip, utilizando um arquivo `requirements.txt`.
    ```
    pip install -r requirements.txt
    ```

### Fluxo de Trabalho (Workflow)
O fluxo de trabalho foi desenhado para garantir clareza e reprodutibilidade:
- **Coleta e Armazenamento:** Os dados brutos são inseridos no diretório `dados_brutos/` e permanecem inalterados.
- **Tratamento (ETL):** Scripts localizados em `scripts/tratamento/` são executados para limpar, padronizar e unificar os dados.
- **Armazenamento de Dados Tratados:** Os datasets resultantes são salvos em `dados_tratados/`, nos formatos CSV e Excel.
- **Análise:** Scripts em `scripts/analise/` utilizam os dados tratados para gerar modelagens, visualizações e insights.
- **Resultados:** Relatórios, dashboards e gráficos finais são armazenados no diretório `analises/`.

### Estratégia de Branches
O repositório utiliza duas branches principais para diferentes finalidades de desenvolvimento:
- **notebook:** Contém arquivos `.ipynb` (Jupyter Notebooks) utilizados para análise exploratória, prototipagem e desenvolvimento interativo.
- **script:** Contém arquivos `.py` (Python scripts) otimizados para produção, automação e reprodutibilidade de código.

## Descrição dos Scripts de Processamento e Análise
### Scripts de Tratamento
| Nome do Notebook | Arquivo(s) de Entrada | Arquivo(s) de Saída | Descrição do Processo |
| :--- | :--- | :--- | :--- |
| **[belo_horrizonte_2002.ipynb](https://github.com/vitimizacaocrisp/Repositorio_pesquisas/blob/main/analises_vitimizacao/scripts/tratamento/belo_horrizonte_2002.ipynb)** | `indices_violencia.csv`<br>`Vitimizacao_UP_27.csv` | `belo_horrizonte_2002.csv`<br>`belo_horrizonte_2002.xlsx` | Foi realizada a junção de dois arquivos CSV. Foram removidas 52 colunas completamente nulas do primeiro arquivo e 114 do segundo. Valores nulos em colunas numéricas foram substituídos por 0. Ao final, os dataframes tratados foram empilhados e exportados para os formatos CSV e XLSX. |
| **[escolas_2006.ipynb](https://github.com/vitimizacaocrisp/Repositorio_pesquisas/blob/main/analises_vitimizacao/scripts/tratamento/escolas_2006.ipynb)** | `alunos_2006.csv`<br>`professores_2006.csv` | `escolas_alunos_2006.csv`<br>`escolas_alunos_2006.xlsx`<br>`escolas_professores_2006.csv`<br>`escolas_professores_2006.xlsx` | Dois conjuntos de dados (alunos e professores) foram carregados e tratados separadamente. Em ambos, os valores numéricos nulos foram preenchidos com 0, as colunas de texto e seus nomes foram convertidos para minúsculas e as colunas que continham apenas valores nulos ou "não" foram removidas. Os nomes das colunas foram padronizados usando um dicionário e, por fim, os dois dataframes foram salvos em formatos CSV e XLSX. |
| **[percepcao_medoMG_2008.ipynb](https://github.com/vitimizacaocrisp/Repositorio_pesquisas/blob/main/analises_vitimizacao/scripts/tratamento/percepcao_medoMG_2008.ipynb)** | `amostra_BH.xls`<br>`amostra_MG.xls`<br>`populacao_idade_sexo.csv` | `percepcao_medoMG.csv`<br>`percepcao_medoMG.xlsx` | Três arquivos de diferentes fontes foram carregados. Em cada um deles, foram removidas linhas duplicadas e colunas completamente nulas. Os valores numéricos nulos foram preenchidos com 0. Após o tratamento individual, os três dataframes foram unificados em um único arquivo, que foi exportado para os formatos CSV e XLSX. |
| **[PNAD_2009.ipynb](https://github.com/vitimizacaocrisp/Repositorio_pesquisas/blob/main/analises_vitimizacao/scripts/tratamento/PNAD_2009.ipynb)** | Múltiplos arquivos `.xls` de diversas pastas (agressao, furto, roubo, etc.) | Múltiplos arquivos `.csv` e `.xlsx`, organizados em pastas por categoria (ex: `agressao.xlsx`, `furto.xlsx`) | O script processou um grande volume de arquivos `.xls` divididos em categorias. Para cada arquivo, os dados foram lidos, as colunas foram renomeadas para maior clareza, os nomes de colunas e índices foram padronizados para minúsculas e os dados foram convertidos para tipos numéricos. Os dataframes tratados foram exportados de duas maneiras: como arquivos individuais (CSV e XLSX) organizados em pastas por categoria e como um único arquivo XLSX por categoria, contendo múltiplas abas. |

### Scripts de Análise
| Nome do Notebook | Arquivo(s) de Entrada | Arquivo(s) de Saída | Descrição do Processo |
| :--- | :--- | :--- | :--- |
| **[escolas_2006.ipynb](https://github.com/vitimizacaocrisp/Repositorio_pesquisas/blob/main/analises_vitimizacao/scripts/analises/escolas_2006.ipynb)** | `escolas_alunos_2006.csv`<br>`escolas_professores_2006.csv` | `relatorio_alunos_escolas.pdf` | O notebook carrega os dados tratados de alunos e professores. Realiza um pré-processamento para limpar e padronizar colunas específicas (como sexo, idade e raça/cor). Gera análises visuais, incluindo distribuição de alunos por idade, sexo e raça, e satisfação com o aprendizado. Ao final, compila todos os gráficos e análises textuais em um relatório consolidado em PDF. |
| **[percepcao_social.ipynb](https://github.com/vitimizacaocrisp/Repositorio_pesquisas/blob/main/analises_vitimizacao/scripts/analises/percepcao_social.ipynb)** | `belo_horrizonte_2002.xlsx`<br>`percepcao_medoMG.xlsx` | `relatorio_completo_percepcao_social.pdf` | Este script combina dois conjuntos de dados sobre percepção de segurança (um de Belo Horizonte 2002 e outro de Minas Gerais). Limpa e prepara os dados combinados, focando em colunas como sexo, faixa etária e estrato do bairro. Gera análises sobre a percepção de risco de roubo, agressão e sequestro, segmentando por sexo, bairro e idade. Também cria uma matriz de correlação entre os tipos de risco e exporta todas as visualizações e tabelas para um relatório em PDF. |
| **[PNAD_2009.ipynb](https://github.com/vitimizacaocrisp/Repositorio_pesquisas/blob/main/analises_vitimizacao/scripts/analises/PNAD_2009.ipynb)** | Múltiplos arquivos `.xls` da PNAD 2009. | Múltiplos arquivos `.csv` e `.xlsx`, organizados por categoria. | O notebook carrega e trata um grande volume de arquivos `.xls` da PNAD 2009. Cada arquivo é processado para limpar cabeçalhos, renomear colunas e converter dados para formato numérico. Os dados tratados são exportados em dois formatos: arquivos individuais (CSV e Excel) e arquivos consolidados (Excel) por categoria, onde cada tabela original se torna uma aba. |

## Metadados e Documentação Técnica
- **Metadados por Fonte:** Documentação detalhada sobre a origem, o escopo e as características de cada conjunto de dados.
- **Dicionário de Variáveis Unificado:** Arquivo `dicionario_unificado.csv` contendo a descrição padronizada de todas as variáveis utilizadas no projeto.
- **Log de Integração:** Histórico detalhado das operações de combinação, transformação e enriquecimento de dados.

## Projetos de Análise e Resultados
A tabela a seguir detalha o status dos projetos de análise, indicando os concluídos (✅), os dados utilizados, os resultados gerados e as análises futuras planejadas (⬜).

| Status | Categoria | Análise | Dados Relevantes | Observações | Arquivos Gerados |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ✅ | **Violência Escolar** | Panorama sobre o perfil e a percepção de alunos e professores em escolas de Minas Gerais (2006). | `alunos_2006.csv`, `professores_2006.csv` | A análise inclui distribuição demográfica, experiência docente e satisfação discente. | [PDF](analises_vitimizacao/analises/relatorio_final_escolas_2006.pdf), [.py](analises_vitimizacao/scripts/analises/escolas_final_2006.py), [.ipynb](analises_vitimizacao/scripts/analises/escolas_final_2006.ipynb) |
| ✅ | **Percepção Social** | Análise da percepção de risco de crimes (roubo, agressão, sequestro) em Belo Horizonte e Minas Gerais. | `belo_horrizonte_2002.xlsx`, `percepcao_medoMG.xlsx` | Os dados foram segmentados por sexo, tipo de bairro e faixa etária, revelando diferenças na experiência do medo. | [PDF](analises_vitimizacao/analises/relatorio_completo_percepcao_social.pdf), [.py](analises_vitimizacao/scripts/analises/percepcao_social.py), [.ipynb](analises_vitimizacao/scripts/analises/percepcao_social.ipynb) |
| ⬜ | **Violência Urbana** | Evolução dos índices de violência ao longo do tempo. | `indices_violencia.csv` | Comparar diferentes anos para identificar tendências. | Links para arquivos de análise |
| ⬜ | **Violência Urbana** | Análise comparativa entre tipos de crimes (agressão, furto, roubo). | `agressao`, `furto`, `roubo` | Analisar proporções para compreender a natureza da criminalidade. | Links para arquivos de análise |
| ⬜ | **Demografia** | Distribuição populacional por idade e sexo. | `populacao_idade_sexo.csv` | Possibilidade de cruzamento com dados de violência para análises aprofundadas. | Links para arquivos de análise |
| ⬜ | **Homicídios** | Análise de homicídios tentados e consumados. | `Homicidios Tentado e Consumado(ENELISE)` | Verificar necessidade de tratamento adicional dos dados. | Links para arquivos de análise |
| ⬜ | **Dados Socioeconômicos** | Análise de indicadores da Pesquisa Nacional por Amostra de Domicílios (PNAD). | PNAD_1998, PNAD_2009 | O intervalo de 11 anos entre as pesquisas deve ser considerado na análise. | Links para arquivos de análise |

## Fontes de Dados Utilizadas
Esta seção detalha os arquivos de dados brutos utilizados, incluindo uma breve descrição do seu conteúdo principal.

| Nome do Arquivo (Caminho) | Planilha(s) no Arquivo | Descrição |
| :--- | :--- | :--- |
| `indices_violencia.csv` | N/A | Contém índices de violência referentes ao Survey de Vitimização em Belo Horizonte (2002). |
| `Vitimizacao_UP_27.csv` | N/A | Contém dados de vitimização de uma unidade de pesquisa específica, como parte do Survey de Vitimização em Belo Horizonte (2002). |
| `amostra_BH.xls` | Plan1, Plan2, Plan3, Plan4 | Contém amostras de dados coletadas em Belo Horizonte no âmbito do "Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã" (2008). |
| `amostra_MG.xls` | Plan1 | Contém amostras de dados para o estado de Minas Gerais, coletadas para a "Pesquisa de percepção de medo em Minas Gerais" e a "Pesquisa Policiamento comunitário: a visão dos policiais" (2008). |
| `populacao_idade_sexo.csv`| N/A | Contém dados demográficos da população brasileira (fonte: IBGE/PNAD), categorizados por idade e sexo. |
| `alunos_2006.csv` | N/A | Contém dados de alunos coletados em 2006, referentes ao projeto "Violência nas escolas públicas de Belo Horizonte e Região Metropolitana". |
| `professores_2006.csv` | N/A | Contém dados de professores coletados em 2006, relacionados ao mesmo projeto de violência nas escolas. |
| `Homicidios Tentado e Consumado(ENELISE).xls`| Homicidios Consumado, Homicidios Tentado, etc. | Inclui dados sobre homicídios tentados e consumados em diversas cidades de Minas Gerais. |
| Dados da PNAD 2009 | Múltiplas | Dados da Pesquisa Nacional por Amostra de Domicílios (2009), com 153.837 domicílios, organizados em subpastas por tipo de ocorrência (agressão, furto, roubo, etc.). |

## Inventário de Pesquisas Relevantes em Segurança Pública
### Tabela 1: Projetos e Pesquisas Geradoras de Dados
Esta tabela lista os principais projetos e pesquisas que resultaram na coleta de dados sobre vitimização e percepção de segurança no Brasil.

| Check List | Duração | Nome do serviço/breve descrição dos principais produtos/resultados | Nome do Contratante e país do serviço |
| :--- | :--- | :--- | :--- |
| ✅ | 2002 | Survey de Vitimização em Belo Horizonte | Belo Horizonte - Minas Gerais |
| | 2005 - 2006 | Pesquisa domiciliar de vitimização na cidade do Rio de Janeiro | Rio de Janeiro - Rio de Janeiro |
| ✅ | 2005 | Prevenção da violência nas escolas públicas de Belo Horizonte: caracterização das escolas e intervenções possíveis | Contagem - Minas Gerais |
| | 2005 | Pesquisa de vitimização nas cidades de Curitiba e Foz do Igraçu | Curitiba e Foz do Igraçu - Paraná |
| | 2006 | Violência nas escolas pública de Belo Horizonte e Região Metropolitana: caracterização do cenário, identificação de intervenções preventivas e capacitação para gestão local do problema | Região Metropolitana de Belo Horizonte - Minas Gerais |
| | 2006 | Survey de Vitimização na Região Metropolitana de Belo Horizonte | Região Metropolitana de Belo Horizonte - Minas Gerais |
| | 2006 | Diagnóstico da violência criminal no município de Itabira e construção do plano de segurança municipal com pesquisa de vitimização | Itabira - Minas Gerais |
| | 2008 | Diagnóstico de cultura cidadania no município de Belo Horizonte | Belo Horizonte - Minas Gerais |
| | 2008 | Pesquisa de percepção de medo em Minas Gerais | Minas Gerais |
| | 2008 | Pesquisa Policiamento comunitário: a visão dos policiais | Minas Gerais |
| | | Diagnóstico da qualidade e efetividade de atendimento socioeducativo | |
| | | Estudo sobre saúde dos profissionais do Sistema de defesa social | |
| | 2009 | Diagnóstico da violência criminal no município de Contagem e construção do Plano de segurança municipal e pesquisa de vitimização | Contagem - Minas Gerais |
| | 2012 | Pesquisa Nacional de Vitimização | Belo Horizonte - Minas Gerais |
| | 2022 | Plano de segurança e ordem pública e pesquisa de vitimização | Santa Bárbara – Minas Gerais |
| | 2023 | Diagnóstico de Criminalidade, Plano municipal de segurança pública do município de Contagem e pesquisa de vitimização | Contagem - Minas Gerais |
| | 2023 | Meta-análise de pesquisas de Vitimização em Minas Gerais e no Brasil | Minas Gerais |
| | 2023 | Diagnóstico da Segurança Pública em Minas Gerais: Pesquisa de Vitimização, Pesquisa de Qualidade de vida dos agentes de segurança, Mapeamento da articulação do Sistema de Justiça e dos Municípios com a segurança pública | Minas Gerais |

---
### Tabela 2: Catálogo Detalhado de Pesquisas de Vitimização (Características Técnicas)
Esta tabela apresenta um panorama de diversas pesquisas de vitimização realizadas no Brasil, com detalhes sobre sua metodologia, abrangência e escopo temporal. **Nota**: Algumas informações podem estar incompletas.

| Check List | Ano | Pesquisa/Instituição Responsável | Abrangência | Período de Referência | Tamanho da Amostra |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ✅ | 1988 | PNAD | Brasil | 1 ano | 81.628 domicílios |
| | 1992 | Ilanud | Município do Rio de Janeiro e Município de São Paulo | 5 anos | 1.000 entrevistados |
| | 1996 | Ilanud | Município do Rio de Janeiro e Município de São Paulo | 5 anos | 1.000 entrevistados |
| | 1996 | Iser/PAHO | Município do Rio de Janeiro | 5 anos | 2.469 entrevistados |
| | 1996 | ISER/FGV | Região Metropolitana do RJ | 1 ano | 1.126 entrevistados |
| | 1997 | Ilanud | Município do Rio de Janeiro e Município de São Paulo | 5 anos | 2.400 entrevistados |
| | 1997/1998 | O Povo e a PM | Distrito Federal | Toda a vida | 2000 entrevistados |
| | 1998 | SEADE | SP - Região Metropolitana e municípios com mais de 50.000 habitantes | 1 ano | 14.000 domicílios |
| | 1999 | USP | Região Metropolitana de SP | 6 meses | 1.000 entrevistados |
| | 2000 | ISER | Baixada Fluminense - RJ | 1 ano | 1.389 entrevistados |
| | 2001 | CDHP - IBGE | Copacabana e Leme | 1 ano | 450 entrevistados |
| | 2001 | Universidade de Caxias do Sul | Caxias do Sul (RS) | Sem informação | Sem informação |
| | 2001 | GUTO - UNESP | Município de Marília - SP | Toda a vida | 828 entrevistados |
| | 2002 | Módulo da PESB / DATAUFF | Brasil | Toda a Vida | 2460 entrevistados |
| | 2002 | Ilanud/FIA/USP | São Paulo, Rio de Janeiro, Vitória e Recife (municípios) | 5 anos | 2.800 entrevistados |
| | 2002 | ISP / Viva Rio | Município do Rio de Janeiro | 1 ano | 765 entrevistados |
| | 2002 | CRISP | Município de Belo Horizonte | 1 ano e 5 anos | 4.000 entrevistados |
| | 2003 | Instituto Futuro Brasil | Município de São Paulo | 1 ano e 5 anos | 5.000 domicílios |
| | 2003 | GUTO - UNESP | Município de Marília - SP | Toda a vida | Sem Informação |
| | 2003 | CPP / INSPER | Município de São Paulo | 1 ano | 5.000 entrevistados |
| | 2004 | Prefeitura | Alvorada (RS) | 1 ano | 500 domicílios |
| | 2005 | IBPS - PMV | Rio de Janeiro | 1 mês | 1.100 entrevistados por telefone |
| | 2005 | CRISP/SSP-Curitiba | Curitiba | 1 ano e 5 anos | 3560 entrevistados |
| | 2005 | NEPP- PR | Foz do Iguaçu | 1 ano e 5 anos | 700 entrevistados |
| | 2005 | SENASP - SEGUP - UFPA/CCS | Região Metropolitana de Belém e 8 municípios do Interior | 2 anos | 2848 entrevistados |
| | 2005/2006 | NUPEVI / UERJ | Município do Rio de Janeiro | Toda vida e 1 ano | 4.000 entrevistados |
| | 2006 | CRISP | Região Metropolitana de Belo Horizonte | 1 ano e 5 anos | 6.220 entrevistados |
| | 2006 | SEADE /Bloco da PED | Região Metropolitana de SP | Sem informação | 3.000 domicílios/mês |
| | 2006 | Pesquisa de Vitimização nas regiões do Orçamento Participativo | Regiões do Orçamento Participativo de Porto Alegre/RS | 1 ano | 1.404 domicílios |
| | 2007 | ISP | Região Metropolitana do RJ | 1 ano e 5 anos | 5.000 entrevistados |
| | 2007 | CRISP | Município de Itabira - MG | 1 ano e 5 anos | 401 entrevistados |
| | 2007 | Prefeitura | Esteio /RS | 23 meses | 2.682 entrevistados |
| | 2007/2008 | Universidade Federal de Pelotas | Município de Pelotas - RS | 1 ano e 5 anos | 2918 entrevistados |
| | 2008 | GUTO - UNESP | Município de Marília - SP | Toda a vida | 741 entrevistados |
| | 2008 | CPP / INSPER | Município de São Paulo | 1 ano | 2.967 entrevistados |
| | 2008 | UFGO | Região Metropolitana de Goiânia – GO | Sem informação | 3200 entrevistados |
| | 2008 | Instituto Futuro Brasil | Município de São Paulo | 1 ano e 5 anos | 3.000 domicílios |
| ✅ | 2008 | Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã | Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais | Toda a vida | 5.607 entrevistados |
| | 2008 | NEI/UFES | Grande Vitória (Serra, Cariacica, Viana, Vitória e Vila Velha) | 12 meses e 05 anos | 5.244 entrevistados |
| | 2009 | Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã | Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais | Toda a vida | 5.067 entrevistados |
| ✅ | 2009 | PNAD | Brasil | 1 ano | 153.837 domicílios |
| | 2009 | Pesquisa de Vitimização de Canoas | Município de Canoas/RS | 12 meses | 1.568 entrevistados |
| | 2010 | Pesquisa de Vitimização no estado do Mato Groso FEC/DataUFF | Mato Grosso | 12 meses | 4.000 domicílios |
| | 2010 | Módulo da PCVAPSP IESP/UERJ | Brasil | | 3.612 domicílios |
| | 2010/2012 | PNV/MJ | Brasil | 1 ano e Toda a vida | 78.008 entrevistados |
| | 2012 | Pesquisa de Vitimização Santa Catarina (DATAUFF/PMSC) | Santa Catarina | Sem Informação | 400 entrevistados |
| | 2013 | CPP / INSPER | Município de São Paulo | 1 ano | 3.000 entrevistados |
| | 2013 | Representações Sociais sobre Violência e Criminalidade de Bagé | Bagé/RS | Sem Informação | 408 entrevistados |
| | 2015 | Pesquisa sobre vitimização e percepção de risco entre profissionais da segurança (FBSP) | Profissionais de Segurança Pública registrados na Rede de Ensino à Distância da SENASP/MJ | Toda a carreira | 10.323 entrevistados |
| | 2015 | (Em andamento) Observatório de Segurança Cidadã | Município de Novo Hamburgo | - | 600 entrevistados |
| | 2015 | (Em andamento) Pesquisa Distrital de Segurança (SSPPS) | Distrito Federal | - | 19.537 domicílios |

---
<p style="text-align: center; font-size: 0.9em; color: #7f8c8d;">
    Repositório de Análises de Vitimização e Percepção de Segurança. <br>
    Dados compilados e analisados para fins de pesquisa científica. <br>
    &copy; 2025
</p>