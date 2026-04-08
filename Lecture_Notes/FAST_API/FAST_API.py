#FAST APIs are used to build REST APIs.
# API: Application Programming Interface : way to interact between client and server
# Backend is divides into : front end will first call to the app server in the backend
#   1. App Server (Java/GoLang etc) makes a call to database
#   2. Database - CRUD Operations : Create, Read, Update, Delete - any operation can be classified in one of these
#   3. Request-Response Cycle : Client Server communication
#    eg. Amazon Login : front end -> /login -> Backend invokde to login funcyion :: /login is API call
# Microservices : sub parts of backend services or monilith codebase
# Big Ball of Mud : Monolith - One code base for one service which handles all the requirenents of services
# Very difficult to manage this Big Ball of Mud, hence this was broken down into MICRO SERVICES
# Just one Language is not easy for entire framework, hence we have the concept of FRAMEWORKS
# Python Frameworks: FAST APIs, DJANGO

# FAST API : It is a modern python based web framework to build production ready applications. It is faster to build and use Web APIs/ REST APIs
# other examples of frameworks are Django, springboot in java
# ADVANTAGES of FAST API :
#   1. APIs built using APIs are faster
#   2. API Documentation is is automatic via SWAGGER UI - uses thge SWAGGER Framework
#   3. FAST API supports pydantic i.e data validation automatically or inbuilt
#   4. Easy to build APIs using FAST API
#   4. FAST API uses ASGI server internally - Asynchronous Server Gateway Interface :: It uses UVICORN server, a type of ASGI server
#          Asynchronous : does not wait for the first request to complete to start the next request - non-blocking call
#          Synchronous : blocking call - sebsequent requests wait for the prior request to complete 

# HTTPS Methods/Conventions : GET -> Read, PUT -> Update(PATCH for partial object update, and PUT is for complete object or replace the whole object) , POST -> Create, DELETE -> Delete (in analogy with the CRUD)

#API Design process : Validate the INPUTS -> PROCESS the inputs -> RETURN the output

#INSTALL pip fastapi, uvicorn

from fastapi import FastAPI, HTTPException, Path, Query, Depends
import json
from Lecture_Notes.FAST_API.common import db_operation

app = FastAPI()     #app is object of thge type FastAPI

#localhost:8000/hello
# @app.get() is DECORATOR/WRAPPER of the method say_hello(). /hello is the endpoint
# eg. amazon.in/login : /login is api endpoint 
@app.get("/hello")   #/ denotes the default api call when the website is called. ACnnot have more than one default for multiple APIs
def say_hello():
    return "Hello World!!"

#localhost:8000/bye
@app.get("/bye")    #/bye is the API endpoint
def say_bye():
    return "Bye Bye Everyone!!"

#command to start the server to run a fast API : uvicorn FAST_API:app
# for any changes : uvicorn server has to be stopped and started again for the changes to take effect. command to stop : Ctrl+C
# but to reload the changes automatically the command can be used : uvicorn FAST_API:app --reload

# Get all students from the students_info.json
# /students : the name should not reveal the endpoint function

# funtion to get the json data from external file
# need to import json to access the json functions
def load_students_data():
    with open('student_info.json', 'r') as f:    # r: read the file, opertaion to be performed on the file and store in the variable f
        students_data  = json.load(f) 

    return students_data

# Get all students
# /students
@app.get("/students")
def get_all_students():
    return load_students_data()


# Get the data for a particular student ID
# This can be done by two ways : PATH Parameters and QUERY uery Parameters

# PATH PARAMETERS - /students/{student_id, eg ST001}. Pass variable in the URL, in the end-point it is path variable
@app.get("/students/{student_id}")   #PATH Paratmeters passed via Curly Braces
def get_student_with_id(student_id: str = Path(..., description = "Id of the Student")):      #Path function: 3 dots mean this parameter is mandatory. If you dont pass student_id it will throw an error :: Import Path
    data = load_students_data()


    #HTTP 200 OK is the default success status code for GET Requests
    if student_id not in data:
        return HTTPException(status_code=404, detail = "Student not found")     # Import HttpException

    return data[student_id]


#FAST API provides automatic documentation
# call method : http://127.0.0.1:8000/docs, to access the APIs defines in this code
# Https Status Code : 200 : Valid Response, 404: Not found.

#QUERY PARAMETRS - Import Query
# /students?student_id = ST001 :: key (student_id): value(ST001) pair - Query parameter is generally key-value pair
# denoted by ? in the url while calling a query parameter
@app.get("/students_query")   #PATH Paratmeters passed via Curly Braces
def get_student_with_id(student_id: str = Query(..., description = "Id of the Student")):      #Path function: 3 dots mean this parameter is mandatory. If you dont pass student_id it will throw an error :: Import Path
    data = load_students_data()

    if student_id not in data:
        return HTTPException(status_code=404, detail = "Student not found")     # Import HttpException

    return data[student_id]


# When we have less parameter use path parametes. If we have more than one or two parameters use query parameters.
#IN Query Parameter we pass the details of the parameter- string, key, value,  queried in the url itself.


# Sort the students by their age or problems solved
# Client should be able to sort the values in ascending or descending order
# eg: /students?sort_by=age&sort_order=asc
@app.get("/sort")
def get_students_in_sorted_order(sort_by: str = Query(..., description = "Sort by their age or problem solved"), sort_order : str = Query('asc', description = "Sorting by asc or desc")):   # In Query function for sort_order, asc is not a mandatory paramater
    valid_sort_by_fields = ['age','problems_solved']

    if sort_by not in valid_sort_by_fields:
        raise HTTPException (status_code = 400 , detail = "Can only sort age or problem solved")

    if sort_order not in ['asc', 'desc']:
        raise HTTPException (status_code = 400 , detail = "Can only sort age or problem solved")

    students_data = load_students_data()


    order = True
    if sort_order == 'desc':
        order = False

    # reverse = TRUE -> ASC Order
    # reverse = FASLE -> DESC Order
    sorted_students_data = sorted(students_data.values(), key= lambda k: k.get('age',0), reverse=order)

    return sorted_students_data

# If we write common functionality in seperate file import the file and function of that file
# DEPENDENCY INJECTION : In FAST API, we need not call the dependies manually, it will do it automatically using the Depends function
# import Depends

@app.get("/api")
def sample_api(x = Depends(db_operation)): #sample_api need input x returned by db_operations()
    return x


# SQLAlchemy - ORM (Object Relation Mapping) Library in Python to deal with DB
# Objects : Models/Class
# Relation : SQL/Tables
# RDBMS/SQL databases store data in the form of tables, tables are related
# FAST API - Build APIs + SQLAlchemy - to connect databases
# eg. HibernaTE IS orm LIBRARY IN java

# SQLAlchemy can be used in two ways : core method and ORM
# core needs manual intervention and ORM is more automatic

# How to create database : pip intall sqlalchemy