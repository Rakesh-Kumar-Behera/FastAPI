from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    
    name: str = Field(..., description="The name of the patient")
    age: int = Field(..., ge=0, description="The age of the patient, must be a non-negative integer")
    weight: float = Field(..., ge=0, description="The weight of the patient in kilograms, must be a non-negative float")
    height: float = Field(..., ge=0, description="The height of the patient in meters, must be a non-negative float")
    married: bool = Field(..., description="Marital status of the patient, True if married, False otherwise")
    allergies: Optional[List[str]] = Field(default_factory=None, description="List of allergies the patient has, if any")
    contact_details: Dict[str, str] = Field(default_factory=NotImplemented , description="Contact details of the patient")

#bydefault all the feilds are required except the ones with default values


def insert_patient_data(patient: Patient):
    # This function would typically insert the patient data into a database or another storage system.
    # For this example, we will just print the patient data.
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight} kg")
    print(f"Height: {patient.height} m")
    print(f"Married: {patient.married}")
    print(f"Allergies: {', '.join(patient.allergies) if patient.allergies else 'None'}")
    print(f"Contact Details: {patient.contact_details if patient.contact_details else 'None'}")
    print("Patient data inserted successfully.")

def update_patient_data(patient: Patient):
    # This function would typically update the patient data in a database or another storage system.
    # For this example, we will just print the updated patient data.
    print(f"Updated Patient Data: {patient.json(indent=4)}")

patient_info = {'name':'John Doe',
    'age':30,
    'weight':70.5,
    'height':1.75,
    'married':True,
    'allergies':['Peanuts', 'Penicillin', 'Dust'],
    'contact_details':{'email': 'xyz@email.com', 'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)
# update_patient_data(patient1)   