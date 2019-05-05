import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("introducao\dados.csv")

histograma = df["preco"].plot.hist()
plt.savefig("introducao\histograma.pdf")
