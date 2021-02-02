# Importing the libraries
import pandas as pd
import pickle
import numpy as np

df = pd.read_csv('Real_Combine.csv')
df=df.dropna(axis='rows')

X=df.iloc[:,:-1] ## independent features
y=df.iloc[:,-1] ## dependent features

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=300, max_depth=15)
print(model)

model.fit(X, y)

# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict(sc.transform([[7.40,9.80,4.80,1017.60,93.00,0.50,4.30,9.40]])))