# models/product.py
from dataclasses import dataclass

@dataclass
class Product:
    pid: int | None
    category: str
    supplier: str
    name: str
    price: float
    qty: int
    status: str

    @classmethod
    def from_row(cls, row):
        # row: (pid, Category, Supplier, name, price, qty, status)
        return cls(
            pid=row[0],
            category=row[1],
            supplier=row[2],
            name=row[3],
            price=float(row[4]),
            qty=int(row[5]),
            status=row[6],
        )
