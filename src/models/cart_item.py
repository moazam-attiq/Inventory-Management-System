# models/cart_item.py
from dataclasses import dataclass

@dataclass
class CartItem:
    pid: str
    name: str
    price: float
    qty: int
    stock: int

    @property
    def total_price(self) -> float:
        return float(self.price) * self.qty
