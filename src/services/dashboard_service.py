# services/dashboard_service.py
import os
import sqlite3
from pathlib import Path

DB_PATH = "ims.db"
BILL_DIR = Path("bill")

class DashboardService:
    def get_stats(self):
        """Centralized stats - **Duplicated Code (13) FIXED**"""
        con = sqlite3.connect(database=DB_PATH)
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            products = len(cur.fetchall())
            
            cur.execute("select * from category") 
            categories = len(cur.fetchall())
            
            cur.execute("select * from employee")
            employees = len(cur.fetchall())
            
            cur.execute("select * from supplier")
            suppliers = len(cur.fetchall())
            
            sales = len([f for f in os.listdir(BILL_DIR) if f.endswith('.txt')]) if BILL_DIR.exists() else 0
            
            return {
                'products': products,
                'categories': categories, 
                'employees': employees,
                'suppliers': suppliers,
                'sales': sales
            }
        finally:
            con.close()
