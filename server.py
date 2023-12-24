import pickle
from fastapi import FastAPI
import uvicorn



app = FastAPI()


model_path = "model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)


@app.get("/predict")
def read_item(tmp : int , dust : int):
    # Use your model to make predictions
    result = list(model.predict([[tmp, dust]]))
    return {result[0].item()}



