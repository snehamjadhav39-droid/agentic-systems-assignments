from pydantic import BaseModel, Field, ConfigDict, field_validator, EmailStr
from typing import Optional
from datetime import datetime

# Address Model
class Address(BaseModel):
    city: str = Field(min_length=3)
    pincode: str = Field(min_length=6, max_length=6)

    @field_validator("pincode")
    def check_digits(cls, v):
        if not v.isdigit():
            raise ValueError("Pincode must contain only digits")
        return v

# User Model
class User(BaseModel):
    user_id: int
    full_name: str 
    email: EmailStr
    age: int = Field(ge=18)
    address: Address
    #is_premium: Optional[bool] = False

# Input Data
data = {
    "user_id": "101",
    "name": "Deepak k",
    "email": "deepak@gmail.com",
    "age": "25",
    "address": {
        "city": "Gurgaon",
        "pincode": "122101"
    }
}

# Create User
user = User(**data)
# Convert to dictionary
result = user.model_dump()

print(result)
