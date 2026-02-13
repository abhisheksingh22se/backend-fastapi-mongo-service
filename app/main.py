from fastapi import FastAPI, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from .database import get_collection
from .models import PatientCreate

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

# Async Route: Non-blocking read 
@app.get("/")
async def read_root(request: Request):
    collection = get_collection("patients")
    # Async cursor to list
    patients = await collection.find().to_list(length=100)
    return templates.TemplateResponse("index.html", {"request": request, "patients": patients})

@app.get("/add")
async def add_patient_form(request: Request):
    return templates.TemplateResponse("add-patient.html", {"request": request})

# Async Write + Pydantic Validation
@app.post("/add")
async def add_patient(
    name: str = Form(...),
    age: int = Form(...),
    disease: str = Form(...),
    gender: str = Form(...),
    condition: str = Form(...)
):
    # 1. Validate data using Pydantic Model
    try:
        patient_data = PatientCreate(
            name=name,
            age=age,
            disease=disease,
            gender=gender,
            condition=condition
        )
    except ValueError as e:
        return {"error": "Validation Failed", "details": str(e)}

    # 2. Insert into DB Asynchronously
    collection = get_collection("patients")
    await collection.insert_one(patient_data.model_dump())
    
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)