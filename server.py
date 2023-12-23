import pickle
from fastapi import FastAPI
import uvicorn



app = FastAPI()


model_path = "model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)


@app.get("/predict")
def read_item():
    # Use your model to make predictions
    result = list(model.predict([[5, 6]]))
    return {"result": result[0].item()}




