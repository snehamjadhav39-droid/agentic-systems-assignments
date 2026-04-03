# write all the tables we want to create in the database

from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String
#from sqlalchemy import * - to import all from sqlalchemy

# stores the schema or structure of the object
metadata = MetaData()

#Users Table -> Student_Id, name, email, password, etc
users = Table("users", # name of the table
              metadata,
              Column("id", Integer, primary_key = True),   #int is for python, Integer is for alchemy, PRIMARY_KEY makes the column nullable=false and auto increment
              Column("name", String(50), nullable = False ),   # name can have max 50 characters, name cannot be Null
              Column("email", String, unique=True, nullable=False)
              )

def create_tables():
    metadata.create_all(engine)