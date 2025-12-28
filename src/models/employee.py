# models/employee.py
from dataclasses import dataclass
from enum import Enum

class SearchField(Enum):
    EMAIL = "email"
    NAME = "name"
    CONTACT = "contact"

# models/employee.py - FIXED FIELD NAMES
@dataclass
class Employee:
    eid: str           # ✅ Matches GUI var_emp_id
    name: str
    email: str
    contact: str
    gender: str
    dob: str
    doj: str           # ✅ Matches GUI var_doj  
    salary: float
    password: str      # ✅ Matches GUI var_pass
    utype: str         # ✅ Matches GUI var_utype
    address: str

    @classmethod
    def from_row(cls, row):
        # ✅ Matches exact DB order
        return cls(
            eid=row[0], name=row[1], email=row[2], gender=row[3],
            contact=row[4], dob=row[5], doj=row[6], password=row[7],
            utype=row[8], address=row[9], salary=row[10]
        )
