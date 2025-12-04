from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

uri = "mongodb+srv://Dolly_san:Dolly2024BD@cluster0.o02nrl7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client["ministerio"]
col = db["pdfs_meta"]

@app.get("/")
def home(request: Request):
    pdfs = list(col.find({}, {"_id": 0}))  # traer docs sin _id
    return templates.TemplateResponse("index.html", {"request": request, "pdfs": pdfs})
