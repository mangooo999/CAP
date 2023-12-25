from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse  
from fastapi.templating import Jinja2Templates
import pickle
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model_path = "model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Initialize variables to store the last prediction
last_tmp = None
last_dust = None
last_prediction = None


@app.get("/predict")
def read_item(tmp: int, dust: int):
    global last_tmp, last_dust, last_prediction

    # Use your model to make predictions
    result = list(model.predict([[tmp, dust]]))
    prediction = result[0].item()

    # Update the last prediction variables
    last_tmp, last_dust, last_prediction = tmp, dust, prediction

    # Return the prediction along with tmp and dust values
    return {"tmp": tmp, "dust": dust, "prediction": prediction}


@app.get("/last_prediction", response_class=JSONResponse)
def get_last_prediction():
    return {"tmp": last_tmp, "dust": last_dust, "prediction": last_prediction}


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

