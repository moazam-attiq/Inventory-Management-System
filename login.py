from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import sqlite3
from billing import billClass
from dashboard import IMS


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700")
        self.root.title("IMS Login")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        # ----------------- Title Bar (Same as Dashboard) -----------------
        self.logo = PhotoImage(file="images/logo1.png")
        title = Label(
            self.root,
            text="Inventory Management System - Login",
            image=self.logo,
            compound=LEFT,
            font=("times new roman", 40, "bold"),
            bg="#010c48",
            fg="white",
            padx=20,
            anchor="w"
        )
        title.place(x=0, y=0, relwidth=1, height=70)

        # ---------------- Clock Bar (Matching Dashboard Style) ----------------
        self.lbl_clock = Label(
            self.root,
            text="Please log in to continue\t\tDate: DD:MM:YYYY\t\tTime: HH:MM:SS",
            font=("times new roman", 15),
            bg="#4d636d",
            fg="white"
        )
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ---------------- Login Frame (Centered Card) -----------------
        login_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        login_frame.place(x=450, y=180, width=450, height=350)

        lbl_title = Label(
            login_frame,
            text="Login Panel",
            font=("times new roman", 25, "bold"),
            bg="white",
            fg="#010c48"
        )
        lbl_title.pack(side=TOP, pady=20)

        # Email
        lbl_user = Label(login_frame, text="Email:", font=("times new roman", 18), bg="white")
        lbl_user.place(x=30, y=100)
        self.txt_user = Entry(login_frame, font=("times new roman", 18), bg="#f0f0f0")
        self.txt_user.place(x=160, y=100, width=230)

        # Password
        lbl_pass = Label(login_frame, text="Password:", font=("times new roman", 18), bg="white")
        lbl_pass.place(x=30, y=160)
        self.txt_pass = Entry(login_frame, font=("times new roman", 18), bg="#f0f0f0", show="*")
        self.txt_pass.place(x=160, y=160, width=230)

        # Login Button
        btn_login = Button(
            login_frame,
            text="Login",
            font=("times new roman", 18, "bold"),
            bg="#009688",
            fg="white",
            cursor="hand2",
            command=self.login
        )
        btn_login.place(x=160, y=230, width=230, height=40)

        # Footer
        lbl_footer = Label(
            self.root,
            text="IMS-Inventory Management System | Made with ❤️",
            font=("times new roman", 12),
            bg="#4d636d",
            fg="white"
        )
        lbl_footer.pack(side=BOTTOM, fill=X)
        self.update_content()

    # ----------------- Update Time -----------------
    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    # ----------------- Authentication Logic -----------------
    def login(self):
        email = self.txt_user.get()
        password = self.txt_pass.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            con = sqlite3.connect("ims.db")
            cur = con.cursor()

            # Modify according to your table fields
            cur.execute("SELECT * FROM employee WHERE email=? AND pass=?", (email, password))
            row = cur.fetchone()

            if row:
                utype = row[8]
                messagebox.showinfo("Success", "Login Successful!", parent=self.root)
                self.root.destroy()

                if utype == "Admin":
                    main_root = Tk()
                    IMS(main_root)
                    main_root.mainloop()
                elif utype == "Employee":
                    main_root = Tk()
                    billClass(main_root)
                    main_root.mainloop()
                else:
                    messagebox.showerror("Error", f"Unknown user role: {utype}")
            else:
                messagebox.showerror("Error", "Invalid Email/Password", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    LoginWindow(root)
    root.mainloop()
