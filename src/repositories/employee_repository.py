# repositories/employee_repository.py
import sqlite3
from src.models.employee import Employee, SearchField

DB_PATH = "ims.db"

def _get_connection():
    return sqlite3.connect(database=DB_PATH)

def fetch_all_employees():
    con = _get_connection()
    cur = con.cursor()
    cur.execute("select * from employee")
    rows = cur.fetchall()
    con.close()
    return [Employee.from_row(r) for r in rows]

def find_employee_by_eid(eid: str) -> Employee | None:
    con = _get_connection()
    cur = con.cursor()
    cur.execute("SELECT * from employee where eid=?", (eid,))
    row = cur.fetchone()
    con.close()
    return Employee.from_row(row) if row else None

def search_employees(field: SearchField, text: str):
    """**Switch Statements (6)** → Polymorphism via SearchField enum"""
    con = _get_connection()
    cur = con.cursor()
    cur.execute(
        f"select * from employee where {field.value} LIKE ?",
        (f"%{text}%",)
    )
    rows = cur.fetchall()
    con.close()
    return [Employee.from_row(r) for r in rows]

def insert_employee(employee: Employee):
    con = _get_connection()
    cur = con.cursor()
    cur.execute("""
        insert into employee(eid,name,email,gender,dob,joining,salary,password,dept,address,contact) 
        values(?,?,?,?,?,?,?,?,?,?,?)
    """, employee.__dict__.values())
    con.commit()
    con.close()

def update_employee(employee: Employee):
    con = _get_connection()
    cur = con.cursor()
    cur.execute("""
        update employee set name=?,email=?,gender=?,dob=?,joining=?,salary=?,password=?,dept=?,address=?,contact=? 
        where eid=?
    """, list(employee.__dict__.values())[1:] + [employee.eid])
    con.commit()
    con.close()

def delete_employee(eid: str):
    con = _get_connection()
    cur = con.cursor()
    cur.execute("delete from employee where eid=?", (eid,))
    con.commit()
    con.close()
