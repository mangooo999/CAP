import pickle5 as pickle
from fastapi import FastAPI




app = FastAPI()


model_path = "model_pkl.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.get("/predict")
def read_item(tmp, dust):
    # Use your model to make predictions
    result = model.predict([(tmp, dust)])
    return {"result": result}


