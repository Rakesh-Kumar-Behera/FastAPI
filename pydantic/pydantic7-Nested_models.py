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

print(patient1)
print(patient1.name)
print(patient1.address)
print(patient1.address.street)
print(patient1.address.city)
