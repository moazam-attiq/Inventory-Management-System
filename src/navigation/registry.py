# navigation/registry.py
from tkinter import Toplevel

class NavigationRegistry:
    def __init__(self):
        self.handlers = {
            "employee": self._open_employee,
            "supplier": self._open_supplier,
            "category": self._open_category,
            "product": self._open_product,
            "sales": self._open_sales,
        }

    def navigate(self, route: str, parent_root):
        handler = self.handlers.get(route)
        if handler:
            handler(parent_root)

    def _open_employee(self, parent_root):
        from employee import employeeClass
        new_win = Toplevel(parent_root)
        employeeClass(new_win)

    def _open_supplier(self, parent_root):
        from supplier import supplierClass
        new_win = Toplevel(parent_root)
        supplierClass(new_win)

    def _open_category(self, parent_root):
        from category import categoryClass
        new_win = Toplevel(parent_root)
        categoryClass(new_win)

    def _open_product(self, parent_root):
        from product import productClass
        new_win = Toplevel(parent_root)
        productClass(new_win)

    def _open_sales(self, parent_root):
        from sales import salesClass
        new_win = Toplevel(parent_root)
        salesClass(new_win)
