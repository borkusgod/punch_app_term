from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
# below is deprecated but still working for now
"""/punch_app_term/neural_nine_sqla.py:5: MovedIn20Warning: The 
``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). 
(deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", String)
    age = Column("age", Integer)

    def __init__(self,
                 ssn,
                 first,
                 last,
                 gender,
                 age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    # the next object defines how to print out object(person)
    def __repr__(self):
        return f"(({self.ssn}) {self.firstname} {self.lastname} " \
               f"({self.gender} " \
               f"{self.age}))"


class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self,
                 tid,
                 description,
                 owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"


engine = create_engine("sqlite:///neuralnine_tut.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# comment out vvvvvvvvv
# ========================================================
p1 = Person(139555666, "Bill", "Bourque", "Male", 46)
p2 = Person(169555888, "Bobbie", "Kennedey", "Male", 76)
p3 = Person(555444333, "Rhonda", "Bourque", "Female", 45)
p4 = Person(989755187, "Joe", "Dirt", "Male", 55)

t1 = Thing(1, "Some junk", p1.ssn)
t2 = Thing(2, "Some bullshit", p2.ssn)
t3 = Thing(3, "Some other bullshit", p3.ssn)
t4 = Thing(4, "Some ball dander", p4.ssn)

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)

session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)


# need below for it to take to the database
session.commit()
# =========================================================
# comment out above when testing and if db already exists

# commented because of variable
res_all_peeps = session.query(Person).all()
print(res_all_peeps)

res_all_things = session.query(Thing).all()
print(res_all_things)

# results = session.query(Person).filter(Person.lastname == "Bourque")
# for each in results:
#     print(each)

filter_pnames = session.query(Person).filter(Person.age > 45)
for each in filter_pnames:
    print(each)

filter_things = session.query(Thing).filter(Thing.tid > 1)
for each in filter_things:
    print(each)
