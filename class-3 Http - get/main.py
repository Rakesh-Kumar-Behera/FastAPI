from fastapi import FastAPI, Path, HTTPException, Query
import json


app = FastAPI()

def load_data():
    # reading the JSON file
    with open('patients.json', 'r') as file:
        data = json.load(file)

    return data


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
def view_patient(patient_id: str = Path(..., description="The ID of the patient to view", example= 'P001')):
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