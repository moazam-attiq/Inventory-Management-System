# models/employee.py
from dataclasses import dataclass
from enum import Enum

class SearchField(Enum):
    EMAIL = "email"
    NAME = "name"
    CONTACT = "contact"

@dataclass
class Employee:
    eid: str
    name: str
    email: str
    contact: str
    gender: str
    dob: str
    joining: str
    salary: float
    password: str
    dept: str
    address: str

    @classmethod
    def from_row(cls, row):
        return cls(*row)

    def search_key(self, field: SearchField) -> str:
        """**Message Chains (20)** → Single method"""
        match field:
            case SearchField.EMAIL: return self.email
            case SearchField.NAME: return self.name
            case SearchField.CONTACT: return self.contact
