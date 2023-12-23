import pickle
from fastapi import FastAPI
from pydantic import BaseModel


class CAP(BaseModel):
    tmp : int
    dust : int

app = FastAPI()

model=pickle.load(open("model_pkl.pkl","rb"))


@app.post("/predict")
def predict(req : CAP):
    tmp = CAP.tmp
    dust = CAP.dust
    feat  = (tmp, dust)
    res = model.predict([feat])
    return {res}

    


