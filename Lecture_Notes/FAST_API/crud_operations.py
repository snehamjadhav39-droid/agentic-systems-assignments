from Lecture_Notes.FAST_API.db import engine
from Lecture_Notes.FAST_API.tables import users
from sqlalchemy import  insert

# create user
def create_user(input_name :str, input_email : str):
    with engine.connect() as conn:
        # insert into users values
        query = insert(users).values(name = input_name, email = input_email )
        conn.execute(query)
        conn.commit()
