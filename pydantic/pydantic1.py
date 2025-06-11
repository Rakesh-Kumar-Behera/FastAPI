from pydantic import BaseModel, Field

class Patient(BaseModel):
    
    name: str = Field(..., description="The name of the patient")
    age: int = Field(..., ge=0, description="The age of the patient, must be a non-negative integer")
    

def insert_patient_data(patient: Patient):
    # This function would typically insert the patient data into a database or another storage system.
    # For this example, we will just print the patient data.
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")


patient_info = {'name': 'John Doe', 'age': 30}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)