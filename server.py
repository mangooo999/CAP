import pickle
from fastapi import FastAPI
from pydantic import BaseModel


class CAP(BaseModel):
    tmp:int
    dust:int
    

app = FastAPI()


model_path = "model_pkl.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)
'''
@app.post("/predict")
def predict(tmp, dust):
    # Use your model to make predictions
    result = model.predict([(tmp, dust)])
    return {"result": result}
'''
@app.post("/predict")
def predict(req:CAP):
    pass

@app.get("/predicttttt")
def read(tmp : int, dust : int):
    # Use your model to make predictions
    return {"result": 4, "tmp" : tmp, "dust" : dust }

if __name__=="__main__":
    uvicorn.run(app)
