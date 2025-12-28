# models/supplier.py
from dataclasses import dataclass

@dataclass
class Supplier:
    invoice: str
    name: str
    contact: str
    description: str

    @classmethod
    def from_row(cls, row):
        # row: (invoice, name, contact, desc)
        return cls(
            invoice=row[0],
            name=row[1],
            contact=row[2],
            description=row[3],
        )
