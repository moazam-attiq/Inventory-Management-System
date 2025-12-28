# repositories/category_repository.py
import sqlite3
from src.models.category import Category

DB_PATH = "ims.db"

def _get_connection():
    return sqlite3.connect(database=DB_PATH)

def fetch_all_categories():
    con = _get_connection()
    cur = con.cursor()
    cur.execute("select * from category")
    rows = cur.fetchall()
    con.close()
    return [Category.from_row(r) for r in rows]


def insert_category(category: Category):
    con = _get_connection()
    cur = con.cursor()
    cur.execute("insert into category(name) values(?)", (category.name,))
    con.commit()
    con.close()

def update_category(category: Category):
    con = _get_connection()
    cur = con.cursor()
    cur.execute("update category set name=? where name=?", 
                (category.name, category.name))  # Note: assumes name is PK
    con.commit()
    con.close()

def find_category_by_name(name: str) -> Category | None:
    con = _get_connection()
    cur = con.cursor()
    # ✅ Changed to select * to get cid too
    cur.execute("SELECT * from category where name=?", (name,))
    row = cur.fetchone()
    con.close()
    return Category.from_row(row) if row else None

def delete_category(identifier: str | Category):
    """✅ FIXED: Accepts name OR Category object"""
    con = _get_connection()
    cur = con.cursor()
    try:
        if isinstance(identifier, Category):
            name = identifier.name
        else:
            name = identifier
            
        cur.execute("DELETE FROM category WHERE name=?", (name,))
        con.commit()
    finally:
        con.close()

