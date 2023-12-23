import pickle
from fastapi import FastAPI


app = FastAPI()

model=pickle.load(open("model_pkl.pkl","rb"))


@app.get("/predict")
def predict(tmp : int , dust : int):
    feat  = (tmp, dust)
    res = model.predict([feat])
    return {res}

    


