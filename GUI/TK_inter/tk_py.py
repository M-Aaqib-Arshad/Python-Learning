from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

def handle_login():
    email = input1.get()
    password = input2.get()
    if email == 'aaqib@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy','Login Successful')
    else:
        messagebox.showerror('Error','Login Failed') 

root= Tk()

root.iconbitmap('logo.jpeg')
root.title("Login Form")

root.minsize(400,400) # to set the minimum size of window
# tk.geometry('350x500')
root.config(background='#ade8f4')

img = Image.open('logo.jpeg')
resized_img = img.resize((70,70))


img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

w = Label(root,text="Aaqib Arshad",background='#ade8f4')
w.pack()

f1_label = Label(text="Enter Email")
f1_label.pack(pady=(20,5))
f1_label.config(font=('verdana',12),background='#ade8f4')

input1 = Entry(root, width=55)
input1.pack(ipady=(3),pady=(1,5))

f2_label = Label(text="Enter Password")
f2_label.pack(pady=(1,1))
f2_label.config(font=('verdana',12),background='#ade8f4')

input2 = Entry(root, width=55)
input2.pack(ipady=(3),pady=(1,5))

Login_btn = Button(root,text='Login Here',background='red',fg='white',width=20,command=handle_login)
Login_btn.pack(pady=(10,1))
Login_btn.config(font=('verdana',10))

root.mainloop()
