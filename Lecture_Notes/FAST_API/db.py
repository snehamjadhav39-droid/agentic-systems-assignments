# This file db.py will help to connect with database
# Can use any database : SQL, mongoDB. here we are using SQL Lite

from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./MJ.db"

# create an object called engine
engine = create_engine(DATABASE_URL, echo = True)