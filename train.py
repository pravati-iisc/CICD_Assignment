import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
labels = np.sort(np.unique(y))
y = np.array([np.where(labels == x) for x in y]).flatten()

model = LogisticRegression().fit(X, y)

try:
    with open("model.pkl", 'wb') as f:
        pickle.dump(mod, f)
except Exception as e:
    print('\n\n## Creating Manual error for forcing it to fail. ##\n\n')
    raise
