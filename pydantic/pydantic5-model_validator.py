from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

   
        
    @model_validator(mode='after')  # 'after' mode is used to validate after all fields are validated
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years of age')
        return model
        

# field_validator can validate only a signle field at a time,
# agar multiple fields ko validate karna hai to humein model_validator use karna padega,
# example - agar koi patient ka age 60 se upar hai to contact_details mein ek emergency contact number hona chahiye, --> isi case main hum field validator use nahi kar sakte


def insert_into_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print("Inserted Successfully")

patient_info = {
    'name':'Rakesh',
    'email': 'behera@hdfc.com',
    'age': 66,
    'weight': 60,
    'married':False,
    'allergies': ['Dust'],
    'contact_details': {'mobile':'676785465', 'emergency_contact': '123-456-7890'}
}

patient1 = Patient(**patient_info)

insert_into_patient(patient1)