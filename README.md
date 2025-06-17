## 📑 Sumário
- [📌 Introdução](#Introdução)
- [📂 Estrutura do Repositório](#Estrutura-do-Repositório)
- [🚀 Começando](#Começando)
- [🔁 Fluxo de Trabalho](#Fluxo-de-Trabalho)
- [🌿 Estratégia de Branches](#Estratégia-de-Branches)
- [⚙️ Visão Geral dos Scripts](#Visão-Geral-dos-Scripts)
- [📂 Metadados e Documentação Técnica](#Metadados-e-Documentação-Técnica)
- [📊 Análises Possíveis e Dados Relevantes](#Análises-Possíveis-e-Dados-Relevantes)
- [📁 Arquivos Buscados](#Arquivos-Buscados)



## Introdução
<p>Este repositório tem como objetivo centralizar, tratar e analisar dados de vitimização e percepção de segurança, com foco especial em pesquisas realizadas no Brasil. O projeto foi estruturado para garantir a gestão da informação científica e a reprodutibilidade das análises, seguindo as melhores práticas de organização de dados e código.</p>>

Aqui você encontrará desde os dados brutos e scripts de tratamento (ETL) até as análises estatísticas e relatórios finais.


## Estrutura do Repositório
O projeto está organizado da seguinte forma para separar claramente os dados, códigos e resultados:
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
<ul>
    <li>dados_brutos/: Contém os dados originais e imutáveis, conforme coletados.</li>
    <li>dados_tratados/: Armazena os dados após o processo de limpeza e tratamento, prontos para a análise.</li>
    <li>scripts/: Código-fonte dividido em tratamento (ETL) e analise (modelagem e visualização).</li>
    <li>analises/: Guarda os resultados finais, como relatórios (.pdf) e gráficos.</li>
    <li>documentos/: Documentação de apoio, como os questionários originais das pesquisas.</li>
    <li>metadados/: Dicionários de variáveis, logs de integração e documentação técnica.</li>
</ul>

## Começando
Para configurar o ambiente e executar as análises, siga os passos abaixo:

Clone o Repositório
```text
git clone <https://github.com/vitimizacaocrisp/Repositorio_pesquisas>
cd analises_vitimizacao
```
Baixe os Dados Brutos</li>
Os dados originais não estão no repositório para manter o tamanho gerenciável. Baixe-os do seguinte link:

Drive: <https://drive.google.com/drive/folders/1k4qvQ4Vq6tAyDYbkf6zF0jkFH89Tp3Hf?usp=sharing>
Organize os Dados
Descompacte e coloque os arquivos baixados dentro da pasta /dados_brutos/.

Instale as Dependências
Todas as bibliotecas Python necessárias estão listadas no arquivo pyproject.toml. Instale-as com o pip:
```text
pip install -r requirements.txt
```

## Fluxo de Trabalho
O fluxo de trabalho foi desenhado para ser claro e reprodutível:

Dados Brutos: Os dados são inseridos na pasta dados_brutos/ e nunca são alterados.
Tratamento (ETL): Os scripts na pasta scripts/tratamento/ são executados para limpar, padronizar e unificar os dados.
Dados Tratados: Os datasets resultantes são salvos em dados_tratados/ nos formatos CSV e Excel.
Análise: Os scripts em scripts/analise/ utilizam os dados tratados para gerar visualizações e insights.
Resultados: Relatórios (.pdf), dashboards e gráficos finais são salvos na pasta analises/.

## Estratégia de Branches
O repositório é dividido em duas branches principais para organização dos tipos de scripts:

notebook: Contém os arquivos .ipynb utilizados para análise exploratória, prototipagem e visualização interativa.
script: Contém os arquivos .py otimizados para produção, automação e reprodutibilidade de código.

## Visão Geral dos Scripts

<table>
  <thead>
    <tr>
      <th>Nome do Notebook</th>
      <th>Arquivo(s) Usado(s)</th>
      <th>Arquivo(s) Gerado(s)</th>
      <th>O que foi feito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>belo_horrizonte_2002.ipynb</b></td>
      <td><code>indices_violencia.csv</code><br><code>Vitimizacao_UP_27.csv</code></td>
      <td><code>belo_horrizonte_2002.csv</code><br><code>belo_horrizonte_2002.xlsx</code></td>
      <td><p>Foi realizada a junção de dois arquivos CSV. Foram removidas 52 colunas completamente nulas do primeiro arquivo e 114 do segundo. Valores nulos em colunas numéricas foram substituídos por 0. Ao final, os dataframes tratados foram empilhados e exportados para os formatos CSV e XLSX.</p></td>
    </tr>
    <tr>
      <td><b>escolas_2006.ipynb</b></td>
      <td><code>alunos_2006.csv</code><br><code>professores_2006.csv</code></td>
      <td><code>escolas_alunos_2006.csv</code><br><code>escolas_alunos_2006.xlsx</code><br><code>escolas_professores_2006.csv</code><br><code>escolas_professores_2006.xlsx</code></td>
      <td>Dois conjuntos de dados (alunos e professores) foram carregados e tratados separadamente. Em ambos, os valores numéricos nulos foram preenchidos com 0, as colunas de texto e seus nomes foram convertidos para minúsculas e as colunas que continham apenas valores nulos ou "não" foram removidas. Os nomes das colunas foram padronizados usando um dicionário e, por fim, os dois dataframes foram salvos em formatos CSV e XLSX.</td>
    </tr>
    <tr>
      <td><b>percepcao_medoMG_2008.ipynb</b></td>
      <td><code>amostra_BH.xls</code><br><code>amostra_MG.xls</code><br><code>populacao_idade_sexo.csv</code></td>
      <td><code>percepcao_medoMG.csv</code><br><code>percepcao_medoMG.xlsx</code></td>
      <td>Três arquivos de diferentes fontes foram carregados. Em cada um deles, foram removidas linhas duplicadas e colunas completamente nulas. Os valores numéricos nulos foram preenchidos com 0. Após o tratamento individual, os três dataframes foram unificados em um único arquivo, que foi exportado para os formatos CSV e XLSX.</td>
    </tr>
    <tr>
      <td><b>PNAD_2009.ipynb</b></td>
      <td>Múltiplos arquivos <code>.xls</code> de diversas pastas (agressao, furto, roubo, etc.)</td>
      <td>Múltiplos arquivos <code>.csv</code> e <code>.xlsx</code>, organizados em pastas por categoria (ex: <code>agressao.xlsx</code>, <code>furto.xlsx</code>)</td>
      <td>O script processou um grande volume de arquivos <code>.xls</code> divididos em categorias. Para cada arquivo, os dados foram lidos, as colunas foram renomeadas para maior clareza, os nomes de colunas e índices foram padronizados para minúsculas e os dados foram convertidos para tipos numéricos. Os dataframes tratados foram exportados de duas maneiras: como arquivos individuais (CSV e XLSX) organizados em pastas por categoria e como um único arquivo XLSX por categoria, contendo múltiplas abas.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Nome do Notebook</th>
      <th>Arquivo(s) de Entrada</th>
      <th>Arquivo(s) de Saída</th>
      <th>Descrição do Processo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>escolas_2006.ipynb</b></td>
      <td><code>escolas_alunos_2006.csv</code><br><code>escolas_professores_2006.csv</code></td>
      <td><code>relatorio_alunos_escolas.pdf</code></td>
      <td><p>O notebook carrega os dados tratados de alunos e professores. Realiza um pré-processamento para limpar e padronizar colunas específicas (como sexo, idade e raça/cor). Gera análises visuais, incluindo distribuição de alunos por idade, sexo e raça, e satisfação com o aprendizado. Ao final, compila todos os gráficos e análises textuais em um relatório consolidado em PDF.</p></td>
    </tr>
    <tr>
      <td><b>percepcao_social.ipynb</b></td>
      <td><code>belo_horrizonte_2002.xlsx</code><br><code>percepcao_medoMG.xlsx</code></td>
      <td><code>relatorio_completo_percepcao_social.pdf</code></td>
      <td>Este script combina dois conjuntos de dados sobre percepção de segurança (um de Belo Horizonte 2002 e outro de Minas Gerais). Limpa e prepara os dados combinados, focando em colunas como sexo, faixa etária e estrato do bairro. Gera análises sobre a percepção de risco de roubo, agressão e sequestro, segmentando por sexo, bairro e idade. Também cria uma matriz de correlação entre os tipos de risco e exporta todas as visualizações e tabelas para um relatório em PDF.</td>
    </tr>
    <tr>
      <td><b>PNAD_2009.ipynb</b></td>
      <td>Múltiplos arquivos <code>.xls</code> de diversas pastas (agressao, furto, etc.)</td>
      <td>Múltiplos arquivos <code>.csv</code> e <code>.xlsx</code>, organizados em pastas por categoria (ex: <code>agressao.xlsx</code>)</td>
      <td>O notebook carrega e trata um grande volume de arquivos <code>.xls</code> da PNAD 2009, organizados em subdiretórios por tipo de crime. Cada arquivo é processado para limpar o cabeçalho, renomear colunas e converter dados para formato numérico. Os dados tratados são então exportados em dois formatos: arquivos individuais (CSV e Excel) por tabela original e arquivos consolidados (Excel) por categoria, onde cada tabela se torna uma aba.</td>
    </tr>
  </tbody>
</table>

## Metadados e Documentação Técnica
<ul>
    <li>Metadados por Fonte: Documentação detalhada sobre cada conjunto de dados.</li>
    <li>Dicionário de Variáveis: Arquivo dicionario_unificado.csv com descrição de todas as variáveis padronizadas.</li>
    <li>Log de Integração: Histórico de combinações e transformações de dados.</li>
</ul>

## Análises Possíveis e Dados Relevantes

<p>A tabela a seguir detalha o status dos projetos de análise, indicando quais já foram concluídos (✅), os dados utilizados, e os resultados gerados, além de análises futuras.</p>
<table>
    <thead>
        <tr>
            <th>✔️</th>
            <th>Categoria</th>
            <th>Análise</th>
            <th>Dados Relevantes</th>
            <th>Observações</th>
            <th>Arquivos Gerados</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>✅</td>
            <td><strong>Violência Escolar</strong></td>
            <td>Panorama sobre o perfil e a percepção dos alunos e professores em escolas de Minas Gerais em 2006.</td>
            <td>alunos_2006.csv, professores_2006.csv</td>
            <td>A análise inclui distribuição demográfica (idade, sexo, raça), experiência docente e satisfação dos alunos.</td>
            <td class="file-links">
                <a href="analises_vitimizacao/analises/relatorio_final_escolas_2006.pdf">PDF</a>,
                <a href="analises_vitimizacao/scripts/analises/escolas_final_2006.py">.py</a>,
                <a href="analises_vitimizacao/scripts/analises/escolas_final_2006.ipynb">.ipynb</a>
            </td>
        </tr>
        <tr>
            <td>✅</td>
            <td><strong>Percepção Social</strong></td>
            <td>Percepção de risco de crimes (roubo, agressão, sequestro) em Belo Horizonte e Minas Gerais.</td>
            <td>belo_horrizonte_2002.xlsx, percepcao_medoMG.xlsx</td>
            <td>Os dados foram segmentados por sexo, tipo de bairro e faixa etária. A análise mostra como o medo é experienciado de forma diferente por cada grupo.</td>
            <td class="file-links">
                <a href="analises_vitimizacao/analises/relatorio_completo_percepcao_social.pdf">PDF</a>,
                <a href="analises_vitimizacao/scripts/analises/percepcao_social.py">.py</a>,
                <a href="analises_vitimizacao/scripts/analises/percepcao_social.ipynb">.ipynb</a>
            </td>
        </tr>
        <tr>
            <td>⬜</td>
            <td><strong>Violência Urbana</strong></td>
            <td>Evolução dos índices de violência ao longo do tempo.</td>
            <td>indices_violencia.csv</td>
            <td>Comparar diferentes anos para identificar tendências.</td>
            <td>Links para arquivos de análise</td>
        </tr>
        <tr>
            <td>⬜</td>
            <td><strong>Violência Urbana</strong></td>
            <td>Comparação entre tipos de crimes (agressão, furto, roubo).</td>
            <td><code>agressao</code>, <code>furto</code>, <code>roubo</code></td>
            <td>Analisar proporções para entender a natureza da criminalidade.</td>
            <td>Links para arquivos de análise</td>
        </tr>
        <tr>
            <td>⬜</td>
            <td><strong>Demografia</strong></td>
            <td>Distribuição populacional por idade e sexo.</td>
            <td>populacao_idade_sexo.csv</td>
            <td>Pode ser cruzado com dados de violência para análises mais profundas.</td>
            <td>Links para arquivos de análise</td>
        </tr>
        <tr>
            <td>⬜</td>
            <td><strong>Homicídios</strong></td>
            <td>Análise de homicídios tentados e consumados.</td>
            <td>Homicidios Tentado e Consumado(EN)</td>
            <td>Verificar se os dados precisam de tradução ou tratamento adicional.</td>
            <td>Links para arquivos de análise</td>
        </tr>
        <tr>
            <td>⬜</td>
            <td><strong>Dados Socioeconômicos</strong></td>
            <td>Análise de indicadores da Pesquisa Nacional por Amostra de Domicílios (PNAD).</td>
            <td>PNAD_1998, PNAD_2009</td>
            <td>O intervalo de 11 anos entre as pesquisas deve ser considerado na análise.</td>
            <td>Links para arquivos de análise</td>
        </tr>
    </tbody>
</table>

## Arquivos Buscados

<div class="security-tables">
<h2>Tabela 1: Inventário de Projetos e Pesquisas Geradoras de Dados em Segurança Pública</h2>
<p>Esta tabela lista os principais projetos, serviços e pesquisas que resultaram na coleta de dados sobre vitimização e percepção de segurança, muitas vezes realizados por ou para instituições específicas.</p>
<table class="security-table">
    <thead>
        <tr>
            <th>Check List</th>
            <th>Duração</th>
            <th>Nome do serviço/breve descrição dos principais produtos/resultados</th>
            <th>Nome do Contratante e país do serviço</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>✅</td>
            <td>2002</td>
            <td>Survey de Vitimização em Belo Horizonte</td>
            <td>Belo Horizonte - Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2005 - 2006</td>
            <td>Pesquisa domiciliar de vitimização na cidade do Rio de Janeiro</td>
            <td>Rio de Janeiro - Rio de Janeiro</td>
        </tr>
        <tr>
            <td>✅</td>
            <td>2005</td>
            <td>Prevenção da violência nas escolas públicas de Belo Horizonte: caracterização das escolas e intervenções possíveis</td>
            <td>Contagem - Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2005</td>
            <td>Pesquisa de vitimização nas cidades de Curitiba e Foz do Igraçu</td>
            <td>Curitiba e Foz do Igraçu - Paraná</td>
        </tr>
        <tr>
            <td></td>
            <td>2006</td>
            <td>Violência nas escolas pública de Belo Horizonte e Região Metropolitana: caracterização do cenário, identificação de intervenções preventivas e capacitação para gestão local do problema</td>
            <td>Região Metropolitana de Belo Horizonte - Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2006</td>
            <td>Survey de Vitimização na Região Metropolitana de Belo Horizonte</td>
            <td>Região Metropolitana de Belo Horizonte - Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2006</td>
            <td>Diagnóstico da violência criminal no município de Itabira e construção do plano de segurança municipal com pesquisa de vitimização</td>
            <td>Itabira - Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2008</td>
            <td>Diagnóstico de cultura cidadania no município de Belo Horizonte</td>
            <td>Belo Horizonte - Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2008</td>
            <td>Pesquisa de percepção de medo em Minas Gerais</td>
            <td>Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2008</td>
            <td>Pesquisa Policiamento comunitário: a visão dos policiais</td>
            <td>Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td>Diagnóstico da qualidade e efetividade de atendimento socioeducativo</td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td>Estudo sobre saúde dos profissionais do Sistema de defesa social</td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td>2009</td>
            <td>Diagnóstico da violência criminal no município de Contagem e construção do Plano de segurança municipal e pesquisa de vitimização</td>
            <td>Contagem - Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2012</td>
            <td>Pesquisa Nacional de Vitimização</td>
            <td>Belo Horizonte - Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2022</td>
            <td>Plano de segurança e ordem pública e pesquisa de vitimização</td>
            <td>Santa Bárbara – Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2023</td>
            <td>Diagnóstico de Criminalidade, Plano municipal de segurança pública do município de Contagem e pesquisa de vitimização</td>
            <td>Contagem - Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2023</td>
            <td>Meta-análise de pesquisas de Vitimização em Minas Gerais e no Brasil</td>
            <td>Minas Gerais</td>
        </tr>
        <tr>
            <td></td>
            <td>2023</td>
            <td>Diagnóstico da Segurança Pública em Minas Gerais: Pesquisa de Vitimização, Pesquisa de Qualidade de vida dos agentes de segurança, Mapeamento da articulação do Sistema de Justiça e dos Municípios com a segurança pública</td>
            <td>Minas Gerais</td>
        </tr>
    </tbody>
</table>

<hr>

<h2>Tabela 2: Catálogo Detalhado de Pesquisas de Vitimização (Características Técnicas)</h2>
<p>Esta tabela apresenta um panorama de diversas pesquisas de vitimização realizadas no Brasil, com detalhes sobre sua metodologia, abrangência e escopo temporal. <strong>Nota</strong>: Algumas informações podem estar incompletas ou necessitar de verificação nas fontes originais.</p>

<table class="security-table">
    <thead>
        <tr>
            <th>Check List</th>
            <th>Ano</th>
            <th>Pesquisa/Instituição Responsável</th>
            <th>Abrangência</th>
            <th>Período de Referência</th>
            <th>Tamanho da Amostra</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>✅</td>
            <td>1988</td>
            <td>PNAD</td>
            <td>Brasil</td>
            <td>1 ano</td>
            <td>81.628 domicílios</td>
        </tr>
        <tr>
            <td></td>
            <td>1992</td>
            <td>Ilanud</td>
            <td>Município do Rio de Janeiro e Município de São Paulo</td>
            <td>5 anos</td>
            <td>1.000 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>1996</td>
            <td>Ilanud</td>
            <td>Município do Rio de Janeiro e Município de São Paulo</td>
            <td>5 anos</td>
            <td>1.000 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>1996</td>
            <td>Iser/PAHO</td>
            <td>Município do Rio de Janeiro</td>
            <td>5 anos</td>
            <td>2.469 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>1996</td>
            <td>ISER/FGV</td>
            <td>Região Metropolitana do RJ</td>
            <td>1 ano</td>
            <td>1.126 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>1997</td>
            <td>Ilanud</td>
            <td>Município do Rio de Janeiro e Município de São Paulo</td>
            <td>5 anos</td>
            <td>2.400 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>1997/1998</td>
            <td>O Povo e a PM</td>
            <td>Distrito Federal</td>
            <td>Toda a vida</td>
            <td>2000 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>1998</td>
            <td>SEADE</td>
            <td>SP - Região Metropolitana e municípios com mais de 50.000 habitantes</td>
            <td>1 ano</td>
            <td>14.000 domicílios</td>
        </tr>
        <tr>
            <td></td>
            <td>1999</td>
            <td>USP</td>
            <td>Região Metropolitana de SP</td>
            <td>6 meses</td>
            <td>1.000 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2000</td>
            <td>ISER</td>
            <td>Baixada Fluminense - RJ</td>
            <td>1 ano</td>
            <td>1.389 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2001</td>
            <td>CDHP - IBGE</td>
            <td>Copacabana e Leme</td>
            <td>1 ano</td>
            <td>450 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2001</td>
            <td>Universidade de Caxias do Sul</td>
            <td>Caxias do Sul (RS)</td>
            <td>Sem informação</td>
            <td>Sem informação</td>
        </tr>
        <tr>
            <td></td>
            <td>2001</td>
            <td>GUTO - UNESP</td>
            <td>Município de Marília - SP</td>
            <td>Toda a vida</td>
            <td>828 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2002</td>
            <td>Módulo da PESB / DATAUFF</td>
            <td>Brasil</td>
            <td>Toda a Vida</td>
            <td>2460 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2002</td>
            <td>Ilanud/FIA/USP</td>
            <td>São Paulo, Rio de Janeiro, Vitória e Recife (municípios)</td>
            <td>5 anos</td>
            <td>2.800 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2002</td>
            <td>ISP / Viva Rio</td>
            <td>Município do Rio de Janeiro</td>
            <td>1 ano</td>
            <td>765 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2002</td>
            <td>CRISP</td>
            <td>Município de Belo Horizonte</td>
            <td>1 ano e 5 anos</td>
            <td>4.000 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2003</td>
            <td>Instituto Futuro Brasil</td>
            <td>Município de São Paulo</td>
            <td>1 ano e 5 anos</td>
            <td>5.000 domicílios</td>
        </tr>
        <tr>
            <td></td>
            <td>2003</td>
            <td>GUTO - UNESP</td>
            <td>Município de Marília - SP</td>
            <td>Toda a vida</td>
            <td>Sem Informação</td>
        </tr>
        <tr>
            <td></td>
            <td>2003</td>
            <td>CPP / INSPER</td>
            <td>Município de São Paulo</td>
            <td>1 ano</td>
            <td>5.000 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2004</td>
            <td>Prefeitura</td>
            <td>Alvorada (RS)</td>
            <td>1 ano</td>
            <td>500 domicílios</td>
        </tr>
        <tr>
            <td></td>
            <td>2005</td>
            <td>IBPS - PMV</td>
            <td>Rio de Janeiro</td>
            <td>1 mês</td>
            <td>1.100 entrevistados por telefone</td>
        </tr>
        <tr>
            <td></td>
            <td>2005</td>
            <td>CRISP/SSP-Curitiba</td>
            <td>Curitiba</td>
            <td>1 ano e 5 anos</td>
            <td>3560 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2005</td>
            <td>NEPP- PR</td>
            <td>Foz do Iguaçu</td>
            <td>1 ano e 5 anos</td>
            <td>700 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2005</td>
            <td>SENASP - SEGUP - UFPA/CCS</td>
            <td>Região Metropolitana de Belém e 8 municípios do Interior</td>
            <td>2 anos</td>
            <td>2848 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2005/2006</td>
            <td>NUPEVI / UERJ</td>
            <td>Município do Rio de Janeiro</td>
            <td>Toda vida e 1 ano</td>
            <td>4.000 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2006</td>
            <td>CRISP</td>
            <td>Região Metropolitana de Belo Horizonte</td>
            <td>1 ano e 5 anos</td>
            <td>6.220 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2006</td>
            <td>SEADE /Bloco da PED</td>
            <td>Região Metropolitana de SP</td>
            <td>Sem informação</td>
            <td>3.000 domicílios/mês</td>
        </tr>
        <tr>
            <td></td>
            <td>2006</td>
            <td>Pesquisa de Vitimização nas regiões do Orçamento Participativo</td>
            <td>Regiões do Orçamento Participativo de Porto Alegre/RS</td>
            <td>1 ano</td>
            <td>1.404 domicílios</td>
        </tr>
        <tr>
            <td></td>
            <td>2007</td>
            <td>ISP</td>
            <td>Região Metropolitana do RJ</td>
            <td>1 ano e 5 anos</td>
            <td>5.000 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2007</td>
            <td>CRISP</td>
            <td>Município de Itabira - MG</td>
            <td>1 ano e 5 anos</td>
            <td>401 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2007</td>
            <td>Prefeitura</td>
            <td>Esteio /RS</td>
            <td>23 meses</td>
            <td>2.682 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2007/2008</td>
            <td>Universidade Federal de Pelotas</td>
            <td>Município de Pelotas - RS</td>
            <td>1 ano e 5 anos</td>
            <td>2918 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2008</td>
            <td>GUTO - UNESP</td>
            <td>Município de Marília - SP</td>
            <td>Toda a vida</td>
            <td>741 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2008</td>
            <td>CPP / INSPER</td>
            <td>Município de São Paulo</td>
            <td>1 ano</td>
            <td>2.967 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2008</td>
            <td>UFGO</td>
            <td>Região Metropolitana de Goiânia – GO</td>
            <td>Sem informação</td>
            <td>3200 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2008</td>
            <td>Instituto Futuro Brasil</td>
            <td>Município de São Paulo</td>
            <td>1 ano e 5 anos</td>
            <td>3.000 domicílios</td>
        </tr>
        <tr>
            <td>✅</td>
            <td>2008</td>
            <td>Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã</td>
            <td>Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais</td>
            <td>Toda a vida</td>
            <td>5.607 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2008</td>
            <td>NEI/UFES</td>
            <td>Grande Vitória (Serra, Cariacica, Viana, Vitória e Vila Velha)</td>
            <td>12 meses e 05 anos</td>
            <td>5.244 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2009</td>
            <td>Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã</td>
            <td>Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais</td>
            <td>Toda a vida</td>
            <td>5.067 entrevistados</td>
        </tr>
        <tr>
            <td>✅</td>
            <td>2009</td>
            <td>PNAD</td>
            <td>Brasil</td>
            <td>1 ano</td>
            <td>153.837 domicílios</td>
        </tr>
        <tr>
            <td></td>
            <td>2009</td>
            <td>Pesquisa de Vitimização de Canoas</td>
            <td>Município de Canoas/RS</td>
            <td>12 meses</td>
            <td>1.568 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2010</td>
            <td>Pesquisa de Vitimização no estado do Mato Groso FEC/DataUFF</td>
            <td>Mato Grosso</td>
            <td>12 meses</td>
            <td>4.000 domicílios</td>
        </tr>
        <tr>
            <td></td>
            <td>2010</td>
            <td>Módulo da PCVAPSP IESP/UERJ</td>
            <td>Brasil</td>
            <td>&nbsp;</td>
            <td>3.612 domicílios</td>
        </tr>
        <tr>
            <td></td>
            <td>2010/2012</td>
            <td>PNV/MJ</td>
            <td>Brasil</td>
            <td>1 ano e Toda a vida</td>
            <td>78.008 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2012</td>
            <td>Pesquisa de Vitimização Santa Catarina (DATAUFF/PMSC)</td>
            <td>Santa Catarina</td>
            <td>Sem Informação</td>
            <td>400 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2013</td>
            <td>CPP / INSPER</td>
            <td>Município de São Paulo</td>
            <td>1 ano</td>
            <td>3.000 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2013</td>
            <td>Representações Sociais sobre Violência e Criminalidade de Bagé</td>
            <td>Bagé/RS</td>
            <td>Sem Informação</td>
            <td>408 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2015</td>
            <td>Pesquisa sobre vitimização e percepção de risco entre profissionais da segurança (FBSP)</td>
            <td>Profissionais de Segurança Pública registrados na Rede de Ensino à Distância da SENASP/MJ</td>
            <td>Toda a carreira</td>
            <td>10.323 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2015</td>
            <td>(Em andamento) Observatório de Segurança Cidadã</td>
            <td>Município de Novo Hamburgo</td>
            <td>-</td>
            <td>600 entrevistados</td>
        </tr>
        <tr>
            <td></td>
            <td>2015</td>
            <td>(Em andamento) Pesquisa Distrital de Segurança (SSPPS)</td>
            <td>Distrito Federal</td>
            <td>-</td>
            <td>19.537 domicílios</td>
        </tr>
    </tbody>
</table>

</div>
