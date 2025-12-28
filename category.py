from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox

# ✅ NEW IMPORTS - REPOSITORY PATTERN
from src.repositories.category_repository import (
    fetch_all_categories,
    find_category_by_name,
    insert_category,
    delete_category,
)
from src.models.category import Category

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.root.focus_force()

        # Variables (UNCHANGED)
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        # Title & Form (UNCHANGED)
        lbl_title = Label(self.root, text="Manage Product Category", font=("goudy old style", 30), 
                         bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        
        lbl_name = Label(self.root, text="Enter Category Name", font=("goudy old style", 30), bg="white").place(x=50, y=100)
        txt_name = Entry(self.root, textvariable=self.var_name, bg="lightyellow", 
                        font=("goudy old style", 18)).place(x=50, y=170, width=300)

        btn_add = Button(self.root, text="ADD", command=self.add, font=("goudy old style", 15), 
                        bg="#4caf50", fg="white", cursor="hand2").place(x=360, y=170, width=150, height=30)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), 
                           bg="red", fg="white", cursor="hand2").place(x=520, y=170, width=150, height=30)

        # Table (UNCHANGED - 2 columns for cid, name)
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=700, y=100, width=380, height=100)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)
        
        self.CategoryTable = ttk.Treeview(cat_frame, columns=("cid", "name"), 
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        
        self.CategoryTable.heading("cid", text="C ID")
        self.CategoryTable.heading("name", text="Name")
        self.CategoryTable["show"] = "headings"
        self.CategoryTable.column("cid", width=90)
        self.CategoryTable.column("name", width=100)
        
        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)
        
        self.show()  # ✅ Uses repository

        # Images (UNCHANGED)
        self.im1 = Image.open("images/cat.jpg")
        self.im1 = self.im1.resize((500, 250))
        self.im1 = ImageTk.PhotoImage(self.im1)
        self.lbl_im1 = Label(self.root, image=self.im1, bd=2, relief=RAISED)
        self.lbl_im1.place(x=50, y=220)

        self.im2 = Image.open("images/category.jpg")
        self.im2 = self.im2.resize((500, 250))
        self.im2 = ImageTk.PhotoImage(self.im2)
        self.lbl_im2 = Label(self.root, image=self.im2, bd=2, relief=RAISED)
        self.lbl_im2.place(x=580, y=220)

    # ✅ REFACTORED: Uses repository - **Long Method (1)** FIXED
    def show(self):
        try:
            categories = fetch_all_categories()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for c in categories:
                # ✅ Table expects (cid, name) - repository provides both
                self.CategoryTable.insert('', END, values=(c.cid if hasattr(c, 'cid') else 'N/A', c.name))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    # ✅ REFACTORED: Uses repository - **Duplicated Code (13)** FIXED
    def add(self):
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category Name must be required", parent=self.root)
                return

            # ✅ Repository handles SQL injection safety
            if find_category_by_name(self.var_name.get()) is not None:
                messagebox.showerror("Error", "Category already present", parent=self.root)
                return

            category = Category(name=self.var_name.get())
            insert_category(category)
            
            messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
            self.clear()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please select category from table first", parent=self.root)
                return

            op = messagebox.askyesno("Confirm", f"Do you really want to delete '{self.var_name.get()}'?", parent=self.root)
            if op:
                delete_category(self.var_name.get())  # ✅ Always name, never ID
                messagebox.showinfo("Success", "Category deleted successfully!", parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Delete failed: {str(ex)}", parent=self.root)


    # ✅ UNCHANGED - GUI specific
    def clear(self):
        self.var_name.set("")
        self.var_cat_id.set("")
        self.show()

    # ✅ UNCHANGED - GUI specific (works with 2-column table)
    def get_data(self, ev):
        f = self.CategoryTable.focus()
        content = self.CategoryTable.item(f)
        row = content['values']
        self.var_cat_id.set(row[0])   # cid
        self.var_name.set(row[1])     # name

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
