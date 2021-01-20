import numpy as np
import pandas as pd

df = pd.read_csv('data/cities.csv')
print(df.head())

print(len(df.population))
print(df.population.value_counts())
print(len(df.population.value_counts()))
print(df.population.value_counts().idxmax())