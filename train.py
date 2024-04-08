import pickle
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# Read training data
df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()

# To convert categorical variables
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train model
gm = GaussianNB()
gm.fit(X, y_encoded)

# save model
with open("model.pkl", 'wb') as f:
    pickle.dump(gm, f)
