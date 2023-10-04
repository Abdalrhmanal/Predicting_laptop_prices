import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from fastapi.middleware.cors import CORSMiddleware
#from sklearn.metrics import mean_absolute_error, mean_squared_error
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

data = pd.read_excel('compData.xlsx')
#print(data)

X = data.drop('price', axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=40)  # تم تصحيح هذا الجزء

model = LinearRegression()
model.fit(X_train, y_train)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getsum/{v1}/{v2}/{v3}/{v4}/{v5}/{v6}/{v7}/{v8}/{v9}/{v10}/{v11}")
def getSum(v1: int, v2: int, v3: int, v4: int, v5: int, v6: int, v7: float, v8: int, v9: int, v10: int, v11: int):
    s = model.predict([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11]])
    return {'s': s.tolist()}




