from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
import json
from typing import Annotated, Literal

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description="ID of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient", examples=["John Doe"])]
    city: Annotated[str, Field(..., description="City of the patient", examples=["New York"])]
    age: Annotated[int, Field(..., ge=0, lt=120, description="Age of the patient", examples=[30])]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., ge=0, description="Height of the patient in meters")]
    weight: Annotated[float, Field(..., ge=0, description="Weight of the patient in kgs")]


    @computed_field
    @property
    def bmi(self) -> float:
        """Calculate Body Mass Index (BMI)"""
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        """Determine the health verdict based on BMI"""
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

def load_data():
    # reading the JSON file
    with open('../patients.json', 'r') as file:
        data = json.load(file)
    return data

def save_data(data):
    # saving the data into the JSON file
    with open('../patients.json', 'w') as file:
        json.dump(data, file)

# ######## Get Methods #########

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient Records"}

@app.get("/patients")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to view", examples= 'P001')):
    # ... indicates that this is a required path parameter
    # This function retrieves a specific patient's data based on the patient_id provided in the URL path.
    #load all the patients data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of Height, Weight or BMI"), 
                 order: str = Query('asc', description="Order of sorting: 'asc' for ascending, 'desc' for descending")):
    
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Use 'asc' or 'desc'.")
      
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse= sort_order)

    return sorted_data

# ######### Post Methods #########

@app.post("/create")
def create_patient(patient: Patient):

    # load existing data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the JSON file
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})


