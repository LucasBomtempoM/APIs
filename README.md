# API's
 
## Objetivo:
Centralizar os trabalhos feitos com API's

## 1- API Delighted:
- Delighted é um plataforma que realiza pesquisas de NPS 
- Link da documentação: https://app.delighted.com/docs/api
- Objetivo: Obter os dados das pepsquisas de NPS via API com atualzação diária com o auxilio de um Job no Databricks.

### Passo a passo:

- Instalar biblioteca da delighted (pip install delighted)
- Importar as bibliotecas auxiliares 
- Setar listas vazias para organização das informações vindas das resposta da requisição
- Setar um dataframe vazio que receberá os dados do dicinário formado com as listas citadas a cima 
- Setar os parametros necessário para realizar o GET (data inicio / data final / páginas / respostas por página)
- Realizar a primeira requisição a API para obter as métricas consolidadas. O objetivo aqui é obter a quantidade total de pesquisas (response_count)
- Exemplo da resposta:
{
  "nps": 51,
  "promoter_count": 32,
  "promoter_percent": 63,
  "passive_count": 13,
  "passive_percent": 25,
  "detractor_count": 6,
  "detractor_percent": 12,
  "response_count": 51
}
- Fazer o calculo do total de páginas que será usado na segunda requisição para o obter a lista de pesquisas recebidas
- Sabendo que a API retorna no máxima 100 respostas por página, fazer o calculo do total de páginas. 
Calculo: response_count / 100 arrendondando para cima
- Fazer um loop para percorer todas as páginas da requisição 
- Dentro do loop citado acima, fazer um segundo loop para acrecentar nas listas setadas inicialmente as informações retornadas da requisição
