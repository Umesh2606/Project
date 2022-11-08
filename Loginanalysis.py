from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        self.login_username="admin@gmail.com"
        self.login_password="Sist*123"
        
        self.bg=ImageTk.PhotoImage(file="image1.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=300,y=100,width=600,height=400)


        title=Label(Frame_login,text="User Login Page",font=("Impact",25,"bold"),fg="black",bg="White").place(x=50,y=50)
        subtitle=Label(Frame_login,text="Enter the Login credentials",font=("Goudy old style",15,"italic"),fg="#1d1d1d",bg="white").place(x=50,y=100)

        label_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=140)
        self.username=Entry(Frame_login,font=("Goudy old style",15,),bg="#e7e7e6")
        self.username.place(x=50,y=170,width=320,height=35)


        label_user=Label(Frame_login,text="Password",font=("goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=215)
        self.password=Entry(Frame_login,font=("goudy old style",15,),bg="#e7e7e6")
        self.password.place(x=50,y=240,width=320,height=35)

        forget=Button(Frame_login,command=self.forgot_password,text="Forgot Password?",bd=0,font=("goudy old style",12),fg="#6162ff",bg="white").place(x=50,y=280)
        submit=Button(Frame_login,command=self.check_function,text="Login",bd=0,font=("Goudy old style",15,"bold"),bg="#6162ff",fg="white").place(x=50,y=320,width=180,height=40)


    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        elif self.username.get()==self.login_username or self.password.get()==self.login_password:
            messagebox.showinfo("Welcome",f"Welcome {self.username.get()}")
        else:
            messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
    

    def forgot_password(self):
        frame_forgot=Frame(self.root,bg="grey")
        frame_forgot.place(x=400,y=200,width=300,height=150)
        title=Label(frame_forgot,text="Enter your E-mail",font=("goudy old style",10,"bold"),fg="grey",bg="white").place(x=15,y=15)
        self.email=Entry(frame_forgot,font=("goudy old style",15,),bg="#e7e7e6")
        self.email.place(x=15,y=45,width=250,height=25)        
        submit=Button(frame_forgot,command=self.check_email,text="Submit",bd=0,font=("goudy old style",15,"bold"),bg="#6162ff",fg="white").place(x=50,y=80,width=150,height=30)

    def check_email(self):
        if self.email.get()=="":
            messagebox.showerror("Error","Please Enter a Mail id",parent=self.root)
        elif self.email.get()!="admin@gmail.com":
            messagebox.showerror("Error","The mail you Entered is not Registered",parent=self.root)
        else:
            messagebox.showinfo("Verification","Enter the Verification Code")
            messagebox.showwarning("Warning","Be Careful That your account had been Tried to be Recovered")
        


root=Tk()
obj=Login(root)
root.mainloop()