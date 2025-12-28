# repositories/supplier_repository.py
import sqlite3
from src.models.supplier import Supplier

DB_PATH = "ims.db"

def _get_connection():
    return sqlite3.connect(database=DB_PATH)

def fetch_all_suppliers():
    con = _get_connection()
    cur = con.cursor()
    cur.execute("select * from supplier")
    rows = cur.fetchall()
    con.close()
    return [Supplier.from_row(r) for r in rows]

def find_supplier_by_invoice(invoice: str) -> Supplier | None:
    con = _get_connection()
    cur = con.cursor()
    cur.execute("SELECT * from supplier where invoice=?", (invoice,))
    row = cur.fetchone()
    con.close()
    return Supplier.from_row(row) if row else None

def insert_supplier(supplier: Supplier):
    con = _get_connection()
    cur = con.cursor()
    cur.execute(
        "insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",
        (supplier.invoice, supplier.name, supplier.contact, supplier.description),
    )
    con.commit()
    con.close()

def update_supplier(supplier: Supplier):
    con = _get_connection()
    cur = con.cursor()
    cur.execute(
        "update supplier set name=?,contact=?,desc=? where invoice=?",
        (supplier.name, supplier.contact, supplier.description, supplier.invoice),
    )
    con.commit()
    con.close()

def delete_supplier(invoice: str):
    con = _get_connection()
    cur = con.cursor()
    cur.execute("delete from supplier where invoice=?", (invoice,))
    con.commit()
    con.close()
