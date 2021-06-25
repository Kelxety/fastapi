from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
from .. import schemas
from ..database import engine, SessionLocal
from sqlalchemy.orm import Session
from .. import models, schemas, crud


models.Base.metadata.create_all(bind=engine)


router_users = APIRouter(
    prefix="/users",
    tags=["USERS"]
)


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router_users.get("/",description="Returns all users" )
async def get_users(db: Session = Depends(get_db)):
    #create(first_name='Addu', last_name='Pagal', email='addu@gmail.com', contact_no='123-494', status=1)
    db_all_user = crud.get_all_user(db)
    return [{
        'status': 'OK',
        'data':db_all_user
        }]


@router_users.get("/{id}", status_code=200)
async def returns_a_single_user( id: int, response: Response, db: Session=Depends(get_db)):
    """
        To view all details related to a single contact
- **id**: The integer id of the contact you want to view details.
    """
    db_one_user = crud.get_user_by_id(db, id)
    if not db_one_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {f'details': 'User with the id {id} is not available'}
    return [{
        'status': 'OK',
        'data':db_one_user
        }]


@router_users.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(id: int, request: schemas.UserInfoBaseCopy, db: Session = Depends(get_db)):
    user_update = crud.update_user_by_id(db, request, id)
    if not user_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id of {id} is not found")
    user_update.update(request)
    db.commit()
    return "done"


@router_users.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_single_user(id: int, db: Session=Depends(get_db)):
    user_delete = crud.delete_user_by_id(db, id)
    db.commit()
    return [{
        'done': user_delete
    }]


@router_users.post('/create', response_model=schemas.UserCreate, status_code=status.HTTP_201_CREATED)
async def create_a_single_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_contact_no(db, contact_no=user.contact_no)
    if db_user:
        raise HTTPException(status_code=400, detail="Contact number already registered")
    return crud.create_user(db=db, user=user)

