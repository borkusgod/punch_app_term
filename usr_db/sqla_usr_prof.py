from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BaseMember = declarative_base()


class Person(BaseMember):
    __tablename__ = "user"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("first_name", String)
    lastname = Column("last_name", String)
    gender = Column("gender", String)
    age = Column("age", Integer)
    email = Column("email_address", String)
    phone_number = Column("phone_number", String)

    def __init__(self,
                 ssn,
                 first_n,
                 last_n,
                 gender,
                 age,
                 email,
                 phone_number):
        self.ssn = ssn
        self.firstname = first_n
        self.lastname = last_n
        self.gender = gender
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"(({self.ssn}) {self.firstname} {self.lastname} " \
               f"({self.gender} " \
               f"{self.age}))"


class TimePunch(BaseMember):
    __tablename__ = "time punches"

    tc_related = Column("time punch related", String, primary_key=True)
    description = Column("Description", String)
    owner = Column(Integer, ForeignKey("user.ssn"))

    def __init__(self,
                 tc_related,
                 description,
                 owner):
        self.tc_related = tc_related
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"time value: ({self.tc_related}) - description: {self.description}\nwas performed by {self.owner}"


engine = create_engine("sqlite:///pat.db", echo=True)

BaseMember.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# testing samples
p1 = Person(139555666, "Bill", "Birdie", "Male", 46, "any_given@gmail.com", "555-555-9111")
p2 = Person(169555888, "Bobbie", "Jenkins", "Male", 76, "a_random@yahoo.com", "888-555-666")
p3 = Person(555444333, "Rhonda", "Boork", "Female", 45, "free_micro@outlook.com", "999-333-1478")
p4 = Person(989755187, "Derek", "Dongster", "Male", 55, "free_timewarner@timewarner.com", "187-589-5656")

# t1 = TimePunch("True", "day start", p1.ssn)
# t2 = TimePunch("False", "lunch out", p1.ssn)
# t3 = TimePunch("True", "lunch in", p1.ssn)
# t4 = TimePunch("False", "end of day punch out", p1.ssn)

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)

# session.add(t1)
# session.add(t2)
# session.add(t3)
# session.add(t4)

session.commit()

# commented because of variable
res_all_peeps = session.query(Person).all()
print(res_all_peeps)

# res_all_things = session.query(TimePunch).all()
# print(res_all_things)
#
# filter_pnames = session.query(Person).filter(Person.age > 45)
# for each in filter_pnames:
#     print(each)
