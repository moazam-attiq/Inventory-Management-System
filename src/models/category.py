# models/category.py
from dataclasses import dataclass

@dataclass
class Category:
    name: str

    @classmethod
    def from_row(cls, row):
        # row: (name,)
        return cls(name=row[0])
