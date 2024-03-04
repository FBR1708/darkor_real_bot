from sqlalchemy import Column, String, Integer, LargeBinary, TEXT

from database import Base


class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    name_username_father_name = Column(String(300))
    user_year = Column(String(300))
    phone_number = Column(String(300))
    specialty = Column(TEXT)
    info = Column(String(300))
    experience = Column(String(300))
    language_level = Column(String(300))
    address = Column(String(300))
    image = Column(LargeBinary, nullable=True)
    comment = Column(TEXT, nullable=True)


class Employer_Info(Base):
    __tablename__ = 'employer_info'



    company_name = Column(String(500))
    responsible_person_name = Column(String(400))
    phone_number = Column(String(300))
    employee_direct = Column(String(400))
    employee_number = Column(String(300))
    employer_duty = TEXT
    work_time = Column(String(400))
    employee_experience = Column(String(400))
    employee_salary = Column(String(300))
    working_vocation = TEXT
