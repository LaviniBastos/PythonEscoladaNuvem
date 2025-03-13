# Script que irá ler os dados de um arquivo csv e os exibe em tela

import pandas as pd
import os


arqui = "pessoas.csv"

df = pd.read_csv(arqui)

print(df)

