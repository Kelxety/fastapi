from typing import List
from pydantic import BaseModel

class UserInfoBase(BaseModel):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    contact_no: str
    bgy_id: int
    password: str

class UserInfoBaseCopy(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    contact_no: str
    bgy_id: int
    password: str


class GetUserInfo(UserInfoBase):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    contact_no: str
    bgy_id: int



class UserCreate(UserInfoBaseCopy):
    first_name: str
    middle_name: str
    last_name: str
    contact_no: str
    bgy_id: int
    password: str

    class Config:
        orm_mode = True