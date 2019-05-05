import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("introducao\dados.csv")

# Histograma
histograma1 = df["preco"].plot.hist()
plt.savefig("introducao\histograma_1.pdf")
plt.close()

histograma2 = df["preco"].plot.hist(bins=30, edgecolor="black")
plt.savefig("introducao\histograma_2.pdf")
plt.close()

# Gráfico de barras verticais
contagem1 = df["bairro"].value_counts().plot.bar()
plt.savefig("introducao\contagem_1.pdf")
plt.close()

# Gráfico de barras horizontais
contagem2 = df["bairro"].value_counts().plot.barh()
plt.savefig("introducao\contagem_2.pdf")
plt.close()

# Título para o gráfico
contagem3 = df["bairro"].value_counts().plot.barh(
    title="Número de apartamentos por bairro")
plt.savefig("introducao\contagem_3.pdf")
plt.close()

# Gráfico de Dispersão
dispersao1 = df.plot.scatter(x="preco", y="area")
plt.savefig("introducao\dispersao_1.pdf")
plt.close()

plt.style.use("ggplot")
dispersao2 = df.plot.scatter(x="preco", y="area")
plt.savefig("introducao\dispersao_2.pdf")
plt.close()

# Gráfico de pizza
pizza1 = df["quartos"].value_counts().plot.pie()
plt.savefig("introducao\pizza_1.pdf")
plt.close()

# Mais sobre Gráfico de Dispersão
dispersao3 = df.plot.scatter(x="preco", y="area", s=.5)
plt.savefig("introducao\dispersao_3.pdf")
plt.close()

# Uso de uma amostragem de dados para montar o gráfico
df.sample(frac=.1).plot.scatter(x='preco', y='area')
plt.savefig("introducao\dispersao_4.pdf")
plt.close()
