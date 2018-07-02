import MySQLdb
import numpy as np
import math as mt
import matplotlib as plt
import pandas.io.sql as psql
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go

# Classe de conexao com o banco de dados
# Retorna os dados de conexao do banco
def for_connect_mysql():
 db = MySQLdb.connect(
  host="localhost",  	# hostname 
  user="root",       	# username
  passwd="",         	# password
  db="municipiostcc")   # database
 return db

# Classe de consulta da query em sql
# Retorna um dataframe para os graficos
def for_query(statement,conexao):
 #resultado da consulta apos ter passado os parametros
 consulta = psql.read_sql_query(statement,for_connect_mysql())
 return consulta

# Query SQl para consulta de dados da tabela
# Dados ja calculados dentro da consulta.

# retorna os dados da view, contem todos os dados
sql_TableView = ("SELECT * FROM municipiostcc.matematico;")

# retorna os dados de uf, nome da regiao, o pib da uf, e calcula a variancia e o desvio padrao
sql_variancDesvPad = ("Select SiglaUF as 'UF', NomeR as 'Regiao',PIB_2010 as 'PIB_2010',"+
 "round((PIB_2010/SUM(PIB_2010))*(PIB_2010/SUM(PIB_2010))/COUNT(NomeR),7) as 'Variancia',"+
 "round(SQRT((PIB_2010/SUM(PIB_2010))*(PIB_2010/SUM(PIB_2010))/COUNT(NomeR)),7) as 'DesvioPadrao'"+
 " from municipiostcc.matematico group by SiglaUF asc;")
 
# retorna os dados para uma table, contem as medias 
# de populacoes entre os anos de 2013 e 2016 
sql_mediaPop = (
 "SELECT distinct SiglaUF as 'UF',"+
 "round(avg(POP_2013),1) as 'AVG_POP_2013',"+
 "round(avg(POP_2014),1) as 'AVG_POP_2014',"+
 "round(avg(POP_2015),1) as 'AVG_POP_2015',"+
 "round(avg(POP_2016),1) as 'AVG_POP_2016' " +
 "FROM municipiostcc.matematico "+
 "where SiglaUF <> 'DF' group by SiglaUF;")
 
# retorna os dados para o grafico de ÁREA, contem os dados de idh e gini de 2010
sql_graphRow = ("Select SiglaUF as 'UF', IDH_2010 as 'IDH_2010', GINI_2010 as 'GINI_2010', "+
 "round(SQRT((PIB_2010/SUM(PIB_2010))*(PIB_2010/SUM(PIB_2010))/COUNT(SiglaUF)),5) as 'Desvio_Padrao' "+
 "from municipiostcc.matematico group by SiglaUF asc;")
 
# retorna os dados para o grafico de colunas, contem os dados da regiao, o idh e o gini de 2010
sql_graphREG =(  "Select NomeR as 'Regiao',round(IDH_2010,2) as 'IDH_2010',GINI_2010 as 'GINI_2010'"+
 "from municipiostcc.matematico group by NomeR;")

# retorna os dados para o grafico de coluna, contem os dados da uf, o idh e o gini de 2010 
sql_graphUF =( "Select SiglaUF as 'UF', round(avg(IDH_2010),5) as 'IDH_2010',"+
 "round(avg(GINI_2010),5) as 'GINI_2010' "+
 "from municipiostcc.matematico group by SiglaUF;")
# retorna os dados para o grafico de coluna, contem os dados dos municipios, idh e o gini de 2010 
sql_graphMUNIC =( "Select NomeM as 'Municipio', IDH_2010 as 'IDH_2010',GINI_2010 as 'GINI_2010' "+
 "from municipiostcc.matematico where POP_2016 >= 100000;")
 
# Retorna o dados da consulta, passando o dataframe para um array
# Cada variavel tem por definicao um grafico apropriado.
 
dadosViewAVG_POP = for_query(sql_mediaPop, for_connect_mysql())
dataTable = for_query(sql_variancDesvPad, for_connect_mysql())
dataTableView = for_query(sql_TableView, for_connect_mysql())
dadosView = for_query(sql_TableView, for_connect_mysql())
dadosGraphREG= for_query(sql_graphREG, for_connect_mysql())
dadosGraphMUNIC = for_query(sql_graphMUNIC, for_connect_mysql())
dadosGraphUF = for_query(sql_graphUF, for_connect_mysql())
dadosGraphRow = for_query(sql_graphRow, for_connect_mysql())
dataTable.loc[0:20]
dataTableView.loc[0:20]

# Atribui o objeto da biblioteca dash em uma variavel da main
app = dash.Dash()
app.scripts.config.serve_locally = True

# Atribui a variavel app.layout componentes de html, passando os 
# parametros do array para os graficos de area, coluna, e linha.
app.layout = html.Div([
 html.H1(children= r'TRABALHO DE CONCLUSÃO DE CURSO - BIGDATA PYTHON',
 style={ 'fontSize': 24,'text-align':'center','margin-top':'25px'}),
 html.Label('Selecione a regiao para analise:'),
 # Campo para pesquisa por região
 dcc.Dropdown(
  options=[
   {'label': 'Centro-Oeste', 'value': 1},
   {'label': 'Nordeste', 'value': 2},
   {'label': 'Norte', 'value': 3},
   {'label': 'Sudeste', 'value': 4},
   {'label': 'Sul', 'value': 5} ],
   value=[1],
   multi=True ),
 # Grafico de pontos IDH VS GINI 2010
 dcc.Graph(
  id='IDHM_2010-vs-GINI_2010',
  figure={
   'data': [
    go.Scatter(
     x=dadosView[dadosView['NomeR'] == i]['IDH_2010'],
     y=dadosView[dadosView['NomeR'] == i]['GINI_2010'],
     text=dadosView[dadosView['NomeR'] == i]['NomeM'],
     mode='markers',
     opacity=0.7,
     marker={
      'size': 15,
      'line': {'width': 0.5, 'color': 'white'}
      },
     name=i
    )for i in dadosView.NomeR.unique() ],
   'layout': go.Layout(
     xaxis={'type': 'log', 'title': 'GINI_2010'},
     yaxis={'title': 'IDH_2010'},
     margin={'l': 40, 'b': 40, 't': 50, 'r': 10},
     legend={'x': 0, 'y': 1},
     hovermode='closest',
     title = 'GRÁFICO DE PONTOS - IDH vs GINI 2010' )}
 ),
 # Grafico de coluna de idh e gini por habitantes
 dcc.Graph(
  id='graph-MUNIC',
  figure={
   'data': [
    {'x': dadosGraphMUNIC ['Municipio'],'y': dadosGraphMUNIC['IDH_2010'],
	'type': 'bar','name':'IDH_2010'},
    {'x': dadosGraphMUNIC ['Municipio'],'y': dadosGraphMUNIC['GINI_2010'],
	'type': 'bar','name':'GINI_2010'}, ],
   'layout': {
    'title': 'GRÁFICO DE COLUNAS - IDH POR MUNICIPIO A CADA 100 MIL HAB.',
    'color': 'dark', 
    'fontSize': 14,
    'text-align':'center',
    'margin-top':'25px'
    }
   }),
 # Grafico de coluna de idh e gini por UF   
 dcc.Graph(
  id='graph-UF',
  figure={
   'data': [
    {'x': dadosGraphUF ['UF'],'y': dadosGraphUF['IDH_2010'],
	'type': 'bar','name':'IDH_2010'},
    {'x': dadosGraphUF ['UF'],'y': dadosGraphUF['GINI_2010'],
	'type': 'bar','name':'GINI_2010'},
    ],
    'layout': {
     'title': 'GRÁFICO DE COLUNAS - IDH E GINI POR UF',
     'text-align':'center',
     'margin-top':'25px', }
    }),
 # Grafico de coluna de idh e gini por Regiao
 dcc.Graph(
  id='graph-REG',
  figure={
   'data': [
    {'x': dadosGraphREG ['Regiao'],'y': dadosGraphREG['IDH_2010'],
     'type': 'bar','name':'IDH_2010'},
    {'x': dadosGraphREG ['Regiao'],'y': dadosGraphREG['GINI_2010'],
     'type': 'bar','name':'GINI_2010'}, ],
   'layout': {
    'title': 'GRÁFICO DE COLUNAS - IDH E GINI POR REGIÃO',
    'text-align':'center',
    'margin-top':'25px', }
   }),
  # Grafico de ÁREAs de idh e gini 2010 por uf
  html.H2(children='GRÁFICO DE ÁREA - IDH E GINI POR UF',
  style={'color': 'black','fontSize': 16,'text-align':'center'}),
 html.Div([
  html.Div(
   dcc.Graph(
    id='graph-ROWUF',
    style={
     'overflow-x': 'wordwrap',
    })
  )
 ]),
 # Grafico de linha, contendo os dados de idh e gini por Regiao
  html.H2(children='GRÁFICO DE ÁREA - IDH E GINI POR REGIÃO',
  style={'color': 'black','fontSize': 16,'text-align':'center'}),
 html.Div([
  html.Div(
   dcc.Graph(
    id='graph-ROWREG',
    style={
     'overflow-x': 'wordwrap',
    })
  )
 ]),
 # Grafico de linha, contendo os dados da media da populacao
  html.H2(children='GRÁFICO DE ÁREA - MÉDIAS DAS POPULAÇÕES',
  style={'color': 'black','fontSize': 16,'text-align':'center'}),
 html.Div([
  html.Div(
   dcc.Graph(
    id='graph-ROWPOP',
    style={
     'overflow-x': 'wordwrap',
    })
  )
 ]),
 # Tabela de variancia e desvio padrao em relacao aos dados do pib_2010
  html.H2(children='DADOS DE VARIÂNCIA E DESVIO PADRÃO EM RELAÇÃO A PIB 2010',
  style={'color': 'black', 'fontSize': 16,'text-align':'center',}),
  dt.DataTable(
   rows=dataTable.to_dict('records'),
   row_selectable=False,
   filterable=True,
   sortable=False,
   editable= False,
   selected_row_indices=[],
   id='datatable-gapminder' ),
 # Tabela geral dos dados da view municipiotcc.matematico  
 html.H2(children=' DADOS GERAIS DE TODOS OS MUNICIPIOS',
  style={'color': 'black', 'fontSize': 16,'text-align':'center','margin-top':'25px'}),
  dt.DataTable(
   rows=dataTableView.to_dict('records'),
   row_selectable=False,
   filterable=True,
   sortable=False,
   editable= False,
   id='datatable-geral',
   )
 ], className="container")
 
# Chamada de metodo de callback do metodo update_figure
@app.callback(
 Output('graph-ROWUF', 'figure'),
 [Input('datatable-geral', 'rows')])
def update_figure(rows):
 return {
  'data': [{
    'x':dadosGraphRow['UF'],'y':dadosGraphRow['IDH_2010'],
     'name':'IDH_2010'},
	{'x':dadosGraphRow['UF'],'y':dadosGraphRow['GINI_2010'],
	 'name':'GINI_2010'},],
  'layout': {
   'margin': {'l': 40, 'r': 30, 't': 30, 'b': 30}
   }
 }
 
 # Chamada de metodo de callback do metodo update_figureReg
@app.callback(
 Output('graph-ROWREG', 'figure'),
 [Input('datatable-geral', 'rows')])
def update_figureReg(rows):
 return {
  'data': [
    {'x': dadosGraphREG ['Regiao'],'y': dadosGraphREG['IDH_2010'],
     'name':'IDH_2010'},
    {'x': dadosGraphREG ['Regiao'],'y': dadosGraphREG['GINI_2010'],
     'name':'GINI_2010'}, ],
  'layout': {
   'margin': {'l': 40, 'r': 30, 't': 30, 'b': 30}
   }
 }
 # Chamada de metodo de callback do metodo update_figurePOP
@app.callback(
 Output('graph-ROWPOP', 'figure'),
 [Input('datatable-geral', 'rows')])
def update_figurePop(rows):
 return {
  'data': [
    {'x': dadosViewAVG_POP ['UF'],'y': dadosViewAVG_POP['AVG_POP_2013'],
     'name':'MÉDIA POP_2013'},
    {'x': dadosViewAVG_POP ['UF'],'y': dadosViewAVG_POP['AVG_POP_2014'],
     'name':'MÉDIA POP_2014'},
    {'x': dadosViewAVG_POP ['UF'],'y': dadosViewAVG_POP['AVG_POP_2015'],
     'name':'MÉDIA POP_2015'},
	{'x': dadosViewAVG_POP ['UF'],'y': dadosViewAVG_POP['AVG_POP_2016'],
     'name':'MÉDIA POP_2016'}, ],
  'layout': {
   'margin': {'l': 40, 'r': 30, 't': 30, 'b': 30}
   }
 }
# importacao dos componentes de estilos css para a pagina e os graficos
app.css.append_css({
 'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# Classe principal do sistema, executa todos os metodos e 
# e mostra os dados no navegador
if __name__ == '__main__':
 app.run_server(debug=True)