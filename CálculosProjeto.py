#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import scipy 

from scipy.stats import normaltest

import pandas as pd

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
caminho_arquivo = '/Users/joaonolasco/statdisk_data.csv'

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv(caminho_arquivo)

# Exiba as primeiras linhas do DataFrame
print(df.head())


import pandas as pd

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
caminho_arquivo = '/Users/joaonolasco/statdisk_data.csv'

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv(caminho_arquivo)

# Exiba as primeiras linhas do DataFrame
print(df.head())

dataframe = pd.read_csv('statdisk_data.csv')

# A coluna desejada com os dados será acessada usando o nome da coluna no DataFrame.
coluna_desejada = dataframe['NomeDaColuna']


dataframe = pd.read_csv('/Users/joaonolasco/statdisk_data.csv')

# A coluna desejada com os dados será acessada usando o nome da coluna no DataFrame.
coluna_desejada = dataframe['NomeDaColuna']

array_de_dados = np.array(coluna_desejada)

df = pd.read_csv('file:///Users/joaonolasco/Downloads/statdisk_data.csv')


from scipy import stats
nomes_colunas = df.columns
print(nomes_colunas)


dados = df['Index(['1', '2', '3', '4', '5'], dtype='object')']


# In[21]:


dados = df[1', '2', '3', '4', '5'']


# In[22]:


dados = df['1']


# In[23]:


estatistica_teste, valor_p = stats.normaltest(dados)


# In[24]:


print("Estatística de Teste:", estatistica_teste)
print("Valor-p:", valor_p)


# In[25]:


print(dataframe)


# In[26]:


print(df)


# In[27]:


import pandas as pd

# Suponha que você tenha um DataFrame chamado df
df = pd.DataFrame({'1': [1, 2, 3, 4, 5]})

# Extrair os dados da coluna "coluna_desejada" em um array
array_de_dados = df['1'].values

print(array_de_dados)


# In[28]:


df = pd.read_csv('file:///Users/joaonolasco/Downloads/statdisk_data.csv')


# In[29]:


dados = df['1']
print(dados)


# In[30]:


array_de_dados = df['1'].to_numpy()

print(array_de_dados)


# In[32]:


array_de_dados='data'



# In[33]:


print(data)


# In[34]:


array_de_dados = df['1'].to_numpy()

print(array_de_dados)


# In[35]:


estatistica_teste, valor_p = stats.normaltest(array_de_dados)

# Exiba os resultados
print("Estatística de Teste:", estatistica_teste)
print("Valor-p:", valor_p)

# Interprete os resultados
nivel_de_significancia = 0.05
if valor_p > nivel_de_significancia:
    print("Os dados parecem seguir uma distribuição normal.")
else:
    print("Os dados não seguem uma distribuição normal.")


# In[36]:


estatistica_teste, valor_p = stats.normaltest(dados)

# Exiba os resultados
print("Estatística de Teste:", estatistica_teste)
print("Valor-p:", valor_p)

# Interprete os resultados
nivel_de_significancia = 0.01
if valor_p > nivel_de_significancia:
    print("Os dados parecem seguir uma distribuição normal.")
else:
    print("Os dados não seguem uma distribuição normal.")


# In[37]:


estatistica_teste, valor_p = stats.normaltest(dados)

# Exiba os resultados
print("Estatística de Teste:", estatistica_teste)
print("Valor-p:", valor_p)

# Interprete os resultados
nivel_de_significancia = 0.05
if valor_p > nivel_de_significancia:
    print("Os dados parecem seguir uma distribuição normal.")
else:
    print("Os dados não seguem uma distribuição normal.")


# In[38]:


media_amostral = 65.7668
media_populacional = 45
desvio_padrao_populacional = 14.96886
tamanho_amostra = 800

# Calcule a estatística de teste Z
z = (media_amostral - media_populacional) / (desvio_padrao_populacional / np.sqrt(tamanho_amostra))

print("Valor de Z:", z)


# In[40]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Parâmetros da distribuição normal (média e desvio padrão)
media = 65.7668
desvio_padrao = 14.96886

# Gere uma série de números ao longo do intervalo da distribuição
x = np.linspace(0, 3, 100)

# Calcule os valores da função de densidade de probabilidade da distribuição normal
pdf = norm.pdf(x, loc=media, scale=desvio_padrao)

# Crie um gráfico da distribuição normal
plt.plot(x, pdf, label='Distribuição Normal')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Gráfico da Distribuição Normal')
plt.legend()
plt.grid(True)

# Exiba o gráfico
plt.show()


# In[43]:


media = 65.7668
desvio_padrao = 14.96886

# Gere uma amostra de dados de uma distribuição normal
amostra = array_de_dados

# Crie um histograma
plt.hist(amostra, bins=30, density=True, alpha=0.05, color='#469C57')

# Calcule os valores da função de densidade de probabilidade da distribuição normal para o gráfico da curva
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
pdf = norm.pdf(x, media, desvio_padrao)

# Plote a curva de densidade de probabilidade
plt.plot(x, pdf, 'k-', linewidth=2)

# Adicione rótulos de eixos e um título
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Histograma de uma Distribuição Normal')

# Exiba o histograma
plt.show()





# In[49]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Parâmetros da distribuição normal
media = 45
desvio_padrao = 14.96886

# Valor crítico (você pode ajustar esse valor conforme necessário)
valor_critico = 1.645  # Por exemplo, para um intervalo de confiança de 95%

amostra = array_de_dados

plt.hist(amostra, bins=30, density=True, alpha=0.05, color='#469C57')

# Calcule os valores da função de densidade de probabilidade da distribuição normal
pdf = norm.pdf(x, loc=media, scale=desvio_padrao)

# Crie um gráfico da distribuição normal
plt.plot(x, pdf, label='Distribuição Normal')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Gráfico de uma Distribuição Normal com Valor Crítico')

# Adicione uma linha vertical para o valor crítico
plt.axvline(x=valor_critico, color='red', linestyle='--', label='Valor Crítico')

# Adicione a média populacional como uma linha vertical
plt.axvline(x=media, color='green', linestyle='--', label='Média Populacional')

# Exiba uma legenda
plt.legend()

# Exiba o gráfico
plt.show()


# In[55]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Parâmetros da distribuição normal
media = 70 # Média da distribuição
desvio_padrao = 5  # Desvio padrão da distribuição

# Gere uma série de números ao longo do intervalo da distribuição
x = np.linspace(0,100)  # Intervalo de -5 a 5

# Calcule os valores da função de densidade de probabilidade da distribuição normal
pdf = norm.pdf(x, loc=media, scale=desvio_padrao)

# Crie um gráfico da distribuição normal
plt.plot(x, pdf, label='Distribuição Normal')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Gráfico de uma Distribuição Normal')

# Exiba o gráfico
plt.legend()
plt.show()


# In[56]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Parâmetros da amostra e da distribuição sob a hipótese nula
media_nula = 45  # Média sob a hipótese nula
desvio_padrao = 14
n = 800  # Tamanho da amostra

# Valor crítico para um teste unilateral à direita (por exemplo, alfa = 0.05)
alfa = 0.05
z_critico = norm.ppf(1 - alfa)  # Valor crítico unilateral à direita

# Gere os dados de amostra sob a hipótese nula
amostra_nula = np.random.normal(media_nula, desvio_padrao, n)

# Calcule a curva de densidade de probabilidade para a distribuição sob a hipótese nula
x = np.linspace(-3, 5, 1000)  # Intervalo para o gráfico
pdf_nula = norm.pdf(x, loc=media_nula, scale=desvio_padrao)

# Crie um gráfico da distribuição sob a hipótese nula
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_nula, label='Hipótese Nula', color='blue')

# Área sombreada para a região de rejeição à direita
plt.fill_between(x, 0, pdf_nula, where=(x > z_critico), color='gray', alpha=0.5, label='Região de Rejeição à Direita')

# Rótulos de eixos e título
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Gráfico de Teste de Hipótese Unilateral à Direita para a Média')

# Adicione legendas
plt.legend()

# Exiba o gráfico
plt.show()


# In[57]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Parâmetros das amostras e das distribuições
media_nula = 45  # Média sob a hipótese nula
media_alternativa = 45  # Média sob a hipótese alternativa
desvio_padrao = 14
n = 800  # Tamanho da amostra

# Gere os dados de amostra sob a hipótese nula e alternativa
amostra_nula = np.random.normal(media_nula, desvio_padrao, n)
amostra_alternativa = np.random.normal(media_alternativa, desvio_padrao, n)

# Calcule as curvas de densidade de probabilidade para as distribuições
x = np.linspace(-3, 5, 1000)  # Intervalo para o gráfico
pdf_nula = norm.pdf(x, loc=media_nula, scale=desvio_padrao)
pdf_alternativa = norm.pdf(x, loc=media_alternativa, scale=desvio_padrao)

# Crie um gráfico das distribuições
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_nula, label='Hipótese Nula', color='blue')
plt.plot(x, pdf_alternativa, label='Hipótese Alternativa', color='red')

# Área sombreada para a região de rejeição (por exemplo, alfa = 0.05)
alfa = 0.05
z_critico = norm.ppf(1 - alfa / 2)  # Valor crítico bilateral
plt.fill_between(x, 0, pdf_nula, where=(x > z_critico), color='gray', alpha=0.5, label='Região de Rejeição')

# Rótulos de eixos e título
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Gráfico de Teste de Hipótese para a Média')

# Adicione legendas
plt.legend()

# Exiba o gráfico
plt.show()


# In[58]:


from scipy import stats
import numpy as np
import pandas as pd

# Substitua 'seu_arquivo.csv' pelo caminho completo para o seu arquivo CSV
dataframe = pd.read_csv('')

# Escolha a coluna que você deseja testar para normalidade
dados = dataframe['1']

# Realize o teste de normalidade
estatistica_teste, valor_p = stats.normaltest(dados)

# Exiba os resultados
print("Estatística de Teste:", estatistica_teste)
print("Valor-p:", valor_p)

# Interprete os resultados
if valor_p > 0.05:
    print("Os dados são consistentes com uma distribuição normal.")
else:
    print("Os dados não seguem uma distribuição normal.")


# In[59]:


import os

# Substitua 'seuarquivo.csv' pelo nome do seu arquivo CSV
nome_arquivo = 'statdisk_data (2) 2.numbers'

# Obtenha o caminho absoluto do arquivo
caminho_absoluto = os.path.abspath(nome_arquivo)

# Exiba o caminho absoluto
print('Caminho absoluto do arquivo CSV:', caminho_absoluto)


# In[61]:


import pandas as pd
from scipy import stats

# Carregue os dados do arquivo CSV em um DataFrame
dados = pd.read_csv('/Users/joaonolasco/statdisk_data (2) 2.numbers')

# Realize o teste t de uma amostra
# Substitua 'coluna_de_interesse' pelo nome da coluna que deseja testar
# e 'valor_hipotese_nula' pelo valor da hipótese nula (normalmente 0)
resultado_teste = stats.ttest_1samp(dados['coluna_de_interesse'], valor_hipotese_nula)

# Obtenha o valor-p do resultado do teste
valor_p = resultado_teste.pvalue

# Imprima o valor-p
print('Valor-p:', valor_p)

# Verifique se o valor-p é menor que um limiar de significância pré-determinado (por exemplo, 0.05)
if valor_p < 0.05:
    print('Rejeita-se a hipótese nula')
else:
    print('Não rejeita-se a hipótese nula')


# In[62]:


import os

# Substitua 'seuarquivo.csv' pelo nome do seu arquivo CSV
nome_arquivo = 'dados.csv'

# Obtenha o caminho absoluto do arquivo
caminho_absoluto = os.path.abspath(nome_arquivo)

# Exiba o caminho absoluto
print('Caminho absoluto do arquivo CSV:', caminho_absoluto)


# In[63]:


import pandas as pd
from scipy import stats

# Carregue os dados do arquivo CSV em um DataFrame
dados = pd.read_csv('/Users/joaonolasco/dados.csv')

# Realize o teste t de uma amostra
# Substitua 'coluna_de_interesse' pelo nome da coluna que deseja testar
# e 'valor_hipotese_nula' pelo valor da hipótese nula (normalmente 0)
resultado_teste = stats.ttest_1samp(dados['coluna_de_interesse'], valor_hipotese_nula)

# Obtenha o valor-p do resultado do teste
valor_p = resultado_teste.pvalue

# Imprima o valor-p
print('Valor-p:', valor_p)

# Verifique se o valor-p é menor que um limiar de significância pré-determinado (por exemplo, 0.05)
if valor_p < 0.05:
    print('Rejeita-se a hipótese nula')
else:
    print('Não rejeita-se a hipótese nula')


# In[64]:


df = pd.read_csv('file:///Users/joaonolasco/Downloads/dados.csv')


# In[65]:


import pandas as pd
from scipy import stats


# Realize o teste t de uma amostra
# Substitua 'coluna_de_interesse' pelo nome da coluna que deseja testar
# e 'valor_hipotese_nula' pelo valor da hipótese nula (normalmente 0)
resultado_teste = stats.ttest_1samp(df['1'], valor_hipotese_nula)

# Obtenha o valor-p do resultado do teste
valor_p = resultado_teste.pvalue

# Imprima o valor-p
print('Valor-p:', valor_p)

# Verifique se o valor-p é menor que um limiar de significância pré-determinado (por exemplo, 0.05)
if valor_p < 0.05:
    print('Rejeita-se a hipótese nula')
else:
    print('Não rejeita-se a hipótese nula')


# In[66]:


array_de_dados = df['1'].to_numpy()

print(array_de_dados)


# In[67]:


estatistica_teste, valor_p = stats.normaltest(array_de_dados)

# Exiba os resultados
print("Estatística de Teste:", estatistica_teste)
print("Valor-p:", valor_p)

# Interprete os resultados
nivel_de_significancia = 0.05
if valor_p > nivel_de_significancia:
    print("Os dados parecem seguir uma distribuição normal.")
else:
    print("Os dados não seguem uma distribuição normal.")


# In[68]:


print(array_de_dados)


# In[69]:


df = pd.read_csv('file:///Users/joaonolasco/Downloads/data2.csv')


# In[70]:


array_de_dados = df['1'].to_numpy()

print(array_de_dados)


# In[71]:


estatistica_teste, valor_p = stats.normaltest(array_de_dados)

# Exiba os resultados
print("Estatística de Teste:", estatistica_teste)
print("Valor-p:", valor_p)

# Interprete os resultados
nivel_de_significancia = 0.05
if valor_p > nivel_de_significancia:
    print("Os dados parecem seguir uma distribuição normal.")
else:
    print("Os dados não seguem uma distribuição normal.")


# In[72]:


df = pd.read_csv('file:///Users/joaonolasco/Downloads/statdisk_data.csv')


# In[73]:


array_de_dados = df['1'].to_numpy()

print(array_de_dados)


# In[75]:


import matplotlib.pyplot as plt

# Exemplo de dados
x = 
y = 

# Criar o gráfico de dispersão
plt.scatter(x, y)

# Personalizar o gráfico
plt.xlabel('Valores de X')
plt.ylabel('Valores da Base de Dados')
plt.title('Gráfico da Base de Dados em Função de X')

# Exibir o gráfico
plt.show()


# In[76]:


import matplotlib.pyplot as plt
import numpy as np


# Valores de tempo em segundos
tempo_em_segundos = np.arange(1000, 5000, 1000)

# Criar o gráfico
plt.plot(tempo_em_segundos, array_de_dados, marker='o', linestyle='-')

# Personalizar o gráfico
plt.xlabel('Tempo (s)')
plt.ylabel('Uso da CPU (%)')
plt.title('Desempenho Temporal da CPU')
plt.grid(True)

# Exibir o gráfico
plt.show()


# In[77]:


import matplotlib.pyplot as plt
import numpy as np


# Valores de tempo em segundos (800 valores correspondentes)
tempo_em_segundos = np.arange(1000, 5001, 1000)  # Certifique-se de que corresponda ao número de dados

# Criar o gráfico
plt.plot(tempo_em_segundos, array_de_dados, marker='o', linestyle='-')

# Personalizar o gráfico
plt.xlabel('Tempo (s)')
plt.ylabel('Uso da CPU (%)')
plt.title('Desempenho Temporal da CPU')
plt.grid(True)

# Exibir o gráfico
plt.show()


# In[85]:


import matplotlib.pyplot as plt
import numpy as np

num_dados = len(array_de_dados)

# Valores de tempo em segundos (4 valores correspondentes)
Frames = np.linspace(0, 4000, num_dados)

# Criar o gráfico
plt.plot(Frames, array_de_dados, marker='o', linestyle='-')

# Personalizar o gráfico
plt.xlabel('Frames (F)')
plt.ylabel('Uso da CPU (%)')
plt.title('Desempenho da CPU por processamento de frames')
plt.grid(True)

# Exibir o gráfico
plt.show()


# In[ ]:




