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
- Exemplo da resposta (Exemplo tirado da documentação):

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
- Dentro do loop citado acima, fazer um segundo loop para acrecentar as informações retornadas da requisição nas listas setadas inicialmente

- Exemplo da resposta (Exemplo tirado da documentação):

[
  {
    "id": "1",
    "person": "10",
    "survey_type": "nps",
    "score": 0,
    "comment": null,
    "permalink": "xhttps://app.delighted.com/r/2jo3B7Gak9q37XkuHrGLGAbCdevemcx8",
    "created_at": 1643574875,
    "updated_at": null,
    "person_properties": { "purchase_experience": "Retail Store", "country": "USA" },
    "notes": [],
    "tags": [],
    "additional_answers": [
      {
        "id": "4",
        "value": {
          "free_response": null,
          "scale": null,
          "select_one": null,
          "select_many": [
            {
              "id": "DxmjNj",
              "text": "Convenience"
            },
            {
              "id": "uNQIig",
              "text": "Friendly staff"
            }
          ]
        },
        "question": {
          "id": "enum_z9EvYV",
          "type": "select_many",
          "text": "What specifically did you enjoy about your experience with us?"
        }
      },
      {
        "id": "5",
        "value": {
          "free_response": null,
          "scale": null,
          "select_one": {
            "id": "tp0Q4K",
            "text": "Yes"
          },
          "select_many": null
        },
        "question": {
          "id": "enum_caUUdY",
          "type": "select_one",
          "text": "Have you purchased from us in the past?"
        }
      },
      {
        "id": "6",
        "value": {
          "free_response": null,
          "scale": 4,
          "select_one": null,
          "select_many": null
        },
        "question": {
          "id": "integer_buwb3w",
          "type": "scale",
          "text": "How often do you shop at one of our stores?"
        }
      },
      {
        "id": "7",
        "value": {
          "free_response": "A friend recommended you to me!",
          "scale": null,
          "select_one": null,
          "select_many": null
        },
        "question": {
          "id": "text_BJPEm0",
          "type": "free_response",
          "text": "How did you hear about us?"
        }
      }
    ]
  },
  {
    "id": "2",
    "person": "11",
    "survey_type": "nps",
    "score": 9,
    "comment": "I loved this app!",
    "permalink": "xhttps://app.delighted.com/r/5pFDpmlyC8GUc5oxU6USto5VonSKAqOa",
    "created_at": 1643576675,
    "updated_at": 1643577275,
    "person_properties": null,
    "notes": [
      { "id": "1", "text": "Note 1", "user_email": "foo@bar.com", "created_at": 1643576675 },
      { "id": "2", "text": "Note 2", "user_email": "gyp@sum.com", "created_at": 1643577575 }
    ],
    "tags": [],
    "additional_answers": []
  }
]

- Criar dicionário com as listas preenchidas 
- Transforma o dicionário em um dataframe
