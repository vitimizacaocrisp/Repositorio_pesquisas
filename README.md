# Repositório de Pesquisas em Segurança Pública

Repositório organizado para análise de dados de vitimização, seguindo boas práticas de gestão da informação científica e reprodutibilidade.

## Instruções

Drive: <a>https://drive.google.com/drive/folders/1k4qvQ4Vq6tAyDYbkf6zF0jkFH89Tp3Hf?usp=sharing</a></br>
baixe os arquivos do drive e os coloque em: /analises_vitimizacao/dados_brutos/</br>

instale as dependencias do python mostradas em:
```text
/analises_vitimizacao/pyproject.toml
```

## 📂 Estrutura do Repositório
```text
/Repositorio_pesquisas
├── dados_brutos/                   # Dados originais imutáveis
│   └── "identificação_data_dataset"/  
├── dados_tratados/                   # Dados prontos para análise
│   ├── csv/  
│   │   └── "identificação_data_dataset".csv
│   └── excel/  
│       └── "identificação_data_dataset".csv
├── scripts/
│   ├── tratamento/                # ETL e limpeza
│   │   ├── "identificação_data_dataset".ipynb
│   │   └── "identificação_data_dataset".py
│   ├── analise/                   # Modelagem estatística
│   │   ├── "identificação_data_dataset".ipynb
│   │   └── "identificação_data_dataset".py
│   └── visualizacao/              # Dashboards e gráficos
│       ├── "identificação_data_dataset".ipynb
│       └── "identificação_data_dataset".py
├── analises/                    # Projetos específicos
│   ├── relatorios/
│   └── visualizacoes/
├── documentos/
│   └──  "identificação_data_dataset"/                # ETL e limpeza
│       └── questionario.pdf
└── metadados/                   # Documentação técnica
    ├── por_fonte/                # Metadados específicos
    ├── dicionario_unificado.csv  # Variáveis padronizadas
    └── log_integracao.md         # Histórico de combinações
```

## 🌿 Branches
```text
O repositório é dividido em duas branches principais para organização dos tipos de scripts:

    📓 notebook: Contém os arquivos .ipynb utilizados para análise exploratória, prototipagem e visualização interativa.
    🐍 script: Contém os arquivos .py otimizados para produção, automação e reprodutibilidade de código.

Cada branch pode ter seu próprio .gitignore específico, ajustado ao tipo de arquivo e ferramenta utilizada.
```
## 📂 Metadados e Documentação Técnica
<ul>
    <li>Metadados por Fonte: Documentação detalhada sobre cada conjunto de dados.</li>
    <li>Dicionário de Variáveis: Arquivo dicionario_unificado.csv com descrição de todas as variáveis padronizadas.</li>
    <li>Log de Integração: Histórico de combinações e transformações de dados.</li>
</ul>

# 📂 Fluxo de Trabalho de Dados
<h3>Adicionar Dados</h3>
<ul>
    <li>Coloque os dados brutos na pasta <code>/2_dados/brutos/</code>, seguindo a estrutura por fonte.</li>
    <li>Documente os metadados na pasta <code>/6_metadados/por_fonte/</code>.</li>
</ul>

<h3>Processamento e Análise</h3>
<ul>
    <li>Utilize os scripts em <code>/3_scripts/</code> para tratamento e análise.</li>
    <li>Salve os resultados intermediários em <code>/2_dados/intermediarios/</code> e os finais em <code>/2_dados/tratados/</code>.</li>
</ul>

<h3>Publicação de Resultados</h3>
<ul>
    <li>Armazene relatórios, artigos e visualizações em <code>/5_outputs/</code>.</li>
</ul>

## 📂 Arquivos Buscados

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

## 📂 Análises Possíveis e Dados Relevantes

<table class="analysis-table">
  <thead>
    <tr>
      <th>✔️</th>
      <th>Categoria</th>
      <th>Análise Possível</th>
      <th>Dados Relevantes</th>
      <th>Observações</th>
      <th>Arquivos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><input type="checkbox"></td>
      <td rowspan="3">Violência Urbana</td>
      <td>Evolução dos índices de violência ao longo do tempo</td>
      <td>indices_violencia.csv, totais2008ateMAIO.csv</td>
      <td>Comparar anos diferentes</td>
      <td>
        <a href="analises_vitimizacao/analises/indices_violencia.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/indices_violencia.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/indices_violencia.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox"></td>
      <td>Comparação entre tipos de crimes (agressão, furto, roubo)</td>
      <td>agressao, furto, roubo, roubofurto</td>
      <td>Pode-se analisar proporções entre crimes</td>
      <td>
        <a href="analises_vitimizacao/analises/agressao.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/agressao.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/agressao.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox"></td>
      <td>Vítimização por unidades policiais</td>
      <td>Vitimizacao_UP_27.csv, Vitimizacao_UP_27.xlsx</td>
      <td>Dados em dois formatos para comparação</td>
      <td>
        <a href="analises_vitimizacao/analises/Vitimizacao_UP_27.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/Vitimizacao_UP_27.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/Vitimizacao_UP_27.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox">✅</td>
      <td rowspan="2">Percepção Social</td>
      <td>Medo e percepção de segurança em MG/BH</td>
      <td>percepção_medo_MG_2008, segurança</td>
      <td>Dados de 2008 podem estar desatualizados</td>
        <td>
        <a href="analises_vitimizacao/analises/relatorio_completo_percepcao_social.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/percepcao_social.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/percepcao_social.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox">✅</td>
      <td>Comparação entre amostras de BH e MG</td>
      <td>amostra_BH.xls, amostra_MG.xls</td>
      <td>Verificar compatibilidade dos dados</td>
        <td>
        <a href="analises_vitimizacao/analises/relatorio_completo_percepcao_social.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/percepcao_social.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/percepcao_social.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox"></td>
      <td>Demografia</td>
      <td>Distribuição populacional por idade e sexo</td>
      <td>populacao_idade_sexo.csv</td>
      <td>Pode cruzar com dados de violência</td>
      <td>
        <a href="analises_vitimizacao/analises/populacao_idade_sexo.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/populacao_idade_sexo.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/populacao_idade_sexo.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox">✅</td>
      <td rowspan="3">Violência Escolar</td>
      <td>Comparação entre percepção de alunos e professores(apenas alunos)</td>
      <td>alunos_2006.csv, professores_2006.csv</td>
      <td>Análise de divergências</td>
      <td>
        <a href="analises_vitimizacao/analises/relatorio_final_escolas_2006.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/escolas_final_2006.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/escolas_final_2006.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox">✅</td>
      <td>Panorama da violência em escolas</td>
      <td>alunos_2006.csv</td>
      <td>Análise de divergências</td>
      <td>
        <a href="analises_vitimizacao/analises/relatorio_alunos_escolas.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/escolas_2006.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/escolas_2006.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox"></td>
      <td>Metodologia da pesquisa escolar</td>
      <td>roteiro_2006.csv</td>
      <td>Entender como os dados foram coletados</td>
      <td>
        <a href="analises_vitimizacao/analises/roteiro_2006.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/roteiro_2006.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/roteiro_2006.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox"></td>
      <td>Homicídios</td>
      <td>Análise de homicídios tentados e consumados</td>
      <td>Homicidios Tentado e Consumado(EN)</td>
      <td>Verificar se dados estão em inglês</td>
      <td>
        <a href="analises_vitimizacao/analises/Homicidios_Tentado_e_Consumado.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/Homicidios_Tentado_e_Consumado.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/Homicidios_Tentado_e_Consumado.ipynb">.ipynb</a>
      </td>
    </tr>
    <tr>
      <td><input type="checkbox"></td>
      <td>Dados Socioeconômicos</td>
      <td>Análise de indicadores PNAD</td>
      <td>PNAD_1998, PNAD_2009</td>
      <td>Grande intervalo temporal entre pesquisas</td>
      <td>
        <a href="analises_vitimizacao/analises/PNAD_1998.pdf">PDF</a>,
        <a href="analises_vitimizacao/scripts/analises/PNAD_1998.py">.py</a>,
        <a href="analises_vitimizacao/scripts/analises/PNAD_1998.ipynb">.ipynb</a>
      </td>
    </tr>
  </tbody>
</table>
