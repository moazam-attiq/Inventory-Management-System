# models/sale.py
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Sale:
    invoice_id: str
    filepath: Path

    @classmethod
    def from_filename(cls, filename: str):
        invoice_id = filename.replace('.txt', '')
        return cls(invoice_id=invoice_id, filepath=Path('bill') / filename)

    @property
    def display_name(self) -> str:
        return self.invoice_id
