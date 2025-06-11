# computed fields are the fields which are not directly provided by the user 
# but are computed based on other fields in the model.
from pydantic import BaseModel, Field, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        """Calculate Body Mass Index (BMI)"""
        bmi = round(self.weight / (self.height ** 2),2)
        return bmi
    

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print("BMI" , patient.calculate_bmi)
    print("Inserted Successfully")


patient_info = {
    'name':'Rakesh',
    'email': 'behera@hdfc.com',
    'age': 66,
    'weight': 68,
    'height': 1.75,
    'married':False,
    'allergies': ['Dust'],
    'contact_details': {'mobile':'676785465', 'emergency_contact': '123-456-7890'}
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
# computed_field - is used to create a field that is computed based on other fields in the model.