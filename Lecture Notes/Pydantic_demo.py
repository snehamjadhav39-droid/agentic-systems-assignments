# Student Management System

# DRY - Dont Repeat Yourself
# type hinting - name:str and so on. no enforcement on data type
# def create_student(name:str, age:int, college:str):
#     print(name)
#     print(age)
#     print(college)
#     print("Student Created")

# create_student("Sneha", 34, "Oxford")


# Pydantic - Data Validation  - Install Pydantic - pip install pydantic
# Craete BaseModel or Create an Ideal Model Class using Pydantic

#Type Validation : Validating the data type of the input parameters

# from pydantic import BaseModel

# class Student(BaseModel):   #Inherit the Pydantic BaseModel Class
#     name: str
#     age: int = 23   #ASsigning a default value in case the input is not defined
#     college: str = None     #Assigning a None type default value
#     marks: float

# #student_info is dictionary, create Student object using this dictionary
# student_info = {'name': 'Sneha', 'age' : -20, 'marks' : 23}

# #** -> unpacking, converting any data structure like dictionary, map, list into an object
# student = Student(**student_info)
# print(student)


#Field Validators : Validating the field value, eg age > 0, max length of str, email validation
#gt : greater than
#lt : less than
#ge : greater than equal
#le : less than equal
#Import Field for Field Validations
#EmailStr, AnyUrl
#Email should contain @masai.com
#field_validators are executed just bfore object creation
#MOdel Validators
#Computed Fields : calculate the outputs from the inputs, eg compute age from birthdate, percentage from marks

from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator, computed_field
from typing import Dict

class Student(BaseModel):   #Inherit the Pydantic BaseModel Class
    name: str = Field(max_length = 5, description = 'provide user name')
    age: int = Field(gt=0, le=100)
    email: EmailStr = Field(description = 'Provide valid email', )
    website: AnyUrl
    college: str
    marks: float = Field(default=10.0, ge=0)  #marks set to 10.0 in case input not defined
    emergency_contact_number: Dict[str,int]       #import a dictionary: key string, value int

    #this field validator is used to validate if email belongs to @masai.com. It should be triggered when object creation
    @field_validator('email') #field validator only for email, one variable at a time
    @classmethod            #class method will have access within all the class
    def email_validator(cls, value):   #class attributes will be used, represents the class: value is parameter passed for the email
        domain_name = value.split('@')[-1]

        if domain_name!='gmail.com':
            raise ValueError('Not a Valid domain name in email')
        return value

    @field_validator('college')
    @classmethod
    def transform_college_name_to_upper_case(cls, value):
        return value.lower()


#Mode parameter regulates the data type conversion as specified, before or after the value being passed to the function.
#eg if age = "20" and mode = after, means mode validation will happen after the string 20 is converted to int 20
#if age = "20" and mode = before, means mode validation will happen before the sting 20 is converted to int 20 and will raise an exception
    @field_validator('age', mode = 'after') #default for mode is after
    @classmethod
    def validate_age(cls, value):
        if value < 0 and value > 100:
            raise ValueError("Invalid Input")
        return value

#requirement : if age<18, contact number is mandatory.
#model validator : access all the attributes of the student model, as in the above requirement we need to access age and contact number
    @model_validator(mode='after')
    @classmethod
    def validate_contact_number(cls,model): #model contains all attributes of the class
        if model.age<18 and ('fathers' not in model.emergency_contact_number):
            raise ValueError("If age is less than 18, fathers number is mandatory")
        
        return model

    @computed_field     #compute field method is going to create a property called percentage
    @property   #calculating some property of the user
    def percentage(self) ->float: #percentage will created as a field ton the student instance. this function returns a float
        return self.marks;
    #field validators cannot be used on computed fields, BIG NOOOOOO. But model validator can be used. like in the below eg.

    @model_validator(mode='after')
    @classmethod
    def validate_percentage(cls,model):
        if (model.percentage>100):
            raise ValueError ("Percentage Value invalid")
        
        return model;

#student_info is dictionary, create Student object using this dictionary
#order does not matter in dictionary
#it will ignore if there is any extra field in the input
student_info = {'name': 'Sneha', 'age' : 20, 'email' : 'abc@gmail.com', 'website' : 'https://www.google.com', 'college' : 'OXford', 'marks' : 23, 'emergency_contact_number': {'mothers': 123456789}}

#** -> unpacking, converting any data structure like dictionary, map, list into an object
student = Student(**student_info)
print(student)


##serialization - deserialization
#front end and backend are loosely coupled i.e they can be written in any languages
#to make this happen we have the concept of JSON
#eg. front end is java and backend is python, both convert their objects to json format - json is like a translator
# this conversion is serialisation - deserialisation, they are taken care by framework