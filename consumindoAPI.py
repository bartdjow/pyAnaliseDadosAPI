# -*- coding: utf-8 -*-
"""dadosCodiv19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fLYJ1l5CqxttkJB3IcMS9anHfp7L-nlA

# Consumindo API e tratando dados com Python

**APIs REST**

Uma API (application programming interface) é uma especificação que define como componentes de software devem interagir entre si (thanks, wikipedia!). APIs REST se utilizam do protocolo HTTP para fornecer determinadas funcionalidades aos seus clientes. Essas funcionalidades são descritas por conjuntos de recursos que podem ser acessados remotamente pelos clientes do serviço, através de requisições HTTP comuns.

Em uma API REST existem dois conceitos principais: os recursos (resources) e as coleções (collections). Um recurso é uma unidade que representa um objeto (composto por dados, relacionamentos com outros recursos e métodos). Já uma coleção é um conjunto de recursos que pode ser obtido acessando uma URL. Tal coleção poderia representar a coleção de todos os registros de determinado tipo, ou então, todos os registros que possuem relacionamento com determinado objeto, ou todos os registros que atendem à determinada condição, etc.

Como você pôde ver, uma API REST nada mais é do que um serviço que fornece acesso remoto a recursos via HTTP. Para podermos entender melhor e fazer requisições HTTP a um serviço REST, precisamos conhecer um pouquinho mais sobre o protocolo HTTP e como seus métodos são utilizados em uma API REST.



**HTTP e seus métodos**

O protocolo HTTP define que uma requisição de um cliente para um servidor é composta por:

Uma linha descrevendo a requisição, composta por:
Método: indica o que desejamos fazer com o recurso. Pode ser: GET, POST, PUT, DELETE, além de outros menos utilizados.
URL: o endereço do recurso que se deseja acessar.
Versão: a versão do protocolo a ser usada.
O corpo da requisição, que pode conter informações como o nome do host de onde desejamos obter o recurso solicitado, dados a serem enviados do cliente para o servidor, etc.

O método de uma requisição HTTP indica a ação que pretendemos realizar com aquela requisição, e cada método tem um significado próprio:

**GET:** utilizado para a obtenção de dados. É o tipo de requisição que o navegador faz a um servidor quando você digita uma URL ou clica em um link.

**POST:** utilizada na web para o envio de dados do navegador para o servidor, principalmente quando esses dados vão gerar alguma alteração no último.
PUT: serve para solicitar a criação de objetos no servidor caso esses ainda não existirem. Na prática, a maioria das páginas utiliza o método POST para isso também.

**DELETE:** serve para indicar que o usuário (emissor da requisição em questão) deseja apagar determinado recurso do servidor.

Após executar a requisição do cliente, o serviço responde com uma mensagem de resposta HTTP. O protocolo HTTP define que as mensagens de resposta devem possuir um campo indicando o status da requisição. O status mais conhecido na web é o 404 (not found – recurso não encontrado), mas existem vários, como: 200 (OK), 401 (not authorized – indicando falta de autenticação), 500 (internal server error – erro no servidor), dentre outros. Por ser baseado em HTTP, o padrão REST define que as mensagens de resposta devem conter um código de status, para que o cliente do serviço web possa verificar o que aconteceu com a sua requisição.

**O quê vamos fazer:**

Acessar uma API do site https://brasil.io e pegarmos dados do Covid-19 e prepararmos estes dados para um futuro enriquecimento.

Para esta tarefa utilizaremos algumas bibliotecas do Python, são elas:
- **Json:**
A biblioteca json disponível no Python pode operar com objetos json originários de arquivos ou strings. Ao decodificar o objeto , a biblioteca o  converte para listas ou dicionários Python. E também o inverso, ou seja, converte listas ou dicionários Python em objetos json.

- **Requests:**
A biblioteca requests é utilizada para fazer solicitações HTTP em Python. Ele abstrai as complexidades de fazer solicitações por trás de uma API simples e bonita, para que você possa se concentrar na interação com os serviços e no consumo de dados em seu aplicativo.

- **Pandas:**
O pandas é uma biblioteca de análise e manipulação de dados de código aberto, rápida, poderosa, flexível e fácil de usar, construída sobre a linguagem Python .

Bom agora que já entendemos um pouco sobre APIs RESET, sobre algumas bibliotecas do python e oque vamos fazer vamos colocara mão na massa.

**Instala as Bibliotecas necessárias**

Vamos precisar instalar as bibliotecas do python citado acima, caso estes não esteja instalado, execute a celula abaixo:
"""

!pip install json
!pip install requests
!pip install pandas

"""**Importa as Bibliotecas**

Agora precisamos importar as bibliotecas para que possamos utilizá las em nosso algoritimo.
"""

import json
import requests
import pandas as pd

"""**Pega dados do Covid19 da API do Brasil.io**

Com as bibliotecas instanciadas precisamos fazer a requisição à API para capturar os dados e armazena los em uma variável.
"""

dadoscodvi19 = requests.get('https://brasil.io/api/dataset/covid19/caso/data')

"""**Convertendo dados da API para m dicionario**

Os dados capturados estão no formato JSON e para que possamos manipulá los em python precisamos converter o mesmo em um dicionário e para isso utilizamos a função loads da biblioteca JSON.
"""

dicCovid = json.loads(dadoscodvi19.content)

"""**Exibir as chaves do Dicionário**

Precisamos agora entender a estrutura do nosso dicionário e para isso precisamos exibir algumas informações estruturais
"""

dicCovid.keys()

"""Com este resultado podemos ver que temos uma dicionario chamada results e este pode conter nossos dados, para confirmarmos esta hipótese podemos exibir a estrutura da lista results"""

dicCovid['results'][0].keys()

"""Com isso conseguimos ter a confirmação de nossa hipótese, pois o resultado nos mostra as colunas que esperávamos

**Converte dicionário em Data Frame**

Após termos entendido a estrutura do nosso dicionário podemos agora transformar a chave results em um data frame do pandas, pois só assim conseguiremos utilizar as funções do mesmo
"""

dfCodiv19 = pd.DataFrame(dicCovid ['results'])

"""**Descrevendo e limpando o dataset**

Para que possamos entender nosso dataframe e sabermos quais colunas temos que ajustar e quais temos que eliminar ou mesmo manter precisamos entender como estão e para isso precisamos coletar informações sobre o dataframe.
"""

dfCodiv19.count()

"""Com estes dados podemos tirar algumas conclusões:
- temos um total de 1.000 linhas em nosso dataset
- Temos algumas colunas que não nos serão necessárias e que podemos elimina las, são elas:
  - city_ibge_code
  - confirmed_per_100k_inhabitants
  - death_rate
  - estimated_population_2019
  - is_last
  - order_for_place
- deaths e city precisa ser analisada, pois como pudemos ver ela não contem a mesma quantidade de registros que o total do nosso dataset

Vamos liminar as colunas desnecessárias
"""

dfCodiv19.pop('city_ibge_code')
dfCodiv19.pop('confirmed_per_100k_inhabitants')
dfCodiv19.pop('death_rate')
dfCodiv19.pop('estimated_population_2019')
dfCodiv19.pop('is_last')

"""vamos agora analisar a coluna city que identificamos que, possui dados missing(sujeira ou dados faltantes) e vamos iniciar vendo os dados que estão nulos no dataset"""

dfCodiv19[dfCodiv19['city'].isnull()]

"""Com a análise acima podemos ver que os dados que estão com a coluna city nulos são os que mostram as valores de casos confirmados e mortes sumarizados por estado e como não vamos precisar destes dados,pois podemos calcular os mesmo quando precisarmos.

Então vamos remover os  dados desnecessários.
"""

dfCodiv19 = dfCodiv19[dfCodiv19['city'].notnull()]

"""Agora que removemos os dados missing da coluna city, precisamos dar uma analisada no conteúdo da coluna para que possamos ter a certeza que os dados são validos."""

pd.unique(dfCodiv19[['city']].values.ravel('K'))

"""Com isso podemos concluir que a coluna city do nosso dataset está OK

Então vamos agora analisar a coluna deaths
"""

dfCodiv19[dfCodiv19['deaths'].isnull()]

"""Com esta analise podemos ver que existem cidades que não tem mortes e possuem o valor da mesma ausente, então precisamos preencher as mesmas com 0"""

dfCodiv19 = dfCodiv19.fillna(0)

"""Vamos agora verificar se temos mais algum valor nulos e se corrigimos a coluna deaths"""

dfCodiv19.isna().sum()

"""Vamos verificar os valores da coluna place_type, pois precisamos ter apenas as cidades em nosso dataset."""

pd.unique(dfCodiv19[['place_type']].values.ravel('K'))

"""Com isso confirmamos que só possuímos cidades e não temos a necessidade de termos mais esta coluna em nosso dataset, então vamos eliminá-las"""

dfCodiv19.pop('place_type')

"""Com isso chegamos a conclusão que para nossa análise precisaremos apenas das colunas:
- **City:** que armazena a cidade que os dados representam
- **State:** que armazena a informação da UF onde a cidade está
- **Confirmed:** que armazena a quantidade de casos de COVID-19 confirmados na cidade/estado
- **Date:** que armazena a data em que as informações foram atualizadas
- **Deaths:** que armazena a quantidade de mortos por COVID-19 na Cidade/Estado

**Traduzir nome das Colunas**
"""

dfCodiv19 = dfCodiv19.rename(columns={'city': 'cidade', 'confirmed': 'casosConfirmados', 'date': 'dataAtualizacao', 'deaths': 'mortos', 'state': 'uf'  })

"""**Exibir dataset Final**"""

dfCodiv19.head()

"""**Gera CSV com os dados para Utilizarmos em nosso próximo Artigo**"""

dfCodiv19.to_csv('datasetCodiv19.csv', index=False,sep=';')

"""Os scripts deste artigo estão em: https://github.com/AleTavares/pyAnaliseDadosAPI

**Autor:**

*Alexandre Tavares*

*Engenheiro de Dados*

https://www.linkedin.com/in/alexandre-tavares/
"""