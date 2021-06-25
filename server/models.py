from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from server.database import Base


class UserInfo(Base):
    __tablename__ = "tbl_user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    contact_no = Column(String)
    bgy_id = Column(Integer, ForeignKey('tbl_barangay.bgy_id'))
    password = Column(String, unique=True)

    bgy = relationship("BgyInfo", back_populates="user")
    

class BgyInfo(Base):
    __tablename__ = "tbl_barangay"

    bgy_id = Column(Integer, primary_key=True, index=True)
    bgy_name = Column(String)
    bgy_code = Column(String)
    municipal_id = Column(Integer, ForeignKey('tbl_lgu.municipal_id'))

    user = relationship("UserInfo", back_populates="bgy")
    municipal = relationship("MunicipalInfo", back_populates="bgy")

class MunicipalInfo(Base):
    __tablename__ = "tbl_lgu"

    municipal_id = Column(Integer, primary_key=True, index=True)
    municipal_name = Column(String)
    municipal_code = Column(String)

    bgy = relationship("BgyInfo", back_populates="municipal")
