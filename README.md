# Repositório de Pesquisas em Segurança Pública

Repositório organizado para análise de dados de vitimização, seguindo boas práticas de gestão da informação científica e reprodutibilidade.

## 📂 Estrutura do Repositório
```text
/repositorio-seguranca-publica
├── 1_documentacao_geral/
│   ├── plano_gestao_dados.md       # Data Management Plan (DMP)
│   ├── protocolos_coleta.md
│   └── diretrizes_eticas.pdf
├── 2_dados/
│   ├── brutos/                     # Dados originais imutáveis
│   │   ├── pnad/                   # Por fonte de dados
│   │   ├── anuario_fbsp/
│   │   ├── sim/
│   │   └── municipais/
│   ├── intermediarios/            # Dados em processamento
│   └── tratados/                  # Dados prontos para análise
│       ├── versoes/               # Versionamento semântico (v1.0.0)
│       └── padronizados/          # Dados integrados
├── 3_scripts/
│   ├── coleta/                    # Scripts de ingestão
│   ├── tratamento/                # ETL e limpeza
│   ├── analise/                   # Modelagem estatística
│   └── visualizacao/              # Dashboards e gráficos
├── 4_analises/                    # Projetos específicos
│   ├── projeto_tendências/
│   ├── projeto_fatores_risco/
│   └── projeto_comparativo/
├── 5_outputs/
│   ├── relatorios/
│   ├── publicacoes/
│   └── visualizacoes/
└── 6_metadados/                   # Documentação técnica
    ├── por_fonte/                # Metadados específicos
    ├── dicionario_unificado.csv  # Variáveis padronizadas
    └── log_integracao.md         # Histórico de combinações
```

## 📂 Arquivos em Uso
PNAD_2009

## 📂 Arquivos para Uso

<table>
  <thead>
    <tr>
      <th>Duração</th>
      <th>Nome do serviço/breve descrição dos principais produtos/resultados</th>
      <th>Nome do Contratante e país do serviço</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2002</td>
      <td>Survey de Vitimização em Belo Horizonte</td>
      <td>Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2005 - 2006</td>
      <td>Pesquisa domiciliar de vitimização na cidade do Rio de Janeiro</td>
      <td>Rio de Janeiro - Rio de Janeiro</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>Prevenção da violência nas escolas públicas de Belo Horizonte: caracterização das escolas e intervenções possíveis</td>
      <td>Contagem - Minas Gerais</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>Pesquisa de vitimização nas cidades de Curitiba e Foz do Igraçu</td>
      <td>Curitiba e Foz do Igraçu - Paraná</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>Violência nas escolas pública de Belo Horizonte e Região Metropolitana: caracterização do cenário, identificação de intervenções preventivas e capacitação para gestão local do problema</td>
      <td>Região Metropolitana de Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>Survey de Vitimização na Região Metropolitana de Belo Horizonte</td>
      <td>Região Metropolitana de Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>Diagnóstico da violência criminal no município de Itabira e construção do plano de segurança municipal com pesquisa de vitimização</td>
      <td>Itabira - Minas Gerais</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Diagnóstico de cultura cidadania no município de Belo Horizonte</td>
      <td>Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Pesquisa de percepção de medo em Minas Gerais</td>
      <td>Minas Gerais</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Pesquisa Policiamento comunitário: a visão dos policiais</td>
      <td>Minas Gerais</td>
    </tr>
    <tr>
      <td></td>
      <td>Diagnóstico da qualidade e efetividade de atendimento socioeducativo</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Estudo sobre saúde dos profissionais do Sistema de defesa social</td>
      <td></td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Diagnóstico da violência criminal no município de Contagem e construção do Plano de segurança municipal e pesquisa de vitimização</td>
      <td>Contagem - Minas Gerais</td>
    </tr>
    <tr>
      <td>2012</td>
      <td>Pesquisa Nacional de Vitimização</td>
      <td>Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2022</td>
      <td>Plano de segurança e ordem pública e pesquisa de vitimização</td>
      <td>Santa Bárbara – Minas Gerais</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>Diagnóstico de Criminalidade, Plano municipal de segurança pública do município de Contagem e pesquisa de vitimização</td>
      <td>Contagem - Minas Gerais</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>Meta-análise de pesquisas de Vitimização em Minas Gerais e no Brasil</td>
      <td>Minas Gerais</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>Diagnóstico da Segurança Pública em Minas Gerais: Pesquisa de Vitimização, Pesquisa de Qualidade de vida dos agentes de segurança, Mapeamento da articulação do Sistema de Justiça e dos Municípios com a segurança pública</td>
      <td>Minas Gerais</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Ano</th>
      <th>Pesquisa/Instituição Responsável</th>
      <th>Abrangência</th>
      <th>Período de Referência</th>
      <th>Tamanho da Amostra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1988</td>
      <td>PNAD</td>
      <td>Brasil</td>
      <td>1 ano</td>
      <td>81.628 domicílios</td>
    </tr>
    <tr>
      <td>1992</td>
      <td>Ilanud</td>
      <td>Município do Rio de Janeiro e Município de São Paulo</td>
      <td>5 anos</td>
      <td>1.000 entrevistados</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>Ilanud</td>
      <td>Município do Rio de Janeiro e Município de São Paulo</td>
      <td>5 anos</td>
      <td>1.000 entrevistados</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>Iser/PAHO</td>
      <td>Município do Rio de Janeiro</td>
      <td>5 anos</td>
      <td>2.469 entrevistados</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>ISER/FGV</td>
      <td>Região Metropolitana do RJ</td>
      <td>1 ano</td>
      <td>1.126 entrevistados</td>
    </tr>
    <tr>
      <td>1997</td>
      <td>Ilanud</td>
      <td>Município do Rio de Janeiro e Município de São Paulo</td>
      <td>5 anos</td>
      <td>2.400 entrevistados</td>
    </tr>
    <tr>
      <td>1997/1998</td>
      <td>O Povo e a PM</td>
      <td>Distrito Federal</td>
      <td>Toda a vida</td>
      <td>2000 entrevistados</td>
    </tr>
    <tr>
      <td>1998</td>
      <td>SEADE</td>
      <td>SP - Região Metropolitana e municípios com mais de 50.000 habitantes</td>
      <td>1 ano</td>
      <td>14.000 domicílios</td>
    </tr>
    <tr>
      <td>1999</td>
      <td>USP</td>
      <td>Região Metropolitana de SP</td>
      <td>6 meses</td>
      <td>1.000 entrevistados</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>ISER</td>
      <td>Baixada Fluminense - RJ</td>
      <td>1 ano</td>
      <td>1.389 entrevistados</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>CDHP - IBGE</td>
      <td>Copacabana e Leme</td>
      <td>1 ano</td>
      <td>450 entrevistados</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>Universidade de Caxias do Sul</td>
      <td>Caxias do Sul (RS)</td>
      <td>Sem informação</td>
      <td>Sem informação</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>GUTO - UNESP</td>
      <td>Município de Marília - SP</td>
      <td>Toda a vida</td>
      <td>828 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>Módulo da PESB / DATAUFF</td>
      <td>Brasil</td>
      <td>Toda a Vida</td>
      <td>2460 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>Ilanud/FIA/USP</td>
      <td>São Paulo, Rio de Janeiro, Vitória e Recife (municípios)</td>
      <td>5 anos</td>
      <td>2.800 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>ISP / Viva Rio</td>
      <td>Município do Rio de Janeiro</td>
      <td>1 ano</td>
      <td>765 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>CRISP</td>
      <td>Município de Belo Horizonte</td>
      <td>1 ano e 5 anos</td>
      <td>4.000 entrevistados</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>Instituto Futuro Brasil</td>
      <td>Município de São Paulo</td>
      <td>1 ano e 5 anos</td>
      <td>5.000 domicílios</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>GUTO - UNESP</td>
      <td>Município de Marília - SP</td>
      <td>Toda a vida</td>
      <td>Sem Informação</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>CPP / INSPER</td>
      <td>Município de São Paulo</td>
      <td>1 ano</td>
      <td>5.000 entrevistados</td>
    </tr>
    <tr>
      <td>2004</td>
      <td>Prefeitura</td>
      <td>Alvorada (RS)</td>
      <td>1 ano</td>
      <td>500 domicílios</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>IBPS - PMV</td>
      <td>Rio de Janeiro</td>
      <td>1 mês</td>
      <td>1.100 entrevistados por telefone</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>CRISP/SSP-Curitiba</td>
      <td>Curitiba</td>
      <td>1 ano e 5 anos</td>
      <td>3560 entrevistados</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>NEPP- PR</td>
      <td>Foz do Iguaçu</td>
      <td>1 ano e 5 anos</td>
      <td>700 entrevistados</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>SENASP - SEGUP - UFPA/CCS</td>
      <td>Região Metropolitana de Belém e 8 municípios do Interior</td>
      <td>2 anos</td>
      <td>2848 entrevistados</td>
    </tr>
    <tr>
      <td>2005/2006</td>
      <td>NUPEVI / UERJ</td>
      <td>Município do Rio de Janeiro</td>
      <td>Toda vida e 1 ano</td>
      <td>4.000 entrevistados</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>CRISP</td>
      <td>Região Metropolitana de Belo Horizonte</td>
      <td>1 ano e 5 anos</td>
      <td>6.220 entrevistados</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>SEADE /Bloco da PED</td>
      <td>Região Metropolitana de SP</td>
      <td>Sem informação</td>
      <td>3.000 domicílios/mês</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>Pesquisa de Vitimização nas regiões do Orçamento Participativo</td>
      <td>Regiões do Orçamento Participativo de Porto Alegre/RS</td>
      <td>1 ano</td>
      <td>1.404 domicílios</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>ISP</td>
      <td>Região Metropolitana do RJ</td>
      <td>1 ano e 5 anos</td>
      <td>5.000 entrevistados</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>CRISP</td>
      <td>Município de Itabira - MG</td>
      <td>1 ano e 5 anos</td>
      <td>401 entrevistados</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>Prefeitura</td>
      <td>Esteio /RS</td>
      <td>23 meses</td>
      <td>2.682 entrevistados</td>
    </tr>
    <tr>
      <td>2007/2008</td>
      <td>Universidade Federal de Pelotas</td>
      <td>Município de Pelotas - RS</td>
      <td>1 ano e 5 anos</td>
      <td>2918 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>GUTO - UNESP</td>
      <td>Município de Marília - SP</td>
      <td>Toda a vida</td>
      <td>741 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>CPP / INSPER</td>
      <td>Município de São Paulo</td>
      <td>1 ano</td>
      <td>2.967 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>UFGO</td>
      <td>Região Metropolitana de Goiânia – GO</td>
      <td>Sem informação</td>
      <td>3200 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Instituto Futuro Brasil</td>
      <td>Município de São Paulo</td>
      <td>1 ano e 5 anos</td>
      <td>3.000 domicílios</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã</td>
      <td>Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais</td>
      <td>Toda a vida</td>
      <td>5.607 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>NEI/UFES</td>
      <td>Grande Vitória (Serra, Cariacica, Viana, Vitória e Vila Velha)</td>
      <td>12 meses e 05 anos</td>
      <td>5.244 entrevistados</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã</td>
      <td>Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais</td>
      <td>Toda a vida</td>
      <td>5.067 entrevistados</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>PNAD</td>
      <td>Brasil</td>
      <td>1 ano</td>
      <td>153.837 domicílios</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Pesquisa de Vitimização de Canoas</td>
      <td>Município de Canoas/RS</td>
      <td>12 meses</td>
      <td>1.568 entrevistados</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>Pesquisa de Vitimização no estado do Mato Groso FEC/DataUFF</td>
      <td>Mato Grosso</td>
      <td>12 meses</td>
      <td>4.000 domicílios</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>Módulo da PCVAPSP IESP/UERJ</td>
      <td>Brasil</td>
      <td>&nbsp;</td>
      <td>3.612 domicílios</td>
    </tr>
    <tr>
      <td>2010/2012</td>
      <td>PNV/MJ</td>
      <td>Brasil</td>
      <td>1 ano e Toda a vida</td>
      <td>78.008 entrevistados</td>
    </tr>
    <tr>
      <td>2012</td>
      <td>Pesquisa de Vitimização Santa Catarina (DATAUFF/PMSC)</td>
      <td>Santa Catarina</td>
      <td>Sem Informação</td>
      <td>400 entrevistados</td>
    </tr>
    <tr>
      <td>2013</td>
      <td>CPP / INSPER</td>
      <td>Município de São Paulo</td>
      <td>1 ano</td>
      <td>3.000 entrevistados</td>
    </tr>
    <tr>
      <td>2013</td>
      <td>Representações Sociais sobre Violência e Criminalidade de Bagé</td>
      <td>Bagé/RS</td>
      <td>Sem Informação</td>
      <td>408 entrevistados</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>Pesquisa sobre vitimização e percepção de risco entre profissionais da segurança (FBSP)</td>
      <td>Profissionais de Segurança Pública registrados na Rede de Ensino à Distância da SENASP/MJ</td>
      <td>Toda a carreira</td>
      <td>10.323 entrevistados</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>(Em andamento) Observatório de Segurança Cidadã</td>
      <td>Município de Novo Hamburgo</td>
      <td>-</td>
      <td>600 entrevistados</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>(Em andamento) Pesquisa Distrital de Segurança (SSPPS)</td>
      <td>Distrito Federal</td>
      <td>-</td>
      <td>19.537 domicílios</td>
    </tr>
  </tbody>
</table>

Fonte: Catão, 2010 “Treinamento para Pesquisa Nacional de Vitimização realizada em São Paulo. Junho, 2010” apud Relatório da Primeira Pesquisa Nacional de Vitimização – 2013

## 📂 Dados para Cada Pesquisa

<h3>Análise de Vitimização e Percepção de Segurança (Dados dos Serviços e Projetos)</h3>
<table>
  <thead>
    <tr>
      <th>Duração</th>
      <th>Nome do serviço/breve descrição dos principais produtos/resultados</th>
      <th>Nome do Contratante e país do serviço</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2002</td>
      <td>Survey de Vitimização em Belo Horizonte</td>
      <td>Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2005 - 2006</td>
      <td>Pesquisa domiciliar de vitimização na cidade do Rio de Janeiro</td>
      <td>Rio de Janeiro - Rio de Janeiro</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>Prevenção da violência nas escolas públicas de Belo Horizonte: caracterização das escolas e intervenções possíveis</td>
      <td>Contagem - Minas Gerais</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>Pesquisa de vitimização nas cidades de Curitiba e Foz do Iguaçu</td>
      <td>Curitiba e Foz do Iguaçu - Paraná</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>Violência nas escolas pública de Belo Horizonte e Região Metropolitana: caracterização do cenário, identificação de intervenções preventivas e capacitação para gestão local do problema</td>
      <td>Região Metropolitana de Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>Survey de Vitimização na Região Metropolitana de Belo Horizonte</td>
      <td>Região Metropolitana de Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>Diagnóstico da violência criminal no município de Itabira e construção do plano de segurança municipal com pesquisa de vitimização</td>
      <td>Itabira - Minas Gerais</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Diagnóstico de cultura cidadania no município de Belo Horizonte</td>
      <td>Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Pesquisa de percepção de medo em Minas Gerais</td>
      <td>Minas Gerais</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Pesquisa Policiamento comunitário: a visão dos policiais</td>
      <td>Minas Gerais</td>
    </tr>
    <tr>
      <td></td>
      <td>Diagnóstico da qualidade e efetividade de atendimento socioeducativo</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Estudo sobre saúde dos profissionais do Sistema de defesa social</td>
      <td></td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Diagnóstico da violência criminal no município de Contagem e construção do Plano de segurança municipal e pesquisa de vitimização</td>
      <td>Contagem - Minas Gerais</td>
    </tr>
    <tr>
      <td>2012</td>
      <td>Pesquisa Nacional de Vitimização</td>
      <td>Belo Horizonte - Minas Gerais</td>
    </tr>
    <tr>
      <td>2022</td>
      <td>Plano de segurança e ordem pública e pesquisa de vitimização</td>
      <td>Santa Bárbara – Minas Gerais</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>Diagnóstico de Criminalidade, Plano municipal de segurança pública do município de Contagem e pesquisa de vitimização</td>
      <td>Contagem - Minas Gerais</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>Meta-análise de pesquisas de Vitimização em Minas Gerais e no Brasil</td>
      <td>Minas Gerais</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>Diagnóstico da Segurança Pública em Minas Gerais: Pesquisa de Vitimização, Pesquisa de Qualidade de vida dos agentes de segurança, Mapeamento da articulação do Sistema de Justiça e dos Municípios com a segurança pública</td>
      <td>Minas Gerais</td>
    </tr>
  </tbody>
</table>
<h3>Análise de Metodologia e Escopo de Pesquisas (Detalhes Técnicos)</h3>
<table>
  <thead>
    <tr>
      <th>Ano</th>
      <th>Pesquisa/Instituição Responsável</th>
      <th>Abrangência</th>
      <th>Período de Referência</th>
      <th>Tamanho da Amostra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1988</td>
      <td>PNAD</td>
      <td>Brasil</td>
      <td>1 ano</td>
      <td>81.628 domicílios</td>
    </tr>
    <tr>
      <td>1992</td>
      <td>Ilanud</td>
      <td>Município do Rio de Janeiro e Município de São Paulo</td>
      <td>5 anos</td>
      <td>1.000 entrevistados</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>Ilanud</td>
      <td>Município do Rio de Janeiro e Município de São Paulo</td>
      <td>5 anos</td>
      <td>1.000 entrevistados</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>Iser/PAHO</td>
      <td>Município do Rio de Janeiro</td>
      <td>5 anos</td>
      <td>2.469 entrevistados</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>ISER/FGV</td>
      <td>Região Metropolitana do RJ</td>
      <td>1 ano</td>
      <td>1.126 entrevistados</td>
    </tr>
    <tr>
      <td>1997</td>
      <td>Ilanud</td>
      <td>Município do Rio de Janeiro e Município de São Paulo</td>
      <td>5 anos</td>
      <td>2.400 entrevistados</td>
    </tr>
    <tr>
      <td>1997/1998</td>
      <td>O Povo e a PM</td>
      <td>Distrito Federal</td>
      <td>Toda a vida</td>
      <td>2000 entrevistados</td>
    </tr>
    <tr>
      <td>1998</td>
      <td>SEADE</td>
      <td>SP - Região Metropolitana e municípios com mais de 50.000 habitantes</td>
      <td>1 ano</td>
      <td>14.000 domicílios</td>
    </tr>
    <tr>
      <td>1999</td>
      <td>USP</td>
      <td>Região Metropolitana de SP</td>
      <td>6 meses</td>
      <td>1.000 entrevistados</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>ISER</td>
      <td>Baixada Fluminense - RJ</td>
      <td>1 ano</td>
      <td>1.389 entrevistados</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>CDHP - IBGE</td>
      <td>Copacabana e Leme</td>
      <td>1 ano</td>
      <td>450 entrevistados</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>Universidade de Caxias do Sul</td>
      <td>Caxias do Sul (RS)</td>
      <td>Sem informação</td>
      <td>Sem informação</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>GUTO - UNESP</td>
      <td>Município de Marília - SP</td>
      <td>Toda a vida</td>
      <td>828 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>Módulo da PESB / DATAUFF</td>
      <td>Brasil</td>
      <td>Toda a Vida</td>
      <td>2460 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>Ilanud/FIA/USP</td>
      <td>São Paulo, Rio de Janeiro, Vitória e Recife (municípios)</td>
      <td>5 anos</td>
      <td>2.800 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>ISP / Viva Rio</td>
      <td>Município do Rio de Janeiro</td>
      <td>1 ano</td>
      <td>765 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>CRISP</td>
      <td>Município de Belo Horizonte</td>
      <td>1 ano e 5 anos</td>
      <td>4.000 entrevistados</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>Instituto Futuro Brasil</td>
      <td>Município de São Paulo</td>
      <td>1 ano e 5 anos</td>
      <td>5.000 domicílios</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>GUTO - UNESP</td>
      <td>Município de Marília - SP</td>
      <td>Toda a vida</td>
      <td>Sem Informação</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>CPP / INSPER</td>
      <td>Município de São Paulo</td>
      <td>1 ano</td>
      <td>5.000 entrevistados</td>
    </tr>
    <tr>
      <td>2004</td>
      <td>Prefeitura</td>
      <td>Alvorada (RS)</td>
      <td>1 ano</td>
      <td>500 domicílios</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>IBPS - PMV</td>
      <td>Rio de Janeiro</td>
      <td>1 mês</td>
      <td>1.100 entrevistados por telefone</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>CRISP/SSP-Curitiba</td>
      <td>Curitiba</td>
      <td>1 ano e 5 anos</td>
      <td>3560 entrevistados</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>NEPP- PR</td>
      <td>Foz do Iguaçu</td>
      <td>1 ano e 5 anos</td>
      <td>700 entrevistados</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>SENASP - SEGUP - UFPA/CCS</td>
      <td>Região Metropolitana de Belém e 8 municípios do Interior</td>
      <td>2 anos</td>
      <td>2848 entrevistados</td>
    </tr>
    <tr>
      <td>2005/2006</td>
      <td>NUPEVI / UERJ</td>
      <td>Município do Rio de Janeiro</td>
      <td>Toda vida e 1 ano</td>
      <td>4.000 entrevistados</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>CRISP</td>
      <td>Região Metropolitana de Belo Horizonte</td>
      <td>1 ano e 5 anos</td>
      <td>6.220 entrevistados</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>SEADE /Bloco da PED</td>
      <td>Região Metropolitana de SP</td>
      <td>Sem informação</td>
      <td>3.000 domicílios/mês</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>Pesquisa de Vitimização nas regiões do Orçamento Participativo</td>
      <td>Regiões do Orçamento Participativo de Porto Alegre/RS</td>
      <td>1 ano</td>
      <td>1.404 domicílios</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>ISP</td>
      <td>Região Metropolitana do RJ</td>
      <td>1 ano e 5 anos</td>
      <td>5.000 entrevistados</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>CRISP</td>
      <td>Município de Itabira - MG</td>
      <td>1 ano e 5 anos</td>
      <td>401 entrevistados</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>Prefeitura</td>
      <td>Esteio /RS</td>
      <td>23 meses</td>
      <td>2.682 entrevistados</td>
    </tr>
    <tr>
      <td>2007/2008</td>
      <td>Universidade Federal de Pelotas</td>
      <td>Município de Pelotas - RS</td>
      <td>1 ano e 5 anos</td>
      <td>2918 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>GUTO - UNESP</td>
      <td>Município de Marília - SP</td>
      <td>Toda a vida</td>
      <td>741 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>CPP / INSPER</td>
      <td>Município de São Paulo</td>
      <td>1 ano</td>
      <td>2.967 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>UFGO</td>
      <td>Região Metropolitana de Goiânia – GO</td>
      <td>Sem informação</td>
      <td>3200 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Instituto Futuro Brasil</td>
      <td>Município de São Paulo</td>
      <td>1 ano e 5 anos</td>
      <td>3.000 domicílios</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã</td>
      <td>Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais</td>
      <td>Toda a vida</td>
      <td>5.607 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>NEI/UFES</td>
      <td>Grande Vitória (Serra, Cariacica, Viana, Vitória e Vila Velha)</td>
      <td>12 meses e 05 anos</td>
      <td>5.244 entrevistados</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã</td>
      <td>Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais</td>
      <td>Toda a vida</td>
      <td>5.067 entrevistados</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>PNAD</td>
      <td>Brasil</td>
      <td>1 ano</td>
      <td>153.837 domicílios</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Pesquisa de Vitimização de Canoas</td>
      <td>Município de Canoas/RS</td>
      <td>12 meses</td>
      <td>1.568 entrevistados</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>Pesquisa de Vitimização no estado do Mato Groso FEC/DataUFF</td>
      <td>Mato Grosso</td>
      <td>12 meses</td>
      <td>4.000 domicílios</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>Módulo da PCVAPSP IESP/UERJ</td>
      <td>Brasil</td>
      <td>&nbsp;</td>
      <td>3.612 domicílios</td>
    </tr>
    <tr>
      <td>2010/2012</td>
      <td>PNV/MJ</td>
      <td>Brasil</td>
      <td>1 ano e Toda a vida</td>
      <td>78.008 entrevistados</td>
    </tr>
    <tr>
      <td>2012</td>
      <td>Pesquisa de Vitimização Santa Catarina (DATAUFF/PMSC)</td>
      <td>Santa Catarina</td>
      <td>Sem Informação</td>
      <td>400 entrevistados</td>
    </tr>
    <tr>
      <td>2013</td>
      <td>CPP / INSPER</td>
      <td>Município de São Paulo</td>
      <td>1 ano</td>
      <td>3.000 entrevistados</td>
    </tr>
    <tr>
      <td>2013</td>
      <td>Representações Sociais sobre Violência e Criminalidade de Bagé</td>
      <td>Bagé/RS</td>
      <td>Sem Informação</td>
      <td>408 entrevistados</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>Pesquisa sobre vitimização e percepção de risco entre profissionais da segurança (FBSP)</td>
      <td>Profissionais de Segurança Pública registrados na Rede de Ensino à Distância da SENASP/MJ</td>
      <td>Toda a carreira</td>
      <td>10.323 entrevistados</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>(Em andamento) Observatório de Segurança Cidadã</td>
      <td>Município de Novo Hamburgo</td>
      <td>-</td>
      <td>600 entrevistados</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>(Em andamento) Pesquisa Distrital de Segurança (SSPPS)</td>
      <td>Distrito Federal</td>
      <td>-</td>
      <td>19.537 domicílios</td>
    </tr>
  </tbody>
</table>
<p><i>Fonte: Catão, 2010 “Treinamento para Pesquisa Nacional de Vitimização realizada em São Paulo. Junho, 2010” apud Relatório da Primeira Pesquisa Nacional de Vitimização – 2013</i></p>
<h3>Análise de Séries Temporais e Comparação Longitudinal (Evolução ao Longo do Tempo)</h3>
<table>
  <thead>
    <tr>
      <th>Ano</th>
      <th>Pesquisa/Instituição Responsável</th>
      <th>Abrangência</th>
      <th>Período de Referência</th>
      <th>Tamanho da Amostra</th>
      <th>Tipo de Análise Sugerida (Foco em Longitudinal)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1988</td>
      <td>PNAD</td>
      <td>Brasil</td>
      <td>1 ano</td>
      <td>81.628 domicílios</td>
      <td>Comparação de vitimização em nível nacional ao longo do tempo.</td>
    </tr>
    <tr>
      <td>1992</td>
      <td>Ilanud</td>
      <td>Município do Rio de Janeiro e Município de São Paulo</td>
      <td>5 anos</td>
      <td>1.000 entrevistados</td>
      <td>Análise de tendências de vitimização em grandes centros urbanos.</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>Ilanud</td>
      <td>Município do Rio de Janeiro e Município de São Paulo</td>
      <td>5 anos</td>
      <td>1.000 entrevistados</td>
      <td>Continuidade da análise de tendências do Ilanud.</td>
    </tr>
    <tr>
      <td>1997</td>
      <td>Ilanud</td>
      <td>Município do Rio de Janeiro e Município de São Paulo</td>
      <td>5 anos</td>
      <td>2.400 entrevistados</td>
      <td>Mais um ponto de dados para tendências Ilanud.</td>
    </tr>
    <tr>
      <td>1997/1998</td>
      <td>O Povo e a PM</td>
      <td>Distrito Federal</td>
      <td>Toda a vida</td>
      <td>2000 entrevistados</td>
      <td>Análise de vitimização ao longo da vida e possíveis comparações com estudos de período específico.</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>Módulo da PESB / DATAUFF</td>
      <td>Brasil</td>
      <td>Toda a Vida</td>
      <td>2460 entrevistados</td>
      <td>Comparação com PNAD e PNV para vitimização ao longo da vida.</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>Ilanud/FIA/USP</td>
      <td>São Paulo, Rio de Janeiro, Vitória e Recife (municípios)</td>
      <td>5 anos</td>
      <td>2.800 entrevistados</td>
      <td>Comparação da vitimização em capitais específicas.</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã</td>
      <td>Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais</td>
      <td>Toda a vida</td>
      <td>5.607 entrevistados</td>
      <td>Análise de percepção de medo e cultura cidadã em diferentes regiões de MG ao longo do tempo.</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Módulo da Pesquisa de Percepção de Medo e Cultura Cidadã</td>
      <td>Belo Horizonte, RMBH, Municípios polo e 16 municípios pequenos do interior de Minas Gerais</td>
      <td>Toda a vida</td>
      <td>5.067 entrevistados</td>
      <td>Continuidade da análise de percepção de medo em MG.</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>PNAD</td>
      <td>Brasil</td>
      <td>1 ano</td>
      <td>153.837 domicílios</td>
      <td>Continuidade da série histórica da PNAD para vitimização nacional.</td>
    </tr>
    <tr>
      <td>2010/2012</td>
      <td>PNV/MJ</td>
      <td>Brasil</td>
      <td>1 ano e Toda a vida</td>
      <td>78.008 entrevistados</td>
      <td>Pesquisa Nacional de Vitimização, fundamental para tendências em nível nacional.</td>
    </tr>
  </tbody>
</table>
<h3>Análise Regional e Comparativa de Casos Específicos (Foco em Localidades)</h3>
<table>
  <thead>
    <tr>
      <th>Ano</th>
      <th>Pesquisa/Instituição Responsável</th>
      <th>Abrangência</th>
      <th>Período de Referência</th>
      <th>Tamanho da Amostra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1996</td>
      <td>Iser/PAHO</td>
      <td>Município do Rio de Janeiro</td>
      <td>5 anos</td>
      <td>2.469 entrevistados</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>ISER/FGV</td>
      <td>Região Metropolitana do RJ</td>
      <td>1 ano</td>
      <td>1.126 entrevistados</td>
    </tr>
    <tr>
      <td>1998</td>
      <td>SEADE</td>
      <td>SP - Região Metropolitana e municípios com mais de 50.000 habitantes</td>
      <td>1 ano</td>
      <td>14.000 domicílios</td>
    </tr>
    <tr>
      <td>1999</td>
      <td>USP</td>
      <td>Região Metropolitana de SP</td>
      <td>6 meses</td>
      <td>1.000 entrevistados</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>ISER</td>
      <td>Baixada Fluminense - RJ</td>
      <td>1 ano</td>
      <td>1.389 entrevistados</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>CDHP - IBGE</td>
      <td>Copacabana e Leme</td>
      <td>1 ano</td>
      <td>450 entrevistados</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>Universidade de Caxias do Sul</td>
      <td>Caxias do Sul (RS)</td>
      <td>Sem informação</td>
      <td>Sem informação</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>GUTO - UNESP</td>
      <td>Município de Marília - SP</td>
      <td>Toda a vida</td>
      <td>828 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>ISP / Viva Rio</td>
      <td>Município do Rio de Janeiro</td>
      <td>1 ano</td>
      <td>765 entrevistados</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>CRISP</td>
      <td>Município de Belo Horizonte</td>
      <td>1 ano e 5 anos</td>
      <td>4.000 entrevistados</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>Instituto Futuro Brasil</td>
      <td>Município de São Paulo</td>
      <td>1 ano e 5 anos</td>
      <td>5.000 domicílios</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>GUTO - UNESP</td>
      <td>Município de Marília - SP</td>
      <td>Toda a vida</td>
      <td>Sem Informação</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>CPP / INSPER</td>
      <td>Município de São Paulo</td>
      <td>1 ano</td>
      <td>5.000 entrevistados</td>
    </tr>
    <tr>
      <td>2004</td>
      <td>Prefeitura</td>
      <td>Alvorada (RS)</td>
      <td>1 ano</td>
      <td>500 domicílios</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>IBPS - PMV</td>
      <td>Rio de Janeiro</td>
      <td>1 mês</td>
      <td>1.100 entrevistados por telefone</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>CRISP/SSP-Curitiba</td>
      <td>Curitiba</td>
      <td>1 ano e 5 anos</td>
      <td>3560 entrevistados</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>NEPP- PR</td>
      <td>Foz do Iguaçu</td>
      <td>1 ano e 5 anos</td>
      <td>700 entrevistados</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>SENASP - SEGUP - UFPA/CCS</td>
      <td>Região Metropolitana de Belém e 8 municípios do Interior</td>
      <td>2 anos</td>
      <td>2848 entrevistados</td>
    </tr>
    <tr>
      <td>2005/2006</td>
      <td>NUPEVI / UERJ</td>
      <td>Município do Rio de Janeiro</td>
      <td>Toda vida e 1 ano</td>
      <td>4.000 entrevistados</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>CRISP</td>
      <td>Região Metropolitana de Belo Horizonte</td>
      <td>1 ano e 5 anos</td>
      <td>6.220 entrevistados</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>SEADE /Bloco da PED</td>
      <td>Região Metropolitana de SP</td>
      <td>Sem informação</td>
      <td>3.000 domicílios/mês</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>Pesquisa de Vitimização nas regiões do Orçamento Participativo</td>
      <td>Regiões do Orçamento Participativo de Porto Alegre/RS</td>
      <td>1 ano</td>
      <td>1.404 domicílios</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>ISP</td>
      <td>Região Metropolitana do RJ</td>
      <td>1 ano e 5 anos</td>
      <td>5.000 entrevistados</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>CRISP</td>
      <td>Município de Itabira - MG</td>
      <td>1 ano e 5 anos</td>
      <td>401 entrevistados</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>Prefeitura</td>
      <td>Esteio /RS</td>
      <td>23 meses</td>
      <td>2.682 entrevistados</td>
    </tr>
    <tr>
      <td>2007/2008</td>
      <td>Universidade Federal de Pelotas</td>
      <td>Município de Pelotas - RS</td>
      <td>1 ano e 5 anos</td>
      <td>2918 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>GUTO - UNESP</td>
      <td>Município de Marília - SP</td>
      <td>Toda a vida</td>
      <td>741 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>CPP / INSPER</td>
      <td>Município de São Paulo</td>
      <td>1 ano</td>
      <td>2.967 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>UFGO</td>
      <td>Região Metropolitana de Goiânia – GO</td>
      <td>Sem informação</td>
      <td>3200 entrevistados</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Instituto Futuro Brasil</td>
      <td>Município de São Paulo</td>
      <td>1 ano e 5 anos</td>
      <td>3.000 domicílios</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>NEI/UFES</td>
      <td>Grande Vitória (Serra, Cariacica, Viana, Vitória e Vila Velha)</td>
      <td>12 meses e 05 anos</td>
      <td>5.244 entrevistados</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Pesquisa de Vitimização de Canoas</td>
      <td>Município de Canoas/RS</td>
      <td>12 meses</td>
      <td>1.568 entrevistados</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>Pesquisa de Vitimização no estado do Mato Groso FEC/DataUFF</td>
      <td>Mato Grosso</td>
      <td>12 meses</td>
      <td>4.000 domicílios</td>
    </tr>
    <tr>
      <td>2012</td>
      <td>Pesquisa de Vitimização Santa Catarina (DATAUFF/PMSC)</td>
      <td>Santa Catarina</td>
      <td>Sem Informação</td>
      <td>400 entrevistados</td>
    </tr>
    <tr>
      <td>2013</td>
      <td>CPP / INSPER</td>
      <td>Município de São Paulo</td>
      <td>1 ano</td>
      <td>3.000 entrevistados</td>
    </tr>
    <tr>
      <td>2013</td>
      <td>Representações Sociais sobre Violência e Criminalidade de Bagé</td>
      <td>Bagé/RS</td>
      <td>Sem Informação</td>
      <td>408 entrevistados</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>(Em andamento) Observatório de Segurança Cidadã</td>
      <td>Município de Novo Hamburgo</td>
      <td>-</td>
      <td>600 entrevistados</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>(Em andamento) Pesquisa Distrital de Segurança (SSPPS)</td>
      <td>Distrito Federal</td>
      <td>-</td>
      <td>19.537 domicílios</td>
    </tr>
  </tbody>
</table>
<h3>Análise Focada em Profissionais de Segurança (Qualidade de Vida e Percepção)</h3>
<table>
  <thead>
    <tr>
      <th>Ano</th>
      <th>Pesquisa/Instituição Responsável</th>
      <th>Abrangência</th>
      <th>Período de Referência</th>
      <th>Tamanho da Amostra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2015</td>
      <td>Pesquisa sobre vitimização e percepção de risco entre profissionais da segurança (FBSP)</td>
      <td>Profissionais de Segurança Pública registrados na Rede de Ensino à Distância da SENASP/MJ</td>
      <td>Toda a carreira</td>
      <td>10.323 entrevistados</td>
    </tr>
  </tbody>
</table>