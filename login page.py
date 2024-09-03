from tkinter import *
import ast

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    try:
        with open('datasheet.txt', "r") as file:
            d = file.read()
            r = ast.literal_eval(d)
    except FileNotFoundError:
        r = {}

    if username in r.keys() and password == r[username]:
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
        Label(screen, text="WELCOME!", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)
    else:
        message_label.config(text="Invalid username or password", fg="red")

def signup_command():
    window = Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    def signup():
        username = user_entry.get()
        password = code_entry.get()
        confirm_password = confirm_code_entry.get()

        if password == confirm_password:
            try:
                with open('datasheet.txt', 'r+') as file:
                    d = file.read()
                    r = ast.literal_eval(d)
                    dict2 = {username: password}
                    r.update(dict2)
                    file.seek(0)  # Move the cursor to the start of the file
                    file.truncate()  # Clear the file contents
                    file.write(str(r))
                signup_message_label.config(text="Successfully signed up", fg="green")
            except FileNotFoundError:
                with open('datasheet.txt', 'w') as file:
                    pp = str({username: password})
                    file.write(pp)
                signup_message_label.config(text="Successfully signed up", fg="green")
        else:
            signup_message_label.config(text="Passwords do not match", fg="red")

    def sign():
        window.destroy()

    img = PhotoImage(file="signup.png")
    Label(window, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    def on_enter_user(e):
        user_entry.delete(0, 'end')

    def on_leave_user(e):
        if user_entry.get() == '':
            user_entry.insert(0, 'Username')

    user_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user_entry.place(x=30, y=80)
    user_entry.insert(0, 'Username')
    user_entry.bind("<FocusIn>", on_enter_user)
    user_entry.bind("<FocusOut>", on_leave_user)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter_code(e):
        code_entry.delete(0, 'end')

    def on_leave_code(e):
        if code_entry.get() == '':
            code_entry.insert(0, 'Password')

    code_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show='*')
    code_entry.place(x=30, y=150)
    code_entry.insert(0, 'Password')
    code_entry.bind("<FocusIn>", on_enter_code)
    code_entry.bind("<FocusOut>", on_leave_code)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    def on_enter_confirm_code(e):
        confirm_code_entry.delete(0, 'end')

    def on_leave_confirm_code(e):
        if confirm_code_entry.get() == '':
            confirm_code_entry.insert(0, 'Confirm Password')

    confirm_code_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show='*')
    confirm_code_entry.place(x=30, y=220)
    confirm_code_entry.insert(0, 'Confirm Password')
    confirm_code_entry.bind("<FocusIn>", on_enter_confirm_code)
    confirm_code_entry.bind("<FocusOut>", on_leave_confirm_code)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    signup_message_label = Label(frame, text="", bg='white', fg='red', font=('Microsoft Yahei UI Light', 9))
    signup_message_label.place(x=30, y=250)

    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
    label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90, y=340)
    signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=200, y=340)

    window.mainloop()

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter_user(e):
    user.delete(0, 'end')

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_user)
user.bind('<FocusOut>', on_leave_user)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter_code(e):
    code.delete(0, 'end')

def on_leave_code(e):
    if code.get() == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11), show='*')
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_code)
code.bind('<FocusOut>', on_leave_code)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

message_label = Label(frame, text="", bg='white', fg='red', font=('Microsoft YaHei UI Light', 9))
message_label.place(x=30, y=180)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup_command)
sign_up.place(x=215, y=270)

root.mainloop()
