## Exporting pydantic models to JSON with Pydantic v2.0
## Exporting pydantic models to python dictionary with Pydantic v2.0

from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_info = {
    'street': '123 Main St',
    'city': 'Springfield',
    'state': 'IL',
    'zip_code': '62701'
}

address1 = Address(**address_info)

patient_info = {
    'name': 'John Doe',
    'gender' : 'male',
    'age': 30,
    'address': address1
}

patient1 = Patient(**patient_info)

temp = patient1.model_dump() # Exporting to a Python dictionary
print(temp)
print(type(temp))

json_temp = patient1.model_dump_json() # Exporting to JSON
print(json_temp)
print(type(json_temp))

temp2 = patient1.model_dump(include={'name', 'age'})  # Exporting specific fields to a Python dictionary
print(temp2)

temp3 = patient1.model_dump(exclude={'address':['state']})  # Excluding specific fields from the export
print(temp3)