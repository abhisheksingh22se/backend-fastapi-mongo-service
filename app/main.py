from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Connect to MongoDB
client = MongoClient(os.getenv("MONGODB_URL", "mongodb://admin:password@mongodb:27017/"))
db = client.hospital
patients_collection = db.patients

@app.get("/")
def read_root(request: Request):
    patients = list(patients_collection.find())
    return templates.TemplateResponse("index.html", {"request": request, "patients": patients})

@app.get("/add")
def add_patient_form(request: Request):
    return templates.TemplateResponse("add-patient.html", {"request": request})

@app.post("/add")
def add_patient(name: str = Form(...), age: int = Form(...), disease: str = Form(...), gender: str = Form(...), condition: str = Form(...)):
    patients_collection.insert_one({
        "name": name,
        "age": age,
        "gender": gender,
        "condition": condition,
        "disease": disease
    })
    return RedirectResponse("/", status_code=302)
