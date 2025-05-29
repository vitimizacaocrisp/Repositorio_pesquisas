# Repositório de Pesquisas em Segurança Pública

Repositório organizado para análise de dados de vitimização, seguindo boas práticas de gestão da informação científica e reprodutibilidade.

## 📂 Arquivos em Uso
PNAD_2009


## 📂 Estrutura do Repositório

/repositorio-seguranca-publica
├── 1_documentacao_geral/
│ ├── plano_gestao_dados.md # Data Management Plan (DMP)
│ ├── protocolos_coleta.md
│ └── diretrizes_eticas.pdf
├── 2_dados/
│ ├── brutos/ # Dados originais imutáveis
│ │ ├── pnad/ # Por fonte de dados
│ │ ├── anuario_fbsp/
│ │ ├── sim/
│ │ └── municipais/
│ ├── intermediarios/ # Dados em processamento
│ └── tratados/ # Dados prontos para análise
│ ├── versoes/ # Versionamento semântico (v1.0.0)
│ └── padronizados/ # Dados integrados
├── 3_scripts/
│ ├── coleta/ # Scripts de ingestão
│ ├── tratamento/ # ETL e limpeza
│ ├── analise/ # Modelagem estatística
│ └── visualizacao/ # Dashboards e gráficos
├── 4_analises/ # Projetos específicos
│ ├── projeto_tendências/
│ ├── projeto_fatores_risco/
│ └── projeto_comparativo/
├── 5_outputs/
│ ├── relatorios/
│ ├── publicacoes/
│ └── visualizacoes/
└── 6_metadados/ # Documentação técnica
├── por_fonte/ # Metadados específicos
├── dicionario_unificado.csv # Variáveis padronizadas
└── log_integracao.md # Histórico de combinações

