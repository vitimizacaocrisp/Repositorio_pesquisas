# Analise e Previsões de vitimização

Projeto organizado para análises integradas de múltiplas fontes de dados sobre segurança pública e vitimização

## 📂 Estrutura de Diretorio
``` text
dados_brutos/
├── belo_horizonte_2002/
│   ├── csv/
│   │   ├── indices_violencia.csv
│   │   └── Vitimizacao_UP_27.csv
│   └── excel/
│       └── Vitimizacao_UP_27.xlsx
├── percepcao_medo_MG_2008/
│   ├── amostra_BH.xls
│   ├── amostra_MG.xls
│   └── populacao_idade_sexo.csv
├── PNAD_1998/
│   └── (arquivos da PNAD de 1998)
├── PNAD_2009/
│   ├── agressao/
│   ├── furto/
│   ├── roubo/
│   ├── roubofurto/
│   ├── seguranca/
│   └── tentativa/
├── violencia_escolas_2006/
│   ├── alunos_2006.csv
│   ├── professores_2006.csv
│   └── roteiro_2006.csv
├── Homicidios_Tentado_e_Consumado...(nome provisorio)
└── totais2008ateMAIO...(nome provisorio)
```



## 📂 Análises Possíveis e Dados Relevantes

<style>
.analysis-table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  font-family: sans-serif;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.analysis-table thead tr {
  background-color: #2c3e50;
  color: #ffffff;
  text-align: left;
}

.analysis-table th,
.analysis-table td {
  padding: 12px 15px;
  border: 1px solid #dddddd;
}

.analysis-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.analysis-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.analysis-table tbody tr:last-of-type {
  border-bottom: 2px solid #2c3e50;
}

.analysis-table tbody tr:hover {
  background-color: #e1f5fe;
  color: #000000;
}

.analysis-table td[rowspan] {
  vertical-align: top;
  font-weight: bold;
  color: #2c3e50;
}
</style>

<table class="analysis-table">
  <thead>
    <tr>
      <th>Categoria</th>
      <th>Análise Possível</th>
      <th>Dados Relevantes</th>
      <th>Observações</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Violência Urbana</td>
      <td>Evolução dos índices de violência ao longo do tempo</td>
      <td>indices_violencia.csv, totais2008ateMAIO.csv</td>
      <td>Comparar anos diferentes</td>
    </tr>
    <tr>
      <td>Comparação entre tipos de crimes (agressão, furto, roubo)</td>
      <td>agressao, furto, roubo, roubofurto</td>
      <td>Pode-se analisar proporções entre crimes</td>
    </tr>
    <tr>
      <td>Vítimização por unidades policiais</td>
      <td>Vitimizacao_UP_27.csv, Vitimizacao_UP_27.xlsx</td>
      <td>Dados em dois formatos para comparação</td>
    </tr>
    <tr>
      <td rowspan="2">Percepção Social</td>
      <td>Medo e percepção de segurança em MG/BH</td>
      <td>percepção_medo_MG_2008, segurança</td>
      <td>Dados de 2008 podem estar desatualizados</td>
    </tr>
    <tr>
      <td>Comparação entre amostras de BH e MG</td>
      <td>amostra_BH.xls, amostra_MG.xls</td>
      <td>Verificar compatibilidade dos dados</td>
    </tr>
    <tr>
      <td>Demografia</td>
      <td>Distribuição populacional por idade e sexo</td>
      <td>populacao_idade_sexo.csv</td>
      <td>Pode cruzar com dados de violência</td>
    </tr>
    <tr>
      <td rowspan="3">Violência Escolar</td>
      <td>Panorama da violência em escolas (2006)</td>
      <td>violencia_escolas_2006, alunos_2006.csv, professores_2006.csv</td>
      <td>Perspectivas de diferentes atores</td>
    </tr>
    <tr>
      <td>Comparação entre percepção de alunos e professores</td>
      <td>alunos_2006.csv, professores_2006.csv</td>
      <td>Análise de divergências</td>
    </tr>
    <tr>
      <td>Metodologia da pesquisa escolar</td>
      <td>roteiro_2006.csv</td>
      <td>Entender como os dados foram coletados</td>
    </tr>
    <tr>
      <td>Homicídios</td>
      <td>Análise de homicídios tentados e consumados</td>
      <td>Homicidios Tentado e Consumado(EN)</td>
      <td>Verificar se dados estão em inglês</td>
    </tr>
    <tr>
      <td>Dados Socioeconômicos</td>
      <td>Análise de indicadores PNAD</td>
      <td>PNAD_1998, PNAD_2009</td>
      <td>Grande intervalo temporal entre pesquisas</td>
    </tr>
  </tbody>
</table>
