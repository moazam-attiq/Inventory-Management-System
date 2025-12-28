# repositories/sales_repository.py
import os
from pathlib import Path
from typing import List
from src.models.sale import Sale

BILL_DIR = Path('bill')

def list_all_sales() -> List[Sale]:
    """**Duplicated Code (13)** → Centralized file listing"""
    if not BILL_DIR.exists():
        return []
    
    sales = []
    for filename in os.listdir(BILL_DIR):
        if filename.endswith('.txt'):
            sales.append(Sale.from_filename(filename))
    return sales

def get_sale_content(invoice_id: str) -> str:
    """Returns bill content as string"""
    filepath = BILL_DIR / f"{invoice_id}.txt"
    if not filepath.exists():
        raise FileNotFoundError(f"Bill {invoice_id} not found")
    
    with open(filepath, 'r') as f:
        return f.read()
