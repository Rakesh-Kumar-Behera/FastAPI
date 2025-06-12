from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    # applying transformation
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = [ 'hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        # Convert the name to uppercase
        return value.upper()

    @field_validator('age', mode= 'after') # by default mode is 'after'
    @classmethod
    def age_validator(cls, value):
        # Ensure age is a positive integer
        if 0 < value < 100:
            return value
        else: 
            raise ValueError('Age should be between 0 and 100')
        

# field_validator can validate only a signle field at a time,
# agar multiple fields ko validate karna hai to humein model_validator use karna padega,
# example - agar koi patient ka age 60 se upar hai to contact_details mein ek emergency contact number hona chahiye, --> isi case main hum field validator use nahi kar sakte



# field_validator - kisi bhi field pe custom data validation and transformation apply karne ke liye use kar sakte hain, 
# for example, patients ka naam hamesha capital pe ho
# specific company ke emplyees ko discount milega specific hospital main, for example :- hdfc ke emplyees ka email hamesh xyz@hdfc.com, icici ka --> njbb@icici.com

def insert_into_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print("Inserted Successfully")

patient_info = {
    'name':'Rakesh',
    'email': 'behera@hdfc.com',
    'age': 26,
    'weight': 60,
    'married':False,
    'allergies': ['Dust'],
    'contact_details': {'mobile':'676785465'}
}

patient1 = Patient(**patient_info)

insert_into_patient(patient1)