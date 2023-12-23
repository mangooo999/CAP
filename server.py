import pickle
from fastapi import FastAPI
from pydantic import BaseModel




app = FastAPI()


model_path = "model_pkl.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.post("/predict")
def predict(tmp : int, dust : int):
    # Use your model to make predictions
    result = model.predict([(tmp, dust)])
    return {"result": result}


@app.get("/predicttttt")
def read():
    # Use your model to make predictions
    return {model.predict([(0,49)]) }


