from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def checking(self):
        if (self.ety_username.get() == "") or (self.ety_password.get() == ""):
            messagebox.showerror("Error","Username and password can't be empty.")
        elif (self.ety_username.get()=="Zachary Roman") and (self.ety_password.get()=="roman4949"):
            messagebox.showinfo("Welcome","Created By Mr.Zachary Roman.")
        elif (self.ety_username.get()!="Zachary Roman"):
            messagebox.showerror("Error","Incorrect Username.")
        elif ((self.ety_password.get()!="roman4949")):
            messagebox.showerror("Error","Incorrect Password.")
    def main(self):
        #Main Frame
        root=Tk()
        self.root=root
        self.root.title("Login System")
        self.root.geometry("700x400+400+150")
        self.root.resizable(False,False)

        self.bg=ImageTk.PhotoImage(file="Mainbg.jpg")
        self.bg_image=Label(self.root,image=self.bg)
        self.bg_image.place(x=0,y=0,relwidth=1,relheight=1)

        #Alpha Frame
        frame_login=Frame(self.root,bg="snow")
        frame_login.place(x=40,y=100,width=250,height=250)

        self.lbl_title=Label(frame_login,text="Login Here",font=("Impact",20),fg="#6162ff",bg="white")
        self.lbl_title.place(x=50,y=10)
        self.lbl_subtitle=Label(frame_login,text="Bank Login Area",font=("Goudy old style Bold",16),fg="#1d1d1d",bg="white")
        self.lbl_subtitle.place(x=30,y=50)
        self.lbl_username=Label(frame_login,text="Username",font=("Goudy old style Bold",16,),fg="grey",bg="snow")
        self.lbl_username.place(x=50,y=80)
        self.lbl_password=Label(frame_login,text="Password",font=("Goudy old style Bold",14),fg="grey",bg="snow")
        self.lbl_password.place(x=50,y=140)

        self.ety_username=Entry(frame_login,font=("Goudy old style",14),bg="#E7E6E6")
        self.ety_username.place(x=30,y=110,width=150,height=30)
        self.ety_password=Entry(frame_login,font=("Goudy old style",14),bg="#E7E6E6",show="*")
        self.ety_password.place(x=30,y=170,width=150,height=30)

        self.btn_forgot=Button(frame_login,text="forgot password?",bd=0,font=("Goudy old style",10),fg="#6162ff",bg="white")
        self.btn_forgot.place(x=30,y=200)
        self.btn_login=Button(frame_login,command=self.checking,text="Login",bd=0,font=("Goudy old style",14),fg="white",bg="#6162ff")
        self.btn_login.place(x=170,y=210)
        self.root.mainloop() 
    

obj=Login()
obj.main()

       