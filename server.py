import pickle
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


@app.get("/predictttt")
async def predict(temp: int = Query(..., title="Temperature", description="Temperature value"),
                  dust: int = Query(..., title="Dust", description="Dust value")):
    result = f"Temperature: {temp}, Dust: {dust}"
    print(result)
    return {"result": result}


