# importando as bibliotecas
import pandas as pd
import datetime
import time
import pytz
import math
from dateutil.relativedelta import *
import delighted

# definindo a chave disponibilizada na plataforma da delighted
delighted.api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# definindo um df vazio que receberá o os dados vindos da api
respostas_nps_pf_df_final = pd.DataFrame(
    columns={'id', 'person_id', 'score', 'comment', 'created_at', 'updated_at', 'permalink', 'customer_id'})

# definindo listas vazias que auxiliará na organização dos dados retornados em JSON
lista_id = []
lista_person = []
lista_score = []
lista_comment = []
lista_created_at = []
lista_updated_at = []
lista_permalink = []
lista_customer_id = []


local_time = pytz.timezone("America/Sao_paulo")

# definindo a data inicio do parametro pedido na url
# primeiro dia do mês de M-6
date_since = datetime.date.today().replace(day=1) - relativedelta(months=+6)
since = datetime.datetime(date_since.year, date_since.month, date_since.day)
local_datetime = local_time.localize(since, is_dst=None)
utc_since = local_datetime.astimezone(pytz.utc)
since_unix = time.mktime(utc_since.timetuple())

# definindo a data final do parametro pedido na url
# dia atual meia noite
date_now_until = datetime.date.today()
until = datetime.datetime(date_now_until.year, date_now_until.month, date_now_until.day)
local_datetime = local_time.localize(until, is_dst=None)
utc_until = local_datetime.astimezone(pytz.utc)
until_unix = time.mktime(utc_until.timetuple())

print(since, until)
print(utc_since, utc_until)
print(since_unix, until_unix)

# requisição que extrai metricas consolidadas da Delighted
r = delighted.Metrics.retrieve(
    since=since_unix,
    until=until_unix
)
print(r)

# usa response_count da resposta a cima para calular o total de paginas para a próxima requisição
pagina_final = math.ceil(r['response_count'] / 100)

# loop para percorrer todos as páginas da resposta da requisição
# esse requisição reporta cada uma das respostas
for pagina in range(1, pagina_final + 1):
    r = delighted.SurveyResponse.all(
        per_page=100,
        page=pagina,
        since=since_unix,
        until=until_unix
    )

    print('{} de {}'.format(pagina, pagina_final))

    # lood para organizar as respostas em listas por tipo de dado
    for resposta in r:
        lista_id.append(resposta['id'])

        lista_person.append(resposta['person'])

        lista_score.append(resposta['score'])

        lista_comment.append(resposta['comment'])

        created_at = datetime.datetime.fromtimestamp(resposta['created_at'])
        lista_created_at.append(created_at)

        updated_at = datetime.datetime.fromtimestamp(resposta['updated_at'])
        lista_updated_at.append(updated_at)

        lista_permalink.append(resposta['permalink'])

        lista_customer_id.append(resposta['person_properties']['customer_id'])

# cria um dicionário a partir das listas abixo
respostas_dict = {
    'id': lista_id,
    'person_id': lista_person,
    'score': lista_score,
    'comment': lista_comment,
    'created_at': lista_created_at,
    'updated_at': lista_updated_at,
    'permalink': lista_permalink,
    'customer_id': lista_customer_id,
}

trasforma o dicionário em um df pandas
respostas_nps_pf_df = pd.DataFrame.from_dict(respostas_dict)
print(respostas_nps_pf_df.head())














