import pandas as pd

df = pd.read_csv('Datasetinfectedhealthy.csv', header=None)

df = df.sample(frac=1)
df.to_csv('Datasetinfectedhealthy.csv')
# print(df.head(5))