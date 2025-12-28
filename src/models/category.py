# src/models/category.py - UPDATED
from dataclasses import dataclass

@dataclass
class Category:
    cid: int | None = None  # ✅ Added for table display
    name: str = ""

    @classmethod
    def from_row(cls, row):
        # row: (cid, name) from "select * from category"
        return cls(cid=row[0], name=row[1])  # ✅ Now handles both columns
