import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("introducao\dados.csv")

histograma1 = df["preco"].plot.hist()
plt.savefig("introducao\histograma_1.pdf")

histograma2 = df["preco"].plot.hist(bins=30, edgecolor="black")
plt.savefig("introducao\histograma_2.pdf")
