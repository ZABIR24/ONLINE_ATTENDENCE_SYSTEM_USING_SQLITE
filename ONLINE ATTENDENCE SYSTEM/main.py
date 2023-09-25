from tkinter import ttk
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import sqlite3

root = Tk()
root.title("Online Attendence System")

width = 1000
height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)-(width/2)
y = (screen_height)-(height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)

USER_NAME = StringVar()
PASSWORD = StringVar()
FIRST_NAME = StringVar()
LAST_NAME = StringVar()
STUDENT_NAME = StringVar()
REG_NO = StringVar()
VAR = IntVar()

def Database():
    global conn, cursor
    conn = sqlite3.connect("db_StudentDetails.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'Member' (Mem_Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname Text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS 'Student'(Stud_No INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, studentname TEXT, regno TEXT, var text)")
    
def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
        
def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP,pady=80)
    title = Label(LoginFrame, text="LOGIN FORM", fg="red", font=('arial', 25), bd=18)
    title.grid(row=0)
    lbl_username = Label(LoginFrame, text="Username", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_pass = Label(LoginFrame, text="Password", font=('arial', 25), bd=18)
    lbl_pass.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 25), bd=18)
    lbl_result1.grid(row=3, columnspan=2)
    Username = Entry(LoginFrame,font=('arial', 20), textvariable=USER_NAME, width= 15)
    Username.grid(row=1, column=1)
    Pass = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15)
    Pass.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="LOGIN", font=('arial', 20), width=35, command=Login)
    btn_login.grid(row=5,columnspan=2,pady=20)
    
    lbl_regis = Label(LoginFrame, text="CREATE ACCOUNT", fg="blue", font=('arial', 20))
    lbl_regis.grid(row=4, sticky=W)
    lbl_regis.bind('<Button-1>', ToggleToRegister)
    
def RegisterForm():
    global RegisFrame, lbl_result2
    RegisFrame = Frame(root)
    RegisFrame.pack(side=TOP,pady=40)
    title1 = Label(RegisFrame, text="REGISTRATION FORM", fg="red", font=('arial', 25), bd=18)
    title1.grid(row=0)
    lbl_username = Label(RegisFrame, text="Username", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_pass = Label(RegisFrame, text="Password", font=('arial', 25), bd=18)
    lbl_pass.grid(row=2)
    lbl_firstname = Label(RegisFrame, text="First Name", font=('arial', 25), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisFrame, text="Last Name", font=('arial', 25), bd=18)
    lbl_lastname.grid(row=4)
    lbl_result2 = Label(RegisFrame, text="", font=('arial', 25), bd=18)
    lbl_result2.grid(row=5)
    username = Entry(RegisFrame,font=('arial', 20), textvariable=USER_NAME, width= 15)
    username.grid(row=1, column=1)
    password = Entry(RegisFrame, font=('arial', 20), textvariable=PASSWORD, width=15)
    password.grid(row=2, column=1)
    firstname = Entry(RegisFrame,font=('arial', 20), textvariable=FIRST_NAME, width= 15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisFrame, font=('arial', 20), textvariable=LAST_NAME, width=15)
    lastname.grid(row=4, column=1)
    btn_login = Button(RegisFrame, text="REGISTER", font=('arial', 20), width=35, command=Register)
    btn_login.grid(row=6,columnspan=2,pady=20)
        
    lbl_regis = Label(RegisFrame, text="GO TO LOGIN FORM", fg="blue", font=('arial', 20))
    lbl_regis.grid(row=7, sticky=W)
    lbl_regis.bind('<Button-1>', ToggleToLogin)


def AttendenceForm():
    global AttendenceForm, lbl_result3
    AttendenceFrame = Frame(root)
    AttendenceFrame.pack(side=TOP, pady=20)
    title2 = Label(AttendenceFrame, text="ONLINE ATTENDENCE", fg="red", font=('arial', 25), bd=18)
    title2.grid(row=0)
    lbl_stu_name = Label(AttendenceFrame, text="Student Name :", font=('arial', 25), bd=18)
    lbl_stu_name.grid(row=1)
    lbl_regno = Label(AttendenceFrame, text="Reg No. :", font=('arial', 25), bd=18)
    lbl_regno.grid(row=2)
    Label_3 = Label(AttendenceFrame, text="STATUS", width=20 ,font=('arial', 25), bd=18)
    Label_3.grid(row=4, column=0)
    lbl_result3 = Label(AttendenceFrame, text="", font=('arial', 25), bd=18)
    lbl_result3.grid(row=5, columnspan=2)
    studentname = Entry(AttendenceFrame,font=('arial', 20), textvariable=STUDENT_NAME, width= 15)
    studentname.grid(row=1, column=1)
    regno = Entry(AttendenceFrame, font=('arial', 20), textvariable=REG_NO, width=15)
    regno.grid(row=2, column=1)
    
    present = Radiobutton(AttendenceFrame, text="PRESENT", padx=5, variable=VAR, value=1)
    present.grid(row=4, column=1)
    present = Radiobutton(AttendenceFrame, text="ABSENT", padx=20, variable=VAR, value=0)
    present.grid(row=4, column=2)
    
    btn_submit = Button(AttendenceFrame, text="SUBMIT", font=('arial',20), width=35, command=Submit)
    btn_submit.grid(row=6, columnspan=2, pady=20)
    
def ToggleToLogin (event=None):
    RegisFrame.destroy()
    LoginForm()
    
def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()
    
def ToggleToSubmit(event=None):
    LoginFrame.destroy()
    AttendenceForm()
    
def Register():
    Database()
    if USER_NAME.get() == "" or PASSWORD.get() == "" or FIRST_NAME.get() == "" or LAST_NAME.get() == "" :
        lbl_result2.config(text="Please Complete The Required Fields!!", fg="orange")
    else:
        cursor.execute("SELECT * FROM 'Member' WHERE 'username' = ?", (USER_NAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Usrname Is Already Taken", fg="red")
        else:
            cursor.execute("INSERT INTO 'Member' (username, password, firstname, lastname) VALUES(?,?,?,?)", (str(USER_NAME.get()), str(PASSWORD.get()), str(FIRST_NAME.get()), str(LAST_NAME.get())))
            conn.commit()
            USER_NAME.set("")
            PASSWORD.set("")
            FIRST_NAME.set("")
            LAST_NAME.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()
        
def Login():
    Database()
    if USER_NAME.get() == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please Complete The Required Fields!!", fg="orange")
    else:
        try:
            cursor.execute("SELECT * FROM Member WHERE username = ? AND password = ?", (USER_NAME.get(), PASSWORD.get()))
            result = cursor.fetchone()
            if result is not None:
                ToggleToSubmit()
            else:
                lbl_result1.config(text="Invalid Username Or Password", fg="red")
        except sqlite3.Error as e:
            print("Database error:", e)


def Submit():
    Database()
    if STUDENT_NAME.get() == "" or REG_NO.get() == "" or VAR.get() == "" :
        lbl_result3.config(text="Please Complete The Required Fields!!", fg="orange")
    else:
        cursor.execute("SELECT * FROM 'Student' WHERE 'studentname' = ?", (STUDENT_NAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result3.config(text="Student Name Is Already Taken", fg="red")
        else:
            cursor.execute("INSERT INTO 'Student' (studentname, regno, var) VALUES(?,?,?)", (str(STUDENT_NAME.get()), str(REG_NO.get()), str(VAR.get())))
            conn.commit()
            STUDENT_NAME.set("")
            REG_NO.set("")
            VAR.set("")
            def view():
                conn = sqlite3.connect("db_StudentDetails.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM student")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                    tree.insert("",tk.END, values=row)
                conn.close()
            tree = ttk.Treeview(root, column=("column1","column2","column3","column4"), show='headings')
            tree.heading("#1", text="Stud_No")
            tree.heading("#2", text="Studentname")
            tree.heading("#3", text="regno")
            tree.heading("#4", text="Status")
            tree.pack()
            cursor.close()
            conn.close()
            b2 = tk.Button(text="View Data", command=view)
            b2.pack()

LoginForm ()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

if __name__ == '__main__':
    root.mainloop()