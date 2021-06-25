from sqlalchemy.orm import Session

from . import models, schemas

def get_all_user(db: Session):
    return db.query(models.UserInfo).all()

def get_user_by_id(db: Session, id: int):
    getUserByID = db.query(models.UserInfo).filter(models.UserInfo.id == id).first()
    return getUserByID


def get_user_by_contact_no(db: Session, contact_no: str):
    return db.query(models.UserInfo).filter(models.UserInfo.contact_no == contact_no).first()


def update_user_by_id(db, request, id):
    user = db.query(models.UserInfo).filter(models.UserInfo.id == id)
    return user
    

def delete_user_by_id(db: Session, id: int):
    deleteUserByID = db.query(models.UserInfo).filter(models.UserInfo.id == id).delete(synchronize_session=False)
    return deleteUserByID


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.UserInfo(first_name=user.first_name, middle_name=user.middle_name, last_name=user.last_name, contact_no=user.contact_no, bgy_id=user.bgy_id, password=user.password )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user