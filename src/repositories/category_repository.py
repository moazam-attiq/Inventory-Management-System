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

def find_category_by_name(name: str) -> Category | None:
    con = _get_connection()
    cur = con.cursor()
    cur.execute("SELECT name from category where name=?", (name,))
    row = cur.fetchone()
    con.close()
    return Category.from_row(row) if row else None

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

def delete_category(name: str):
    con = _get_connection()
    cur = con.cursor()
    cur.execute("delete from category where name=?", (name,))
    con.commit()
    con.close()
