from pydantic import BaseModel, Field , EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: Annotated[str, Field(max_length=50, title= 'Name of the Patient' , description= 'Give the name of the patient in less than 50 chars' , examples = ['Amit' , 'Anshu'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt = 0, lt = 120)
    weight: Annotated[float, Field(gt = 0, strict= True)]
    married: Annotated[bool , Field(default=None , description='Is the patient married or not')] # default value
    allergies: Annotated[Optional[List[str]],  Field(default=None, max_length=5)]
    contact_details: Dict[str, str] 

# by default all the feilds are required except the ones with default values
# Field - to attach metadata and for custom data validation
# EmailStr - to validate Email_id
# AnyUrl - to validate websites (e.g; returns error if there is no https:// or .com)
# strict=True - Allow only a Specific type of input,input of any other datatype will return error

def insert_patient_data(patient: Patient):
    # This function would typically insert the patient data into a database or another storage system.
    # For this example, we will just print the patient data.
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight} kg")
    print(f"Married: {patient.married}")
    print(f"Allergies: {', '.join(patient.allergies) if patient.allergies else 'None'}")
    print(f"Contact Details: {patient.contact_details if patient.contact_details else 'None'}")
    print("Patient data inserted successfully.")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("Updated")

patient_info = {'name':'John Doe',
                'email': 'abc@gmail.com',
                'linkedin_url': 'https://linkedin.com/behera.r.k_1234',
                'age':30,
                'weight':70.5,
                'married':True,
                'allergies':['Peanuts', 'Dust'],
                'contact_details':{'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)
# update_patient_data(patient1)   