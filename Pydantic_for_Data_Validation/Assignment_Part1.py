from pydantic import BaseModel, EmailStr, Field, ValidationError


class UserRegister(BaseModel):
    username: str = Field(..., min_length=5)
    email: str
    age: int = Field(..., ge=18)


try:
    user = UserRegister(
        username="sanidhya",
        email="sanidhya@example.com",
        age=19
    )

    print("User registered successfully")
    print(user)

except ValidationError as e:
    print("Validation Error:")
    print(e)

