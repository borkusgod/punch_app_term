# uses sqlalchemy but also uses a library called uuid
import uuid

from sqlalchemy import create_engine, ForeignKey, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from uuid import *

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())


class Person(Base):
    __tablename__ = "users"

    userID = Column("userID", String, primary_key=True, default=generate_uuid)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    email = Column("email", String)
    profilename = Column("profilename", String)

    def __init__(self,
                 firstname,
                 lastname,
                 email,
                 profilename):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.profilename = profilename

    def __repr__(self):
        return f"first name: {self.firstname}\n" \
               f"last name: {self.lastname}\n" \
               f"email: {self.email}\n" \
               f"profile name: {self.profilename}"


engine = create_engine("sqlite:///pydude_tut.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

test1 = Person("Bill", "Boork", "lr@gmail.com", "borkus")
test2 = Person("Rhonda", "Toole", "rhifort@yahoo.com", "rhi")

session.add(test1)
session.add(test2)

session.commit()

res_all_peeps = session.query(Person).all()
print(res_all_peeps)

