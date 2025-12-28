# repositories/product_repository.py
import sqlite3
from src.models.product import Product

DB_PATH = "ims.db"

def _get_connection():
    return sqlite3.connect(database=DB_PATH)

def fetch_all_products():
    con = _get_connection()
    cur = con.cursor()
    cur.execute("select * from product")
    rows = cur.fetchall()
    con.close()
    return [Product.from_row(r) for r in rows]

def fetch_active_products_for_billing():
    con = _get_connection()
    cur = con.cursor()
    cur.execute("select pid,name,price,qty,status from product where status='Active'")
    rows = cur.fetchall()
    con.close()
    return rows  # used by billClass as-is

def fetch_categories():
    con = _get_connection()
    cur = con.cursor()
    cur.execute("select name from category")
    rows = cur.fetchall()
    con.close()
    return [r[0] for r in rows]

def fetch_suppliers():
    con = _get_connection()
    cur = con.cursor()
    cur.execute("select name from supplier")
    rows = cur.fetchall()
    con.close()
    return [r[0] for r in rows]

def find_product_by_name(name: str) -> Product | None:
    con = _get_connection()
    cur = con.cursor()
    cur.execute("Select * from product where name=?", (name,))
    row = cur.fetchone()
    con.close()
    return Product.from_row(row) if row else None

def insert_product(product: Product):
    con = _get_connection()
    cur = con.cursor()
    cur.execute(
        "insert into product(Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",
        (product.category, product.supplier, product.name,
         product.price, product.qty, product.status),
    )
    con.commit()
    con.close()

def update_product(product: Product):
    con = _get_connection()
    cur = con.cursor()
    cur.execute(
        "update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",
        (product.category, product.supplier, product.name,
         product.price, product.qty, product.status, product.pid),
    )
    con.commit()
    con.close()

def delete_product(pid: int):
    con = _get_connection()
    cur = con.cursor()
    cur.execute("delete from product where pid=?", (pid,))
    con.commit()
    con.close()

VALID_SEARCH_COLUMNS = {
    "Category": "Category",
    "Supplier": "Supplier",
    "Name": "name",
}

def search_products(by_label: str, text: str):
    column = VALID_SEARCH_COLUMNS.get(by_label)
    if not column:
        raise ValueError("Invalid search field")
    con = _get_connection()
    cur = con.cursor()
    cur.execute(
        f"select * from product where {column} LIKE ?",
        (f"%{text}%",),
    )
    rows = cur.fetchall()
    con.close()
    return [Product.from_row(r) for r in rows]
