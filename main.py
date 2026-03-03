                                               #ANALISE DE DADOS COM PYTHON 
import pandas as pd
import plotly.express as px

# Passo 1: Importar a base de dados
tabela = pd.read_csv("cancelamentos.csv")

# Passo 2: Visualizar a base de dados
tabela = tabela.drop(columns="CustomerID")
print(tabela.head())

# Passo 3: Corrigir problemas da base
print("\nINFO ANTES:")
print(tabela.info())

tabela = tabela.dropna()

print("\nINFO DEPOIS:")
print(tabela.info())

# Passo 4: Análise inicial dos cancelamentos
print("\nQuantidade de cancelamentos:")
print(tabela["cancelou"].value_counts())

print("\nPercentual de cancelamentos:")
print(tabela["cancelou"].value_counts(normalize=True))

# Passo 5: Análise das causas dos cancelamentos
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

# Aplicando filtros com base na análise
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"] <= 4]
tabela = tabela[tabela["dias_atraso"] <= 20]

print("\nCancelamentos após filtros:")
print(tabela["cancelou"].value_counts())

print("\nPercentual após filtros:")
print(tabela["cancelou"].value_counts(normalize=True))
