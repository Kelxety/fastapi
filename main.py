from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#get index
@app.get('/', tags=['INDEX'])
def index(limit=12):
    return {"data" : 'User List'}

#get main_user
@app.get('/main_user', tags=['MAIN USER'])
def show_all_main_user(limit=12):
    return {"data" : 'User List'}

#get all user
@app.get('/user', tags=['USER'])
def show_all_user(limit=12):
    return {'data' : {"User" : 'user'}}

#get user by id
@app.get('/user/{id}', tags=['USER'])
def show_user_by_id(id: int,limit=12):
    return {'data' : {"User" : id}}


@app.get('/user/{id}/comments', tags=['USER'])
def show_user_comments(id: int,limit=12):
    return {'data': {"user": id}}

class User(BaseModel):
    first_name: str
    middle_name: str
    surname: str
    contanct_no: str
    bgy_id: int
    password: str

@app.post('/user', tags=['USER'])
def add_user(request: User):
    return {'data': f"user added with the contact no of {request.contanct_no}"}
    
